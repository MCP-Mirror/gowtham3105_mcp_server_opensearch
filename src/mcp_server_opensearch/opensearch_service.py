import os

from mcp_server_opensearch.models import SearchQuery, SearchResponse
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[{'host': os.getenv('OPENSEARCH_HOST', 'localhost'), 'port': os.getenv('OPENSEARCH_PORT', 9200)}],
    http_auth=(os.getenv('OPENSEARCH_USER', 'admin'), os.getenv('OPENSEARCH_PASSWORD', 'admin')),
    use_ssl=True,
    verify_certs=False,
    ssl_show_warn=False
)


def search(search_query: SearchQuery) -> SearchResponse:
    """
    Search for a query in the database and return the results.
    """

    client.search(
        index=search_query.indexPattern,
        body=search_query.query,
        from_=search_query.offset,
        size=search_query.size,
        sort=search_query.sort
    )
    response = client.search(
        index=search_query.indexPattern,
        body=search_query.query,
        from_=search_query.offset,
        size=search_query.size,
        sort=search_query.sort
    )

    return response
