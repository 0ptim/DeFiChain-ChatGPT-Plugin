# DeFiChain ChatGPT Plugin

ChatGPT Plugin for Defichain.

## Core objectives

1. Can answer questions about DeFiChain.
2. Can get live blockchain data.

## Implementation overview

1. Retrieve relevant documents from the `DeFiChainWiki` Qdrant vector database to provide ChatGPT with relevant information.
2. Relay Ocean API requests to the Ocean API.

## Implementation details

- We'll create a Python Flask app that will serve all the endpoints and the plugin definition.
- The API will be hosted on fly.io.
- We'll use Docker to containerize the app.
- The Qdrant vector database is already created and live on Qdrant Cloud (Already used by JellyChat).

### Plugin Definition

_https://platform.openai.com/docs/plugins/getting-started/plugin-manifest_

Hosted at: [`/.well-known/ai-plugin.json`](./src/.well-known/ai-plugin.json)

### OpenAPI definition

_https://platform.openai.com/docs/plugins/getting-started/openapi-definition_

Hosted at: [`/.well-known/openapi.yaml`](./src/.well-known/openapi.yaml)

## Basic commands

### Create virtual environment

```
python -m venv venv
```

### Activate virtual environment

```
.\venv\Scripts\activate
```

### Deactivate virtual environment

```
Deactivate
```
