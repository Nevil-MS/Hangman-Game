from tkinter import *
from tkinter import messagebox
from wonderwords import RandomWord
from random import *
from string import ascii_uppercase

#Creates the root window for game to be displayed
root=Tk()
root.title("Hangman")
root.config(bg='#94d2bd')
root.resizable(False,False)

#Stores the hangman image locations
images=[]
for i in range(12):
    images.append(PhotoImage(file=f"images/hang{i}.png"))

#Label for images
img_lbl=Label(root,image=images[0],bg='#94d2bd')
img_lbl.grid(row=0,column=0,columnspan=4,padx=10,pady=40)

#Label for word
blank_word=Label(root,font=('Consolas 26 bold'),text="Click New Game to Start!",bg='#94d2bd')
blank_word.grid(row=0,column=3,columnspan=6)

buttons={}

#Creates clues like letter clues and button clues
def clue():
    global guessed
    global templ,tempb,t
    if len(word)>4: 
        while True:
            clue=choice(word)
            print(clue)
            if word.count(clue)==1 and (clue) not in (templ):
                gues=list(guessed)
                buttons[clue].config(state=DISABLED,bg="#bfff57")
                gues[word_spaces.index(clue)]=clue
                guessed=gues
                blank_word.config(text="".join(gues))
                templ.append(clue)
                break
    
    while t!=3:
        clb=choice(list(buttons.keys()))
        if clb not in word and clb not in tempb and clb not in templ:
            buttons[clb].config(state=DISABLED,bg="#bfb28c",fg="black")
            t+=1
            tempb.append(clb)

#Resets the game for playing again               
def newgame():
    global num_mistakes,word_spaces,guessed,word
    global templ,tempb,t
    templ=[]
    tempb=[]
    t=0
    w=RandomWord()
    img_lbl.config(image=images[0])
    num_mistakes=0
    word=w.word().upper()
    while "-" in word or len(word)>10:
        word=w.word().upper()

    print(word)
    word_spaces=" ".join(word)
    guessed=" ".join("_"*len(word))

    blank_word.config(text=(guessed))

    for b in buttons.values():
        b.config(state=NORMAL,bg='#e9d8a6',fg='black')

    if len(word)>5:
        for j in range(2):
            clue()
    elif len(word)>4:
        clue()
    elif len(word)<=4:
        clue()

#Checks if the guess is correct or not #and does the processing

def guess(c):
    global num_mistakes
    global guessed
    guess=list(guessed)
    lswrd=list(word_spaces)

    if num_mistakes<11:
        if word_spaces.count(c)>0:
            for i in range (len(lswrd)):
                if lswrd[i]==c:
                    guess[i]=c
                    guessed=guess
                    blank_word.config(text=str(''.join(guess)))
                    buttons[c].config(state=DISABLED,bg="#bfff57")
                    if list(guessed)==lswrd:
                        for btn in buttons.values():
                            btn.config(state=DISABLED)
                        messagebox.showinfo("hangman","You Guessed it!")
                                                     
        else:
            num_mistakes+=1
            buttons[c].config(state=DISABLED,bg="#bfb28c")
            img_lbl.config(image=images[num_mistakes])
            if num_mistakes==11:
                for btn in buttons.values():
                            btn.config(state=DISABLED)
                blank_word.config(text=word_spaces)
                messagebox.showerror("Hangman","You Lost!")
                
#sets up buttons for the virtual keyboard 
n=0
for c in ascii_uppercase:
    btn=Button(root,text=c,command=lambda c=c:guess(c),font="Helvatica 18",width=6,height=2,bg='#e9d8a6')
    btn.grid(row=1+n//9,column=n%9)
    buttons[c]=btn
    n+=1
newg=Button(root,text="New\nGame",font="Helvatica 16",command=lambda:newgame(),bg='#e9d8a6').grid(row=3,column=8,sticky="NSEW") 

root.mainloop()