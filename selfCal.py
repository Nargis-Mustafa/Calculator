#importing the required libraries

from tkinter import *
import string

# Setup the main window
root=Tk()
root.title("Simple Calculator")
root.resizable(height=False,width=False)
root.geometry("480x568+450+120")
root.configure(bg="black")
#root.iconbitmap("calicon.ico")

cal=Frame(root)
cal.grid()

#val is a global variable to store the value of the expression
#that is being evaluated

val=""

#button click function
#this function will be called when the button is clicked
def clickbtn(num):
    global val
    if num == "\u221A":
        if val.isdigit():
            val="\u221A"+val
        else:
            val=""
    elif num == "-1*":
        if val == "" or val == "-":
            val="-1*"
        elif val[0]=="-":
            val=val[1:]
        else:
            val="-1*"+val
    else:
        val=val+str(num)
    data.set(val)

# clear_All function
# this function will clean the entry when the CE button is clicked
def clear_All():
    global val
    val=""
    data.set(val)

# clear function
# this function will delete the  last entry when the C button is clicked
def clear():
    global val
    val=val[:-1]
    data.set(val)

# evaluation function
# this function will evaluate the expression when the = button is clicked
def equal():
    global val
    if "\u221A" in val:
        val=val.replace("\u221A","")
        val=val+"**0.5"
    result=str(eval(val))
    data.set(result)
    val=result

#creating a StringVar() to store the data

data=StringVar()

#creating the entry field for the calculator
#this will display the value of the expression that is being evaluated

textdisplay=Entry(cal,bg="white",fg="black",font=('Helvetica',20,'bold'),width="28",justify="right",bd=30,textvariable=data)
textdisplay.grid(row=0,column=0, columnspan=5, pady=1,padx=5)
textdisplay.configure(state="readonly")

#creating the buttons for the calculator

#row 1

btn1=Button(cal,width=6,height=2,bg="black",fg="white",text=chr(67),font=('Helvetica',20,'bold'),pady=2,bd=4,command=clear)
btn1.grid(row=1,column=0)

btn2=Button(cal,width=6,height=2,bg="black",fg="white",text=chr(67)+chr(69),font=('Helvetica',20,'bold'),pady=2,bd=4,command=clear_All)
btn2.grid(row=1,column=1)

btn3=Button(cal,width=6,height=2,bg="black",fg="white",text="\u221A",font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("\u221A"))
btn3.grid(row=1,column=2)

btn4=Button(cal,width=6,height=2,bg="black",fg="white",text="+",font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("+"))
btn4.grid(row=1,column=3)

#row 2

btn5=Button(cal,width=6,height=2,fg="black",text=7,font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("7"))
btn5.grid(row=2,column=0)

btn6=Button(cal,width=6,height=2,fg="black",text=8,font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("8"))
btn6.grid(row=2,column=1)

btn7=Button(cal,width=6,height=2,fg="black",text=9,font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("9"))
btn7.grid(row=2,column=2)

btn8=Button(cal,width=6,height=2,bg="black",fg="white",text="-",font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("-"))
btn8.grid(row=2,column=3)


#row 3

btn9=Button(cal,width=6,height=2,fg="black",text=4,font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("4"))
btn9.grid(row=3,column=0)

btn10=Button(cal,width=6,height=2,fg="black",text=5,font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("5"))
btn10.grid(row=3,column=1)

btn11=Button(cal,width=6,height=2,fg="black",text=6,font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("6"))
btn11.grid(row=3,column=2)

btn12=Button(cal,width=6,height=2,bg="black",fg="white",text="x",font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("*"))
btn12.grid(row=3,column=3)

#row 4

btn13=Button(cal,width=6,height=2,fg="black",text=1,font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("1"))
btn13.grid(row=4,column=0)

btn14=Button(cal,width=6,height=2,fg="black",text=2,font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("2"))
btn14.grid(row=4,column=1)

btn15=Button(cal,width=6,height=2,fg="black",text=3,font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("3"))
btn15.grid(row=4,column=2)

btn16=Button(cal,width=6,height=2,bg="black",fg="white",text="/",font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("/"))
btn16.grid(row=4,column=3)


#row 5

btn17=Button(cal,width=6,height=2,fg="black",text=0,font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("0"))
btn17.grid(row=5,column=0)

btn18=Button(cal,width=6,height=2,fg="black",text=".",font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("."))
btn18.grid(row=5,column=1)

btn19=Button(cal,width=6,height=2,fg="black",text=chr(177),font=('Helvetica',20,'bold'),pady=2,bd=4,command=lambda:clickbtn("-1*"))
btn19.grid(row=5,column=2)

btn20=Button(cal,width=6,height=2,bg="black",fg="white",text="=",font=('Helvetica',20,'bold'),pady=2,bd=4,command=equal)
btn20.grid(row=5,column=3)


root.mainloop()

