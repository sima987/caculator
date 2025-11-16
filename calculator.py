import tkinter

# Button layout
button_values = [
    ["AC", " +/- ", "%", "/"],
    ["7", "8", "9", "*"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

right_symbols = ["+", "-", "*", "/", "="]
top_symbols = ["AC", " +/- ", "%"]

row_count = len(button_values)
col_count = len(button_values[0])

# Colors (must include # for hex values)
color1 = "#E0BBE4"
color2 = "#957DAD"
color3 = "#D291BC"
color4 = "#FEC8D8"
color5 = "#FFDFD3"

# Window setup
window = tkinter.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tkinter.Frame(window)

# Label display
label = tkinter.Label(frame, text="0", font=("Arial", 45), background="black", foreground="white",anchor="e",width=col_count)
label.grid(row=0, column=0, columnspan=col_count, sticky="we")

# Button click handler
def button_clicked(value):
    print("Button clicked:", value)  # for now just prints

# Create buttons
for row in range(row_count):
    for column in range(col_count):
        value = button_values[row][column]
        button = tkinter.Button(
            frame, text=value, font=("Arial", 20),
            width=8, height=3,
            command=lambda value=value: button_clicked(value)
        )
        if value in top_symbols:
            button.config(foreground="black",background="#EBE1DD")
        elif value in right_symbols:
            button.config(foreground="white", background="#E09232")
        else:
            button.config(foreground="black", background="#E8E4E0")
        button.grid(row=row+1, column=column)

frame.pack()





#a+b
A="0"
operator=None
B=None

def clear_all():
    global A,B,operator
    A="0"
    operator=None
    B=None
    
def remove_zero_decimal(num):
    if num%1==0:
        num=int(num)
    return str(num)    

def button_clicked(value):
    global right_symbols,top_symbols,A,B,operator
    
    if value in right_symbols:
        if value=="=":
            if A is not None and operator is not None:
                B=label["text"]
                num1=float(A)
                num2=float(B)
                
                if operator=="+":   
                    label["text"]=remove_zero_decimal(num1+num2)
                elif operator=="-":
                    label["text"]=remove_zero_decimal(num1-num2)
                elif operator=="*":
                    label["text"]=remove_zero_decimal(num1*num2)
                elif operator=="/":
                    label["text"]=remove_zero_decimal(num1/num2)
                clear_all()
                    
        elif value in "+-*":
           if operator is None:
               A=label["text"]
               label["text"]="0"
               B="0"
               operator=value
    elif value in top_symbols:
        if value=="AC":
            clear_all()
            label["text"]="0"
            
        elif value==" +/- ":
            result=float(label["text"])*-1
            label["text"]=remove_zero_decimal(result)
        elif value=="%":
            result=float(label["text"])/100
            label["text"]=remove_zero_decimal(result)
            pass
        elif value=="√":
            result=float(label["text"])**0.5
            label["text"]=remove_zero_decimal(result)
            pass
    else:
        if value==".":
            if value not in label["text"]:
                label["text"]+=value
        elif value in "0123456789":
            if label["text"]=="0":
                label["text"]=value
            else:
                label["text"]+=value
                






#center the window
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

window.mainloop()
