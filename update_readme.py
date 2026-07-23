from __future__ import annotations

import os
import httpx
from typing import Any, Dict

async def fetch_catalog_info() -> Dict[str, str]:
    """Fetch catalog information from the MCP API."""
    api_url = os.getenv("MCP_API_ENDPOINT")
    topic = os.getenv("KAFKA_TOPIC")
    if not api_url or not topic:
        raise ValueError("Required environment variables are missing.")
    
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{api_url}/topics/{topic}")
        response.raise_for_status()
        data: Dict[str, Any] = response.json()
    
    catalog_info = {
        "topic_name": data["topicName"],
        "entity_name": data["entityName"],
        "catalog_link": data["catalogLink"],
        "steward_email": data["stewardEmail"]
    }
    
    return catalog_info

async def update_readme() -> None:
    """Update the README file with catalog information."""
    catalog_info = await fetch_catalog_info()
    readme_path = "docs/README.md"
    with open(readme_path, "r") as file:
        lines = file.readlines()
    
    start_line = lines.index("## Data Catalog\n")
    new_content = [
        "- **Topic Name**: {topic_name}\n",
        "- **Entity Name**: {entity_name}\n",
        "- **Catalog Link**: [View in Catalog]({catalog_link})\n",
        "- **Steward Email**: {steward_email}\n"
    ]

    content_to_write = "".join(lines[:start_line+1]) + "\n".join(new_content).format(**catalog_info)
    
    with open(readme_path, "w") as file:
        file.write(content_to_write)

if __name__ == "__main__":
    import asyncio
    asyncio.run(update_readme())
