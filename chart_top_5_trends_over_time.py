import pandas as pd
import plotly.express as px
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# 1. Perform Sentiment Analysis
# Get the raw data from the source table
df = pd.read_csv("engagements.csv")

# Initialize the NLTK sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Analyze sentiment for each comment
df['Sentiment_Scores'] = df['comment_text'].astype(str).apply(lambda x: sia.polarity_scores(x)['compound'])

# Define sentiment categories
df['Sentiment'] = df['Sentiment_Scores'].apply(lambda x: 'Positive' if x > 0.05 
                                             else ('Negative' if x < -0.05 
                                             else 'Neutral'))

# 2. Identify Top 5 Trends
# Filter for positive sentiment
positive_df = df[df['Sentiment'] == 'Positive'].copy()

# Get the top 5 media captions with the most positive comments
top_5_captions = positive_df['media_caption'].value_counts().nlargest(5).index

# Filter the DataFrame to include only data for the top 5 captions
top_5_df = positive_df[positive_df['media_caption'].isin(top_5_captions)]

# 3. Create the Time-Series Chart
# Convert timestamp to datetime and extract just the date
top_5_df.loc[:, 'date'] = pd.to_datetime(top_5_df['timestamp']).dt.date


# Group by date and media caption to get daily counts of positive comments
daily_trends = top_5_df.groupby(['date', 'media_caption']).size().reset_index(name='count')

# Create the line chart
fig = px.line(
    daily_trends, 
    x='date', 
    y='count', 
    color='media_caption', 
    title='Daily Positive Sentiment Trends for Top 5 Media Captions'
)

# Update layout for clarity
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Number of Positive Comments",
    legend_title="Media Caption"
)

# Show the chart in the sheet
fig.show()
