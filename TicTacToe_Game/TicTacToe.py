from tkinter import *
import random

def next_turn(row, column):
    global player

    if button[row][column]['text']==" " and check_winner()is False:

     if player == players[0]:

         button[row][column]['text']=player

        if check_winner() is False:
            player =players[1]
            label.config(text=(players[1]+" turn"))

        elif check_winner() is True:
            label.config(text=(players[0]+" wins"))

        elif check_winner() == "Tie":
            label.config(text=("tie"))

    else:

        button[row][column]['text'] = player

        if check_winner() is False:
            player = players[0]
            label.config(text=(players[0] + " turn"))

        elif check_winner() is True:
            label.config(text=(players[1] + " wins"))

        elif check_winner() == "Tie":
            label.config(text=("tie"))




def check_winner():
   for row in range(3):
       if button[row][0]['text']==button[row][1]['text']==button[row][2]['text'] !="":
           button[row][0].config(bg="pink")
           button[row][1].config(bg="pink")
           button[row][2].config(bg="pink")
           return True

    for column in range(3):
       if button[0][column]['text']==button[1][column]['text']==button[2][column]['text'] !="":
           button[0][column].config(bg="pink")
           button[1][column].config(bg="pink")
           button[2][column].config(bg="pink")

           return  True

   if button[0][0]['text'] == button[1][1]['text']==button[2][2]['text'] != "":
       button[0][0].config(bg="pink")
       button[1][1].config(bg="pink")
       button[2][2].config(bg="pink")
       return True

   elif button[0][2]['text'] == button[1][1]['text']==button[2][0]['text'] != "":
       button[0][2].config(bg="pink")
       button[1][1].config(bg="pink")
       button[2][0].config(bg="pink")
       return True

   elif empty_spaces() is False:
       for row in range(3):
           for column in range(3):
               button[row][column].config(bg="blue")

       return "Tie"

   else:
       return False


def empty_spaces():
    spaces = 9

    for row in range(3):
        for column in range(3):
            if button[row][column]['text']!="":
                spaces-=1
    if spaces == 0:
        return  False
    else :
        return True




def new_game():
    global player
    player = random.choice(players)
    label.config(text=player+" turn")
    for row in range(3):
        for column in range(3):
            button[row][column].config(text="", bg="#F0F0F0")







window =Tk()
window.title("X & Os")
players =["x","o"]
player = random.choice(players)
button = [[0,0,0],
        [0,0,0],
        [0,0,0]]
label = Label(text= player + "turn", font=("Arial",40))
label.pack(side="top")

reset_button = Button(Text="restart",font=('Arial',20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        button[row][column] = Button(frame, text=" ",font=('Arial',20), width=5, height=2,
                                    command= lambda row = row, column = column: next_turn(row,column))
        button[row][column].grid(row=row, column=column)




window.mainloop()