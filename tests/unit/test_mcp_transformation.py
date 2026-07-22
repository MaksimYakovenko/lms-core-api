from __future__ import annotations

import pytest
import os
import asyncpg
from src.data_catalog.mcp_transformation import MCPInteractor, DataCatalog

DATABASE_URL = "postgres://user:password@localhost:5432/database"

@pytest.fixture
async def mcp_interactor() -> MCPInteractor:
    return MCPInteractor(connection_url=DATABASE_URL)

@pytest.fixture
async def data_catalog(mcp_interactor: MCPInteractor) -> DataCatalog:
    return DataCatalog(mcp_interactor=mcp_interactor)

@pytest.mark.asyncio
async def test_fetch_data(mcp_interactor: MCPInteractor) -> None:
    query = "SELECT * FROM sample_table"
    result = await mcp_interactor.fetch_data(query)
    assert isinstance(result, list)

@pytest.mark.asyncio
async def test_transform_data(data_catalog: DataCatalog) -> None:
    query = "SELECT * FROM sample_table"
    result = await data_catalog.transform_data(query)
    assert isinstance(result, list)
