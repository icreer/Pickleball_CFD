import tkinter as tk

# Creating a window in Tkinter
window = tk.Tk()

window.title("Test")



window.geometry("700x500")

'''
# will be useful for creating the widow state that not in fix diemtions
width = window.winfo_screenwidth()               
height = window.winfo_screenheight()               
window.geometry("%dx%d" % (width, height))
'''

# Create a label widget in Tkinter
label = tk.Label(window, text="Click the Button to update this Text",
font=('Calibri 15 bold'))
label.pack(pady=20)
 
# Function to update the label text for first button click in Tkinter
def on_click_btn1():
    label["text"] = "You clicked first button"
     
# Function to update the label text for second button click in Tkinter
def on_click_btn2():
    label["text"] = "You clicked second button"

# Function for updating the lable text for the entry_button
def display_text():
    value = int(entry.get())

    label["text"] =  value ** 2
     
# Create 1st button to update the label widget
btn1 = tk.Button(window, text="Button1", command=on_click_btn1)
btn1.pack(pady=20)
 
# Create 2nd button to update the label widget
btn2 = tk.Button(window, text="Button2", command=on_click_btn2)
btn2.pack(pady=40)
 
# Creating an Entry widget to accept user Input
entry = tk.Entry(window, width = 40)
entry.focus_set()
entry.pack()

entry_button = tk.Button(window, text= "data" , width=20, command = display_text).pack(pady=20)

# Run main loop
window.mainloop()
