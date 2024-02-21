import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK resources
nltk.download('punkt')
nltk.download('vader_lexicon')

# Read the dataset
data = pd.read_csv("covid_2021_1.csv")

# i. Data cleaning operations
# Remove rows with missing comments
data.dropna(subset=['comment'], inplace=True)

# ii. Tokenize the comments in words
data['tokenized_comments'] = data['comment'].apply(lambda x: word_tokenize(str(x)))

# iii. Perform sentiment analysis
sid = SentimentIntensityAnalyzer()
data['sentiment'] = data['comment'].apply(lambda x: sid.polarity_scores(str(x)))

# Function to determine sentiment category
def get_sentiment_category(sentiment):
    if sentiment['compound'] >= 0.05:
        return 'Positive'
    elif sentiment['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Add sentiment category column
data['sentiment_category'] = data['sentiment'].apply(get_sentiment_category)

# Calculate percentage of positive, negative, and neutral comments
sentiment_counts = data['sentiment_category'].value_counts(normalize=True) * 100

# Print results
print("Percentage of comments by sentiment category:")
print(sentiment_counts)

# Print first few rows of cleaned dataset
print("\nCleaned dataset:")
print(data.head())
