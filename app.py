import streamlit as st

# Set the title of the web app
st.title("Welcome to Amir's Ph.D. Thesis")

# Add a text input field for the user's name
user_name = st.text_input("Enter your name:")

# Check if the user has entered a name and clicked the button
if st.button("Submit"):
    # Display a personalized greeting message
    st.success(f"Hello, {user_name}! Welcome to Streamlit.")

# Display a simple slider widget
age = st.slider("Select your age:", 10, 100, 25)
st.write(f"Your selected age is: {age}")