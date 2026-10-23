"""OCR provider adapters."""

from docsmind.providers.ocr.base import BaseOCRProvider, NullOCRProvider, OCRResult
from docsmind.providers.ocr.factory import (
    SUPPORTED_PROVIDERS,
    build_ocr_provider,
    get_ocr_provider,
    reset_ocr_cache,
)
from docsmind.providers.ocr.tesseract import TesseractOCRProvider
from docsmind.providers.ocr.vision_llm import VisionOCRProvider

__all__ = [
    "BaseOCRProvider",
    "NullOCRProvider",
    "OCRResult",
    "SUPPORTED_PROVIDERS",
    "TesseractOCRProvider",
    "VisionOCRProvider",
    "build_ocr_provider",
    "get_ocr_provider",
    "reset_ocr_cache",
]
