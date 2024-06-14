import pandas as pd
import plotly.express as px
from textblob import TextBlob
import spacy


# Load spaCy model
nlp = spacy.load("en_core_web_sm")
# Load data
data = pd.read_csv('data.csv')


def analyze_sentiment(text):
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0:
        return polarity, "Positive"
    elif polarity < 0:
        return polarity, "Negative"
    else:
        return polarity, "Neutral"

def extract_key_phrases(text):
    return [chunk.text for chunk in nlp(text).noun_chunks]

def evaluate_answer(answer, expected_phrases):
    expected_phrases_list = expected_phrases.lower().split(', ')
    found_phrases = [phrase for phrase in expected_phrases_list if phrase in answer.lower()]
    total_phrases = len(expected_phrases_list)
    score = len(found_phrases) / total_phrases if total_phrases > 0 else 0
    return score, found_phrases


# process the dataset
data[['polarity', 'sentiment']] = data['answer'].apply(lambda x: pd.Series(analyze_sentiment(x)))
data['key_phrases'] = data['answer'].apply(extract_key_phrases)
data[['relevance_score', 'found_phrases']] = data.apply(lambda row: pd.Series(evaluate_answer(row['answer'], 
                                                                                              row['expected_phrases'])), axis=1)
data['overall_quality'] = (data['polarity'] + data['relevance_score']) / 2

# save the result on a CSV
results_df = data[['answer', 'sentiment', 'key_phrases', 'overall_quality']]
results_df.to_csv('output.csv', index=False)

total_overall_score_percent = results_df['overall_quality'].mean() * 100
print(f"Final Overall Score: {total_overall_score_percent:.2f}%")


# frequency distribution of the sentiments
sentiment_counts = results_df['sentiment'].value_counts().reset_index()
sentiment_counts.columns = ['sentiment', 'count']

# visualize the distribution
fig = px.pie(sentiment_counts, values='count', names='sentiment', title='Sentiment Analysis of Interview Answers', 
             hover_data=['count'], labels={'count': 'Number of Responses'})
fig.update_traces(textinfo='percent+label')
fig.show()
