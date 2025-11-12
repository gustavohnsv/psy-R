import re
from typing import List, Set, Dict, Optional
from docx import Document
from docx.document import Document as DocumentType
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import Table
from docx.text.paragraph import Paragraph

from .field_validator import FieldValidator


class TemplateProcessor:
    """Processes DOCX templates for field extraction and replacement."""
    
    FIELD_PATTERN = re.compile(r'\{([a-zA-Z0-9_]+)\}')
    
    def __init__(self, document: Optional[Document] = None):
        """Initialize with an optional document."""
        self.document = document
    
    def set_document(self, document: Document):
        """Set the document to process."""
        self.document = document
    
    def extract_fields(self, document: Optional[Document] = None) -> Set[str]:
        """Extract all field names from a DOCX document.
        
        Searches through paragraphs, tables, headers, and footers.
        
        Args:
            document: Optional document to process. If None, uses self.document.
            
        Returns:
            Set of unique field names (without braces)
        """
        doc = document or self.document
        if doc is None:
            return set()
        
        fields = set()
        
        # Extract from main document paragraphs
        for paragraph in doc.paragraphs:
            fields.update(self._extract_from_paragraph(paragraph))
        
        # Extract from tables
        for table in doc.tables:
            fields.update(self._extract_from_table(table))
        
        # Extract from headers
        for section in doc.sections:
            header = section.header
            for paragraph in header.paragraphs:
                fields.update(self._extract_from_paragraph(paragraph))
            
            # Extract from header tables
            for table in header.tables:
                fields.update(self._extract_from_table(table))
        
        # Extract from footers
        for section in doc.sections:
            footer = section.footer
            for paragraph in footer.paragraphs:
                fields.update(self._extract_from_paragraph(paragraph))
            
            # Extract from footer tables
            for table in footer.tables:
                fields.update(self._extract_from_table(table))
        
        return fields
    
    def _extract_from_paragraph(self, paragraph: Paragraph) -> Set[str]:
        """Extract field names from a paragraph."""
        fields = set()
        text = paragraph.text
        
        # Find all field patterns in the paragraph text
        matches = self.FIELD_PATTERN.findall(text)
        fields.update(matches)
        
        return fields
    
    def _extract_from_table(self, table: Table) -> Set[str]:
        """Extract field names from a table."""
        fields = set()
        
        for row in table.rows:
            for cell in row.cells:
                # Extract from paragraphs in each cell
                for paragraph in cell.paragraphs:
                    fields.update(self._extract_from_paragraph(paragraph))
        
        return fields
    
    def validate_fields(self, document: Optional[Document] = None) -> tuple:
        """Validate all fields in the document against naming convention.
        
        Args:
            document: Optional document to process. If None, uses self.document.
            
        Returns:
            Tuple of (valid_fields, invalid_fields_with_reasons)
        """
        fields = self.extract_fields(document)
        return FieldValidator.validate_fields(list(fields))
    
    def check_required_fields(self, field_names: Set[str], available_data: Dict[str, str]) -> tuple:
        """Check if all required fields have data.
        
        Args:
            field_names: Set of field names found in template
            available_data: Dictionary mapping field names to their values
            
        Returns:
            Tuple of (missing_fields, fields_with_empty_values)
        """
        missing_fields = []
        empty_fields = []
        
        for field_name in field_names:
            if field_name not in available_data:
                missing_fields.append(field_name)
            elif not available_data[field_name] or str(available_data[field_name]).strip() == "":
                empty_fields.append(field_name)
        
        return missing_fields, empty_fields

