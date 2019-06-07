from readtweet import *
from stop import *
from final_predict import *
from livegraphing import *
import tkinter

def pred():
     b=predict()
     p2.destroy()
     xxxxx=b[0]
     predictions=b[1]

     
     #print(xxxxx)
     #print(predictions)
     plotshow()     
     predictions1=[]
     for i in range (len(predictions)):
          if predictions[i]==0:
               predictions1.append('Negative Sentiment')
          elif predictions[i]==4:
               predictions1.append('Positive Sentiment')
     #print(predictions1)
     height = 35
     width = 2
     #print(height)
     screen3=tkinter.Tk()
     screen3.geometry('1800x900')

     screen3.title("Twitter Sentimment Analysis")
     for i in range(height):
         for j in range(2):
                           
             if j==0:
                  l = tkinter.Label(text=xxxxx[i])
             else:
                  l = tkinter.Label(text=predictions1[i])
               
             l.grid(row=i, column=j)

     
     screen3.mainloop()

     

     

def stop1():
     root.destroy()
     
     p2 = tkinter.Tk()
     global p2
     p2.geometry('1800x900')

     p2.title("Twitter Sentimment Analysis")


     with open("keywords.txt", "r") as f:
         readlines=f.readlines()
     f.close()
     readlines = list(dict.fromkeys(readlines))

     label = tkinter.Label( p2, text='The following are the topics of which tweets have been discovered' + ' \n')

     label.pack()

     listbox = tkinter.Listbox(p2)
     listbox.pack()

     listbox.insert(tkinter.END, "Tweet Topics")

     for item in readlines:
         listbox.insert(tkinter.END, item)

     btn2 = tkinter.Button(p2, text="Make Predictions", command=pred)
     btn2.pack()

     p2.mainloop()
     stop()
     
     
     
     


     
root = tkinter.Tk()

root.geometry('1800x900')

root.title("Twitter")





btn2 = tkinter.Button(root, text="Start the Tweet Search", command=readtweet)

btn2.pack()
btn1 = tkinter.Button(root, text="Stop Tweet Search", command=stop1)
btn1.pack()



root.mainloop()

