import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Get correct dataset path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "dataset", "resources.csv")

# Load dataset
df = pd.read_csv(DATA_PATH)

# Fill missing values
df = df.fillna("")

def recommend(topic):

    topic = topic.lower().strip()

    # Filter by subject or topic
    filtered_df = df[
        df["topic"].str.lower().str.contains(topic, na=False) |
        df["subject"].str.lower().str.contains(topic, na=False)
    ]

    if filtered_df.empty:
        return df.head(0)[["title","resource_link","resource_type"]]

    # Create text content
    content = filtered_df["topic"] + " " + filtered_df["title"] + " " + filtered_df["description"]

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(content)

    query_vector = vectorizer.transform([topic])

    similarity = cosine_similarity(query_vector, tfidf_matrix)

    top_indices = similarity.argsort()[0][-5:][::-1]

    results = filtered_df.iloc[top_indices]

    return results[["title","resource_link","resource_type"]]