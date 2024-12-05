import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the model
@st.cache(allow_output_mutation=True)
def load_model():
    # with open("nlp_fnd_model.pkl", "rb") as file:
    with open("nlp_fnd_model.pkl", "rb") as file:
    # your code here
        model = pickle.load(file)
    return model



model = load_model()


st.title("Fake News Detection")
st.write("Enter a news article and click the button to check if it is real or fake.")

# Text input for user to enter news article
user_input = st.text_area("Enter News Article")

if st.button("Check News"):
    if user_input:
        try:

            # Make prediction
            prediction = model.predict([user_input])
            # Display result
            if prediction == 1:
                st.success("The news is REAL.")
            else:
                st.error("The news is FAKE.")
        except:
            st.error("Failed to process the news article. Please try again.")
    else:
        st.warning("Please enter some news text.")
