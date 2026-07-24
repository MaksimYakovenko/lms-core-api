from unittest.mock import patch
from src.data_retrieval.mcp_entity_locator import MCPDataRetriever

def test_retrieve_with_mcp_calls_dependencies_correctly():
    """Test `retrieve_with_mcp` executes solely using MCP functions."""
    query = 'test query'
    mock_search_results = [{'id': '123'}, {'id': '456'}]
    mock_details = {'id': '123', 'detail': 'details about the data'}

    with patch('src.data_retrieval.mcp_entity_locator.search_data', return_value=mock_search_results) as mock_search,
         patch('src.data_retrieval.mcp_entity_locator.get_data_details', return_value=mock_details) as mock_get_details:

        retriever = MCPDataRetriever()
        result = retriever.retrieve_with_mcp(query)

        mock_search.assert_called_once_with(query)
        assert mock_get_details.call_count == len(mock_search_results)
        assert result == [mock_details for _ in mock_search_results]