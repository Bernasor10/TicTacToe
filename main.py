import tkinter as tk
import pygame
import random
from tkinter import messagebox

from PIL import Image, ImageTk

class TicTacToe:

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")
        self.window.resizable(False, False)  # Prevent users from resizing the window

        # Set window dimensions
        window_width = 730
        window_height = 770

        # Get screen dimensions
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Calculate position of the top-left corner of the window
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)

        # Set window position
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", width=10, height=5, font=('Arial', 27),
                                   command=lambda i=i, j=j: self.clicked_button(i, j))
                button.grid(row=i, column=j, padx=10, pady=10)
                button.config(bg='#1D7874', highlightbackground='#FFD700', highlightthickness=2)
                row.append(button)
            self.buttons.append(row)

        # Set background color
        self.window.config(bg='#071E22')

        # Create a mixer object
        self.mixer = pygame.mixer

        # Load the sound effect
        music_files = ['C:\\Users\\My PC\\PycharmProjects\\TicTacToe\\Knight of Firmament (Instrumental) (Bonus Track).mp3',
                       'C:\\Users\\My PC\\PycharmProjects\\TicTacToe\\Alan Walker - The Spectre (Instrumental).mp3',
                       'C:\\Users\\My PC\\PycharmProjects\\TicTacToe\\Freedom Dive.mp3']

        # Choose a random music file to play
        music_files = random.choice(music_files)

        pygame.init()

        # Load the sound effect
        pygame.mixer.music.load(music_files)

        # Play the music
        pygame.mixer.music.play(loops=-1)
        pygame.mixer.music.set_volume(0.4)

        # Setting up the game icon
        icon_img = Image.open('C:\\Users\\My PC\\PycharmProjects\\TicTacToe\\tictactoe.ico')
        icon_photo = ImageTk.PhotoImage(icon_img)
        self.window.iconphoto(True, icon_photo)

        # Bind the WM_DELETE_WINDOW event to a function that shows a confirmation message box
        self.window.protocol("WM_DELETE_WINDOW", self.confirm_exit)

    def confirm_exit(self):
        result = messagebox.askquestion("Exit Game", "Are you sure you want to exit?")
        if result == 'yes':
            self.window.destroy()


    def clicked_button(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            button = self.buttons[row][col]
            button.config(text=self.current_player, state='disabled')
            if self.current_player == "X":
                button.config(bg='#EE2E31', disabledforeground='#4B0082')
            else:
                button.config(bg='#F4C095', disabledforeground='#FF8C00')
            winner = self.check_winner()
            if winner:
                self.end_game(winner)
            elif self.check_draw():
                self.end_game("Draw")
            else:
                self.change_player()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return self.board[0][i]
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return self.board[0][2]
        return None

    def check_draw(self):
        for row in self.board:
            for col in row:
                if col == "":
                    return False
        return True

    def change_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def end_game(self, result):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state='disabled')
        if result == "Draw":
            messagebox.showinfo("Game Over", "It's a draw!")
        else:
            messagebox.showinfo("Game Over", f"{result} wins!")
        play_again = messagebox.askquestion("Play Again?", "Do you want to play again?")
        if play_again == 'yes':
            self.new_game()
        else:
            self.window.destroy()

    def new_game(self):
        self.current_player = "X"
        self.board = [["", "", ""], ["", "", ""], ["", "", ""]]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='', state='normal', bg='#1D7874')

game = TicTacToe()
game.window.mainloop()