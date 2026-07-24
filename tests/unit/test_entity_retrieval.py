import pytest
import unittest.mock as mock
from src.data_catalog.entity_retrieval import DataCatalog, get_environment_variable, create_data_catalog

pytestmark = pytest.mark.asyncio

async def test_retrieve_entity_details_valid():
    db_mock = mock.AsyncMock()
    db_mock.fetchrow.return_value = {
        "entity_id": "entity1",
        "basic": "basic_data",
        "governance": "governance_data",
        "links": "links_data"
    }
    with mock.patch("asyncpg.create_pool", return_value=mock.MagicMock(acquire=mock.AsyncMock(return_value=db_mock))):
        catalog = DataCatalog(db_url="mock_url")
        result = await catalog.retrieve_entity_details(entity_id="entity1")
        assert result == {
            "entity_id": "entity1",
            "basic": "basic_data",
            "governance": "governance_data",
            "links": "links_data"
        }

async def test_retrieve_entity_details_not_found():
    db_mock = mock.AsyncMock()
    db_mock.fetchrow.return_value = None
    with mock.patch("asyncpg.create_pool", return_value=mock.MagicMock(acquire=mock.AsyncMock(return_value=db_mock))):
        catalog = DataCatalog(db_url="mock_url")
        with pytest.raises(ValueError, match="Entity entity1 not found."):
            await catalog.retrieve_entity_details(entity_id="entity1")

def test_get_environment_variable_success():
    env_value = "mock_db_url"
    with mock.patch.dict("os.environ", {"DATABASE_URL": env_value}):
        result = get_environment_variable("DATABASE_URL")
        assert result == env_value

def test_get_environment_variable_missing():
    with mock.patch.dict("os.environ", {}, clear=True):
        with pytest.raises(EnvironmentError, match="Environment variable DATABASE_URL is not set."):
            get_environment_variable("DATABASE_URL")

def test_create_data_catalog():
    env_value = "mock_db_url"
    with mock.patch.dict("os.environ", {"DATABASE_URL": env_value}):
        catalog = create_data_catalog()
        assert catalog.db_url == env_value