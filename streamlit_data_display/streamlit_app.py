import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud


def fetch_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return pd.DataFrame(response.json())
    else:
        return None


def main():
    st.title('Visualizations from FastAPI')

    # Fetching sentiment data from FastAPI
    sentiment_url = "http://127.0.0.1:8000/sentiment"
    sentiment = fetch_data(sentiment_url)

    # Fetching message count from FastAPI
    message_count_url = "http://127.0.0.1:8000/message_count"
    message_count = fetch_data(message_count_url)

    # Fetching topics count from FastAPI
    topics_url = "http://127.0.0.1:8000/topics"
    topics = fetch_data(topics_url)

    # Fetching reaction count from FastAPI
    reaction_count_url = "http://127.0.0.1:8000/reaction_count"
    reaction_count = fetch_data(reaction_count_url)
    if sentiment is not None and message_count is not None and topics is not None and reaction_count is not None:
        # Creating a Word Cloud
        st.subheader('Word Cloud')
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(
            dict(zip(message_count['sender_name'], message_count['count']))
        )

        # Displaying the Word Cloud
        fig, ax = plt.subplots(figsize=(10, 8))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)

        # Creating a Seaborn pairplot for data exploration
        st.subheader('Pair Plot')
        pair_plot = sns.pairplot(sentiment)
        st.pyplot(pair_plot)

        # Creating a pie chart for reaction_count
        st.subheader('Pie Chart')
        fig, ax = plt.subplots()
        ax.pie(reaction_count['reaction_count'], labels=reaction_count['user'], autopct='%1.1f%%')
        st.pyplot(fig)
    else:
        st.error("Failed to fetch data from FastAPI.")


if __name__ == '__main__':
    main()
