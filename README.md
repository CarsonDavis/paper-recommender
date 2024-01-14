# paper-recommender
LLM-based system to recommend papers

## Setup
Weaviate needs a special version, so we need to install like this:
`pip install --pre -r requirements.txt`

## Start Weaviate
Run `docker compose up -d` in the root directory of this repository.

If this is your first time setting up weaver, you will need to provide an api key for gpt in the .env file. Use the .env-example as a starting place.
