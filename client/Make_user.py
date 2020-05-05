import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox


class Apps(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=15, weight="bold", slant="italic")

        self.title("Sea Your Info")
        self.geometry('1050x650')
        self.resizable(False, False)
        self.configure(background='white')
        self.iconbitmap(r'imagefile\sea_your_info.ico')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (
        StartPage, Make_User_page, Find_User_Info, main, Change_User_Info, Mk_U_Suss, ch_U_Suss, Find_ID, Find_PW):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.pack(side="top", fill="x", pady=10)

        def clickMe():
            # 아무것도 입력하지 않았을때 오류 발생문 필요

            messagebox.showinfo("Button CLicked", str1.get())
            messagebox.showinfo("Button CLicked", str2.get())
            controller.show_frame("main")

        label3 = tk.Label(self, text="Login", font=controller.title_font, background = 'white')
        label3.place(x=40, y=135)

        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="E-mail", background = 'white')
        # LabelWidget1.pack(side=LEFT)
        LabelWidget1.place(x=190, y=130)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        # display1.pack(side=RIGHT)
        display1.place(x=290, y=130)

        str2 = StringVar()
        LabelWidget3 = tk.Label(self, text="PW", background = 'white')
        # LabelWidget3.pack(side=LEFT)
        LabelWidget3.place(x=190, y=230)
        display3 = tk.Entry(self, width=20, textvariable=str2)
        # display3.pack(side=RIGHT)
        display3.place(x=290, y=230)

        button1 = tk.Button(self, text="회원가입", command=lambda: controller.show_frame("Make_User_page"), background='white')
        button2 = tk.Button(self, text="아이디/비번 찾기", command=lambda: controller.show_frame("Find_User_Info"), background='white')
        button3 = tk.Button(self, text="Login", command=clickMe, background='white')

        button1.place(x=220, y=330)
        button2.place(x=320, y=330)
        button3.place(x=400, y=270)


class main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background = 'white')
        label.pack(side="top", fill="x", pady=10)
        LabelWidget1 = tk.Label(self, text="Main Page", background = 'white')
        LabelWidget1.place(x=180, y=180)

        button1 = tk.Button(self, text="로그아웃", command=lambda: controller.show_frame("StartPage"))
        button1.place(x=430, y=350)
        button2 = tk.Button(self, text="회원정보 수정", command=lambda: controller.show_frame("Change_User_Info"))
        button2.place(x=430, y=300)


class Make_User_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')

        def clickMe():
            messagebox.showinfo("Button CLicked", str1.get())
            messagebox.showinfo("Button CLicked", str2.get())
            messagebox.showinfo("Button CLicked", str3.get())
            messagebox.showinfo("Button CLicked", str4.get())
            controller.show_frame("Mk_U_Suss")

        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background = 'white')
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="회원가입", font=controller.title_font, background = 'white')
        label2.place(x=140, y=90)

        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="E-mail", background = 'white')
        # LabelWidget1.pack(side=LEFT)
        LabelWidget1.place(x=170, y=130)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        # display1.pack(side=RIGHT)
        display1.place(x=270, y=130)

        str2 = StringVar()
        LabelWidget2 = tk.Label(self, text="Name", background = 'white')
        # LabelWidget2.pack(side=LEFT)
        LabelWidget2.place(x=170, y=180)
        display2 = tk.Entry(self, width=20, textvariable=str2)
        # display2.pack(side=RIGHT)
        display2.place(x=270, y=180)

        str3 = StringVar()
        LabelWidget3 = tk.Label(self, text="PW", background = 'white')
        # LabelWidget3.pack(side=LEFT)
        LabelWidget3.place(x=170, y=230)
        display3 = tk.Entry(self, width=20, textvariable=str3)
        # display3.pack(side=RIGHT)
        display3.place(x=270, y=230)

        str4 = StringVar()
        LabelWidget3_1 = tk.Label(self, text="PW Check", background = 'white')
        # LabelWidget3_1.pack(side=LEFT)
        LabelWidget3_1.place(x=170, y=280)
        display3_1 = tk.Entry(self, width=20, textvariable=str4)
        # display3_1.pack(side=RIGHT)
        display3_1.place(x=270, y=280)

        button = tk.Button(self, text="회원가입", command=clickMe)
        button.place(x=420, y=330)


class Change_User_Info(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background = 'white')
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="회원정보 수정", font=controller.title_font, background = 'white')
        label2.place(x=140, y=90)

        def clickMe():
            messagebox.showinfo("Button CLicked", str1.get())
            messagebox.showinfo("Button CLicked", str2.get())
            messagebox.showinfo("Button CLicked", str3.get())
            messagebox.showinfo("Button CLicked", str4.get())
            controller.show_frame("ch_U_Suss")

        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="E-mail", background = 'white')
        # LabelWidget1.pack(side=LEFT)
        LabelWidget1.place(x=170, y=130)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        # display1.pack(side=RIGHT)
        display1.place(x=270, y=130)

        str2 = StringVar()
        LabelWidget2 = tk.Label(self, text="Name", background = 'white')
        # LabelWidget2.pack(side=LEFT)
        LabelWidget2.place(x=170, y=180)
        display2 = tk.Entry(self, width=20, textvariable=str2)
        # display2.pack(side=RIGHT)
        display2.place(x=270, y=180)

        str3 = StringVar()
        LabelWidget3 = tk.Label(self, text="PW", background = 'white')
        # LabelWidget3.pack(side=LEFT)
        LabelWidget3.place(x=170, y=230)
        display3 = tk.Entry(self, width=20, textvariable=str3)
        # display3.pack(side=RIGHT)
        display3.place(x=270, y=230)

        str4 = StringVar()
        LabelWidget3_1 = tk.Label(self, text="PW Check", background = 'white')
        # LabelWidget3_1.pack(side=LEFT)
        LabelWidget3_1.place(x=170, y=280)
        display3_1 = tk.Entry(self, width=20, textvariable=str4)
        # display3_1.pack(side=RIGHT)
        display3_1.place(x=270, y=280)

        button = tk.Button(self, text="완료", command=clickMe)
        button.place(x=420, y=330)


class Find_User_Info(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background = 'white')
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="find ID", font=controller.title_font, background = 'white')
        # label2.pack(side="top", pady=5)
        label2.place(x=120, y=80)

        LabelWidget1 = tk.Label(self, text="E-mail", background = 'white')
        # LabelWidget1.pack(side=LEFT)
        LabelWidget1.place(x=170, y=120)
        display1 = tk.Entry(self, width=20)
        # display1.pack(side=RIGHT)
        display1.place(x=270, y=120)

        LabelWidget2 = tk.Label(self, text="Name", background = 'white')
        # LabelWidget1.pack(side=LEFT)
        LabelWidget2.place(x=170, y=150)
        display2 = tk.Entry(self, width=20)
        # display2.pack(side=RIGHT)
        display2.place(x=270, y=150)

        label3 = tk.Label(self, text="find PW", font=controller.title_font, background = 'white')
        label3.pack(side="top", pady=5)
        label3.place(x=120, y=220)

        LabelWidget3 = tk.Label(self, text="E-mail", background = 'white')
        # LabelWidget3.pack(side=LEFT)
        LabelWidget3.place(x=170, y=260)
        display3 = tk.Entry(self, width=20)
        # display3.pack(side=RIGHT)
        display3.place(x=270, y=260)

        button1 = tk.Button(self, text="완료", command=lambda: controller.show_frame("Find_ID"))
        # button1.pack()
        button1.place(x=400, y=180)

        button2 = tk.Button(self, text="완료", command=lambda: controller.show_frame("Find_PW"))
        # button2.pack()
        button2.place(x=400, y=290)


class Find_ID(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background = 'white')
        label.pack(side="top", fill="x", pady=10)

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력
        label2 = tk.Label(self, text="등록하신 아이디는... 입니다.", font=controller.title_font, background = 'white')
        label2.place(x=200, y=100)

        button1 = tk.Button(self, text="확인", command=lambda: controller.show_frame("StartPage"))
        # button1.pack()
        button1.place(x=450, y=300)


class Find_PW(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.pack(side="top", fill="x", pady=10)

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력
        label2 = tk.Label(self, text="임시 비밀번호 ... 이 되었습니다.\n 접속후 PW를 변경해 주세요", font=controller.title_font, background='white')
        label2.place(x=200, y=100)

        button1 = tk.Button(self, text="확인", command=lambda: controller.show_frame("StartPage"))
        # button1.pack()
        button1.place(x=450, y=300)


class Mk_U_Suss(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background = 'white')
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="회원가입에 성공했습니다.", font=controller.title_font, background = 'white')
        label2.place(x=200, y=100)

        button1 = tk.Button(self, text="돌아가기", command=lambda: controller.show_frame("StartPage"))
        # button1.pack()
        button1.place(x=450, y=300)


class ch_U_Suss(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background = 'white')
        label.pack(side="top", fill="x", pady=10)

        label2 = tk.Label(self, text="회원정보 변경에 성공했습니다.", font=controller.title_font, background = 'white')
        label2.place(x=200, y=100)

        button1 = tk.Button(self, text="돌아가기", command=lambda: controller.show_frame("main"))
        # button1.pack()
        button1.place(x=450, y=300)


if __name__ == "__main__":
    app = Apps()
    app.mainloop()
