import requests
import json

from load_client import client


# Class definition object. Weaviate's autoschema feature will infer properties when importing.
class_obj = {
    "class": "Question",
    "vectorizer": "text2vec-openai",  # If set to "none" you must always provide vectors yourself. Could be any other "text2vec-*" also.
    "moduleConfig": {
        "text2vec-openai": {},
        "generative-openai": {}  # Ensure the `generative-openai` module is used for generative queries
    }
}

# Add the class to the schema
client.schema.create_class(class_obj)
