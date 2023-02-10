from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import showerror, showwarning, showinfo

def convertFromDecimalToAny(num, base, upper=False):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    if base > len(digits): return None
    result = ''
    number = int(num)
    while number > 0:
        result = digits[number % base] + result
        number //= base
    return str(result.upper()) if upper else result


def convertFromAnyToDecimal(num, bas):
    number = str(num)
    base = int(bas)
    return str(int(number, base))

def isCorrect(num,base:int):
    letters = list(map(str,['A','B','C','D','E','F']))
    right = [str(i) for i in range(0,base)]
    if(base>10):
        for l in letters[0:base-10]:
            right.append(l)
    right = set(right)
    for n in str(num):
        print(n)
        if str(n) not in right:
            return False
    return True


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.first_num = Text(root,state = 'normal',font = ("Times New Roman", 24))
        self.first_num.place(x =5, y = 25,width=240,height = 90)

        self.cmb_1 = Combobox(root,font = ("Times New Roman",18),state="readonly")
        self.cmb_1['values'] = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        self.cmb_1.current(10)
        self.cmb_1.place(x = 250, y = 75,width=60,height = 40)

        self.sign = Text(root,font = ("Times New Roman",32))
        self.sign.place(x = 320, y = 45, width = 75,height = 50)
        self.sign.tag_add("center", "1.0", "end")

        self.second_num = Text(root,state = 'normal',font = ("Times New Roman", 24))
        self.second_num.place(x=415, y=25, width=240, height = 90)


        self.cmb_2 = Combobox(root,font = ("Times New Roman",18),state="readonly")
        self.cmb_2['values'] = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        self.cmb_2.current(10)
        self.cmb_2.place(x=660, y=75,width=60,height = 40)

        self.eq = Button(root,text="=",
                   font=("Times New Roman", 32),bg ='#FFF',command = lambda: self.action()).place(x=725, y=45,
                                      width=80,
                                      height=50)

        self.result = Text(root, state='disabled', font=("Times New Roman", 24))
        self.result.place(x=815, y=25, width=240, height=90)

        self.cmb_3 = Combobox(root, font=("Times New Roman", 18),state="readonly")
        self.cmb_3['values'] = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        self.cmb_3.current(10)
        self.cmb_3.place(x=1060, y=75, width=60, height=40)

        btns = [
            "C", "DEL", "*","/","+","-","^"

    ]

        x = 20
        y = 140
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Button(text=bt, bg="#FFF",
                   font=("Times New Roman", 32),
                   command=com).place(x=x, y=y,
                                      width=115,
                                      height=79)
            x += 117

    def logicalc(self,operation):
        if operation == 'C':
            self.first_num.delete("1.0", "end")
            self.second_num.delete("1.0","end")
        if operation == 'DEL':
            self.clearSign()
        if operation == "*":
            if self.sign.get !='':
                self.sign.delete("1.0","end")
            self.sign.insert("1.0","  " + operation)
        if operation == "/":
            if self.sign.get !='':
                self.sign.delete("1.0","end")
            self.sign.insert("1.0","   " + operation)
        if operation == "^":
            if self.sign.get !='':
                self.sign.delete("1.0","end")
            self.sign.insert("1.0","  " + operation)
        if operation == "+":
            if self.sign.get !='':
                self.sign.delete("1.0","end")
            self.sign.insert("1.0","  " + operation)
        if operation =="-":
            if self.sign.get !='':
                self.sign.delete("1.0","end")
            self.sign.insert("1.0","   " + operation)
    def clearSign(self):
        self.sign.delete("1.0",END)

    def num_error(self):
        showerror(title="Ошибка", message="Введены недопустимые символы в поле ввода числа!")
    def action(self):
        first_num_act = self.first_num.get("1.0","end")
        first_base_act = self.cmb_1.get()
        second_num_act = self.second_num.get("1.0","end")
        second_base_act = self.cmb_2.get()
        print(first_num_act,first_base_act)
        if (isCorrect(first_num_act,int(first_base_act[1:])) == False) or (isCorrect(second_num_act,int(second_base_act[1:])) == False):
            self.num_error()
    def ans(self):
        first_num = self.first_num.get("1.0","end")
        first_base = self.cmb_1.get()
        second_num = self.second_num.get("1.0", "end")
        second_base = self.cmb_2.get()
        if(first_base != "10"):
            first_num = convertFromAnyToDecimal(first_num,first_base)
        if(second_base != "10"):
            second_num = convertFromAnyToDecimal(second_num, second_base)








if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#6A5ACD"
    root.geometry("1125x250+200+200")
    root.title("Калькулятор")
    root.resizable(True, True)
    app = Main(root)
    app.pack()
    root.mainloop()



