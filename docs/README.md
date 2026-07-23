# Verify Exclusivity of MCP Data Usage

To ensure that data is always accessed using specified MCP tools and avoid hardcoding or manual data entry, we use the following standards:

## Guidelines

- Always retrieve data exclusively through MCP tools, such as `search_data` and `get_data_details`.
- Never hardcode data or manually input values.
- Use the fallback mechanisms provided within the MCP tools in case of errors or data unavailability.

## Implementation Details

Developers must ensure that no direct connections to databases or manual configuration adjustments are performed. Only use the MCP APIs to fetch, query, and manage data.

## Data Catalog

The following details pertain to the data catalog information related to our Kafka topics:

```python
import os
import requests

def fetch_catalog_info() -> dict[str, str]:
    api_url = os.getenv("MCP_API_ENDPOINT")
    topic = os.getenv("KAFKA_TOPIC")
    if not api_url or not topic:
        raise ValueError("Missing required environment configuration.")
    response = requests.get(f"{api_url}/topics/{topic}")
    response.raise_for_status()
    data = response.json()
    return {
        "topic_name": data["topicName"],
        "entity_name": data["entityName"],
        "catalog_link": data["catalogLink"],
        "steward_email": data["stewardEmail"]
    }

def generate_documentation(catalog_info: dict[str, str]) -> str:
    documentation = (
        "## Data Catalog\n"
        "\n"
        f"- **Topic Name**: {catalog_info['topic_name']}\n"
        f"- **Entity Name**: {catalog_info['entity_name']}\n"
        f"- **Catalog Link**: [View in Catalog]({catalog_info['catalog_link']})\n"
        f"- **Steward Email**: {catalog_info['steward_email']}\n"
    )
    return documentation

if __name__ == "__main__":
    catalog_info = fetch_catalog_info()
    print("Documentation Updated with: ")
    print(generate_documentation(catalog_info))
