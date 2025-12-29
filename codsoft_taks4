# CodSoft Python Internship Task
# Task Name: Rock Paper Scissors (Streamlit App)
# Author: Kaavya B M

import streamlit as st
import random

# Game choices
choices = ["rock", "paper", "scissors"]

# Initialize session state for scores
if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0

# App title
st.title("🎮 Rock Paper Scissors Game")

# Instructions
st.subheader("Instructions")
st.write("""
- Select **Rock**, **Paper**, or **Scissors**
- Rock beats Scissors  
- Scissors beats Paper  
- Paper beats Rock
""")

# User choice
user_choice = st.radio("Choose your option:", choices)

# Play button
if st.button("Play"):
    computer_choice = random.choice(choices)

    st.write(f"**You chose:** {user_choice}")
    st.write(f"**Computer chose:** {computer_choice}")

    # Decide winner
    if user_choice == computer_choice:
        st.info("It's a Tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        st.success("You Win this round!")
        st.session_state.user_score += 1
    else:
        st.error("Computer Wins this round!")
        st.session_state.computer_score += 1

# Scoreboard
st.subheader("Score Board")
st.write(f"👤 **Your Score:** {st.session_state.user_score}")
st.write(f"💻 **Computer Score:** {st.session_state.computer_score}")

# Reset button
if st.button("Reset Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.success("Game reset successfully!")

