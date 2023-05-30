import streamlit as st

def main():
    st.title("Speech-enabled Chatbot")
    
    # Get user input
    text_input = st.text_input("Enter your message", "")
    
    if text_input:
        # Call chatbot algorithm to generate response
        response = chatbot(text_input)

        # Display the chatbot response
        st.text_area("Chatbot:", value=response, height=200)

if __name__ == "__main__":
    main()
