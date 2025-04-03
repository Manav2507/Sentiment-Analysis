import streamlit as st
import pickle

def load_model():
    with open("sentiment_pipeline.pkl", "rb") as f:
        sentiment_pipeline = pickle.load(f)
    return sentiment_pipeline

def main():
    st.title("Sentiment Analysis App")
    st.write("Enter your review below, and the model will predict the sentiment.")

    user_input = st.text_area("Enter your feedback:", "")

    sentiment_pipeline = load_model()

    if st.button("Predict"):
        if user_input:
            result = sentiment_pipeline(user_input)
            sentiment = result[0]['label']
            score = result[0]['score']

            st.subheader("Sentiment Prediction")
            st.write(f"**Sentiment:** {sentiment}")
            st.write(f"**Confidence Score:** {score:.2f}")

            if sentiment == "LABEL_2":
                st.success("This is a Positive Review! 😊")
            elif sentiment == "LABEL_0":
                st.error("This is a Negative Review! 😞")
            elif sentiment == "LABEL_1":
                st.warning("This is a Neutral Review! 😐")
        else:
            st.warning("Please enter text before clicking Predict.")

if __name__ == "__main__":
    main()
