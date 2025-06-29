"""Generate Sentiment Analysis DataFrame"""
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd


# Get text data and create DataFrame
df = pd.read_csv("engagements.csv")

# Initialize the NLTK sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Analyze sentiment
df['Sentiment_Scores'] = df['comment_text'].astype(str).apply(lambda x: sia.polarity_scores(x)['compound'])

# Define sentiment categories
df['Sentiment'] = df['Sentiment_Scores'].apply(lambda x: 'Positive' if x > 0.05 
                                             else ('Negative' if x < -0.05 
                                             else 'Neutral'))

# Filter for positive and negative sentiments
positive_df = df[df['Sentiment'] == 'Positive']

# Get the value counts of the 'media_caption' column
trends = positive_df['media_caption'].value_counts().reset_index()
trends.columns = ['Media Caption', 'Count']

# Return the top 5 trends
trends.head(5)


#Creates a bar chart to visualize the top 5 media captions with positive sentiment:

import plotly.express as px

df = pd.DataFrame(trends)

# Create a bar chart
fig = px.bar(df, x='Media Caption', y='Count', title='Top 5 Media Captions with Positive Sentiment')

# Show the chart
fig.show()