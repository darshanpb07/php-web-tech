import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Read the dataset
data = pd.read_csv("top_1000_instagram_influencers.csv")

# i. Find the top 5 Instagram influencers from India
top_5_indian_influencers = data[data['country'] == 'India'].nlargest(5, 'followers')
print("Top 5 Instagram influencers from India:")
print(top_5_indian_influencers[['username', 'followers']])

# ii. Find the Instagram account having the least number of followers
least_followers_account = data.nsmallest(1, 'followers')
print("\nInstagram account with the least number of followers:")
print(least_followers_account[['username', 'followers']])

# iii. Remove stopwords from the 'Category' column and plot wordcloud
stop_words = set(stopwords.words('english'))
category_words = ' '.join(data['category'].dropna())
word_tokens = word_tokenize(category_words.lower())
filtered_words = [word for word in word_tokens if word not in stop_words]
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(filtered_words))

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Wordcloud of Categories')
plt.show()

# iv. Group Instagram accounts category-wise
category_counts = Counter(data['category'].dropna())
print("\nCategory-wise counts:")
for category, count in category_counts.items():
    print(f"{category}: {count}")

# v. Visualize the relationship between Followers and Authentic engagement columns
plt.figure(figsize=(10, 6))
plt.scatter(data['followers'], data['authentic engagement'], alpha=0.5)
plt.title('Relationship between Followers and Authentic Engagement')
plt.xlabel('Followers')
plt.ylabel('Authentic Engagement')
plt.grid(True)
plt.show()
