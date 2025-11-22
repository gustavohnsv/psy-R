from typing import Set, Dict, Optional, List, Tuple
from docx import Document

from .template.extractor import TemplateExtractor
from .template.validator import TemplateValidator
from .template.replacer import TemplateReplacer
from .document_service import DocumentService

class TemplateProcessor:
    """Facade for template processing operations.
    
    Delegates actual work to specialized services:
    - TemplateExtractor: Field extraction
    - TemplateValidator: Field validation
    - TemplateReplacer: Field replacement
    - DocumentService: File I/O and conversion
    """
    
    def __init__(self, document: Optional[Document] = None):
        """Initialize with an optional document."""
        self.document = document
        self._extractor = TemplateExtractor()
        self._validator = TemplateValidator()
        self._replacer = TemplateReplacer()
        self._doc_service = DocumentService()
    
    def set_document(self, document: Document):
        """Set the document to process."""
        self.document = document
    
    def extract_fields(self, document: Optional[Document] = None) -> Set[str]:
        """Extract all field names from a DOCX document."""
        doc = document or self.document
        return self._extractor.extract_fields(doc)
    
    def validate_fields(self, document: Optional[Document] = None) -> Tuple[List[str], List[Tuple[str, str]]]:
        """Validate all fields in the document against naming convention."""
        fields = self.extract_fields(document)
        return self._validator.validate_fields(fields)
    
    def check_required_fields(self, field_names: Set[str], available_data: Dict[str, str]) -> Tuple[List[str], List[str]]:
        """Check if all required fields have data."""
        return self._validator.check_required_fields(field_names, available_data)
    
    def replace_fields(self, field_mapping: Dict[str, str], document: Optional[Document] = None) -> Document:
        """Replace all field placeholders in the document with actual values."""
        doc = document or self.document
        if doc is None:
            raise ValueError("No document provided for field replacement")
            
        count = self._replacer.replace_fields(doc, field_mapping)
        print(f"Replaced {count} field occurrences in document")
        return doc
    
    def save_document(self, document: Document, output_path: str) -> str:
        """Save the document to a file."""
        return self._doc_service.save_document(document, output_path)
    
    def convert_to_pdf(self, docx_path: str, pdf_path: Optional[str] = None) -> str:
        """Convert a DOCX file to PDF."""
        return self._doc_service.convert_to_pdf(docx_path, pdf_path)


