import streamlit as st

def quiz():
    st.title("Welcome to the Quiz by Vignesh 🤖")
    st.write("Let's play 😉 ")

    score = 0

    # Question 1
    answer = st.text_input("Question 1: What does CPU stand for in a computer? 🖥️ ")
    if answer.lower() == "central processing unit":
        st.write("Correct!")
        score += 1
    else:
        st.write("Incorrect!")

    # Question 2
    answer = st.text_input("Question 2: What is the capital of France? 🇫🇷 ")
    if answer.lower() == "paris":
        st.write("Correct!")
        score += 1
    else:
        st.write("Incorrect!")

    # Question 3
    answer = st.text_input("Question 3: Who painted the Mona Lisa? 🎨 ")
    if answer.lower() == "leonardo da vinci":
        st.write("Correct!")
        score += 1
    else:
        st.write("Incorrect!")

    # Question 4
    answer = st.text_input("Question 4: Which planet is known as the Red Planet? 🪐 ")
    if answer.lower() == "mars":
        st.write("Correct!")
        score += 1
    else:
        st.write("Incorrect!")

    # Question 5
    answer = st.text_input("Question 5: What is the chemical symbol for gold? 🌟 ")
    if answer.lower() == "au":
        st.write("Correct!")
        score += 1
    else:
        st.write("Incorrect!")

    st.write("Quiz completed! Your score is:", score)
    percentage = (score / 5) * 100
    st.write("You got", str(percentage) + "%")

if __name__ == '__main__':
    playing = st.radio("Do you want to play?", ["Yes 👍🏻 ", "No 👎🏻 "])

    if playing == "Yes 👍🏻 ":
        quiz()
    else:
        st.write("Okay, maybe next time! 🥲 ")
