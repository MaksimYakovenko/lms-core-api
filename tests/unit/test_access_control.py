from __future__ import annotations

import pytest

from src.security.access_control import validate_profile_access

def test_validate_profile_access_authorized() -> None:
    """Test valid access to the profile."""
    validate_profile_access(requesting_user_id=1, target_user_id=1)

def test_validate_profile_access_unauthorized() -> None:
    """Test unauthorized access to the profile."""
    with pytest.raises(Exception) as excinfo:
        validate_profile_access(requesting_user_id=1, target_user_id=2)
    assert excinfo.value.status_code == 403
    assert "Access denied" in excinfo.value.detail
