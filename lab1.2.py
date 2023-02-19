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

def isCorrect(num):
    digits = set(['0','1','2','3','4','5','6','7','8','9'])
    for n in list(str(num)):
        if n not in digits:
            print(type(n))
            print(n)
            return False
    return True


class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    res = 0
    def build(self):
        self.num1 = ["0"]*4
        self.num2 = ["0"]*4
        i=0
        btns = ["м", "дм", "см", "мм"]
        x=5; y=25
        for bt in btns:
            print(self.num1[i])
            self.num1[i]=Text(root, state = 'normal',
                   font=("Times New Roman", 24))
            self.num1[i].place(x=x, y=y,width=150,height=90)
            x += 200; i+=1

        x = 160;y = 75
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Label(root, text = bt,
                 font=("Times New Roman", 18)).place(x=x, y=y, width=40, height=40)
            x += 200

        x = 5;
        y = 225
        i=0
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            self.num2[i]=Text(root, state='normal',
                 font=("Times New Roman", 24))
            self.num2[i].place(x=x, y=y, width=150, height=90)
            x += 200; i+=1


        x = 160;
        y = 275
        for bt in btns:
            com = lambda x=bt: self.logicalc(x)
            Label(root, text=bt,
                  font=("Times New Roman", 18)).place(x=x, y=y, width=40, height=40)
            x += 200

        self.sign = Text(root, font=("Times New Roman", 32))
        self.sign.place(x=340, y=145, width=75, height=50)
        self.sign.tag_add("center", "1.0", "end")

        self.eq = Button(root,text="=",
                   font=("Times New Roman", 32),bg ='#FFF',command = lambda: self.action())\
                                      .place(x=825, y=145,width=80,height=50)

        self.result = Text(root, state='disabled', font=("Times New Roman", 24))
        self.result.place(x=940, y=125, width=200, height=90)

        self.cmb_3 = Combobox(root, font=("Times New Roman", 18),state="readonly")
        self.cmb_3['values'] = ("м","дм","см","мм")
        self.cmb_3.current(2)
        self.cmb_3.place(x=1160, y=175, width=60, height=40)

        btns = ["C", "DEL","+", "-"]

        x = 20
        y = 340
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
        if operation == "+":
            if self.sign.get !='':
                self.sign.delete("1.0","end")
            self.sign.insert("1.0",operation)
        if operation =="-":
            if self.sign.get !='':
                self.sign.delete("1.0","end")
            self.sign.insert("1.0",operation)

    def num_error(self):
        showwarning(title="Ошибка", message="Введены недопустимые символы в поле ввода числа!")

    def action(self):
        kf=1000
        res1=0
        for i in range(0,4):
            temp=self.num1[i].get("1.0","end")
            temp = temp.replace('\n','')
            if not isCorrect(temp):
                self.num_error()
            if(temp!="\n"):
                res1+=int(temp)*kf
            kf/=10

        res2=0
        kf=1000
        for i in range(0,4):
            temp=self.num2[i].get("1.0","end")
            temp = temp.replace('\n', '')
            if not isCorrect(temp):
                self.num_error()
            if(temp!="\n"):
                res2+=int(temp)*kf
            kf/=10

        sign = self.sign.get("1.0", "end")
        sign = sign.replace("\n", "")
        if sign == '+':
            res = res1 + res2
        if sign == '-':
            res = res1 - res2

        base=self.cmb_3.get()
        res=convertFromMMToAny(res,base)

        self.result.config(state=NORMAL)
        if (self.result.get != ""):
            self.result.delete("1.0","end")
        self.result.insert("1.0", res)
        self.result.config(state=DISABLED)

        return res

if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#6A5ACD"
    root.geometry("1300x500+0+100")
    root.title("Калькулятор")
    root.resizable(True, True)
    app = Main(root)
    app.pack()
    root.mainloop()
