import sys
import subprocess
import tkinter as tk
import turtle
import pygame
from PIL import ImageTk, Image
from PIL import Image as PILImage
pygame.init()
my_sound=pygame.mixer.Sound('sunet.mp3')
my_sound.play(loops=-1)

game_over = 0
win = 0
num_tries = 0
def get_text(event):
    global len_word
    global word
    global text
    text = text_box.get()
    text.lower()
    len_word = len(text)
    word=[0]* len_word
    for i in range(len_word):
        word[i] = "_"
    letter = " "
    
    print(word)
    text_box.delete(0,'end')
    turtle_canvas.create_window(0, 210, window=label_word)
    label_word.config(text = " ".join(["_"]*len_word), font = ("Cascadia Mono", 30))
    label1.config(text = "Guess a letter!")
    text_box.config(state = "disabled")
    turtle_canvas.create_window(0, 280, window=letter_box)
    letter_box.bind('<Return>', get_letter)
    
def get_letter(event):
    letter = letter_box.get()
    letter_box.delete(0,'end')
    guess(text,word,letter,len_word)

def guess(text,word,letter,len_word):
    global win
    global num_tries
    print(letter)
    print(text)
    text = [i for i in text]
    found = 0
    for i in range(len_word):
        if text[i] is letter:
            word[i]=letter
            label_word.config(text = word, font = ("Cascadia Mono", 30))
            found+=1
            if word == text:
                win+=1
                over()  
    if found == 0:
        num_tries+=1
        turtle_draw(num_tries)
            
    
def turtle_draw(num_tries):
    global game_over
    
    if(num_tries == 1):
        my_sound=pygame.mixer.Sound('wrong-answer.mp3')
        my_sound.play()
        # prima linie
        my_turtle.up()
        my_turtle.goto(-200,-100)
        my_turtle.down()
        my_turtle.forward(300)
    elif(num_tries == 2):
        my_sound=pygame.mixer.Sound('wrong-answer.mp3')
        my_sound.play()
        # a doua linie
        my_turtle.up()
        my_turtle.goto(-50,-100)
        my_turtle.left(90)
        my_turtle.down()
        my_turtle.forward(400)
    elif(num_tries == 3):
        my_sound=pygame.mixer.Sound('wrong-answer.mp3')
        my_sound.play()
        # a treia linie
        my_turtle.right(90)
        my_turtle.forward(150)
    elif(num_tries == 4):
        my_sound=pygame.mixer.Sound('wrong-answer.mp3')
        my_sound.play()
        # a patra linie
        my_turtle.right(90)
        my_turtle.forward(100)
    elif(num_tries == 5):
        my_sound=pygame.mixer.Sound('wrong-answer.mp3')
        my_sound.play()
        # capul
        my_turtle.up()
        my_turtle.goto(70,170)
        my_turtle.down()
        my_turtle.circle(30)
    elif(num_tries == 6):
        my_sound=pygame.mixer.Sound('wrong-answer.mp3')
        my_sound.play()
        # corp
        my_turtle.up()
        my_turtle.goto(100,140)
        my_turtle.down()
        my_turtle.forward(80)
        my_turtle.up()
    elif(num_tries == 7):
        my_sound=pygame.mixer.Sound('wrong-answer.mp3')
        my_sound.play()
        # prima mana
        my_turtle.goto(100,115)
        my_turtle.down()
        my_turtle.left(25)
        my_turtle.forward(65)
    elif(num_tries == 8):
        my_sound=pygame.mixer.Sound('wrong-answer.mp3')
        my_sound.play()
        # a doua mana
        my_turtle.goto(100,115)
        my_turtle.down()
        my_turtle.right(50)
        my_turtle.forward(65)
    elif(num_tries == 9):
        my_sound=pygame.mixer.Sound('wrong-answer.mp3')
        my_sound.play()
        # primul picior
        my_turtle.up()
        my_turtle.goto(100,60)
        my_turtle.down()
        my_turtle.left(50)
        my_turtle.forward(65)
    elif(num_tries == 10):
        # al doilea picior
        my_turtle.up()
        my_turtle.goto(100,60)
        my_turtle.down()
        my_turtle.right(50)
        my_turtle.forward(65)
        game_over+=1
        over()          
    get_letter

def over():
    global game_over
    my_sound.stop()
    turtle_canvas.delete('all')
    turtle_canvas.configure(bg="#ffffff")
    button_retry = tk.Button(main_window, text="Retry", command = restart_program)
    button_retry.pack(padx=20, pady=20)
    button_quit = tk.Button(main_window, text="Quit", command = exit)
    button_quit.pack(padx=20, pady=20)
    if game_over > 0:
        my_sound2=pygame.mixer.Sound('gameover1.mp3')
        my_sound2.play()

        img = PILImage.open("game_over.png")
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(turtle_canvas, image=photo)
        label.image = photo  # Store the PhotoImage object in a persistent variable
        label.pack()
    else:
        my_sound2=pygame.mixer.Sound('win.mp3')
        my_sound2.play()
        img = PILImage.open("you_win.png")
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(turtle_canvas, image=photo)
        label.image = photo  # Store the PhotoImage object in a persistent variable
        label.pack()

    
def restart_program():
    python = sys.executable
    cmd = f'{python} {" ".join(sys.argv)}'
    main_window.destroy()
    subprocess.run(cmd)
#    python = sys.executable
#    os.execl(python, python, * sys.argv)
      

main_window = tk.Tk()
main_window.title("Hangman")

turtle_canvas = tk.Canvas(main_window, width=650, height=650)
turtle_canvas.pack(padx=20, pady=20)

turtle_screen = turtle.TurtleScreen(turtle_canvas)
my_turtle = turtle.RawTurtle(turtle_screen)
my_turtle.hideturtle()

def press_play():
    
        turtle_canvas.configure(bg="#8e6ec4")
        turtle_canvas.create_window(0, 256, window=label1)
        turtle_canvas.create_window(0, 280, window=text_box, state = "normal")
        my_sound=pygame.mixer.Sound('play.mp3')
        my_sound.play()
        text_box.bind('<Return>', get_text)
        button_play.forget()
text_box = tk.Entry(main_window,show="*")
letter_box = tk.Entry(main_window)
label1 = tk.Label(main_window, bg="#8e6ec4", text="Type a word!")
label_word = tk.Label(main_window, bg="#8e6ec4", text="")

button_play = tk.Button(main_window, text="Play", command = press_play)
button_play.pack(padx=20, pady=20)


main_window.mainloop()

