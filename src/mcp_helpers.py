from __future__ import annotations

async def get_data_from_mcp(data_id: str) -> dict:
    """Fetches data from the MCP using the get_data_details tool."""
    # Simulate API logic (should be implemented using the real MCP APIs)
    import asyncio
    await asyncio.sleep(0.1)  # Simulate async I/O
    return {"id": data_id, "name": "Sample Data", "value": 42}

async def search_data_in_mcp(query: str) -> list[dict]:
    """Searches data entries in the MCP using the search_data tool."""
    # Simulate API logic (should be implemented using the real MCP APIs)
    import asyncio
    await asyncio.sleep(0.1)  # Simulate async I/O
    return [{"id": "data1", "name": "Sample Data 1"}, {"id": "data2", "name": "Sample Data 2"}]
