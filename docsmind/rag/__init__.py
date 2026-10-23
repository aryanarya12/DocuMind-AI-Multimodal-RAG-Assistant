"""The RAG engine: chunk -> embed -> index -> retrieve -> rerank -> answer -> cite.

This package is completely independent of Streamlit and of any single vendor;
it is the part that migrates to FastAPI unchanged.
"""

from docsmind.rag.chunking import Chunker, chunk_documents
from docsmind.rag.citations import (
    CitationBundle,
    build_citations,
    verify_and_clean,
)
from docsmind.rag.embeddings import EmbeddingPipeline, build_embedding_pipeline
from docsmind.rag.generation import (
    AnswerGenerator,
    GenerationRequest,
    build_generator,
)
from docsmind.rag.hybrid import build_bm25_index, reciprocal_rank_fusion
from docsmind.rag.query_rewrite import QueryPlan, parse_query
from docsmind.rag.reranker import RerankingService, build_reranking_service
from docsmind.rag.retrieval import RetrievalRequest, Retriever, build_retriever
from docsmind.rag.vector_store import (
    BaseVectorStore,
    InMemoryVectorStore,
    QdrantVectorStore,
    SearchFilter,
    get_vector_store,
)

__all__ = [
    "AnswerGenerator",
    "BaseVectorStore",
    "Chunker",
    "CitationBundle",
    "EmbeddingPipeline",
    "GenerationRequest",
    "InMemoryVectorStore",
    "QdrantVectorStore",
    "QueryPlan",
    "RerankingService",
    "RetrievalRequest",
    "Retriever",
    "SearchFilter",
    "build_bm25_index",
    "build_citations",
    "build_embedding_pipeline",
    "build_generator",
    "build_reranking_service",
    "build_retriever",
    "chunk_documents",
    "get_vector_store",
    "parse_query",
    "reciprocal_rank_fusion",
    "verify_and_clean",
]
