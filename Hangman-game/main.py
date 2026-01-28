import tkinter as tk
import random
import winsound
import os

# -------------------------------
# THEME COLORS
# -------------------------------
BG_COLOR = "#1e293b"      # dark blue
CARD_COLOR = "#334155"    # slate
BTN_COLOR = "#38bdf8"     # cyan
BTN_TEXT = "#020617"
TEXT_COLOR = "#e5e7eb"
ACCENT = "#facc15"        # yellow

FONT_TITLE = ("Segoe UI", 22, "bold")
FONT_TEXT = ("Segoe UI", 12)
FONT_WORD = ("Consolas", 20, "bold")

# -------------------------------
# DATA
# -------------------------------
WORD_CATEGORIES = {
    "Fruits": ["apple", "banana", "grapes", "orange", "mango"],
    "Animals": ["tiger", "lion", "elephant", "giraffe", "zebra"],
    "Countries": ["india", "canada", "brazil", "france", "japan"]
}

DIFFICULTY = {"Easy": 8, "Medium": 6, "Hard": 4}
TIME_LIMIT = 10
HIGH_SCORE_FILE = "highscore.txt"

# -------------------------------
# GUI CLASS
# -------------------------------
class HangmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("700x550")
        self.root.configure(bg=BG_COLOR)

        self.category = tk.StringVar()
        self.difficulty = tk.StringVar(value="Medium")

        self.word = ""
        self.display_word = []
        self.attempts = 6
        self.score = 0
        self.high_score = self.load_high_score()
        self.time_left = TIME_LIMIT
        self.timer_id = None

        self.create_ui()

    # -------------------------------
    # UI
    # -------------------------------
    def create_ui(self):
        tk.Label(
            self.root, text="🎯 Hangman Game",
            font=FONT_TITLE, fg=ACCENT, bg=BG_COLOR
        ).pack(pady=10)

        card = tk.Frame(self.root, bg=CARD_COLOR, padx=15, pady=15)
        card.pack(pady=10)

        tk.Label(card, text="Category", fg=TEXT_COLOR, bg=CARD_COLOR).grid(row=0, column=0)
        tk.OptionMenu(card, self.category, *WORD_CATEGORIES.keys()).grid(row=1, column=0)

        tk.Label(card, text="Difficulty", fg=TEXT_COLOR, bg=CARD_COLOR).grid(row=0, column=1)
        tk.OptionMenu(card, self.difficulty, *DIFFICULTY.keys()).grid(row=1, column=1)

        tk.Button(
            card, text="Start Game",
            bg=BTN_COLOR, fg=BTN_TEXT, font=FONT_TEXT,
            command=self.start_game
        ).grid(row=1, column=2, padx=10)

        self.info_label = tk.Label(
            self.root, text="", fg=ACCENT, bg=BG_COLOR, font=FONT_TEXT
        )
        self.info_label.pack()

        self.canvas = tk.Canvas(
            self.root, width=220, height=260,
            bg="#020617", highlightthickness=0
        )
        self.canvas.pack(pady=10)

        self.word_label = tk.Label(
            self.root, text="", font=FONT_WORD,
            fg=TEXT_COLOR, bg=BG_COLOR
        )
        self.word_label.pack(pady=5)

        self.letters_frame = tk.Frame(self.root, bg=BG_COLOR)
        self.letters_frame.pack(pady=10)

        self.score_label = tk.Label(
            self.root,
            text=f"Score: {self.score} | High Score: {self.high_score}",
            fg=ACCENT, bg=BG_COLOR, font=FONT_TEXT
        )
        self.score_label.pack()

        tk.Button(
            self.root, text="Restart",
            bg="#ef4444", fg="white",
            command=self.reset_game
        ).pack(pady=10)

    # -------------------------------
    # GAME LOGIC (same as before)
    # -------------------------------
    def start_game(self):
        if not self.category.get():
            self.info_label.config(text="⚠️ Select a category")
            return

        self.word = random.choice(WORD_CATEGORIES[self.category.get()])
        self.display_word = ["_"] * len(self.word)
        self.attempts = DIFFICULTY[self.difficulty.get()]
        self.score = 0
        self.update_score()
        self.create_buttons()
        self.update_display()
        self.start_timer()

    def create_buttons(self):
        for w in self.letters_frame.winfo_children():
            w.destroy()

        for ch in "abcdefghijklmnopqrstuvwxyz":
            tk.Button(
                self.letters_frame,
                text=ch,
                width=3,
                bg=BTN_COLOR,
                fg=BTN_TEXT,
                command=lambda c=ch: self.guess(c)
            ).pack(side=tk.LEFT, padx=1, pady=1)

    def guess(self, letter):
        self.reset_timer()
        if letter in self.word:
            winsound.Beep(800, 120)
            for i, ch in enumerate(self.word):
                if ch == letter:
                    self.display_word[i] = letter
            self.score += 5
        else:
            winsound.Beep(400, 150)
            self.attempts -= 1
            self.score -= 1

        self.update_score()
        self.update_display()
        self.check_game_status()

    def draw_hangman(self):
        self.canvas.delete("all")
        if self.attempts <= 5:
            self.canvas.create_oval(90, 20, 130, 60, outline="white")
        if self.attempts <= 4:
            self.canvas.create_line(110, 60, 110, 140, fill="white")
        if self.attempts <= 3:
            self.canvas.create_line(110, 80, 80, 110, fill="white")
        if self.attempts <= 2:
            self.canvas.create_line(110, 80, 140, 110, fill="white")
        if self.attempts <= 1:
            self.canvas.create_line(110, 140, 80, 180, fill="white")
        if self.attempts <= 0:
            self.canvas.create_line(110, 140, 140, 180, fill="white")

    # -------------------------------
    # TIMER + STATUS
    # -------------------------------
    def start_timer(self):
        self.time_left = TIME_LIMIT
        self.update_timer()

    def update_timer(self):
        self.info_label.config(text=f"⏱️ Time Left: {self.time_left}s")
        if self.time_left > 0:
            self.time_left -= 1
            self.timer_id = self.root.after(1000, self.update_timer)
        else:
            self.attempts -= 1
            self.draw_hangman()
            self.check_game_status()
            self.start_timer()

    def reset_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.start_timer()

    def update_display(self):
        self.word_label.config(text=" ".join(self.display_word))
        self.draw_hangman()

    def check_game_status(self):
        if "_" not in self.display_word:
            self.end_game("🎉 You Won!")
        elif self.attempts <= 0:
            self.end_game(f"😢 Game Over! Word: {self.word}")

    def end_game(self, msg):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.info_label.config(text=msg)
        for b in self.letters_frame.winfo_children():
            b.config(state=tk.DISABLED)
        self.save_high_score()

    # -------------------------------
    # SCORE
    # -------------------------------
    def update_score(self):
        self.score_label.config(
            text=f"Score: {self.score} | High Score: {self.high_score}"
        )

    def load_high_score(self):
        return int(open(HIGH_SCORE_FILE).read()) if os.path.exists(HIGH_SCORE_FILE) else 0

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            open(HIGH_SCORE_FILE, "w").write(str(self.high_score))
            self.update_score()

    def reset_game(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        self.canvas.delete("all")
        self.word_label.config(text="")
        self.info_label.config(text="")
        for w in self.letters_frame.winfo_children():
            w.destroy()

# -------------------------------
# RUN APP
# -------------------------------
if __name__ == "__main__":
    root = tk.Tk()
    HangmanGUI(root)
    root.mainloop()
