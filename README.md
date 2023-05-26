# DeFiChain ChatGPT Plugin

> https://defichain-chatgpt-plugin.fly.dev

## Core objectives

1. Can answer questions about DeFiChain.
2. Can get live blockchain data.

## How do we achieve this?

1. Retrieve relevant documents from the `DeFiChainWiki` Qdrant vector database to provide ChatGPT with relevant information.
   1. Get a query from ChatGPT.
   2. Embed the query with the OpenAI API.
   3. Retrieve similar documents from the `DeFiChainWiki` Qdrant vector database.
2. Use Ocean API under the hood for blockchain data.
   1. This ist till in the works.

## Implementation

- API is written in Python using Flask.
- Containerized using Docker.
- Deployed on Fly.io.

## Key components

The following components are key to the implementation of the plugin.

### Plugin definition

- Source: [`.well-known/ai-plugin.json`](./src/.well-known/ai-plugin.json)
- Live at: https://defichain-chatgpt-plugin.fly.dev/.well-known/ai-plugin.json
- Docs: https://platform.openai.com/docs/plugins/getting-started/plugin-manifest

### OpenAPI definition

- Source: [`.well-known/openapi.yaml`](./src/.well-known/openapi.yaml)
- Live at: https://defichain-chatgpt-plugin.fly.dev/.well-known/openapi.yaml
- To test: [Swagger Editor](https://editor-next.swagger.io/)
- Docs: https://platform.openai.com/docs/plugins/getting-started/openapi-definition

### Logo

- Source: [`.well-known/logo.png`](./src/.well-known/logo.png)
- Live at: https://defichain-chatgpt-plugin.fly.dev/.well-known/logo.png

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

## Docker

We use Docker to package and run the Plugin API. This makes the deployment more reliable and easier.

When deploying to Fly.io, we don't use Docker commands ourselves. The generation of the Docker image is done by Fly.io.

### Create image

```
docker build -t defichain-chatgpt-plugin .
```

### Run the image

```
docker container run --name DeFiChain_ChatGPT_Plugin --env-file .env -d -p 8080:8080 defichain-chatgpt-plugin
```
