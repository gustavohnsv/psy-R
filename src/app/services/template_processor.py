import re
import os
from typing import List, Set, Dict, Optional
from docx import Document
from docx.document import Document as DocumentType
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import Table
from docx.text.paragraph import Paragraph
from docx.text.run import Run

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
    
    def replace_fields(self, field_mapping: Dict[str, str], document: Optional[Document] = None) -> Document:
        """Replace all field placeholders in the document with actual values.
        
        Preserves formatting by handling fields that may be split across multiple runs.
        
        Args:
            field_mapping: Dictionary mapping field names (without braces) to replacement values
            document: Optional document to process. If None, uses self.document.
            
        Returns:
            The document with fields replaced (modifies in place)
        """
        doc = document or self.document
        if doc is None:
            raise ValueError("No document provided for field replacement")
        
        # Replace in main document paragraphs
        for paragraph in doc.paragraphs:
            self._replace_in_paragraph(paragraph, field_mapping)
        
        # Replace in tables
        for table in doc.tables:
            self._replace_in_table(table, field_mapping)
        
        # Replace in headers
        for section in doc.sections:
            header = section.header
            for paragraph in header.paragraphs:
                self._replace_in_paragraph(paragraph, field_mapping)
            for table in header.tables:
                self._replace_in_table(table, field_mapping)
        
        # Replace in footers
        for section in doc.sections:
            footer = section.footer
            for paragraph in footer.paragraphs:
                self._replace_in_paragraph(paragraph, field_mapping)
            for table in footer.tables:
                self._replace_in_table(table, field_mapping)
        
        return doc
    
    def _replace_in_paragraph(self, paragraph: Paragraph, field_mapping: Dict[str, str]):
        """Replace fields in a paragraph, handling fields split across runs."""
        # Get full paragraph text to find field positions
        full_text = paragraph.text
        
        # Find all field matches with their positions
        matches = list(self.FIELD_PATTERN.finditer(full_text))
        
        if not matches:
            return
        
        # Work backwards to preserve indices
        for match in reversed(matches):
            field_name = match.group(1)
            start_pos = match.start()
            end_pos = match.end()
            
            if field_name in field_mapping:
                replacement = str(field_mapping[field_name])
                self._replace_field_in_runs(paragraph, start_pos, end_pos, replacement)
    
    def _replace_field_in_runs(self, paragraph: Paragraph, start_pos: int, end_pos: int, replacement: str):
        """Replace a field that may span multiple runs in a paragraph."""
        # Collect all runs and their text positions
        runs_data = []
        current_pos = 0
        
        for run in paragraph.runs:
            run_text = run.text
            run_start = current_pos
            run_end = current_pos + len(run_text)
            runs_data.append((run, run_start, run_end, run_text))
            current_pos = run_end
        
        # Find which runs contain the field
        target_runs = []
        for run, run_start, run_end, run_text in runs_data:
            if not (run_end <= start_pos or run_start >= end_pos):
                target_runs.append((run, run_start, run_end, run_text))
        
        if not target_runs:
            return
        
        # Reconstruct the text across runs and replace
        if len(target_runs) == 1:
            # Simple case: field is in a single run
            run, run_start, run_end, run_text = target_runs[0]
            # Calculate relative positions within the run
            rel_start = max(0, start_pos - run_start)
            rel_end = min(len(run_text), end_pos - run_start)
            new_text = run_text[:rel_start] + replacement + run_text[rel_end:]
            run.text = new_text
        else:
            # Complex case: field spans multiple runs
            # Replace in first run
            first_run, first_start, first_end, first_text = target_runs[0]
            rel_start = max(0, start_pos - first_start)
            first_run.text = first_text[:rel_start] + replacement
            
            # Clear middle runs
            for run, _, _, _ in target_runs[1:-1]:
                run.text = ""
            
            # Replace in last run
            if len(target_runs) > 1:
                last_run, last_start, last_end, last_text = target_runs[-1]
                rel_end = min(len(last_text), end_pos - last_start)
                last_run.text = last_text[rel_end:]
    
    def _replace_in_table(self, table: Table, field_mapping: Dict[str, str]):
        """Replace fields in a table."""
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    self._replace_in_paragraph(paragraph, field_mapping)
    
    def save_document(self, document: Document, output_path: str) -> str:
        """Save the document to a file.
        
        Args:
            document: The document to save
            output_path: Full path including filename and .docx extension
            
        Returns:
            The path where the document was saved
        """
        # Ensure directory exists
        os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else '.', exist_ok=True)
        
        document.save(output_path)
        return output_path
    
    def convert_to_pdf(self, docx_path: str, pdf_path: Optional[str] = None) -> str:
        """Convert a DOCX file to PDF.
        
        Args:
            docx_path: Path to the DOCX file
            pdf_path: Optional path for PDF output. If None, uses same name with .pdf extension
            
        Returns:
            The path where the PDF was saved
        """
        try:
            from docx2pdf import convert
        except ImportError:
            raise ImportError(
                "docx2pdf library is required for PDF conversion. "
                "Install it with: pip install docx2pdf"
            )
        
        if pdf_path is None:
            pdf_path = os.path.splitext(docx_path)[0] + '.pdf'
        
        # Ensure directory exists
        os.makedirs(os.path.dirname(pdf_path) if os.path.dirname(pdf_path) else '.', exist_ok=True)
        
        convert(docx_path, pdf_path)
        return pdf_path

