import pandas as pd
import matplotlib.pyplot as plt

# i. Read the dataset and perform data cleaning operations
data = pd.read_csv("INvideos.csv")

# Remove rows with missing values
data.dropna(inplace=True)

# ii. Calculate total views, likes, dislikes, and comment count
total_views = data['views'].sum()
total_likes = data['likes'].sum()
total_dislikes = data['dislikes'].sum()
total_comments = data['comment_count'].sum()

print("Total views:", total_views)
print("Total likes:", total_likes)
print("Total dislikes:", total_dislikes)
print("Total comment count:", total_comments)

# iii. Find the least and topmost liked and commented videos
least_liked_video = data.loc[data['likes'].idxmin()]
most_liked_video = data.loc[data['likes'].idxmax()]
least_commented_video = data.loc[data['comment_count'].idxmin()]
most_commented_video = data.loc[data['comment_count'].idxmax()]

print("\nLeast liked video:")
print(least_liked_video[['title', 'likes']])
print("\nMost liked video:")
print(most_liked_video[['title', 'likes']])
print("\nLeast commented video:")
print(least_commented_video[['title', 'comment_count']])
print("\nMost commented video:")
print(most_commented_video[['title', 'comment_count']])

# iv. Perform year-wise statistics for views and plot the analyzed data
data['trending_date'] = pd.to_datetime(data['trending_date'], errors='coerce')
data['publish_time'] = pd.to_datetime(data['publish_time'], errors='coerce')

data['publish_year'] = data['publish_time'].dt.year
yearly_views = data.groupby('publish_year')['views'].sum()

plt.figure(figsize=(10, 5))
yearly_views.plot(kind='bar')
plt.title('Year-wise Total Views')
plt.xlabel('Year')
plt.ylabel('Total Views')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# v. Plot the viewers who reacted on videos
reaction_counts = data[['likes', 'dislikes']].sum()

plt.figure(figsize=(6, 6))
reaction_counts.plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightcoral'])
plt.title('Distribution of Reactions')
plt.ylabel('')
plt.show()
