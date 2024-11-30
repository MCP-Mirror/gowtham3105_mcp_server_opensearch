# Status and Error Types
from enum import Enum
from typing import Dict, Any, Optional, List
from uuid import UUID

from pydantic import BaseModel, Field


class Tools(str, Enum):
    SEARCH = "search"



class OperationStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"


# Base Models for Request/Response
class SearchQuery(BaseModel):
    """Search query parameters following OpenSearch Query DSL"""
    query: Dict[str, Any]
    offset: int = Field(default=0, alias="from")
    size: int = Field(default=10, ge=0, le=10000)  # Adding validation
    indexPattern: str = Field(default="*")  # Default to all indices
    sort: Optional[List[Dict[str, Any]]] = None





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
