"""Document ingestion: raw upload -> canonical Document."""

from docsmind.ingestion.base import BaseDocumentProcessor, ProcessingContext
from docsmind.ingestion.docx import WordProcessor
from docsmind.ingestion.image import ImageProcessor
from docsmind.ingestion.pdf import PDFProcessor
from docsmind.ingestion.pptx import PowerPointProcessor
from docsmind.ingestion.router import (
    DocumentRouter,
    FileValidation,
    get_router,
    reset_router,
)
from docsmind.ingestion.text import TextProcessor

__all__ = [
    "BaseDocumentProcessor",
    "DocumentRouter",
    "FileValidation",
    "ImageProcessor",
    "PDFProcessor",
    "PowerPointProcessor",
    "ProcessingContext",
    "TextProcessor",
    "WordProcessor",
    "get_router",
    "reset_router",
]
