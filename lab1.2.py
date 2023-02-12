from tkinter import *
from tkinter.ttk import Combobox
from tkinter.messagebox import showerror, showwarning, showinfo


def convertFromMMToAny(num, bas):
    number = int(num)
    base = str(bas)
    global min1
    min1=0
    if (base == "см"):
        number /= 10
    if (base == "дм"):
        number /= 100
    if (base == "м"):
        number /= 1000
    return str(number)


def convertFromAnyToMM(num, bas):
    number = int(num)
    base = str(bas)
    if(base=="см"):
        number*=10
    if (base == "дм"):
        number*=100
    if (base == "м"):
        number*=1000
    return str(number)

def isCorrect(num,base:int):
    letters = list(map(str,['A','B','C','D','E','F']))
    right = [str(i) for i in range(0,base)]
    if(base>10):
        for l in letters[0:base-10]:
            right.append(l)
    right = set(right)
    for n in str(num):
        if str(n) not in right:
            return False
    return True


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    res = 0
    def build(self):
        min_count_0 = 4
        self.first_num = Text(root,state = 'normal',font = ("Times New Roman", 24))
        self.first_num.place(x =5, y = 25,width=240,height = 90)

        self.cmb_1 = Combobox(root,font = ("Times New Roman",18),state="readonly")
        self.cmb_1['values'] = ("м","дм","см","мм")
        self.cmb_1.current(2)
        self.cmb_1.place(x = 250, y = 75,width=60,height = 40)

        self.sign = Text(root, font=("Times New Roman", 32))
        self.sign.place(x=320, y=45, width=75, height=50)
        self.sign.tag_add("center", "1.0", "end")

        self.second_num = Text(root, state='normal', font=("Times New Roman", 24))
        self.second_num.place(x=415, y=25, width=240, height=90)

        self.eq = Button(root,text="=",
                   font=("Times New Roman", 32),bg ='#FFF',command = lambda: self.action())\
                                      .place(x=725, y=45,width=80,height=50)

        self.result = Text(root, state='disabled', font=("Times New Roman", 24))
        self.result.place(x=815, y=25, width=240, height=90)

        self.cmb_2 = Combobox(root, font=("Times New Roman", 18), state="readonly")
        self.cmb_2['values'] = ("м","дм","см","мм")
        self.cmb_2.current(2)
        self.cmb_2.place(x=660, y=75, width=60, height=40)

        self.cmb_3 = Combobox(root, font=("Times New Roman", 18),state="readonly")
        self.cmb_3['values'] = ("м","дм","см","мм")
        self.cmb_3.current(2)
        self.cmb_3.place(x=1060, y=75, width=60, height=40)

        btns = ["C", "DEL", "*", "/", "+", "-", "^"]

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
            self.sign.insert("1.0",operation)
        if operation == "/":
            if self.sign.get !='':
                self.sign.delete("1.0","end")
            self.sign.insert("1.0",operation)
        if operation == "^":
            if self.sign.get !='':
                self.sign.delete("1.0","end")
            self.sign.insert("1.0",operation)
        if operation == "+":
            if self.sign.get !='':
                self.sign.delete("1.0","end")
            self.sign.insert("1.0",operation)
        if operation =="-":
            if self.sign.get !='':
                self.sign.delete("1.0","end")
            self.sign.insert("1.0",operation)

    def num_error(self):
        showerror(title="Ошибка", message="Введены недопустимые символы в поле ввода числа!")

    def action(self):
        first_num_act = self.first_num.get("1.0","end")
        second_num_act = self.second_num.get("1.0", "end")
        first_dim = self.cmb_1.get()
        second_dim = self.cmb_2.get()
        third_dim = self.cmb_3.get()

        first_num_act = first_num_act.replace("\n", "")
        second_num_act = second_num_act.replace("\n", "")
        first_dim = first_dim.replace("\n", "")
        second_dim = second_dim.replace("\n", "")
        third_dim = third_dim.replace("\n", "")

        #if (first_num_act not in {0,1,2,3,4,5,6,7,8,9} or second_num_act not in {0,1,2,3,4,5,6,7,8,9}):
        #   self.num_error()

        first_num_act1 = int(convertFromAnyToMM(first_num_act,first_dim))
        second_num_act1 = int(convertFromAnyToMM(second_num_act, second_dim))
        first_num_act = int(first_num_act)
        second_num_act = int(second_num_act)

        print(first_num_act, ' ',second_num_act,first_dim,second_dim)

        sign = self.sign.get("1.0", "end")
        sign = sign.replace("\n", "")
        if sign == '+':
            res = first_num_act1 + second_num_act1
        if sign == '-':
            res = first_num_act1 - second_num_act1
        if sign == '*':
            res = first_num_act1 * second_num_act1
        if sign == '/':
            res = (first_num_act1) / second_num_act1

        if sign == '^':
            res = pow(first_num_act1, second_num_act1)

        res = convertFromMMToAny(res,third_dim)

        self.result.config(state=NORMAL)
        if (self.result.get != ""):
            self.result.delete("1.0","end")
        self.result.insert("1.0", res)
        self.result.config(state=DISABLED)

        return res

if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#6A5ACD"
    root.geometry("1125x250+80+200")
    root.title("Калькулятор")
    root.resizable(True, True)
    app = Main(root)
    app.pack()
    root.mainloop()


