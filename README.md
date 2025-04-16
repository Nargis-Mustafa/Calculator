## Abstract

This is a graphical user interface (GUI) calculator. Which perform basic mathematical operation such as addition, subtraction, multiplication etc. We have to just give the expression by using button provided inside the calculator and click equal(=) button now we get the output of the expression.

## Language Used

**Python** [Download Here](https://www.python.org/downloads/)

## Library user

- tkinter
- string

## Sample Program

```python
from tkinter import *
import string
root=Tk()
root.title("Simple Calculator")
root.resizable(height=False,width=False)
root.geometry("480x568+450+120")
root.configure(bg="black")
```
## Visual

![calculator pic](https://github.com/user-attachments/assets/2fe704fe-5e55-44af-a904-7735c7a481e0)

## Adding Custom Logo

If we want to add logo in the application then we have to add the logo file having .ico extention. There is default logo because line no. 12 is comment out.
If we add logo file and uncomment the line no. 12 then our application support custom logo. I have also added the logo file with name "calocon.ico"
After adding custom logo application look like this. 


![Calculator with logo](https://github.com/user-attachments/assets/1970efd8-4e3d-42d8-a181-aba8169d37fc)

## Result

It will show the output of the calculation in the entry field.
