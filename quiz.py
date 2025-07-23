import tkinter as tk
from tkinter import messagebox

# Quiz data (question, options, correct answer)
quiz = [
    ("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Rome"], "Paris"),
    ("Which planet is known as the Red Planet?", ["Earth", "Mars", "Venus", "Jupiter"], "Mars"),
    ("Who wrote 'Hamlet'?", ["Shakespeare", "Tolkien", "Rowling", "Twain"], "Shakespeare"),
]

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.q_index = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400)
        self.question_label.pack(pady=20)

        self.options = []
        for i in range(4):
            btn = tk.Button(root, text="", font=("Arial", 14), width=25, command=lambda i=i: self.check_answer(i))
            btn.pack(pady=5)
            self.options.append(btn)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        question, choices, _ = quiz[self.q_index]
        self.question_label.config(text=f"Q{self.q_index+1}: {question}")
        for i, choice in enumerate(choices):
            self.options[i].config(text=choice, state=tk.NORMAL)
        self.next_button.config(state=tk.DISABLED)

    def check_answer(self, i):
        _, choices, correct = quiz[self.q_index]
        selected = choices[i]
        if selected == correct:
            self.score += 1
            messagebox.showinfo("Correct!", "That's the right answer.")
        else:
            messagebox.showerror("Wrong!", f"Oops! The correct answer was: {correct}")
        for btn in self.options:
            btn.config(state=tk.DISABLED)
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.q_index += 1
        if self.q_index < len(quiz):
            self.load_question()
        else:
            messagebox.showinfo("Quiz Completed", f"You scored {self.score}/{len(quiz)}.")
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x400")
    app = QuizGame(root)
    root.mainloop()
