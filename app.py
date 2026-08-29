import streamlit as st

# ---------- Quiz Data ----------
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct": 1
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "correct": 2
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
        "correct": 1
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "correct": 3
    }
]

# ---------- Session State Initialization ----------
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_option = None
    st.session_state.quiz_finished = False

# ---------- Helper Functions ----------
def check_answer():
    """Check the selected answer and update score."""
    q_data = questions[st.session_state.current_question]
    if st.session_state.selected_option == q_data["correct"]:
        st.session_state.score += 1
    st.session_state.answered = True

def next_question():
    """Move to the next question or finish the quiz."""
    st.session_state.current_question += 1
    st.session_state.answered = False
    st.session_state.selected_option = None
    if st.session_state.current_question >= len(questions):
        st.session_state.quiz_finished = True

def restart_quiz():
    """Reset all session state variables."""
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.selected_option = None
    st.session_state.quiz_finished = False

# ---------- UI Layout ----------
st.set_page_config(page_title="Python Quiz", page_icon="🧠", layout="centered")

# Title and header
st.title("🧠 Python Quiz Game")
st.markdown("---")

# ---------- Quiz Logic ----------
if st.session_state.quiz_finished:
    # Final score screen
    st.balloons()
    st.header("🎉 Quiz Finished!")
    st.subheader(f"Your final score: **{st.session_state.score} / {len(questions)}**")
    if st.session_state.score == len(questions):
        st.success("Perfect score! You're a genius!")
    elif st.session_state.score >= len(questions) * 0.7:
        st.info("Great job! You know your stuff.")
    else:
        st.warning("Keep practicing! You'll get better.")
    st.button("Restart Quiz", on_click=restart_quiz)

else:
    # Display progress
    progress = st.session_state.current_question / len(questions)
    st.progress(progress)
    st.markdown(f"**Question {st.session_state.current_question + 1} of {len(questions)}**")
    st.markdown(f"**Score: {st.session_state.score}**")

    # Get current question data
    q_data = questions[st.session_state.current_question]
    st.subheader(q_data["question"])

    # Option selection (radio buttons)
    options = q_data["options"]
    selected = st.radio(
        "Choose your answer:",
        options,
        index=None,
        key=f"option_{st.session_state.current_question}",
        disabled=st.session_state.answered
    )
    st.session_state.selected_option = options.index(selected) if selected is not None else None

    # Layout for buttons
    col1, col2 = st.columns([1, 1])

    with col1:
        if not st.session_state.answered:
            if st.button("Submit", type="primary", use_container_width=True):
                if st.session_state.selected_option is not None:
                    check_answer()
                else:
                    st.warning("Please select an answer first.")

    with col2:
        if st.session_state.answered:
            if st.button("Next ➡️", type="primary", use_container_width=True):
                next_question()
                st.rerun()

    # Show feedback after answering
    if st.session_state.answered:
        correct_idx = q_data["correct"]
        if st.session_state.selected_option == correct_idx:
            st.success("✅ Correct!")
        else:
            st.error(f"❌ Incorrect! The correct answer was **{options[correct_idx]}**.")
