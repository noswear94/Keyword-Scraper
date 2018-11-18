from bs4 import BeautifulSoup
import requests
import urllib.request
import re
from collections import Counter
import sys
from tkinter import *

root=Tk()
root.title("Keywords Counter")
root.resizable(width=False, height=False)
root.geometry("350x190+0+0")

heading=Label(root,text="Welcome to the Keyword Counter",font="Arial 10").pack()

label1=Label(root, text="Enter the text to search : ").place(x=20,y=30)
query=StringVar()
entry_box1=Entry(root,textvariable=query,width=25).place(x=160,y=30)

label5=Label(root, text="Enter the file name : ").place(x=20,y=70)
file=StringVar()
entry_box5=Entry(root,textvariable=file,width=25).place(x=160,y=70)

def search():
    queries = query.get()
    queries = queries.replace(" ","+")
    url = "http://www.google.com/search?q="+queries

    text = []
    final_text = []

    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")

    for desc in soup.find_all("span",{"class":"st"}):
        text.append(desc.text)

    for title in soup.find_all("h3",attrs={"class":"r"}):
        text.append(title.text)

    for string in text:
        string  = re.sub("[^A-Za-z ]","",string)
        final_text.append(string)

    count_text = ' '.join(final_text)
    res = Counter(count_text.split())
    keyword_Count = dict(sorted(res.items(), key=lambda x: (-x[1], x[0])))

    for x,y in keyword_Count.items():
        filename=str("output/"+file.get())+".txt"
        with open(filename, "a", encoding='utf-8') as f:
            f.write("%s : %s\n"%(x,y))


work=Button(root,text="Scrape",width=10,height=2,command=search).place(x=120,y=100)

root.mainloop()
