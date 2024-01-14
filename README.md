# paper-recommender
LLM-based system to recommend papers

## Start Weaviate
Run `docker compose up -d` in the root directory of this repository.

If this is your first time setting up weaver, you will need to provide an api key for gpt.

Since it is best practice to never store secrets in an infrastructure file, the resulting docker-compose transcript will read your API key from an environment variable. Make sure you have an environment variable OPENAI_APIKEY set on your host machine that contains the key. For example you can run "export OPENAI_APIKEY=my-key-here" prior to running "docker-compose up". You can also provide the key with each request using the X-OpenAI-Api-Key header.
