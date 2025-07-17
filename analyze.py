import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from app import get_video_details

df = get_video_details("Netflix trailer", max_results=50)  # noqa: F821
df['Published At'] = pd.to_datetime(df['Published At'])

# 📈 Top 10 most viewed videos
top_views = df.sort_values(by='Views', ascending=False).head(10)
plt.figure(figsize=(10, 6))
sns.barplot(data=top_views, x='Views', y='Video Title')
plt.title("Top 10 Most Viewed Videos")
plt.xlabel("Views")
plt.ylabel("Video Title")
plt.tight_layout()
plt.show()
# 📊 Views vs Likes scatter

plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Likes', y='Views')
plt.title("Views vs Likes")
plt.xlabel("Likes")
plt.ylabel("Views")
plt.grid(True)
plt.show()