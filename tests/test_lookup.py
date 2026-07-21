from __future__ import annotations

import os
import pytest
from data_catalog.lookup import perform_mcp_entity_lookup

def test_perform_mcp_entity_lookup() -> None:
    """Test the perform_mcp_entity_lookup function."""
    os.environ["KAFKA_TOPIC_NAME"] = "epm-skls-ai.courses-to-take"
    result = perform_mcp_entity_lookup(os.environ["KAFKA_TOPIC_NAME"])
    assert result["schema"] == "mock_schema_definition","Expected schema definition to match."

if __name__ == "__main__":
    pytest.main([__file__])
