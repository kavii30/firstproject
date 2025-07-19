import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load movies list from pickle
movies = pickle.load(open('artifacts/movie_list.pkl', 'rb'))

# Vectorize the tags column
cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(movies['tags']).toarray()

# Compute cosine similarity matrix
similarity = cosine_similarity(vectors)

# Save similarity matrix
pickle.dump(similarity, open('artifacts/similarity.pkl', 'wb'))
