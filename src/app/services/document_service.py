import os
from docx import Document

class DocumentService:
    """Service responsible for document I/O operations."""
    
    @staticmethod
    def save_document(document: Document, output_path: str) -> str:
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
    
    @staticmethod
    def convert_to_pdf(docx_path: str, pdf_path: str = None) -> str:
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
