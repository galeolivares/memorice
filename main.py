import random
import time
from tkinter import Tk, Button, Label, DISABLED, messagebox


def show_symbol(x, y):
    global first
    global previousX, previousY
    global totpoint, points
    buttons[x, y]['text'] = button_symbols[x, y]
    buttons[x, y].update()

    if first:
        previousX = x
        previousY = y
        first = False
    elif previousX != x or previousY != y:
        if button_symbols[previousX, previousY] != button_symbols[x, y]:
            time.sleep(2)
            buttons[previousX, previousY]['text'] = ''
            buttons[x, y]['text'] = ''
            flip_player()
        else:
            buttons[previousX, previousY]['command'] = DISABLED
            buttons[x, y]['command'] = DISABLED
            points[currPlayer] += 1
            totpoint += 1
            print("Player %s points = %s" % (currPlayer, points[currPlayer]))
            if totpoint == numpairs:
                game_over()
        first = True


def flip_player():
    global currPlayer
    if currPlayer == 1:
        currPlayer = 2
    else:
        currPlayer = 1
    print("Turn: Player %s" % currPlayer)


def game_over():
    global points
    if points[1] > points[2]:
        text = "Player 1 wins with %s points" % points[1]
    elif points[1] < points[2]:
        text = "Player 2 wins with %s points" % points[2]
    else:
        text = "It is a draw!"
    messagebox.showinfo("Game Over", text, command=close_window)


def close_window(self):
    root.destroy()


root = Tk()
root.geometry("800x500")
root.title('Matchmaker')
root.resizable(width=False, height=False)

buttons = {}
first = True
previousX = 0
previousY = 0
currPlayer = 1
points = {1: 0, 2: 0}
totpoint = 0

button_symbols = {}
symbols = [u'\u2702', u'\u2702', u'\u2705', u'\u2705', u'\u2708', u'\u2708', u'\u2709',
           u'\u2709', u'\u270A', u'\u270A', u'\u270B', u'\u270B', u'\u270C', u'\u270C',
           u'\u270F', u'\u270F', u'\u2712', u'\u2712', u'\u2714', u'\u2714', u'\u2716',
           u'\u2716', u'\u2728', u'\u2728']
numpairs = len(symbols) / 2

random.shuffle(symbols)

# debug
print(symbols)

for x in range(6):
    for y in range(4):
        button = Button(command=lambda x=x, y=y: show_symbol(x, y), width=10, height=3)
        button.grid(column=x, row=y, padx=2, pady=2)
        buttons[x, y] = button
        button_symbols[x, y] = symbols.pop()

score = dict()

for p in [1, 2]:
    score[p] = Label(root, text="Score P%s=0" % p)
    score[p].grid(column=p - 1, row=4)

root.mainloop()
