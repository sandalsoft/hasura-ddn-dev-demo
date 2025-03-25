# Hasura DDN Dev Demo

This shows interacting with a Hasura DDN-powered API from the developer's perspective

## Usage

### Node

- `bun run get-customer-dashboard.js`

### Python

- `uv add requests`
- `uv run get_customer_dashboard.py`

### PromptQL

- Currently, you need a PromptQL API token (found in [Settings > PromptQL] page) to run this script. Export that token via: `export PROMPTQL_API_TOKEN=<enter_your-token_here>`
- The AI prompt is:
  `show me my iphone customers`
- The results and artifacts can be retrieved with `uv run iphone-users.prompt-ql.py`

### Schema

JSON:API Swagger docs can be found at: https://telco-jsonapi.hasura-demo.com/
