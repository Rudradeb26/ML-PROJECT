import tkinter as tk

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

# ---------- Main Application Class ----------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Quiz Game")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f4f7")

        # State variables
        self.current_question = 0
        self.score = 0

        # Fonts and colors
        self.question_font = ("Arial", 16, "bold")
        self.option_font = ("Arial", 12)
        self.button_font = ("Arial", 12, "bold")
        self.bg_color = "#f0f4f7"
        self.card_color = "#ffffff"
        self.primary_color = "#4a90d9"
        self.success_color = "#4caf50"
        self.danger_color = "#f44336"
        self.text_color = "#333333"

        # Build UI
        self.create_widgets()
        self.load_question()

    def create_widgets(self):
        # Score label (top right)
        self.score_label = tk.Label(
            self.root,
            text="Score: 0",
            font=self.button_font,
            bg=self.bg_color,
            fg=self.primary_color
        )
        self.score_label.pack(anchor="ne", padx=20, pady=10)

        # Main card frame (holds question and options)
        self.card = tk.Frame(self.root, bg=self.card_color, bd=2, relief="groove")
        self.card.pack(pady=10, padx=20, fill="both", expand=True)

        # Question label
        self.question_label = tk.Label(
            self.card,
            text="",
            font=self.question_font,
            bg=self.card_color,
            fg=self.text_color,
            wraplength=500,
            justify="center"
        )
        self.question_label.pack(pady=20, padx=20)

        # Options frame
        self.options_frame = tk.Frame(self.card, bg=self.card_color)
        self.options_frame.pack(pady=10, padx=20)

        # Buttons for the four options
        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(
                self.options_frame,
                text="",
                font=self.option_font,
                bg=self.primary_color,
                fg="white",
                activebackground="#3a7bc8",
                activeforeground="white",
                width=30,
                pady=8,
                command=lambda idx=i: self.check_answer(idx)
            )
            btn.grid(row=i//2, column=i%2, padx=10, pady=5)
            self.option_buttons.append(btn)

        # Next button (initially disabled)
        self.next_button = tk.Button(
            self.root,
            text="Next",
            font=self.button_font,
            bg=self.primary_color,
            fg="white",
            activebackground="#3a7bc8",
            activeforeground="white",
            state="disabled",
            command=self.next_question
        )
        self.next_button.pack(pady=20)

    def load_question(self):
        """Display the current question and its options."""
        q_data = questions[self.current_question]
        self.question_label.config(text=q_data["question"])

        # Reset option button styles and enable them
        for i, btn in enumerate(self.option_buttons):
            btn.config(
                text=q_data["options"][i],
                bg=self.primary_color,
                state="normal"
            )

        # Disable Next button until an answer is chosen
        self.next_button.config(state="disabled")

    def check_answer(self, selected_idx):
        """Handle answer selection, give feedback, and update score."""
        q_data = questions[self.current_question]
        correct_idx = q_data["correct"]

        # Disable all option buttons after selection
        for btn in self.option_buttons:
            btn.config(state="disabled")

        # Highlight correct and wrong answers
        self.option_buttons[correct_idx].config(bg=self.success_color)
        if selected_idx != correct_idx:
            self.option_buttons[selected_idx].config(bg=self.danger_color)
            # If user selected wrong, still show correct answer
        else:
            # Increment score if correct
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")

        # Enable Next button
        self.next_button.config(state="normal")

    def next_question(self):
        """Move to the next question or show final result."""
        self.current_question += 1
        if self.current_question < len(questions):
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        """Display the final score screen."""
        # Clear the card and show final score
        self.card.destroy()
        self.next_button.destroy()

        result_label = tk.Label(
            self.root,
            text=f"Quiz Finished!\nYour score: {self.score}/{len(questions)}",
            font=("Arial", 20, "bold"),
            bg=self.bg_color,
            fg=self.primary_color,
            justify="center"
        )
        result_label.pack(expand=True)

        # Optional: Add a "Quit" button
        quit_button = tk.Button(
            self.root,
            text="Quit",
            font=self.button_font,
            bg=self.danger_color,
            fg="white",
            command=self.root.quit,
            width=10,
            pady=5
        )
        quit_button.pack(pady=20)

# ---------- Run the Application ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()