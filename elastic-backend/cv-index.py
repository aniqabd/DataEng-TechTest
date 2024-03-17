from elasticsearch import Elasticsearch, helpers
import pandas as pd
import json

# Initialize Elasticsearch client with the Elasticsearch server running on localhost port 9200
es = Elasticsearch("http://localhost:9200")

# Function to index data into Elasticsearch:
# Read the updated CSV file containing transcriptions and prepare bulk indexing actions with 'helpers'
def index_data():
    df = pd.read_csv("cv-valid-dev-updated.csv")
    actions = [
        {
            "_index": "cv-transcriptions",
            "_type": "document",
            "_source": {
                "generated_text": row["generated_text"],
                "duration": row["duration"],
                "age": row["age"],
                "gender": row["gender"],
                "accent": row["accent"]
            }
        }
        for index, row in df.iterrows()
    ]

    helpers.bulk(es, actions)

if __name__ == '__main__':
    index_data()