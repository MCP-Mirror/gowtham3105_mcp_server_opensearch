import os

from mcp_server_opensearch.models import SearchQuery, SearchResponse
from opensearchpy import OpenSearch

client = OpenSearch(
    hosts=[os.getenv('OPENSEARCH_URL', 'localhost:9200')],
    http_auth=(os.getenv('OPENSEARCH_USER', 'admin'), os.getenv('OPENSEARCH_PASSWORD', 'admin')),
    use_ssl=True,
    verify_certs=False,
    ssl_show_warn=False
)


def search(search_query: SearchQuery) -> SearchResponse:
    """
    Search for a query in the database and return the results.
    """

    response = client.search(
        index=search_query.index_pattern,
        body=search_query.body,
        from_=search_query.offset,
        size=search_query.size,
        sort=search_query.sort
    )

    return response
