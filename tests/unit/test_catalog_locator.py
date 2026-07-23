import pytest
from unittest.mock import AsyncMock, Mock
from modules.catalog_locator import CatalogLocator, MCPClient

# Test for CatalogLocator class
def test_locate_success():
    """Ensure locate works for a matching kafka topic."""
    
    # Mock MCPClient with expected behavior
    mock_mcp_client = Mock(spec=MCPClient)
    mock_mcp_client.search_data.return_value = {"id": "1234", "name": "epm-skls-ai.courses-to-take"}
    mock_mcp_client.get_data_details.return_value = {"id": "1234", "name": "Entity Details"}

    # Instantiate CatalogLocator
    kafka_topic = "epm-skls-ai.courses-to-take"
    locator = CatalogLocator(mcp_client=mock_mcp_client, kafka_topic=kafka_topic)

    # Call locate method and verify the expected output
    result = locator.locate()
    expected = {"id": "1234", "name": "Entity Details"}
    assert result == expected
    
    # Verify calls to mocked MCPClient
    mock_mcp_client.search_data.assert_called_once_with(kafka_topic)
    mock_mcp_client.get_data_details.assert_called_once_with("1234")

def test_locate_no_match():
    """Ensure locate raises when no entity matches the topic."""
    
    # Mock MCPClient with no match behavior
    mock_mcp_client = Mock(spec=MCPClient)
    mock_mcp_client.search_data.return_value = None

    # Instantiate CatalogLocator
    kafka_topic = "non_existent_topic"
    locator = CatalogLocator(mcp_client=mock_mcp_client, kafka_topic=kafka_topic)

    # Call locate method and verify it raises the expected exception
    with pytest.raises(ValueError, match=f"No entity found for topic: {kafka_topic}"):
        locator.locate()
    
    # Verify calls to mocked MCPClient
    mock_mcp_client.search_data.assert_called_once_with(kafka_topic)
    mock_mcp_client.get_data_details.assert_not_called()