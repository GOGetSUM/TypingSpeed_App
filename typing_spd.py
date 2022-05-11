from tkinter import *
import math


#---------------------------------------------------------------
timer =0
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

#----------------------------Start Timer-------------------------------------------

def start_timer():
    text.delete("1.0",END)
    timed = 30
    inst_label.config(text='GO GO GO , You Gotta Be Faster THAN THAT!')
    count_down(timed)



#----------------------Count Down Mechanism-------------------------------------------------

def count_down(count):
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f'{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count -1)
    else:
        results()


# ----------------------------Calculate Results-------------------------------------------

def results():
    test_text = text.get("1.0", END)
    list =[]
    count =0
    for char in test_text:
        if char==" ":
            count +=1
            char = "SPACE"
            list.append(char)
        else:
            list.append(char)
    wpm = count * 2;
    inst_label.config(text= f"Woah, your Words Per Min. score is {wpm} wpm.")


# ----------------------------Timer Reset-------------------------------------------
def reset_timer():
    window.after_cancel(timer)
    inst_label.config(text="Instructions:Hit start, type(..fast), reset")
    canvas.itemconfig(timer_text,text="00")
    text.delete("1.0",END)





#---------------------------UI SETUP------------------------------------

window = Tk()
window.title('Speed Test')
window.config(padx=100,pady=50, bg='grey')

test_var = StringVar()


title_label = Label(width=30,pady=20,text="Speed Tester", fg=GREEN, font=(FONT_NAME,35,'bold'), bg=YELLOW)
title_label.grid(column=0,columnspan=3,row=0)

inst_label = Label(width=105,pady=20,text="Instructions:Hit start, type(..fast), reset", fg=RED, font=(FONT_NAME,10,'bold'), bg=YELLOW)
inst_label.grid(column=0,columnspan=3,row=1)


paragraph_type = Label(width=120,pady=20,text="""this is a simple paragraph that is meant 
to be nice and easy to type which is why there will 
be mommas no periods or any capital letters so i guess this means 
that it cannot really be considered a paragraph but just a series 
of run on sentences this should help you get faster at typing as im 
trying not to use too many difficult words in it although i think that 
i might start making it hard by including some more difficult letters I'm 
typing pretty quickly so forgive me for any mistakes i think that i will 
not just tell you a story about the time i went to the zoo and found a 
monkey and a fox playing together they were so cute and i think that they 
were not supposed to be in the same cage but they""")

paragraph_type.grid(column=0,columnspan=3,row=3)

#Text
text = Text(height=20, width=105)
#Puts cursor in textbox.
text.focus()
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.grid(column=0,columnspan=3,row=4)

canvas = Canvas(width=200,height=40,bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(100,20,text="00", fill="black",font=(FONT_NAME,12,'bold'))
canvas.grid(column=0,row=5)


start_button = Button(text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=1,row=5)

reset_button = Button(text="Reset",command=reset_timer, highlightthickness=0)
reset_button.grid(column=2,row=5)


window.mainloop()