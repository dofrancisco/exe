from tkinter import *
#import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from joblib import dump, load
import numpy as np
import pandas as pd
top = Tk()
top.geometry("200x200")
# label to show the image


def helloCallBack():
   msg=messagebox.showinfo( "Hello Python", "Hello World")

def make_inference():
    

    file_inference= askopenfilename()
    data = pd.read_csv(file_inference,sep=';')
    print(data.head())
    model= askopenfilename()
    clf = load(model)
    
    X = data.loc[:,data.columns != 'CLASSE']

    result=clf.predict(X)
    print(result)

    np.savetxt('myarray.txt', result)
B = Button(top, text ="Hello", command = helloCallBack)
C = Button(top, text ="Inferencia", command = make_inference)




B.place(x=50,y=50)
C.place(x=50,y=100)


top.mainloop()

