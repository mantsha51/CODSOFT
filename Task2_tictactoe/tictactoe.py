import tkinter as tk
import math

# game board
board = [" " for _ in range(9)]

# main window
root = tk.Tk()
root.title(" Mantsha's Tic-Tac-Toe game <33")
root.configure(bg="#fff0f5")
root.geometry("420x420")

buttons = []

def cute_popup(message):

    popup = tk.Toplevel(root)
    popup.title("Game Result")
    popup.configure(bg="#ffd6e7")
    popup.geometry("300x150")

    label = tk.Label(
        popup,
        text=message,
        font=("Comic Sans MS", 14, "bold"),
        bg="#ffd6e7", #backgroundcolor
        fg="#6b3e50" #text color
    )

    label.pack(pady=20)

    reset_btn = tk.Button(
        popup,
        text="reset:)",
        font=("Arial", 10, "bold"),
        bg="#ffb6c1",
        command=popup.destroy
    )

    reset_btn.pack()


# who won
def check_winner(player):

    # rows
    if board[0] == board[1] == board[2] == player:
        return True

    if board[3] == board[4] == board[5] == player:
        return True

    if board[6] == board[7] == board[8] == player:
        return True

    # columns
    if board[0] == board[3] == board[6] == player:
        return True

    if board[1] == board[4] == board[7] == player:
        return True

    if board[2] == board[5] == board[8] == player:
        return True

    # diagonals
    if board[0] == board[4] == board[8] == player:
        return True

    if board[2] == board[4] == board[6] == player:
        return True

    return False

def is_draw():
    return " " not in board


# minimax algorithm
def minimax(is_ai_turn):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_ai_turn:

        best_score = -math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                best_score = max(best_score, score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                best_score = min(best_score, score)

        return best_score


def ai_move():

    best_score = -math.inf
    best_move = -1

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:

                best_score = score
                best_move = i

    board[best_move] = "O"
    buttons[best_move]["text"] = "O"

    if check_winner("O"):

        cute_popup("I Won!!")
        reset_game()

    elif is_draw():

        cute_popup("It's a Draw!")
        reset_game()


def player_move(index):

    if board[index] != " ":
        return

    board[index] = "X"
    buttons[index]["text"] = "X"

    if check_winner("X"):

        cute_popup("You Win! 🎉💕")
        reset_game()
        return

    if is_draw():

        cute_popup("It's a Draw! 🌸")
        reset_game()
        return

    ai_move()


# resetting 
def reset_game():

    global board

    board = [" " for _ in range(9)]

    for button in buttons:
        button.config(text="")


for i in range(9):

    button = tk.Button(
        root,
        text="",
        font=("Comic Sans MS", 24, "bold"),
        width=5,
        height=2,
        bg="#ffe4ec",
        activebackground="#ffc8dd",
        fg="#6b3e50",
        command=lambda i=i: player_move(i)
    )

    button.grid(row=i // 3, column=i % 3, padx=3, pady=3)

    buttons.append(button)


root.mainloop()