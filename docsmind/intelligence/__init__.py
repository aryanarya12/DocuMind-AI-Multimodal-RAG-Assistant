"""Document intelligence: OCR, handwriting, visual understanding, tables, layout."""

from docsmind.intelligence.handwriting import HandwritingExtractor, HandwritingResult
from docsmind.intelligence.layout import (
    PageLayoutInfo,
    TextSpan,
    analyze_page_layout,
    looks_like_heading,
)
from docsmind.intelligence.ocr import OCREngine, OCRResult, build_ocr_engine
from docsmind.intelligence.tables import build_table, summarize_table, table_to_text
from docsmind.intelligence.vision import (
    VisionAnalyzer,
    VisualAnalysis,
    build_vision_analyzer,
)

__all__ = [
    "HandwritingExtractor",
    "HandwritingResult",
    "OCREngine",
    "OCRResult",
    "PageLayoutInfo",
    "TextSpan",
    "VisionAnalyzer",
    "VisualAnalysis",
    "analyze_page_layout",
    "build_ocr_engine",
    "build_table",
    "build_vision_analyzer",
    "looks_like_heading",
    "summarize_table",
    "table_to_text",
]
