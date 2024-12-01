import json
from mcp import types
from mcp.types import TextContent

from mcp_server_opensearch.models import SearchQuery, SearchResponse
from mcp_server_opensearch.opensearch_service import search as search_documents


def handle_search(arguments: dict) -> list[TextContent]:
    body = arguments.get("body", {})
    index_pattern = arguments.get("index_pattern", "*")
    routing = arguments.get("routing", None)

    # Call the search function
    results = search(body, index_pattern, routing)

    return [
        types.TextContent(
            text=json.dumps(results, indent=2),
            contentType="text/plain"
        ),
    ]


def search(body: dict, index_pattern: str, routing: str | None) -> SearchResponse:
    """
    Search for a query in the database and return the results.
    """

    search_query = SearchQuery(
        body=body,
        index_pattern=index_pattern,
        routing=routing
    )

    # validate search query
    # search_query.validate()

    # Get the results from the database
    results = search_documents(search_query)

    # Return the results
    return results
