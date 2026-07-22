from __future__ import annotations

from src.data_retrieval.mcp_entity_locator import MCPDataRetriever

def test_mcp_data_retrieval() -> None:
    """Validate `MCPDataRetriever` ensures proper usage of MCP-exclusive functions."""
    retriever = MCPDataRetriever()
    data = retriever.retrieve_with_mcp('sample query')
    # Include necessary assertions for expected behavior
    assert data == [
        {'id': '123', 'detail': 'details about the data'},
        {'id': '456', 'detail': 'details about the data'}
    ]
