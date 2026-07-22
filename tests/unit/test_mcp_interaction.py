from __future__ import annotations

import os
import pytest
from aiohttp import web
import aiohttp

from src.data_catalog.mcp_interaction import MCPInteraction

@pytest.fixture
async def mock_server(aiohttp_server):
    def search_handler(request):
        return web.json_response({"results": [{"id": "12345"}]})

    def details_handler(request):
        return web.json_response({"id": "12345", "name": "example-topic", "type": "KafkaTopic"})

    app = web.Application()
    app.router.add_post("/search", search_handler)
    app.router.add_get("/details/{entity_id}", details_handler)

    return await aiohttp_server(app)

@pytest.mark.asyncio
async def test_mcp_interaction(mock_server) -> None:
    base_url = str(mock_server.make_url(""))
    mcp_service = MCPInteraction(base_url=base_url)

    filters = {"type": "KafkaTopic", "name": "example-topic"}
    search_results = await mcp_service.search_data(filters=filters)
    assert len(search_results["results"]) > 0

    entity_id = search_results["results"][0]["id"]
    entity_details = await mcp_service.get_data_details(entity_id=entity_id)
    assert entity_details["id"] == entity_id
