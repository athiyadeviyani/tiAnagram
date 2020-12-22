from nltk.corpus import brown
import random
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
from tkinter import Menu

word_list = brown.words()
word_list = [x for x in word_list if x.isalpha()]
six_letters = [w.lower() for w in word_list if len(w) == 6]

done = False


def find_word(short, long):
    long = list(long)

    for s in short:
        if s in long and long:
            long.remove(s) 
        else:
            return False

    return True

def get_all_words(word):
    l = []
    for w in word_list:
        if find_word(w, word) and len(w) >= 3:
            l.append(w)

    return l

def shuffle(letters):
    return random.sample(letters, len(letters))

def gen_letters():
    random_word = six_letters[random.randint(0, len(six_letters))]
    letters = random.sample(list(random_word), 6)
    all_words = get_all_words(random_word)
    return (', '.join(map(str, letters))), all_words

letters, all_words = gen_letters()
all_words = list(set(all_words))

def main():
    
    start = "y"

    while start == "y":
        print("Starting game...")
        random_word = six_letters[random.randint(0, len(six_letters))]

        letters = random.sample(list(random_word), 6)
        start = input("Play again? (y/n) ")

def submit():
    word = txt.get()
    txt.delete(0,"end")
    if word in all_words and word not in final:
        final.append(word)
        res.configure(text=', '.join(map(str, final)), wraplength=430, justify='center')
        if len(final) == len(all_words):
            warning.configure(text='Congratulations! You\'ve found all the words!', fg="green")
            done = True
        else:
            warning.configure(text=word + ' found!', fg="green")
    elif word in final:
        warning.configure(text=word + ' already found!', fg="red")
    else:
        warning.configure(text=word + ' not found!', fg="red")

### GUI

window = Tk()
window.title("Welcome to TiAnagram!")
window.geometry('430x450')

final = []

blank1 = Label(window, text = "SPACE", fg='white', font = ("Arial Bold",20))
blank1.grid(column = 0, row = 1)

letter_container = Label(window, text = "Here are your letters: " + letters, font = ("Arial Bold",20))
letter_container.grid(column = 0, row = 3)

# letter_container.configure(text="Here are your letters: " + letters)
print(all_words)
s = "There is a total of " + str(len(all_words)) + " words that you can form."
word_count = Label(window, text = s, font = ("Arial",20))
word_count.grid(column = 0, row = 4)

# get input using entry class
txt = Entry(window, width = 20, font=("Arial, 20"), justify='center')
# use the grid function as usual to add it to the window
txt.grid(column = 0, row = 5)
txt.focus()


btn = Button(window, text = "Submit", bg = "black", fg = "black", command = submit, font = ("Arial",20))
btn.grid(column = 0, row = 6)

warning = Label(window, text = "", font = ("Arial",20))
warning.grid(column = 0, row = 7)

res = Label(window, text = "", font = ("Arial",20))
res.grid(column = 0, row = 8)

def countdown(count):
    # change text in label        
    
    if count > 0 and (len(final) != len(all_words)):
        # call countdown again after 1000ms (1s)
        cdown['text'] = count
        window.after(1000, countdown, count-1)

    elif len(final) == len(all_words):
        cdown['text'] = '0'

    else:       
        txt.configure(state='disabled')
        score = len(final)
        warning.configure(text="TIME'S UP \n Final score: " + str(score), fg="red", font=("Arial", 30))
        not_found = []
        for word in all_words:
            if word not in final:
                not_found.append(word)
        
        cdown.configure(text="Words not found: " + (', '.join(map(str, not_found))), font=("Arial", 20), wraplength=430, justify='center')



cdown = Label(window, font=("Arial", 30))
cdown.grid(column = 0, row = 10)

# call countdown first time    
countdown(90)
# root.after(0, countdown, 5)

window.mainloop()