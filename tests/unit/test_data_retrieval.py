# tests/unit/test_data_retrieval.py

import pytest
from unittest.mock import patch
from src.app.data_retrieval import search_data, get_data_details, retrieve_entities

def test_search_data_returns_expected_entities():
    result = search_data(query="test")
    assert result == ["entity1", "entity2"], "search_data didn't return expected entities"

def test_get_data_details_returns_correctly():
    entity_id = "entity1"
    result = get_data_details(entity_id=entity_id)
    assert result == {"id": "entity1", "name": "EntityName"}, "get_data_details didn't return correct entity details"
@patch('src.app.data_retrieval.search_data')
@patch('src.app.data_retrieval.get_data_details')
def test_retrieve_entities_calls_methods_correctly(mock_get_data_details, mock_search_data):
    query = "TestQuery"
    mock_search_data.return_value = ["entity1", "entity2"]
    mock_get_data_details.side_effect = lambda entity_id: {"id": entity_id, "name": "MockName"}
    result = retrieve_entities(query=query)
    assert result == [
        {"id": "entity1", "name": "MockName"},
        {"id": "entity2", "name": "MockName"}
    ], "retrieve_entities didn't call methods correctly or return expected results"
    mock_search_data.assert_called_once_with(query="TestQuery")
    mock_get_data_details.assert_has_calls([
        patch.call("entity1"),
        patch.call("entity2")
    ]), "Expected calls to get_data_details were not made"