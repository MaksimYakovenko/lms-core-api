import os
import pytest
from unittest import mock
from update_readme import fetch_catalog_info, update_readme

@pytest.mark.asyncio
async def test_fetch_catalog_info_success():
    """Test the fetch_catalog_info function with a successful API call."""

    mock_response_data = {
        "topicName": "test_topic",
        "entityName": "test_entity",
        "catalogLink": "http://test.link",
        "stewardEmail": "test@example.com"
    }

    with mock.patch.dict(os.environ, {"MCP_API_ENDPOINT": "http://test.api", "KAFKA_TOPIC": "test_topic"}):
        with mock.patch("httpx.AsyncClient.get") as mock_get:
            mock_get.return_value.__aenter__.return_value.json.return_value = mock_response_data
            mock_get.return_value.__aenter__.return_value.raise_for_status.return_value = None

            result = await fetch_catalog_info()

            assert result == {
                "topic_name": "test_topic",
                "entity_name": "test_entity",
                "catalog_link": "http://test.link",
                "steward_email": "test@example.com"
            }

@pytest.mark.asyncio
async def test_fetch_catalog_info_missing_env():
    """Test fetch_catalog_info when mandatory environment variables are missing."""
    with mock.patch.dict(os.environ, {}, clear=True):
        with pytest.raises(ValueError, match="Required environment variables are missing."):
            await fetch_catalog_info()

@pytest.mark.asyncio
async def test_update_readme():
    """Test the update_readme function."""
    with mock.patch("update_readme.fetch_catalog_info") as mock_fetch_catalog_info:
        mock_fetch_catalog_info.return_value = {
            "topic_name": "test_topic",
            "entity_name": "test_entity",
            "catalog_link": "http://test.link",
            "steward_email": "test@example.com"
        }

        mock_file_data = "# README\n\n## Data Catalog\nSample text.\n"
        with mock.patch("builtins.open", mock.mock_open(read_data=mock_file_data)) as mock_file:
            await update_readme()

            mock_file().write.assert_called_once_with(
                "# README\n\n## Data Catalog\n- **Topic Name**: test_topic\n- **Entity Name**: test_entity\n- **Catalog Link**: [View in Catalog](http://test.link)\n- **Steward Email**: test@example.com"
            )