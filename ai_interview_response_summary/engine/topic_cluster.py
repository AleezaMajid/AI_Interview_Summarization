from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

def cluster_topics(sentences):

    vectorizer = TfidfVectorizer(stop_words='english')

    X = vectorizer.fit_transform(sentences)

    kmeans = KMeans(n_clusters=2)

    kmeans.fit(X)

    return kmeans.labels_