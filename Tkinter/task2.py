from tkinter import *
from tkinter import ttk, messagebox

#2. Реализуйте программу с интерфейсом на tkinter, 
# которая будет у пользователя запрашивать два числа 
# и выводить в консоль СУММУ ВСЕХ ЧИСЕЛ МЕЖДУ НИМИ (включительно).

root = Tk()   

def additions(event):
    nums = ent.get().split()
    try:
        nums = [int(x) for x in nums]
    except Exception as e:
        messagebox.showerror(title="Error", message=e)
        return
        
    if len(nums) != 2:
        messagebox.showerror(title="Error", message="Amount of numbers is incorrect")
        return
        
    if nums[0] > nums[1]:
        messagebox.showerror(title="Error", message='Second number is lower than first')
        return

    sum = 0
    for i in range(nums[0], nums[1] + 1):
        sum += i
    lab['text'] = str(sum)

lab1 = ttk.Label(width=50, text='Enter two numbers', background='black', foreground='white')
ent = ttk.Entry(width= 30)
but = ttk.Button(text="multiply")
lab = ttk.Label(width=50, background='black', foreground='white')

but.bind('<Button-1>', additions)

lab1.pack()
ent.pack()
but.pack()
lab.pack()

root.mainloop()