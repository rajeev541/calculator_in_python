from tkinter import *
import getpass
import pyttsx3
import re

shall = Tk()
shall.title('Calculator')
shall.geometry('324x284')
shall.resizable(0, 0)
print()
pyttsx3.speak("Hello I am Rajeev")
pyttsx3.speak("Welcome to my Calculator")
pyttsx3.speak("Enter your password")
inpass = getpass.getpass ("Enter your password :")
apass = "rajeev"

if inpass!=apass:
    pyttsx3.speak("Incorrect Password Try Again ")
    exit()
pyttsx3.speak("Access Granted")

#btn_click function continuously update the input field whatever you enter a number
def btn_click(item):
    global expression
    lastIndex = len(expression) - 1

    # if operator is there and new operator comes then it replace with previous one
    if(item in ['+', '-', '*', '/']):
    
        if(lastIndex >= 0 and expression[lastIndex] in ['+', '-', '*', '/']):
            expression = expression[:-1] + item 
        else:
            expression = expression + str(item)
    
    # if dot is there and dot comes again then it's ignored
    elif(item == '.'):
        nArray = re.split(r'[\+\-\/\*]', expression)
        
        if('.' not in nArray[len(nArray) - 1]):
            expression = expression + str(item)
        else:
            return

    # for the numbers
    else:
        expression = expression + str(item)

    # replace * and / by it's unicode sign
    input_text.set(expression.replace('*', u'\u00D7').replace('/', u'\u00F7'))


# 'btn_clear' function clears the input field
def btn_clear():
    global expression
    expression = ""
    input_text.set("")


# btn_equal calculation the expression present in input field
def btn_equal():
    global expression
    
    # if last val is operator in expression then ignore it
    if(expression[len(expression) - 1] in ['+', '/', '*', '-']):
        expression = expression[:-1]

    # edd exception handling block
    try:
        result = str(eval(expression))  # 'eval' function evaluate the string expression derectly
        input_text.set(result)
    except Exception as e:
        input_text("")
        print(f"exception occured: {e.__cause__}")
    finally:
        expression = ""


expression = ""
# 'stringvar()' is used to get the instance of input field
input_text = StringVar()

# frame for input field
input_frame = Frame(shall, borderwidth='2', relief='solid')
input_frame.place(x=0, y=0, width=320, height='40')

# input field inside frame
input_field = Entry(input_frame, bg='#eee', font=('Arial', 17, 'bold'), textvariable=input_text ,justify='right')
input_field.place(x=1, y=0, width='315', height=36)

# frame for Button
btn_frame = Frame(shall, borderwidth=2, relief='solid')
btn_frame.place(x=0, y=38, width=318, height=245)

# first row
clear = Button(btn_frame, text='c', bg='#fff', font=('Arial', 15), command=lambda: btn_clear())
clear.place(x=0, y=5, width=236, height=45)

divide = Button(btn_frame, text='/', bg='#fff', font=('Arial', 15), command=lambda: btn_click("/"))
divide.place(x=239, y=5, width='75', height=45)

# second row
seven = Button(btn_frame, text='7', bg='#fff', font=('Arial', 15), command=lambda: btn_click(7))
seven.place(x=0, y=53, width=75, height=45)

eight = Button(btn_frame, text='8', font=('Arial', 15), bg='#fff', command=lambda: btn_click(8)).place(x=80, y=53,width=75,height=45)

nine = Button(btn_frame, text='9', font=('Arial', 15), bg='#fff', command=lambda: btn_click(9))
nine.place(x=160, y=53, width=75, height=45)

multiply = Button(btn_frame, text='*', font=('Arial', 15), bg='#fff', command=lambda: btn_click("*"))
multiply.place(x=240, y=53, width=75, height='45')

# third row
four = Button(btn_frame, text='4', font=('Arial', 15), bg='#fff', command=lambda: btn_click(4))
four.place(x=0, y=100, width=75, height=45)

five = Button(btn_frame, text='5', font=('Arial', 15), bg='#fff', command=lambda: btn_click(5))
five.place(x=80, y=100, width=75, height=45)

six = Button(btn_frame, text='6', font=('Arial', 15), bg='#fff', command=lambda: btn_click(6))
six.place(x=160, y=100, width=75, height=45)

substrack = Button(btn_frame, text='-', font=('Arial', 17), bg='#fff', command=lambda: btn_click("-"))
substrack.place(x=240, y=100, width=75, height=45)

# forth row
one = Button(btn_frame, text='1', font=('Arial', 15), bg='#fff', cursor='hand2', command=lambda: btn_click(1))
one.place(x=0, y=147, width=75, height=45)

two = Button(btn_frame, text='2', font=('Arial', 15), bg='#fff', command=lambda: btn_click(2))
two.place(x=80, y=147, width=75, height=45)

third = Button(btn_frame, text='3', font=('Arial', 15), bg='#fff', command=lambda: btn_click(3))
third.place(x=160, y=147, width=75, height=45)

plus = Button(btn_frame, text='+', font=('Arial', 15), bg='#fff', command=lambda: btn_click("+"))
plus.place(x=240, y=147, width=75, height=45)

# fifth row
zero = Button(btn_frame, text='0', font=('Arial', 15), bg='#fff', command=lambda: btn_click(0))
zero.place(x=0, y=195, width=155, height=45)

dot = Button(btn_frame, text='.', font=('Arial', 17), bg='#fff', command=lambda: btn_click("."))
dot.place(x=160, y=195, width=75, height=45)

equal = Button(btn_frame, text='=', font=('Arial', 15), bg='#fff', command=lambda: btn_equal())
equal.place(x=240, y=195, width=75, height=45)

shall.mainloop()
