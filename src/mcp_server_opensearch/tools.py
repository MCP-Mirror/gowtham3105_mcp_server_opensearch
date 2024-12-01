from mcp_server_opensearch.models import SearchQuery, SearchResponse
from mcp_server_opensearch.opensearch_service import search as search_documents


def handle_search(arguments: dict) -> SearchResponse:
    body = arguments.get("body", {})
    offset = arguments.get("offset", 0)
    size = arguments.get("size", 10)
    index_pattern = arguments.get("index_pattern", "*")
    sort = arguments.get("sort", [])
    page = arguments.get("page", 1)
    per_page = arguments.get("per_page", 10)

    # Call the search function
    results = search(body, offset, size, index_pattern, sort, page, per_page)

    return results


def search(body: dict, offset: int, size: int, index_pattern: str, sort: list, page: int, per_page: int):
    """
    Search for a query in the database and return the results.
    """

    search_query = SearchQuery(
        body=body,
        offset=offset,
        size=size,
        index_pattern=index_pattern,
        sort=sort
    )

    # validate search query
    # search_query.validate()

    # Get the results from the database
    results = search_documents(search_query)

    # Return the results
    return results
