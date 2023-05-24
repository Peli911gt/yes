import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import string
import streamlit as st

# Load the text file and preprocess the data
with open('moby_dick.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace('\n', ' ')

# Tokenize the text into sentences
sentences = sent_tokenize(data)

# Preprocess each sentence in the text
def preprocess_sentence(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word.lower() for word in words if word.lower() not in stop_words and word not in string.punctuation]
    return words

# Preprocess each sentence in the text
corpus = [preprocess_sentence(sentence) for sentence in sentences]

# Define a function to find the most relevant sentence given a query
def get_most_relevant_sentence(query):
    # Preprocess the query
    query = preprocess_sentence(query)
    # Compute the similarity between the query and each sentence in the text
    max_similarity = 0
    most_relevant_sentence = ""
    for sentence in corpus:
        common_words = set(query).intersection(sentence)
        if len(sentence) > 0:
            # Calculate the frequency distribution of common words in the sentence
            sentence_freq_dist = FreqDist(sentence)
            # Calculate the relevance score by summing the frequencies of common words
            relevance_score = sum([sentence_freq_dist[word] for word in common_words])
            # Normalize the relevance score by the length of the sentence
            similarity = relevance_score / float(len(sentence))
            if similarity > max_similarity:
                max_similarity = similarity
                most_relevant_sentence = " ".join(sentence)
    return most_relevant_sentence

# Define the chatbot function
def chatbot(question):
    # Find the most relevant sentence
    most_relevant_sentence = get_most_relevant_sentence(question)
    # Return the answer
    return most_relevant_sentence

# Create a Streamlit app
def main():
    st.title("Chatbot")
    st.write("Hello! I'm a chatbot. Ask me anything about the topic in Moby Dick.")
    # Get the user's question
    question = st.text_input("You:")
    # Create a button to submit the question
    if st.button("Submit"):
        # Call the chatbot function with the question and display the response
        response = chatbot(question)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
