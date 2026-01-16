from cmu_graphics import *
from importlib import resources
text = resources.files('wordlist').joinpath('nouns/91K nouns.txt').read_text(encoding='utf-8')
import random
app.c=0
from importlib import resources
from typing import Iterable

def load_words_from_package(pkg: str = "wordlist", *, unique=False) -> list[str]:
    root = resources.files(pkg)
    words: list[str] = []
    for item in root.rglob("*.txt"):
        if item.is_file():
            text = item.read_text(encoding="utf-8", errors="ignore")
            words.extend(text.split())
    if unique:
        return sorted(set(words))
    return words

# usage (works because you have wordlist/__init__.py)
words = load_words_from_package("wordlist", unique=True)
def createBoxes(y):
    Rect(30,y,60,60,fill=None,border='lightGray')
    Rect(100,y,60,60,fill=None,border='lightGray')
    Rect(170,y,60,60,fill=None,border='lightGray')
    Rect(240,y,60,60,fill=None,border='lightGray')
    Rect(310,y,60,60,fill=None,border='lightGray')
def outlines():
    Rect(30,app.c*65+10,60,60,fill=None,border='black',borderWidth=3)
    Rect(100,app.c*65+10,60,60,fill=None,border='black',borderWidth=3)
    Rect(170,app.c*65+10,60,60,fill=None,border='black',borderWidth=3)
    Rect(240,app.c*65+10,60,60,fill=None,border='black',borderWidth=3)
    Rect(310,app.c*65+10,60,60,fill=None,border='black',borderWidth=3)
answer=random.choice(words)
while len(answer)!=5:
    answer=random.choice(words)
answer=answer.upper()
labels=Group()
win=Label('You Win!',200,200,size=90,fill='green',border='gray',visible=False)
lose=Label('You Lose',200,150,size=90,fill='red',border='gray',visible=False)
cover=Rect(0,0,400,400,fill='white',visible=False)
def onMousePress(x,y):
    app.word=app.getTextInput('Enter Word')
    while len(app.word)!=5:
        app.word=app.getTextInput('Enter a 5 Letter Word')
    while app.word.lower()not in words:
        app.word=app.getTextInput('Not in Word List')
    app.word=app.word.upper()
    for a in app.word:
        for b in answer:
            if a==b:
                if a==app.word[0]:
                    Rect(30,app.c*65+10,60,60,fill='yellow')
                elif a==app.word[1]:
                    Rect(100,app.c*65+10,60,60,fill='yellow')
                elif a==app.word[2]:
                    Rect(170,app.c*65+10,60,60,fill='yellow')
                elif a==app.word[3]:
                    Rect(240,app.c*65+10,60,60,fill='yellow')
                elif a==app.word[4]:
                    Rect(310,app.c*65+10,60,60,fill='yellow')
        if app.word[0]==answer[0]:
            Rect(30,app.c*65+10,60,60,fill='green')
        if app.word[1]==answer[1]:
            Rect(100,app.c*65+10,60,60,fill='green')
        if app.word[2]==answer[2]:
            Rect(170,app.c*65+10,60,60,fill='green')
        if app.word[3]==answer[3]:
            Rect(240,app.c*65+10,60,60,fill='green')
        if app.word[4]==answer[4]:
            Rect(310,app.c*65+10,60,60,fill='green')
        if a==app.word[0]:
            labels.add(Label(a,60,app.c*65+40,size=50,bold=True))
        if a==app.word[1]:
            labels.add(Label(a,130,app.c*65+40,size=50,bold=True))
        if a==app.word[2]:
            labels.add(Label(a,200,app.c*65+40,size=50,bold=True))
        if a==app.word[3]:
            labels.add(Label(a,270,app.c*65+40,size=50,bold=True))
        if a==app.word[4]:
            labels.add(Label(a,340,app.c*65+40,size=50,bold=True))
        labels.toFront()
    outlines()
    if app.word==answer:
        cover.visible=True
        cover.toFront()
        win.visible=True
        win.toFront()
    app.c+=1
    if app.c>5:
        cover.visible=True
        cover.toFront()
        lose.visible=True
        lose.toFront()
        Label('Answer:',200,215,fill='red',border='gray',size=50)
        Label(answer,200,275,fill='red',border='gray',size=80)
createBoxes(10)
createBoxes(75)
createBoxes(140)
createBoxes(205)
createBoxes(270)
createBoxes(335)
print(answer)
cmu_graphics.run()