import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string
import streamlit as st

# Load the text file and preprocess the data
with open('moby_dick.txt', 'r', encoding='utf-8') as f:
    data = f.read().replace('\n', ' ')

# Tokenize the text into sentences
sentences = sent_tokenize(data)

# Define a function to preprocess each sentence
def preprocess(sentence):
    # Tokenize the sentence into words
    words = word_tokenize(sentence)
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english')) - {'and', 'his', 'in', 'the', 'a'}
    words = [word.lower() for word in words if word.lower() not in stop_words and word not in string.punctuation]
    # Lemmatize the words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    return words

# Preprocess each sentence in the text
corpus = [preprocess(sentence) for sentence in sentences]

def get_most_relevant_sentence(query):
    # Preprocess the query
    query = preprocess(query)
    # Compute the similarity between the query and each sentence in the text
    max_similarity = 0
    most_relevant_sentence = ""
    for sentence in corpus:
        relevance_scores = []
        for keyword in query:
            if keyword in sentence:
                relevance_scores.append(1)
            else:
                relevance_scores.append(0)
        similarity = sum(relevance_scores) / len(query)
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
    st.write("Hello! I'm a chatbot. Ask me anything about Moby Dick.")
    # Get the user's question
    question = st.text_input("You:")
    # Create a button to submit the question
    if st.button("Submit"):
        # Call the chatbot function with the question and display the response
        response = chatbot(question)
        st.write("Chatbot:", response)

if __name__ == "__main__":
    main()
