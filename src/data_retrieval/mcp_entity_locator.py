from __future__ import annotations

from collections.abc import Callable

def search_data(query: str) -> list[dict[str, str]]:
    """Search for data matching a query. Returns a list of data identifiers."""
    # Example logic of retrieving data identifiers based on query.
    return [{'id': '123'}, {'id': '456'}]

def get_data_details(identifier: str) -> dict[str, str]:
    """Retrieve details of data given its identifier."""
    # Example logic of retrieving data details.
    return {'id': identifier, 'detail': 'details about the data'}

def execute_retrieval(query: str) -> list[dict[str, str]]:
    """Retrieve and detail data by employing `search_data` and `get_data_details` functions."""
    results = search_data(query)
    detailed_results = [get_data_details(item['id']) for item in results]
    return detailed_results

class MCPDataRetriever:
    """Class utilizing exclusive MCP functions to retrieve and describe data."""
    def __init__(self) -> None:
        pass

    def retrieve_with_mcp(self, query: str) -> list[dict[str, str]]:
        """Perform data retrieval using only MCP functions."""
        return execute_retrieval(query)
