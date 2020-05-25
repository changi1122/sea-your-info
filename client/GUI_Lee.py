import tkinter as tk
import GUI_get_posts as Gposts
import Create_User
import Login
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox
import webbrowser


class Apps(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=30, weight="bold", slant="italic")
        global font_logintext
        font_logintext = tkfont.Font(family='Helvetica', size=15)
        global font_startpageinfo
        font_startpageinfo = tkfont.Font(family='Helvetica', size=18)
        global FB
        FB = tkfont.Font(family='Helvetica', size=10)
        global font_hypertext
        font_hypertext = tkfont.Font(size=10, underline=True)
        global font_Cheack_B
        font_Cheack_B = tkfont.Font(size=11, weight="bold", family='Helvetica')
        global font_listbox_content
        font_listbox_content = tkfont.Font(size=13, family='바른고딕')
        global font_radiobutton
        font_radiobutton = tkfont.Font(size=12, family='바른고딕', weight="bold")

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
                StartPage, Make_User_page, Find_User_Info, main, Change_User_Info, Mk_U_Suss, ch_U_Suss, Find_ID,
                Find_PW):
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
        # 맨 위의 Sea Your Info 들어가는 부분
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        # label.pack(side="top", fill="x", pady=10)
        label.place(x=100, y=35)

        image_mainlogo = PhotoImage(file='imagefile/logo2_color.gif')
        label_defaultlogo = Label(image=image_mainlogo, borderwidth=0)
        label_defaultlogo.image = image_mainlogo
        label_defaultlogo.place(x=20, y=20)

        # OP_bar 추가
        image_bar = PhotoImage(file='imagefile/OP_bar.png')
        label_defaultlogo = Label(image=image_bar)
        label_defaultlogo.image = image_bar
        label_defaultlogo.place(x=-10, y=100)

        def clickMe():
            string = []
            user_ID = str1.get()
            user_PW = str2.get()
            display1.delete(0, tk.END)
            display3.delete(0, tk.END)
            Lg = Login.Login(user_ID, user_PW)
            Lg.Check(string)
            print(string)
            if string[0] == 200:
                controller.show_frame("main")
            else:
                txt = ""
                for i in range(1, len(string)):
                    txt += string[i] + '\n'
                messagebox.showwarning("Error", txt)

        # 첫 화면 텍스트 부분
        label4 = tk.Label(self,
                          text="  정보바다에 오신 것을 환영합니다.\n\n정보바다에서는 여러분들의 학업 증진을 위하여\n 학교의 공지사항 정보들을 알려드리고 있습니다.\n\n회원가입과 로그인을 통하여 자세히 알아보세요.\n\n\nWelcome to Sea-Your-Info!\n\nSea-Your-Info will let you know all of the\nimportant school notice.\nIt will save your precious time.\n\nFor more information, do not hesitate to\njoin our free membership!\n\n",
                          font=font_startpageinfo, background='white')
        label4.place(x=440, y=160)

        # 텍스트 옆에 들어가는 로고 이미지 부분
        image_logo = PhotoImage(file='imagefile/logo2_color.gif')
        mainlogo = Label(self, image=image_logo, borderwidth=0)  # borderwidth가 여백을 제거해준다. 꿀팁
        mainlogo.image = image_logo
        mainlogo.place(x=445, y=140)

        label3 = tk.Label(self, text="Login", font=controller.title_font, background='white')
        label3.place(x=40, y=135)

        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="ID", background='white', font=font_logintext)
        LabelWidget1.place(x=40, y=240)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        display1.place(x=115, y=245)

        str2 = StringVar()
        LabelWidget3 = tk.Label(self, text="PW", background='white', font=font_logintext)
        LabelWidget3.place(x=40, y=280)
        bullet = "\u2022"
        display3 = tk.Entry(self, width=20, textvariable=str2, show=bullet)
        display3.place(x=115, y=285)

        log_B = PhotoImage(file='imagefile/OP_button3.png')

        button1 = Button(self, text="처음 오셨나요?", command=lambda: controller.show_frame("Make_User_page"),
                         background='white', borderwidth=0, font=font_hypertext, fg="#0000FF")
        button2 = Button(self, text="아이디와 비밀번호를 잊어버리셨나요?", command=lambda: controller.show_frame("Find_User_Info"),
                         background='white', borderwidth=0, font=font_hypertext, fg="#0000FF")
        button3 = Button(self, borderwidth=3, relief="flat", background='white', command=clickMe, padx=10, pady=10,
                         image=log_B)
        button3.image = log_B  # 이미지 안될 때는 이렇게 재정의 해줘야 함

        # 엔터 누르면 main프레임으로 넘어가는 것 구현
        def onReturn(event):
            value = display1.get()
            clickMe()

        display1.bind("<Return>", onReturn)
        display3.bind("<Return>", onReturn)

        button1.place(x=40, y=570)
        button2.place(x=40, y=590)
        button3.place(x=115, y=380)


class main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')

        # 맨 위에 Sea your Info 가 보이는 부분
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)
        global frame_department_notice
        global frame_school_notice
        global type_list
        type_list = []
        # 좌측 상단 user_image(USER라고 크게 적혀져있고 파란색 원 있는 부분) 출력 부분
        image_user = PhotoImage(file="imagefile/user_image.gif")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=25, y=120)

        # 좌측 상단 user_image 바로 오른 쪽에 있는 로그아웃과 회원정보 수정 버튼 부분
        button1 = tk.Button(self, text="로그아웃", command=lambda: controller.show_frame("StartPage"), borderwidth=0,
                            background='white', font=font_hypertext, fg="#0000FF")
        button1.place(x=145, y=160)
        button2 = tk.Button(self, text="회원정보 수정", command=lambda: controller.show_frame("Change_User_Info"),
                            borderwidth=0, background='white', font=font_hypertext, fg="#0000FF")
        button2.place(x=145, y=185)

        # 라디오 버튼은 사용자가 한개만 선택 가능, 체크박스는 여러게 선택 가능
        self.var0 = IntVar()
        radio_scholar = Checkbutton(self, text="장학금", background='white', font=FB, onvalue=1,
                                    variable=self.var0, command=self.convert)
        # font_radiobutton == FB로, Make_List==M_L로 변경
        radio_scholar.place(x=30, y=290)

        self.var1 = IntVar()
        radio_job = Checkbutton(self, text="대회", background='white', font=FB, onvalue=2, variable=self.var1,
                                command=self.convert)
        radio_job.place(x=130, y=290)

        self.var2 = IntVar()
        radio_event = Checkbutton(self, text="교환학생", background='white', font=FB, onvalue=3, variable=self.var2,
                                  command=self.convert)
        radio_event.place(x=230, y=290)

        self.var3 = IntVar()
        radio_text1 = Checkbutton(self, text="계절수업", background='white', font=FB, onvalue=4, variable=self.var3,
                                  command=self.convert)
        radio_text1.place(x=30, y=360)

        self.var4 = IntVar()
        radio_text2 = Checkbutton(self, text="등록금", background='white', font=FB, onvalue=5, variable=self.var4,
                                  command=self.convert)
        radio_text2.place(x=130, y=360)

        self.var5 = IntVar()
        radio_text3 = Checkbutton(self, text="신입생", background='white', font=FB, onvalue=6, variable=self.var5,
                                  command=self.convert)
        radio_text3.place(x=230, y=360)

        self.var6 = IntVar()
        radio_text4 = Checkbutton(self, text="외국어", background='white', font=FB, onvalue=7,
                                  variable=self.var6, command=self.convert)
        radio_text4.place(x=30, y=430)

        self.var7 = IntVar()
        radio_text5 = Checkbutton(self, text="인턴쉽,채용", background='white', font=FB, onvalue=8,
                                  variable=self.var7, command=self.convert)
        radio_text5.place(x=130, y=430)

        self.var8 = IntVar()
        radio_text6 = Checkbutton(self, text="특강", background='white', font=FB, onvalue=9,
                                  variable=self.var8, command=self.convert)
        radio_text6.place(x=230, y=430)

        self.var9 = IntVar()
        radio_text7 = Checkbutton(self, text="캡스톤", background='white', font=FB, onvalue=10,
                                  variable=self.var9, command=self.convert)
        radio_text7.place(x=30, y=500)

        self.var10 = IntVar()
        radio_text8 = Checkbutton(self, text="이외", background='white', font=FB, onvalue=11,
                                  variable=self.var10, command=self.convert)
        radio_text8.place(x=130, y=500)

        self.var11 = IntVar()
        radio_text9 = Checkbutton(self, text="None", background='white', font=FB, onvalue=12,
                                  variable=self.var11, command=self.convert)
        radio_text9.place(x=230, y=500)

        # 탭 부분 - notebook 이용하면 됨
        notebook_main = ttk.Notebook(self, width=670, height=470, padding=10)
        notebook_main.place(x=330, y=115)

        # 탭 부분 중에서 각 프레임 설정 부분
        # 첫 번째 프레임 설정 부분

        frame_department_notice = Frame(self)
        notebook_main.add(frame_department_notice, text="  학과 공지  ")

        # 두 번째 프레임 설정 부분
        frame_school_notice = Frame(self)
        notebook_main.add(frame_school_notice, text="  학교 공지  ")

        # Updated upstream
        scrollbar = tk.Scrollbar(frame_school_notice)
        scrollbar.pack(side="right", fill="y")
        listbox = tk.Listbox(frame_school_notice, yscrollcommand=scrollbar.set, width=660, height=460,
                             font=font_listbox_content)

        scrollbar2 = tk.Scrollbar(frame_department_notice)
        scrollbar2.pack(side="right", fill="y")
        listbox2 = tk.Listbox(frame_department_notice, yscrollcommand=scrollbar2.set, width=660, height=460,
                              selectmode="extended", font=font_listbox_content)

        def Show_data():
            global type_list
            global url_list
            if listbox.size() != 0:
                listbox.delete(0, listbox.size())

            print(listbox.size())
            a = []
            singly = []  # b는 a에 저장된 텍스틀 나눠서 순서대로 저장하기위함
            https_pos = []  # 각 singly 인덱스에서 https가 시작하는 위치를 알기 위한 배열
            address = []  # 각 주소(하이퍼링크)들을 저장
            Gposts.Get_Department(a)

            # Stashed changes

            txt = ""
            url_list = []
            j = 0
            matching = []
            print("-----------")
            print(a)
            print(type_list)
            print("-----------")
            for i in range(0, len(a), 5):
                # Updated upstream
                if a[i + 4] in type_list:
                    for k in range(i, i + 4):
                        if k % 5 == 3:
                            url_list.append(a[k])
                        elif k % 5 == 0:
                            if j < 9:
                                txt += " " + "0"
                            else:
                                txt += " "
                            txt += str(j + 1) + " | "
                        elif k % 5 != 2:
                            txt += " " + str(a[k]) + " | "
                        else:
                            txt += " " + str(a[k][0:10])
                    # Stashed changes
                    listbox.insert(j, txt)
                    j += 1
                    matching = []
                    txt = ""

            listbox.pack()
            listbox2.pack()
            print(url_list)

            listbox.bind("<Double-Button>", lambda event: openweb(listbox.curselection()))  # 더블클릭 감지하는 코드

            scrollbar["command"] = listbox.yview

        # url_list에 DB에서 가져온 순서대로 append후, listbox.curselection()이 클릭한 위치의 정보를 튜플로 반환하므로, 그에 첫번째 인덱스인 0,1,2,와 같은 값만 받아 그에 해당하는 URL을 리스트에서 찾아 여는 방식

        def openweb(Data):
            global url_list
            url = Data[0]
            webbrowser.open(url_list[url])

        def Delet_data():
            listbox.pack()
            Show_data()

        # Stashed changes
        # DB에서 가져온 data를 학교 공지사항, sw 공지사항 별로 저장할 함수

        button = tk.Button(self, borderwidth=3, relief="flat", text="  Enter  ", fg="white",
                           background="#00b0f0", font=font_Cheack_B, command=Delet_data)
        button.place(x=230, y=560)

    # cheack box 버튼을 통해 버튼이 선택되면 해당값 -1 의 인덱스 값에 해당하는 문자열 저장
    def convert(self):
        global type_list
        title = ["scholarship", "contest", "exchange", "vacation", "tuition", "freshman",
                 "foreign", "job", "lecture", "capstone", "other"]

        type_list = []
        if self.var0.get() == 1:
            type_list.append(title[self.var0.get() - 1])
        if self.var1.get() == 2:
            type_list.append(title[self.var1.get() - 1])
        if self.var2.get() == 3:
            type_list.append(title[self.var2.get() - 1])
        if self.var3.get() == 4:
            type_list.append(title[self.var3.get() - 1])
        if self.var4.get() == 5:
            type_list.append(title[self.var4.get() - 1])
        if self.var5.get() == 6:
            type_list.append(title[self.var5.get() - 1])
        if self.var6.get() == 7:
            type_list.append(title[self.var6.get() - 1])
        if self.var7.get() == 8:
            type_list.append(title[self.var7.get() - 1])
        if self.var8.get() == 9:
            type_list.append(title[self.var8.get() - 1])
        if self.var9.get() == 10:
            type_list.append(title[self.var9.get() - 1])
        if self.var10.get() == 11:
            type_list.append(title[self.var10.get() - 1])
        if self.var11.get() == 12:
            for i in range(0, 11):
                type_list.append(title[i])

        print(type_list)


class Make_User_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')

        def clickMe():
            string = []
            user_ID = str1.get()
            user_Email = str2.get()
            user_PW = str3.get()
            Mk = Create_User.Make_user(user_ID, user_Email, user_PW)
            Mk.make(string)
            print(string)
            if string[0] == 201:
                controller.show_frame("Mk_U_Suss")
            else:
                txt = ""
                for i in range(1, len(string)):
                    txt += string[i] + '\n'
                messagebox.showwarning(
                    "Error", txt)

        # 회원가입 뒤 배경 추가
        image_user = PhotoImage(file="imagefile/OP_make_user.png")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=120)

        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        # label2 = tk.Label(self, text="Sing Up", background='white', font=font_startpageinfo)
        label2 = tk.Label(self, text="회원가입", background='white', font=font_startpageinfo)
        label2.place(x=375, y=230)

        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="ID(user name)", background='white', font=FB)
        LabelWidget1.place(x=375, y=290)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        display1.place(x=475, y=290)

        str2 = StringVar()
        LabelWidget2 = tk.Label(self, text="E-mail", background='white', font=FB)
        LabelWidget2.place(x=375, y=360)
        display2 = tk.Entry(self, width=20, textvariable=str2)
        display2.place(x=475, y=360)

        str3 = StringVar()
        LabelWidget3 = tk.Label(self, text="Password", background='white', font=FB)
        Label_PW_Rool = tk.Label(self,
                                 text="Make sure it's at least 15 characters OR \nat lest 8 characters including a number",
                                 background="white")
        LabelWidget3.place(x=375, y=430)
        Label_PW_Rool.place(x=475, y=450)
        display3 = tk.Entry(self, width=20, textvariable=str3)
        display3.place(x=475, y=430)

        button = tk.Button(self, borderwidth=3, relief="flat", text="Sing up for Sea Your Info", command=clickMe,
                           fg="white", background="#00b0f0", font=font_Cheack_B)
        button.place(x=475, y=560)

        image_back = PhotoImage(file='imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=lambda: controller.show_frame("StartPage"), padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=235, y=550)


class Change_User_Info(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        def clickMe():
            messagebox.showinfo("Button CLicked", str1.get())
            messagebox.showinfo("Button CLicked", str2.get())
            messagebox.showinfo("Button CLicked", str3.get())
            controller.show_frame("ch_U_Suss")

        image_user = PhotoImage(file="imagefile/OP_make_user.png")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=120)

        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        label2 = tk.Label(self, text="Change User Info", background='white', font=font_startpageinfo)
        label2.place(x=375, y=230)

        str1 = StringVar()
        LabelWidget1 = tk.Label(self, text="E-mail", background='white', font=FB)
        LabelWidget1.place(x=375, y=290)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        display1.place(x=475, y=290)

        str2 = StringVar()
        LabelWidget2 = tk.Label(self, text="Name", background='white', font=FB)
        LabelWidget2.place(x=375, y=360)
        display2 = tk.Entry(self, width=20, textvariable=str2)
        display2.place(x=475, y=360)

        str3 = StringVar()
        LabelWidget3 = tk.Label(self, text="Password", background='white', font=FB)
        Label_PW_Rool = tk.Label(self,
                                 text="Make sure it's at least 15 characters OR \nat lest 8 characters including a number",
                                 background="white")
        LabelWidget3.place(x=375, y=430)
        Label_PW_Rool.place(x=475, y=450)
        display3 = tk.Entry(self, width=20, textvariable=str3)
        display3.place(x=475, y=430)

        button = tk.Button(self, borderwidth=3, relief="flat", text="\tComplete\t", command=clickMe, fg="white",
                           background="#00b0f0", font=font_Cheack_B)
        button.place(x=475, y=560)

        image_back = PhotoImage(file='imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=lambda: controller.show_frame("main"), padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=235, y=550)


class Find_User_Info(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        image_user = PhotoImage(file="imagefile/KakaoTalk_20200510_195325903.png")
        user_image = Label(self, image=image_user, background="white", borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=120)

        # 아이디 찾기
        display1 = tk.Entry(self, width=20)
        display1.place(x=470, y=232)
        display2 = tk.Entry(self, width=20)
        display2.place(x=470, y=291)

        display3 = tk.Entry(self, width=20)
        display3.place(x=470, y=522)

        button1 = tk.Button(self, text="   Enter   ", command=lambda: controller.show_frame("Find_ID"))
        button1.place(x=720, y=330)
        button2 = tk.Button(self, text="   Enter   ", command=lambda: controller.show_frame("Find_PW"))
        button2.place(x=720, y=567)

        image_back = PhotoImage(file='imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=lambda: controller.show_frame("StartPage"), padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=185, y=570)


class Find_ID(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력
        label2 = tk.Label(self, text="등록하신 아이디는... 입니다.", font=controller.title_font, background='white')
        label2.place(x=250, y=300)

        button1 = tk.Button(self, text="    확인    ", command=lambda: controller.show_frame("StartPage"))
        button1.place(x=800, y=500)


class Find_PW(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력
        label2 = tk.Label(self, text="임시 비밀번호 ... 이 되었습니다.\n 접속후 PW를 변경해 주세요", font=controller.title_font,
                          background='white')
        label2.place(x=250, y=300)

        button1 = tk.Button(self, text="확인", command=lambda: controller.show_frame("StartPage"))
        button1.place(x=800, y=500)


class Mk_U_Suss(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        # 로그인 성공시 페이지
        image_user = PhotoImage(file="imagefile/Make_User_Successful.png")
        user_image = Label(self, image=image_user, background="white", borderwidth=0)
        user_image.image = image_user
        user_image.place(x=270, y=130)

        button1 = tk.Button(self, borderwidth=3, relief="flat", text="Move Back",
                            command=lambda: controller.show_frame("StartPage"), fg="white", background="#00b0f0",
                            font=font_Cheack_B)
        button1.place(x=700, y=500)


class ch_U_Suss(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        label2 = tk.Label(self, text="회원정보 변경에 성공했습니다.", font=controller.title_font, background='white')
        label2.place(x=250, y=300)

        button1 = tk.Button(self, text="돌아가기", command=lambda: controller.show_frame("main"))
        button1.place(x=700, y=500)


if __name__ == "__main__":
    app = Apps()
    app.mainloop()
