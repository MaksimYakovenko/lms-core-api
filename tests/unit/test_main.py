import pytest
from unittest import mock
from src.workflow.main import get_student_profile, profile_endpoint

@pytest.mark.asyncio
async def test_get_student_profile_valid():
    with mock.patch('src.workflow.main.connect', autospec=True) as mock_connect:
        mock_connection = mock.AsyncMock()
        mock_connect.return_value.__aenter__.return_value = mock_connection

        mock_connection.fetchrow.return_value = {'student_id': 1, 'name': 'John Doe'}

        result = await get_student_profile(1)

        assert result == {'student_id': 1, 'name': 'John Doe'}
        mock_connection.fetchrow.assert_called_once_with('SELECT *\n        FROM public.profiles\n        WHERE student_id = $1\n        LIMIT 1\n        ', 1)

@pytest.mark.asyncio
async def test_get_student_profile_not_found():
    with mock.patch('src.workflow.main.connect', autospec=True) as mock_connect:
        mock_connection = mock.AsyncMock()
        mock_connect.return_value.__aenter__.return_value = mock_connection

        mock_connection.fetchrow.return_value = None

        with pytest.raises(ValueError, match='Student profile with ID 2 not found'):
            await get_student_profile(2)

@pytest.mark.asyncio
async def test_get_student_profile_missing_env_var():
    with mock.patch('src.workflow.main.os.getenv', return_value=None):
        with pytest.raises(ValueError, match='DATABASE_URL environment variable not set'):
            await get_student_profile(1)

@pytest.mark.asyncio
async def test_profile_endpoint_valid():
    with mock.patch('src.workflow.main.get_student_profile', autospec=True) as mock_get_student_profile:
        mock_get_student_profile.return_value = {'student_id': 1, 'name': 'John Doe'}

        result = await profile_endpoint(1)

        assert result == {'student_id': 1, 'name': 'John Doe'}
        mock_get_student_profile.assert_called_once_with(1)