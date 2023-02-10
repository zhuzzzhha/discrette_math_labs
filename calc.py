from tkinter import *
from tkinter.ttk import Combobox

class Main(Frame):
    def __init__(self, root):
        super(Main, self).__init__(root)
        self.build()

    def build(self):
        self.first_num = Text(root,state = 'normal',font = ("Times New Roman", 24))
        self.first_num.place(x =5, y = 25,width=240,height = 90)

        self.cmb_1 = Combobox(root,font = ("Times New Roman",18))
        self.cmb_1['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        self.cmb_1.current(10)
        self.cmb_1.place(x = 250, y = 75,width=60,height = 40)

        self.sign = Text(root,font = ("Times New Roman",32))
        self.sign.place(x = 320, y = 45, width = 75,height = 50)
        self.sign.tag_add("center", "1.0", "end")

        self.second_num = Text(root,state = 'normal',font = ("Times New Roman", 24))
        self.second_num.place(x=415, y=25, width=240, height = 90)


        self.cmb_2 = Combobox(root,font = ("Times New Roman",18))
        self.cmb_2['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        self.cmb_2.current(10)
        self.cmb_2.place(x=660, y=75,width=60,height = 40)

        self.eq = Button(root,text="=",
                   font=("Times New Roman", 32),bg ='#FFF').place(x=725, y=45,
                                      width=80,
                                      height=50)

        self.result = Text(root, state='normal', font=("Times New Roman", 24))
        self.result.place(x=815, y=25, width=240, height=90)

        self.cmb_3 = Combobox(root, font=("Times New Roman", 18))
        self.cmb_3['values'] = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        self.cmb_3.current(10)
        self.cmb_3.place(x=1060, y=75, width=60, height=40)

        btns = [
            "C", "DEL", "*","/","+","-","^"

    ]
        syst_btns = [
            "2","3","4","5","6","7","8","9","10","11","12",
            "13","14","15","16"
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
    def clearFirst(self):
        self.first_num.delete("1.0",END)
    def clearSecond(self):
        self.second_num.delete("1.0",END)
    def clearSign(self):
        self.sign.delete("1.0",END)




if __name__ == '__main__':
    root = Tk()
    root["bg"] = "#6A5ACD"
    root.geometry("1125x250+200+200")
    root.title("Калькулятор")
    root.resizable(True, True)
    app = Main(root)
    app.pack()
    root.mainloop()