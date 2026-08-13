import pytest
import asyncpg
from unittest.mock import Mock, AsyncMock, patch
from src.student_profile.data import StudentDataAccess

@pytest.mark.asyncio
async def test_initialize_creates_pool():
    with patch('asyncpg.create_pool', new_callable=AsyncMock) as mock_create_pool:
        db_access = StudentDataAccess()
        await db_access.initialize()
        mock_create_pool.assert_called_once_with(db_access.DATABASE_URL)

@pytest.mark.asyncio
async def test_close_pool_closes_pool():
    db_access = StudentDataAccess()
    db_access.pool = Mock()
    db_access.pool.close = AsyncMock()
    await db_access.close()
    db_access.pool.close.assert_called_once()

@pytest.mark.asyncio
async def test_get_student_profile_returns_profile():
    db_access = StudentDataAccess()
    db_access.pool = Mock()
    db_access.pool.acquire = AsyncMock()

    mock_connection = AsyncMock()
    db_access.pool.acquire.return_value.__aenter__.return_value = mock_connection

    mock_connection.fetchrow.return_value = {'id': 1, 'name': 'John Doe'}

    result = await db_access.get_student_profile(1)
    assert result == {'id': 1, 'name': 'John Doe'}
    mock_connection.fetchrow.assert_called_once_with('SELECT * FROM students WHERE id = $1;', 1)

@pytest.mark.asyncio
async def test_get_student_profile_returns_none():
    db_access = StudentDataAccess()
    db_access.pool = Mock()
    db_access.pool.acquire = AsyncMock()

    mock_connection = AsyncMock()
    db_access.pool.acquire.return_value.__aenter__.return_value = mock_connection

    mock_connection.fetchrow.return_value = None

    result = await db_access.get_student_profile(1)
    assert result is None
    mock_connection.fetchrow.assert_called_once_with('SELECT * FROM students WHERE id = $1;', 1)

@pytest.mark.asyncio
async def test_get_student_profile_raises_if_pool_not_initialized():
    db_access = StudentDataAccess()
    db_access.pool = None
    with pytest.raises(ValueError, match="Connection pool is not initialized."):
        await db_access.get_student_profile(1)