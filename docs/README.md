# Verify Exclusivity of MCP Data Usage

To ensure that data is always accessed using specified MCP tools and avoid hardcoding or manual data entry, we use the following standards:

## Guidelines

- Always retrieve data exclusively through MCP tools, such as `search_data` and `get_data_details`.
- Never hardcode data or manually input values.
- Use the fallback mechanisms provided within the MCP tools in case of errors or data unavailability.

## Implementation Details

Developers must ensure that no direct connections to databases or manual configuration adjustments are performed. Only use the MCP APIs to fetch, query, and manage data.

To enforce this standard, validation mechanisms and reviews are in place during both the development and deployment stages.
