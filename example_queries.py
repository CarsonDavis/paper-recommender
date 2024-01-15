import json

from load_client import client


# query for vectors related to materials engineering
response = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text({"concepts": ["materials engineering"]})
    .with_limit(2)
    .do()
)
print(json.dumps(response, indent=4))


# filter by category = "ANIMALS"
response = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text({"concepts": ["biology"]})
    .with_where({
        "path": ["category"],
        "operator": "Equal",
        "valueText": "ANIMALS"
    })
    .with_limit(2)
    .do()
)
print(json.dumps(response, indent=4))


# generate text for each database reponse, in these case, combining the question and answer into a single prompt
response = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text({"concepts": ["biology"]})
    .with_generate(single_prompt="Explain why {answer} is the answer to the question '{question}', as you might to a five-year-old.")
    .with_limit(2)
    .do()
)
print(json.dumps(response, indent=4))


# write a tweet about each database response. i think that it sends both responses to the same prompt, so the output is a single tweet
response = (
    client.query
    .get("Question", ["question", "answer", "category"])
    .with_near_text({"concepts": ["biology"]})
    .with_generate(grouped_task="Write a tweet with emojis about these facts.")
    .with_limit(2)
    .do()
)

print(json.dumps(response, indent=4))
print(response["data"]["Get"]["Question"][0]["_additional"]["generate"]["groupedResult"])
