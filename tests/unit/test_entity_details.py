import pytest
from unittest.mock import Mock, create_autospec
from src.data_catalog.entity_details import EntityDetailsFetcher


def test_get_details_success():
    """Test fetching valid entity details."""
    # Mock the MCP client
    mcp_client_mock = Mock()
    mcp_client_mock.get_data_details.return_value = {
        'basic': 'data1',
        'governance': 'data2',
        'links': 'data3',
    }

    # Initialize the EntityDetailsFetcher
    fetcher = EntityDetailsFetcher(mcp_client=mcp_client_mock)

    # Invoke the `get_details` and test the result
    result = fetcher.get_details(entity_id="entity123")

    assert result == {
        'basic': 'data1',
        'governance': 'data2',
        'links': 'data3'
    }, "The returned details should match the expected output"
    mcp_client_mock.get_data_details.assert_called_once_with(
        "entity123", sections=['basic', 'governance', 'links']
    )