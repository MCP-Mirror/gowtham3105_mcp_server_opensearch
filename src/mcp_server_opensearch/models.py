# Status and Error Types
from enum import Enum
from typing import Dict, Any, Optional, List
from uuid import UUID

from pydantic import BaseModel, Field


class Tools(str, Enum):
    SEARCH = "search"
    GET_INDICES = "get_indices"


class OperationStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"


# Base Models for Request/Response
class SearchQuery(BaseModel):
    """Search query parameters following OpenSearch Query DSL"""
    body: Dict[str, Any]
    index_pattern: str = Field(default="*")  # Default to all indices
    routing: Optional[str] = None


class Document(BaseModel):
    """Represents a single document from OpenSearch"""
    id: str
    index: str
    source: Dict[str, Any]
    score: Optional[float] = None


class SearchResponse(BaseModel):
    """Standard response format following MCP"""
    status: OperationStatus
    request_id: UUID
    took: int  # milliseconds
    total_hits: Optional[int] = None
    documents: Optional[List[Document]] = None
    errors: Optional[List[Dict[str, Any]]] = None
