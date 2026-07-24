from __future__ import annotations

def search_data(query: str) -> list[str]:
    """Search data based on a query using MCP tools."""
    # Mocking the MCP interaction
    return ["entity1", "entity2"]

def get_data_details(entity_id: str) -> dict[str, str]:
    """Get data details by entity ID using MCP tools."""
    # Mocking the MCP interaction
    return {"id": entity_id, "name": "EntityName"}

def retrieve_entities(query: str) -> list[dict[str, str]]:
    """Retrieve entity details based on a search query."

    entity_ids = search_data(query)
    entities = [get_data_details(entity_id) for entity_id in entity_ids]
    
    return entities
