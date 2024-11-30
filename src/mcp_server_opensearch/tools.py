from mcp_server_opensearch.models import SearchQuery, SearchResponse
from mcp_server_opensearch.opensearch_service import search as search_documents


def handle_search(arguments: dict) -> SearchResponse:
    query = arguments.get("query", {})
    offset = arguments.get("offset", 0)
    size = arguments.get("size", 10)
    indexPattern = arguments.get("indexPattern", "*")
    sort = arguments.get("sort", [])
    page = arguments.get("page", 1)
    per_page = arguments.get("per_page", 10)

    # Call the search function
    results = search(query, offset, size, indexPattern, sort, page, per_page)

    return results


def search(query: dict, offset: int, size: int, indexPattern: str, sort: list, page: int, per_page: int):
    """
    Search for a query in the database and return the results.
    """

    search_query = SearchQuery(
        query=query,
        offset=offset,
        size=size,
        indexPattern=indexPattern,
        sort=sort
    )

    # validate search query
    # search_query.validate()

    # Get the results from the database
    results = search_documents(search_query)

    # Return the results
    return results
