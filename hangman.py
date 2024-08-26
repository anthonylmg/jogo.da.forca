import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Forca")

        self.categories = {
            "Animais": ["GATO", "CACHORRO", "ELEFANTE", "TIGRE", "URSOS"],
            "Cores": ["AZUL", "VERDE", "AMARELO", "VERMELHO", "ROSA"],
            "Frutas": ["MAÇÃ", "BANANA", "LARANJA", "MORANGO", "UVA"]
        }

        self.selected_category = tk.StringVar(value="Animais")
        self.word = ""
        self.guesses = set()
        self.max_attempts = 10
        self.attempts = 0

        self.setup_ui()
        self.new_game()

    def setup_ui(self):
        # Categorias
        tk.Label(self.root, text="Escolha a Categoria:").pack()

        self.category_menu = tk.OptionMenu(self.root, self.selected_category, *self.categories.keys())
        self.category_menu.pack()

        self.start_button = tk.Button(self.root, text="Iniciar Novo Jogo", command=self.new_game)
        self.start_button.pack()

        # Tela inicial
        self.canvas = tk.Canvas(self.root, width=300, height=200, bg='white')
        self.canvas.pack()

        # Letras adivinhadas
        self.guess_label = tk.Label(self.root, text="Letras adivinhadas:")
        self.guess_label.pack()

        self.guess_display = tk.Label(self.root, text="", font=("Helvetica", 24))
        self.guess_display.pack()

        # Caixa de entrada para adivinhar letras
        self.entry = tk.Entry(self.root)
        self.entry.pack()

        self.submit_button = tk.Button(self.root, text="Adivinhar", command=self.submit_guess)
        self.submit_button.pack()

        # Mensagem de status
        self.status_label = tk.Label(self.root, text="")
        self.status_label.pack()

    def new_game(self):
        self.word = random.choice(self.categories[self.selected_category.get()])
        self.guesses = set()
        self.attempts = 0
        self.update_display()

    def submit_guess(self):
        guess = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Entrada Inválida", "Digite apenas uma letra.")
            return

        if guess in self.guesses:
            messagebox.showinfo("Atenção", "Você já adivinhou essa letra.")
            return

        self.guesses.add(guess)

        if guess in self.word:
            if "_" not in self.get_display_word():
                messagebox.showinfo("Parabéns!", "Você ganhou!")
                self.new_game()
        else:
            self.attempts += 1
            self.draw_hangman()
            if self.attempts >= self.max_attempts:
                messagebox.showinfo("Game Over", f"Você perdeu! A palavra era: {self.word}")
                self.new_game()

        self.update_display()

    def update_display(self):
        self.guess_display.config(text=self.get_display_word())
        self.status_label.config(text=f"Tentativas restantes: {self.max_attempts - self.attempts}")

    def get_display_word(self):
        return ' '.join([letter if letter in self.guesses else '_' for letter in self.word])

    def draw_hangman(self):
        self.canvas.delete("all")
        if self.attempts >= 1:
            self.canvas.create_line(50, 150, 150, 150)  # base
        if self.attempts >= 2:
            self.canvas.create_line(100, 150, 100, 50)  # poste vertical
        if self.attempts >= 3:
            self.canvas.create_line(100, 50, 150, 50)  # travessa superior
        if self.attempts >= 4:
            self.canvas.create_line(150, 50, 150, 80)  # travessa lateral
        if self.attempts >= 5:
            self.canvas.create_oval(135, 80, 165, 110)  # cabeça
        if self.attempts >= 6:
            self.canvas.create_line(150, 110, 150, 140)  # corpo
        if self.attempts >= 7:
            self.canvas.create_line(150, 120, 130, 130)  # braço esquerdo
        if self.attempts >= 8:
            self.canvas.create_line(150, 120, 170, 130)  # braço direito
        if self.attempts >= 9:
            self.canvas.create_line(150, 140, 130, 160)  # perna esquerda
        if self.attempts >= 10:
            self.canvas.create_line(150, 140, 170, 160)  # perna direita

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
