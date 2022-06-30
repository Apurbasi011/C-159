from tkinter import*
from tkinter import messagebox 

root = Tk()
root.geometry("600x400")

list_name = ["Mickey mouse", "Elsa", "Anna", "Donald Duck"]
dict_student = {"Name" : "Shinchan",
                "Age" : "5"}

try:
    print(list_name[5])
    
    print(dict_student["mom"])
    
except IndexError:
    messagebox.showinfo("Error", "This Index Does Not Exist")
    
except KeyError:
    messagebox.showinfo("Error", "This Key Does Not Exist")
    
root.mainloop()



