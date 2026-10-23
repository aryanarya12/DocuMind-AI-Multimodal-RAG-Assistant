"""Embedding provider adapters."""

from docsmind.providers.embeddings.base import BaseEmbeddingProvider, Vector
from docsmind.providers.embeddings.cohere import CohereEmbeddings
from docsmind.providers.embeddings.factory import (
    SUPPORTED_PROVIDERS,
    build_embedding_provider,
    get_embedding_provider,
    reset_embedding_cache,
)
from docsmind.providers.embeddings.gemini import GeminiEmbeddings
from docsmind.providers.embeddings.hashing import HashingEmbeddings
from docsmind.providers.embeddings.openai_compat import OpenAICompatibleEmbeddings

__all__ = [
    "BaseEmbeddingProvider",
    "CohereEmbeddings",
    "GeminiEmbeddings",
    "HashingEmbeddings",
    "OpenAICompatibleEmbeddings",
    "SUPPORTED_PROVIDERS",
    "Vector",
    "build_embedding_provider",
    "get_embedding_provider",
    "reset_embedding_cache",
]
