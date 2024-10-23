import tkinter as tk
import random

# Define the game board with snakes and ladders
board = {
    3: 22,   # Ladder from 3 to 22
    5: 8,    # Ladder from 5 to 8
    11: 26,  # Ladder from 11 to 26
    20: 29,  # Ladder from 20 to 29
    17: 4,   # Snake from 17 to 4
    19: 7,   # Snake from 19 to 7
    27: 1,   # Snake from 27 to 1
    21: 9,   # Snake from 21 to 9
    28: 15   # Snake from 28 to 15
}

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Snakes and Ladders")

        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.pack()

        self.player1_position = 0
        self.player2_position = 0
        self.current_player = 1

        self.player1_label = self.canvas.create_oval(10, 350, 30, 370, fill="blue")
        self.player2_label = self.canvas.create_oval(10, 350, 30, 370, fill="red")

        self.roll_button = tk.Button(master, text="Roll Die", command=self.roll_die)
        self.roll_button.pack()

        self.status_label = tk.Label(master, text="Player 1's turn", font=("Helvetica", 12))
        self.status_label.pack()

    def roll_die(self):
        roll = random.randint(1, 6)
        self.move_player(roll)

    def move_player(self, roll):
        if self.current_player == 1:
            self.player1_position += roll
            if self.player1_position > 30:
                self.player1_position -= roll
            self.player1_position = board.get(self.player1_position, self.player1_position)
            self.update_position(self.player1_label, self.player1_position)
            if self.player1_position == 30:
                self.status_label.config(text="Player 1 wins!")
                self.roll_button.config(state=tk.DISABLED)
            else:
                self.current_player = 2
                self.status_label.config(text="Player 2's turn")
        else:
            self.player2_position += roll
            if self.player2_position > 30:
                self.player2_position -= roll
            self.player2_position = board.get(self.player2_position, self.player2_position)
            self.update_position(self.player2_label, self.player2_position)
            if self.player2_position == 30:
                self.status_label.config(text="Player 2 wins!")
                self.roll_button.config(state=tk.DISABLED)
            else:
                self.current_player = 1
                self.status_label.config(text="Player 1's turn")

    def update_position(self, player_label, position):
        # Calculate the x and y position based on the board's layout
        x = 10 + (position % 10) * 40
        y = 350 - (position // 10) * 40
        self.canvas.coords(player_label, x, y, x + 20, y + 20)

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()

