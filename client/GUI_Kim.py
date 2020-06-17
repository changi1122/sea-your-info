import tkinter as tk
import GUI_get_posts as Gposts
import Create_User
import Login
import Find_User
import Update_User
import Getalluser
import Post_ch
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import *
from tkinter import messagebox
import webbrowser

import os, sys
if getattr(sys, 'frozen', False):
    application_path = sys._MEIPASS
elif __file__:
    application_path = os.path.dirname(__file__)

UserInfo = []
User_token = []
SpUser_sw = []
SpUser_dept = []
user_ID=[]

class Apps(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=30, weight="bold", slant="italic")
        global font_ID
        font_ID = tkfont.Font(family='여기어때 잘난체 OTF', size=50)
        global font_logintext
        font_logintext = tkfont.Font(family='Helvetica', size=15)
        global font_startpageinfo
        font_startpageinfo = tkfont.Font(family='여기어때 잘난체 OTF', size=18)
        global font_SuperButton
        font_SuperButton = tkfont.Font(family='여기어때 잘난체 OTF', size=10)
        global font_superuser_finduser
        font_superuser_finduser = tkfont.Font(family='여기어때 잘난체 OTF', size=14)
        # 여기어때 잘난체 OTF 다른 컴퓨터에서도 잘 작동하는지 확인 필요
        # 없다면 폰트 파일 공유해야할듯
        global FB
        FB = tkfont.Font(family='Helvetica', size=10)
        global font_hypertext
        font_hypertext = tkfont.Font(size=10, underline=True)
        global font_Cheack_B
        font_Cheack_B = tkfont.Font(size=11, weight="bold", family='Helvetica')
        global font_listbox_content
        font_listbox_content = tkfont.Font(size=13, family='휴먼모음T')
        global font_listbox_content2
        font_listbox_content2 = tkfont.Font(size=16, family='휴먼모음T')
        global font_radiobutton
        font_radiobutton = tkfont.Font(size=12, family='바른고딕', weight="bold")

        self.title("Sea Your Info")
        self.geometry('1050x650')
        self.resizable(False, False)
        self.configure(background='white')
        self.iconbitmap(application_path + '\imagefile\sea_your_info.ico')
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (
                StartPage, Make_User_page, Find_User_Info, main, Change_User_Info, Mk_U_Suss, ch_U_Suss, Find_ID,
                Find_PW_S, Find_F, SuperPage, SuperShowUserINFO, SuperChangeListINFO):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


# 시작 페이지
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        # 맨 위의 Sea Your Info 들어가는 부분
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        image_mainlogo = PhotoImage(file=application_path + '/imagefile/logo2_color.gif')
        label_defaultlogo = Label(image=image_mainlogo, borderwidth=0)
        label_defaultlogo.image = image_mainlogo
        label_defaultlogo.place(x=20, y=20)

        # OP_bar 추가
        image_bar = PhotoImage(file=application_path + '/imagefile/OP_bar.png')
        label_defaultlogo = Label(image=image_bar)
        label_defaultlogo.image = image_bar
        label_defaultlogo.place(x=-10, y=100)

        def clickMe():
            global User_token, user_ID
            user_ID.append(str1.get())
            user_PW = str2.get()
            display1.delete(0, tk.END)
            display3.delete(0, tk.END)
            Lg = Login.Login(user_ID[0], user_PW)
            Lg.Check(User_token)
            print(User_token)
            if User_token[0] == 1:
                controller.show_frame("SuperPage")
            elif User_token[1] == 200:
                controller.show_frame("main")
            else:
                txt = ""
                for i in range(2, len(User_token)):
                    if 'password' in User_token[i]:
                        txt += "비밀번호를 확인해 주세요.\n"
                    if 'username' in User_token[i]:
                        txt += "아이디를 확인해 주세요.\n"
                    if 'non_field_errors' in User_token[i]:
                        txt += "아이디 또는 비밀번호가 잘못되었습니다.\n"
                user_ID = []
                User_token = []
                messagebox.showwarning("Error", txt)

        # 비밀번호 별표로 안보이게 가리는 부분
        def toggle_password():
            if checkbutton.var.get():
                display3['show'] = "•"
            else:
                display3['show'] = ""

        # 첫 화면 텍스트 부분
        label4 = tk.Label(self,
                          text="  정보바다에 오신 것을 환영합니다.\n\n정보바다에서는 여러분들의 학업 증진을 위하여\n 학교의 공지사항 정보들을 알려드리고 있습니다.\n\n회원가입과 로그인을 통하여 자세히 알아보세요.\n\n\n\n\nWelcome to Sea-Your-Info!\n\nSea-Your-Info will let you know all of the\nimportant school notice.\nIt will save your precious time.\n\nFor more information, do not hesitate to\njoin our free membership!\n\n",
                          font=font_startpageinfo, background='white')
        label4.place(x=440, y=160)

        # 텍스트 옆에 들어가는 로고 이미지 부분
        image_logo = PhotoImage(file=application_path + '/imagefile/logo2_color.gif')
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
        display3 = tk.Entry(self, width=20, textvariable=str2)
        display3.place(x=115, y=285)

        # 비밀번호 보이게 할 것인지 여부
        display3.default_show_val = display3['show']
        display3['show'] = "•"
        checkbutton = tk.Checkbutton(self, text="Hide password", onvalue=True, offvalue=False, command=toggle_password,
                                     background='white')
        checkbutton.var = tk.BooleanVar(value=True)
        checkbutton['variable'] = checkbutton.var
        checkbutton.place(x=150, y=310)

        log_B = PhotoImage(file=application_path + '/imagefile/OP_button3.png')

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


        quotation_up = PhotoImage(file=application_path + '/imagefile/up.png')
        label_quotation_up = Label(self, image=quotation_up, borderwidth=0)
        label_quotation_up.image = quotation_up
        label_quotation_up.place(x=985, y=270)
        quotation_down = PhotoImage(file=application_path + '/imagefile/down.png')
        label_quotation_down = Label(self, image=quotation_down, borderwidth=0)
        label_quotation_down.image = quotation_down
        label_quotation_down.place(x=380, y=145)
        quotation_middle = PhotoImage(file=application_path + '/imagefile/middle.png')
        label_quotation_middle = Label(self, image=quotation_middle, borderwidth=0)
        label_quotation_middle.image=quotation_middle
        label_quotation_middle.place(x=580, y=340)

        label_quotation_up2 = Label(self, image=quotation_up, borderwidth=0)
        label_quotation_up2.image = quotation_up
        label_quotation_up2.place(x=985, y=565)

        label_quotation_down2 = Label(self, image=quotation_down, borderwidth=0)
        label_quotation_down2.image = quotation_down
        label_quotation_down2.place(x=380, y=390)


# 슈퍼유저 관련 페이지
class SuperPage(tk.Frame):
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
        image_user = PhotoImage(file=application_path + "/imagefile/user_image.gif")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=25, y=120)

        def Logout():  # 로그인 했을때 listbox에 남아있는 ID, PW기록 지우기
            global User_token
            if listbox.size() != 0:
                listbox.delete(0, listbox.size())

            if listbox2.size() != 0:
                listbox2.delete(0, listbox2.size())
            User_token = []  # 유저 정보 저장하는 리스트 초기화
            controller.show_frame("StartPage")

        # 좌측 상단 user_image 바로 오른 쪽에 있는 로그아웃과 회원정보 수정 버튼 부분
        button1 = tk.Button(self, text="로그아웃", command=Logout, borderwidth=0,
                            background='white', font=font_hypertext, fg="#0000FF")
        button1.place(x=145, y=160)
        button2 = tk.Button(self, text="회원정보 관리", command=lambda: controller.show_frame("SuperShowUserINFO"),
                            borderwidth=0, background='white', font=font_hypertext, fg="#0000FF")
        # 유저들이 나오는 페이지로 넘어가는 부분
        button2.place(x=145, y=185)
        button3 = tk.Button(self, text="리스트 정보 수정", command=lambda: controller.show_frame("SuperChangeListINFO"),
                            borderwidth=0, background='white', font=font_hypertext, fg="#0000FF")
        button3.place(x=145, y=210)
        # TODO 통계량 보기 부분 프레임 추가해야함

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
        radio_text9 = Checkbutton(self, text="모두보기", background='white', font=FB, onvalue=12,
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
            global url_list, url_list_sw, SpUser_dept, SpUser_sw
            # 리스트 박스 1,2에 문자열이 있을 경우 이전 data 삭제
            if listbox.size() != 0:
                listbox.delete(0, listbox.size())

            if listbox2.size() != 0:
                listbox2.delete(0, listbox2.size())

            print(listbox.size())
            global a
            a = []
            global b
            b = []
            Gposts.Get_Department(a)
            Gposts.Get_SW(b)

            txt = ""
            txt_sw = ""
            url_list = []
            url_list_sw = []
            if not SpUser_dept :
                SpUser_dept = []
            if not SpUser_sw :
                SpUser_sw = []
            j = 0
            print("-----------")
            print(a)
            print(b)
            print(type_list)
            print("-----------")

            arr1 = []
            arr2 = []
            listbox_order = int(len(a) / 5) + 1

            global cnt
            cnt = 0
            for i in range(0, len(a), 5):
                if a[i + 4] in type_list:
                    SpUser_dept += a[i:i + 5]
                    cnt += 1

            for i in range(0, len(a), 5):
                # Updated upstream
                if a[i + 4] in type_list:
                    for k in range(i, i + 4):
                        if k % 5 == 3:
                            url_list.append(a[k])
                        elif k % 5 == 0:
                            if cnt - j < 10:  # 이 조건문은 숫자 앞에 0을 붙여 주기 위한 조건문이다.
                                txt += " " + "0" + "0"
                            elif cnt - j < 100:
                                txt += " 0"
                            else:
                                txt += " "
                            txt += str(cnt - j) + " | "
                        elif k % 5 != 2:
                            txt += " " + str(a[k]) + " | "
                        else:
                            txt += " " + str(a[k][0:10])
                    arr1.append(txt)  # 이 부분에서 listbox에 바로 넣지 않고
                    # arr1에 넣는다. arr1에 넣어서 아래 for문에서 최신 날짜부터 뒤집어서 출력하기 위해서
                    j += 1
                    txt = ""

            for i in range(len(arr1) - 1, -1, -1):
                listbox.insert(j, arr1[i])
                j += 1

            # 여기서부터 b 배열
            global cnt2
            cnt2 = 0
            for i in range(0, len(b), 5):
                if b[i + 4] in type_list:
                    SpUser_sw += b[i:i + 5]
                    cnt2 += 1

            listbox_order = int(len(b) / 5) + 1
            j = 0
            for i in range(0, len(b), 5):
                # Updated upstream
                if b[i + 4] in type_list:
                    for k in range(i, i + 4):
                        if k % 5 == 3:
                            url_list_sw.append(b[k])
                        elif k % 5 == 0:
                            if cnt2 - j < 10:
                                txt_sw += " " + "0" + "0"
                            elif cnt2 - j < 100:
                                txt_sw += " 0"
                            else:
                                txt_sw += " "
                            txt_sw += str(cnt2 - j) + " | "
                        elif k % 5 != 2:
                            txt_sw += " " + str(b[k]) + " | "

                        else:
                            txt_sw += " " + str(b[k][0:10])
                    arr2.append(txt_sw)
                    j += 1
                    txt_sw = ""

            j = 0
            for i in range(len(arr2) - 1, -1, -1):
                listbox2.insert(j, arr2[i])
                j += 1

            listbox.pack()
            listbox2.pack()
            print(url_list)
            print(url_list_sw)

            listbox.bind("<Double-Button>", lambda event: openweb(listbox.curselection(), 1))  # 더블클릭 감지하는 코드
            listbox2.bind("<Double-Button>", lambda event: openweb(listbox2.curselection(), 2))

            scrollbar["command"] = listbox.yview
            scrollbar["command"] = listbox2.yview

        # url_list에 DB에서 가져온 순서대로 append후, listbox.curselection()이 클릭한 위치의 정보를 튜플로 반환하므로, 그에 첫번째 인덱스인 0,1,2,와 같은 값만 받아 그에 해당하는 URL을 리스트에서 찾아 여는 방식

        def openweb(Data, sep):
            # 이부분에 스토리 보드와 같이 정보수정으로 넘어가는 페이지 구현 필요
            global url_list, url_list_sw, SpUser_ch_L_I
            url = Data[0]
            if sep == 1:
                url = cnt - 1 - url
                webbrowser.open(url_list[url])
            else:
                url = cnt2 - 1 - url
                webbrowser.open(url_list_sw[url])


        def Delet_data():
            listbox.pack()
            listbox2.pack()
            Show_data()

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


# joong
# 슈퍼유저가 회원정보 관리 창을 눌렀을 때 나오는 부분
class SuperShowUserINFO(tk.Frame):  # 스토리 보드상 가입된 유저 목록 출력하는 화면 부분
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        def highlight_searched(*args):
            search = search_var.get()
            for i, item in enumerate(all_listbox_items):
                if search.lower() in item.lower():
                    listbox.selection_set(i)
                else:
                    listbox.selection_clear(i)
            if search == '':
                listbox.selection_clear(0, END)

        image_user = PhotoImage(file=application_path + "/imagefile/user_image.gif")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=25, y=120)

        # 밑에 추가로 구현 필요
        notebook_main = ttk.Notebook(self, width=670, height=470, padding=10)
        notebook_main.place(x=330, y=115)

        userpage = Frame(self)
        notebook_main.add(userpage, text="  유저 정보  ")

        scrollbar = tk.Scrollbar(userpage)
        scrollbar.pack(side="right", fill="y")
        listbox = tk.Listbox(userpage, yscrollcommand=scrollbar.set, width=660, height=460,
                             font=font_listbox_content2)

        image_back = PhotoImage(file=application_path + '/imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=lambda: controller.show_frame("SuperPage"), padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=25, y=550)

        a = []
        userlist = []
        newuserlist = []
        userlist = Getalluser.Getuser.Getuser(a)

        k = 0
        subcnt = 0
        for i in range(0, len(userlist), 5):
            string = " " + str(k + 1) + ""
            for j in range(i, i + 5):
                if userlist[j] == "none" or j % 5 == 0:
                    continue
                else:
                    string += " | " + str(userlist[j])
                if userlist[j] == True:  # 만약 구독을 한 사람이라면 subcnt+=1해준다.
                    subcnt += 1
            newuserlist.append(string)
            listbox.insert(k, newuserlist[k])
            k += 1
        category = "CATEGORY => number | ID | E-Mail | Subscribed or not"
        listbox.insert(0, category)
        listbox.pack()

        registered = tk.Label(self, text="총 가입인원 수 : " + str(k), font=font_startpageinfo, background='white')
        registered.place(x=30, y=400)
        subscribed = tk.Label(self, text="총 구독자 수 : " + str(subcnt), font=font_startpageinfo, background='white')
        subscribed.place(x=30, y=440)


        all_listbox_items = listbox.get(0, END)

        search_label = tk.Label(self, text="사용자 검색", font=font_superuser_finduser, background='white')
        search_label.place(x=30, y=300)

        search_var = StringVar()
        search_var.trace('w', highlight_searched)
        search_entry = Entry(self, textvariable=search_var)
        search_entry.place(x=145, y=303)


class SuperChangeListINFO(tk.Frame):  # 스토리 보드상 리스트의 항복 변경하는 부분
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        # 밑에 추가로 구현 필요

        def Delete():
            global SpUser_dept, SpUser_sw
            display1.delete(0, tk.END)
            display2.delete(0, tk.END)
            display3.delete(0, tk.END)
            display4.delete(0, tk.END)
            display5.delete(0, tk.END)
            self.txt1.set(" ")
            self.txt2.set(" ")
            self.txt3.set(" ")
            self.txt4.set(" ")
            controller.show_frame("SuperPage")

        image_back = PhotoImage(file=application_path + '/imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=Delete, padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=25, y=550)  # 뒤로가기버튼

        image_user = PhotoImage(file=application_path + "/imagefile/ChangListinfo.png")
        user_image = Label(self, image=image_user, background="white", borderwidth=0)
        user_image.image = image_user
        user_image.place(x=120, y=130)

        LIST_INFO = []

        def Cheak():
            global a
            a = RadioVariety_1.get()

        def DeleteData():  # 이거 질문 필요
            global LIST_INFO, a
            num = str1.get()
            print("DDDDDD")
            print(LIST_INFO)
            POST2 = Post_ch.Post_ch(str(LIST_INFO[0]), User_token[2], LIST_INFO[1], LIST_INFO[2], LIST_INFO[3],
                                    LIST_INFO[4])
            string=[]
            if a ==1:
                POST2.delete_list_dept(string)
            else :
                POST2.delete_list_sw(string)

            if string[0] == 'OK':
                self.txt4.set("Data를 성공적으로 삭제했습니다")
            else:
                self.txt4.set("Data 삭제에 실패했습니다")


        def Search():
            global a, SpUser_sw, SpUser_dept, LIST_INFO
            self.txt2.set(" ")
            self.txt3.set(" ")
            self.txt4.set(" ")
            print("SpUser_sw")
            print(SpUser_sw)
            print("SpUser_dept")
            print(SpUser_dept)

            try:
                num = str1.get()
                if num != 0:
                    if a == 1:
                        cnt = len(SpUser_dept) // 5
                        url1 = cnt - num
                        print("cnt :" + str(cnt) + " url1 :" + str(url1))
                        LIST_INFO = SpUser_dept[url1 * 5:url1 * 5 + 5]
                    else:
                        cnt2 = len(SpUser_sw) // 5
                        url2 = cnt2 - num
                        print("cnt2 :" + str(cnt2) + " url2 :" + str(url2))
                        LIST_INFO = SpUser_sw[url2 * 5:url2 * 5 + 5]
            except:
                pass

            try:
                if LIST_INFO:
                    text1 = "제목 : " + LIST_INFO[1]
                    text2 = "날짜 : " + LIST_INFO[2]+" 타입 : " + LIST_INFO[4]
                else:
                    text1 = "Data가 없습니다"
                    text2 = " "
            except:
                text1 = "Data가 없습니다"
                text2 = " "

            self.txt1.set(text1)
            self.txt2.set(text2)

        def openweb():
            global LIST_INFO

            try:
                if LIST_INFO:
                    print(LIST_INFO)
                    webbrowser.open(LIST_INFO[3])
                else:
                    txt = "[ Error : No Data ]"
                    messagebox.showwarning("Error", txt)
            except:
                txt = "[ Error : No Data ]"
                messagebox.showwarning("Error", txt)

        def UpData_LIST():
            global LIST_INFO,a
            if str2.get():
                title = str2.get()
            else:
                title = LIST_INFO[1]

            if str3.get():
                date = str3.get()
            else:
                date = LIST_INFO[2]

            if str4.get():
                type = str4.get()
            else:
                type = LIST_INFO[4]

            if str5.get():
                URL = str5.get()
            else:
                URL = LIST_INFO[3]
            # ID, Token, title, date, URL, tpye
            string = []
            print(str(LIST_INFO[0]) + str(User_token[2]) + str(title) + str(date) + str(URL) + str(type))
            POST = Post_ch.Post_ch(str(LIST_INFO[0]), User_token[2], title, date, URL, type)

            if a==1:
                POST.update_list_dept(string)
            else :
                POST.update_list_sw(string)

            print("string :" + str(string[0]))
            if string[0] == 200:
                display2.delete(0, tk.END)
                display3.delete(0, tk.END)
                display4.delete(0, tk.END)
                display5.delete(0, tk.END)
                self.txt4.set("Data를 성공적으로 변경했습니다")
                self.txt3.set(" ")
                # 성공
            elif string[0] == 404:
                self.txt4.set("수정하고자 하는 List의 ID값이 다릅니다. 다시 확인해 주세요")
                # 아이디 잘못 됬을떄
            elif string[0] == 401:
                self.txt4.set("권한이 없습니다. 관리자에 문의해 토큰을 확인해 주세요.")
                # 리스트의 토큰이 잘못 됬을때
            elif string[0] == 400:
                self.txt3.set("날짜 형식을 확인해 주세요")
                # 날짜 형식이 잘못됬을때

        self.txt1 = StringVar()
        self.txt2 = StringVar()
        self.txt3 = StringVar()
        self.txt4 = StringVar()
        self.txt1.set(" ")
        self.txt2.set(" ")
        self.txt3.set(" ")
        self.txt4.set(" ")
        GetText1 = tk.Label(self, textvariable=self.txt1, background='white', font=font_SuperButton)
        GetText1.place(x=200, y=280)
        GetText2 = tk.Label(self, textvariable=self.txt2, background='white', font=font_SuperButton)
        GetText2.place(x=200, y=300)
        GetText3 = tk.Label(self, textvariable=self.txt3, background='white', font=font_SuperButton)
        GetText3.place(x=360, y=370)
        GetText4 = tk.Label(self, textvariable=self.txt4, background='white', font=font_SuperButton)
        GetText4.place(x=200, y=425)

        RadioVariety_1 = IntVar()

        radio_scholar = tk.Radiobutton(self, text="학교", background='white', font=font_SuperButton, value=1,
                                       variable=RadioVariety_1, command=Cheak)
        # font_radiobutton == FB로, Make_List==M_L로 변경
        radio_scholar.place(x=230, y=250)

        radio_job = tk.Radiobutton(self, text="학과", background='white', font=font_SuperButton, value=2,
                                   variable=RadioVariety_1, command=Cheak)
        radio_job.place(x=300, y=250)

        str1 = IntVar()
        LabelWidget1 = tk.Label(self, text="리스트 번호", background='white', font=font_SuperButton)
        LabelWidget1.place(x=370, y=251)
        display1 = tk.Entry(self, width=20, textvariable=str1)
        display1.place(x=450, y=251)

        button = tk.Button(self, borderwidth=3, relief="flat", text="Search",
                           fg="white", background="#00b0f0", font=font_SuperButton, command=Search)
        button.place(x=600, y=250)

        LabelWidget2 = tk.Label(self, text="제목", background='white', font=font_SuperButton)
        LabelWidget2.place(x=200, y=330)

        LabelWidget3 = tk.Label(self, text="날짜", background='white', font=font_SuperButton)
        LabelWidget3.place(x=355, y=330)

        LabelWidget4 = tk.Label(self, text="타입", background='white', font=font_SuperButton)
        LabelWidget4.place(x=510, y=330)

        LabelWidget5 = tk.Label(self, text="URL", background='white', font=font_SuperButton)
        LabelWidget5.place(x=665, y=330)

        str2 = StringVar()
        display2 = tk.Entry(self, width=20, textvariable=str2)
        display2.place(x=205, y=350)

        str3 = StringVar()
        display3 = tk.Entry(self, width=20, textvariable=str3)
        display3.place(x=360, y=350)

        str4 = StringVar()
        display4 = tk.Entry(self, width=20, textvariable=str4)
        display4.place(x=515, y=350)

        str5 = StringVar()
        display5 = tk.Entry(self, width=20, textvariable=str5)
        display5.place(x=670, y=350)

        button = tk.Button(self, borderwidth=3, relief="flat", text="   Open Web   ",
                           fg="white", background="#00b0f0", font=font_SuperButton, command=openweb)
        button.place(x=205, y=500)

        button = tk.Button(self, borderwidth=3, relief="flat", text="   UploadData   ",
                           fg="white", background="#00b0f0", font=font_SuperButton, command=UpData_LIST)
        button.place(x=355, y=500)

        button = tk.Button(self, borderwidth=3, relief="flat", text="   DeleteData   ",
                           fg="white", background="#00b0f0", font=font_SuperButton, command=DeleteData)
        button.place(x=505, y=500)


# DB쪽 put-post사용해야함, 이거는 제가 구현 할께요 - 김성욱 ( ㅇ우창ㅇ이랑 얘기가 필요해요 )

# 일반 유져 관련 페이지
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
        image_user = PhotoImage(file=application_path + "/imagefile/user_image.gif")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=25, y=120)

        def Logout():  # 로그인 했을때 listbox에 남아있는 ID, PW기록 지우기
            global User_token, user_ID
            if listbox.size() != 0:
                listbox.delete(0, listbox.size())

            if listbox2.size() != 0:
                listbox2.delete(0, listbox2.size())
            User_token = []  # 유저 정보 저장하는 리스트 초기화
            user_ID=[]
            controller.show_frame("StartPage")

        # 좌측 상단 user_image 바로 오른 쪽에 있는 로그아웃과 회원정보 수정 버튼 부분
        button1 = tk.Button(self, text="로그아웃", command=Logout, borderwidth=0,
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
        radio_text9 = Checkbutton(self, text="모두보기", background='white', font=FB, onvalue=12,
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
            global url_list, url_list_sw
            # 리스트 박스 1,2에 문자열이 있을 경우 이전 data 삭제
            if listbox.size() != 0:
                listbox.delete(0, listbox.size())

            if listbox2.size() != 0:
                listbox2.delete(0, listbox2.size())

            print(listbox.size())
            global a
            a = []
            global b
            b = []
            Gposts.Get_Department(a)
            Gposts.Get_SW(b)

            txt = ""
            txt_sw = ""
            url_list = []
            url_list_sw = []
            j = 0
            print("-----------")
            print(a)
            print(b)
            print(type_list)
            print("-----------")

            arr1 = []
            arr2 = []

            global cnt
            cnt = 0
            for i in range(0, len(a), 5):
                if a[i + 4] in type_list:
                    cnt += 1

            for i in range(0, len(a), 5):
                if a[i + 4] in type_list:
                    for k in range(i, i + 4):
                        if k % 5 == 3:
                            url_list.append(a[k])
                        elif k % 5 == 0:
                            if cnt - j < 10:  # 이 조건문은 숫자 앞에 0을 붙여 주기 위한 조건문이다.
                                txt += " " + "0" + "0"
                            elif cnt - j < 100:
                                txt += " 0"
                            else:
                                txt += " "
                            txt += str(cnt - j) + " | "
                        elif k % 5 != 2:
                            txt += " " + str(a[k]) + " | "
                        else:
                            txt += " " + str(a[k][0:10])
                    arr1.append(txt)  # 이 부분에서 listbox에 바로 넣지 않고
                    # arr1에 넣는다. arr1에 넣어서 아래 for문에서 최신 날짜부터 뒤집어서 출력하기 위해서
                    j += 1
                    txt = ""

            for i in range(len(arr1) - 1, -1, -1):
                listbox.insert(j, arr1[i])
                j += 1

            # 여기서부터 b 배열
            global cnt2
            cnt2 = 0
            for i in range(0, len(b), 5):
                if b[i + 4] in type_list:
                    cnt2 += 1

            listbox_order = int(len(b) / 5) + 1
            j = 0
            for i in range(0, len(b), 5):
                if b[i + 4] in type_list:
                    for k in range(i, i + 4):
                        if k % 5 == 3:
                            url_list_sw.append(b[k])
                        elif k % 5 == 0:
                            if cnt2 - j < 10:
                                txt_sw += " " + "0" + "0"
                            elif cnt2 - j < 100:
                                txt_sw += " 0"
                            else:
                                txt_sw += " "
                            txt_sw += str(cnt2 - j) + " | "
                        elif k % 5 != 2:
                            txt_sw += " " + str(b[k]) + " | "

                        else:
                            txt_sw += " " + str(b[k][0:10])
                    arr2.append(txt_sw)
                    j += 1
                    txt_sw = ""

            j = 0
            for i in range(len(arr2) - 1, -1, -1):
                listbox2.insert(j, arr2[i])
                j += 1

            listbox.pack()
            listbox2.pack()
            print(url_list)
            print(url_list_sw)

            listbox.bind("<Double-Button>", lambda event: openweb(listbox.curselection(), 1))  # 더블클릭 감지하는 코드
            listbox2.bind("<Double-Button>", lambda event: openweb(listbox2.curselection(), 2))

            scrollbar["command"] = listbox.yview
            scrollbar["command"] = listbox2.yview

        # url_list에 DB에서 가져온 순서대로 append후, listbox.curselection()이 클릭한 위치의 정보를 튜플로 반환하므로, 그에 첫번째 인덱스인 0,1,2,와 같은 값만 받아 그에 해당하는 URL을 리스트에서 찾아 여는 방식

        def openweb(Data, sep):
            global url_list, url_list_sw
            url = Data[0]
            if sep == 1:
                # url = int(len(a) / 5) - 1 - url
                url = cnt - 1 - url
                webbrowser.open(url_list[url])
            else:
                # url = int(len(b) / 5) - 1 - url
                url = cnt2 - 1 - url
                webbrowser.open(url_list_sw[url])

        def Delet_data():
            listbox.pack()
            listbox2.pack()
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

        global display3, checkbutton
        subVar = IntVar(value=1)

        def clickMe():
            string = []
            user_ID = str1.get()
            user_Email = str2.get()
            user_PW = str3.get()
            if not user_Email :
                txt = ""
                txt += "이메일을 적어주세요\n"
                messagebox.showwarning(
                    "Error", txt)
            if subVar.get() == 1:
                print("hi")
                user_Subscribe = "true"
            else:
                print("bye")
                user_Subscribe = "false"
            Mk = Create_User.Make_user(user_ID, user_Email, user_PW, user_Subscribe)
            Mk.make(string)
            print(string)
            if string[0] == 201:
                display1.delete(0, tk.END)  # 엔트리에 있는 정보 삭제
                display2.delete(0, tk.END)
                display3.delete(0, tk.END)
                controller.show_frame("Mk_U_Suss")
            else:
                txt = ""
                for i in range(1, len(string)):
                    if 'email' in string[i]:
                        txt += "이메일 형식을 확인해주세요\n"
                    if 'username' in string[i]:
                        txt += "이미 존재하는 ID입니다\n"
                messagebox.showwarning(
                    "Error", txt)

        def Error_Messagebox():  # 비밀번호가 조건에 맞지 않을 때 띄우는 에러
            messagebox.showinfo("에러", "ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n| 비밀번호 조건을 다시 확인해 주세요.  |\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")

        def Error_Fill():  # 창에 값이 모두 입력되지 않았을 때 띄우는 에러
            messagebox.showinfo("Error", "Please fill out all of the spaces.")

        def button_hit():  # Sign up for SYI 눌렸을 때 반응하는 함수
            # 암호가 조건에 맞는지 확인하는 것
            chk_pw = str3.get()
            chk = True
            sum = 0
            for i in range(len(chk_pw)):
                if 'a' <= chk_pw[i] <= 'z' or 'A' <= chk_pw[i] <= 'Z':  # 암호가 모두 알파벳으로 돼 있다면
                    sum += 1
            if sum is len(chk_pw):
                chk = False  # False로 바꿈
            if len(chk_pw) < 8 or len(chk_pw) >= 15:  # 비밀번호의 길이가 8자 미만이거나 15자 이상이면 안된다.
                chk = False
            if chk is False:
                display3.delete(0, tk.END)
                Error_Messagebox()
            elif chk is True:
                clickMe()

        def on_enter(event):
            label2.configure(text="Make it at least 8 characters.\nMake it at most 15 characters.\nAdd punctuation.")

        def on_leave(event):
            label2.configure(text="")

        # 비밀번호 별표로 안보이게 가리는 부분
        def toggle_password():
            if checkbutton.var.get():
                display3['show'] = "•"
            else:
                display3['show'] = ""

        # 회원가입 뒤 배경 추가
        image_user = PhotoImage(file=application_path + "/imagefile/OP_make_user.png")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=120)

        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

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
        LabelWidget3.place(x=375, y=430)
        # Label_PW_Rool.place(x=475, y=450)
        display3 = tk.Entry(self, width=20, textvariable=str3)
        display3.place(x=475, y=430)

        # 물음표 이미지 띄우는 부분
        que_image = PhotoImage(file=application_path + '/imagefile/questionmarkimage.gif')
        label_Queimage = tk.Label(self, image=que_image, borderwidth=0)
        label_Queimage.image = que_image
        label_Queimage.place(x=595, y=450)

        label2 = tk.Label(self, text="", width=0, background='white')
        label2.place(x=620, y=450)

        label_Queimage.bind("<Enter>", on_enter)
        label_Queimage.bind("<Leave>", on_leave)

        display3.default_show_val = display3['show']
        display3['show'] = "•"
        checkbutton = tk.Checkbutton(self, text="Hide password", onvalue=True, offvalue=False, command=toggle_password,
                                     background='white')
        checkbutton.var = tk.BooleanVar(value=True)
        checkbutton['variable'] = checkbutton.var
        checkbutton.place(x=620, y=428)

        button = tk.Button(self, borderwidth=3, relief="flat", text="Sign up for Sea Your Info",
                           command=button_hit,
                           fg="white", background="#00b0f0", font=font_Cheack_B)
        button.place(x=475, y=560)

        image_back = PhotoImage(file=application_path + '/imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=lambda: controller.show_frame("StartPage"), padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=235, y=550)

        LabelWidget4 = tk.Label(self, text="Subscribe", background='white', font=FB)
        LabelWidget4.place(x=375, y=500)
        # subVar = IntVar(value=1)
        subscribe_checkbutton = tk.Checkbutton(self, background='white', variable=subVar)
        # subscribe_checkbutton.var = tk.BooleanVar(value=True)
        subscribe_checkbutton.place(x=475, y=500)


class Change_User_Info(tk.Frame):

    def __init__(self, parent, controller):
        global User_token
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        subVar2 = IntVar(value=1)

        def clickMe():
            if subVar2.get() == 1:
                user_Subscribe = "true"
                print("got true")
            else:
                user_Subscribe = "false"
                print("got false")
            message = []
            print(User_token[2])
            CH = Update_User.Update_User(user_ID[0], str2.get(), str3.get(), str4.get(), User_token[2], user_Subscribe)
            CH.UUD_INFO(message)
            print(message)
            self.str1.set(" ")
            display2.delete(0, tk.END)
            display3.delete(0, tk.END)
            display4.delete(0, tk.END)
            subVar = IntVar(value=1)
            controller.show_frame("ch_U_Suss")

        image_user = PhotoImage(file=application_path + "/imagefile/OP_make_user.png")
        user_image = Label(self, image=image_user, borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=120)

        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        label2 = tk.Label(self, text="Change User Info", background='white', font=font_startpageinfo)
        label2.place(x=375, y=230)

        def Show(event):
            print(1122)
            self.str1.set(user_ID[0])

        self.bind("<Enter>", Show)

        self.str1 = StringVar()
        self.str1.set(" ")
        LabelWidget1 = tk.Label(self, text="ID", background='white', font=FB)
        LabelWidget1.place(x=375, y=290)
        show_ID = tk.Label(self, textvariable=self.str1, background='white', font=FB)
        show_ID.place(x=475, y=290)


        str2 = StringVar()
        LabelWidget2 = tk.Label(self, text="Email", background='white', font=FB)
        LabelWidget2.place(x=375, y=340)
        display2 = tk.Entry(self, width=20, textvariable=str2)
        display2.place(x=475, y=340)

        # 비밀번호 별표로 안보이게 가리는 부분
        def toggle_password():
            if checkbutton1.var.get():
                display3['show'] = "•"
            else:
                display3['show'] = ""

            if checkbutton2.var.get():
                display4['show'] = "•"
            else:
                display4['show'] = ""

        str3 = StringVar()
        LabelWidget3 = tk.Label(self, text="Password", background='white', font=FB)
        LabelWidget3.place(x=375, y=390)
        display3 = tk.Entry(self, width=20, textvariable=str3)
        display3.place(x=475, y=390)
        # 비번 안보이게 하는 부분
        display3.default_show_val = display3['show']
        display3['show'] = "•"
        checkbutton1 = tk.Checkbutton(self, text="Hide password", onvalue=True, offvalue=False, command=toggle_password,
                                      background='white')
        checkbutton1.var = tk.BooleanVar(value=True)
        checkbutton1['variable'] = checkbutton1.var
        checkbutton1.place(x=620, y=385)

        str4 = StringVar()
        LabelWidget4 = tk.Label(self, text="New_Password", background='white', font=FB)
        LabelWidget4.place(x=375, y=440)
        display4 = tk.Entry(self, width=20, textvariable=str4)
        display4.place(x=475, y=440)

        # 비번 안보이게 하는 부분
        display4.default_show_val = display4['show']
        display4['show'] = "•"
        checkbutton2 = tk.Checkbutton(self, text="Hide password", onvalue=True, offvalue=False, command=toggle_password,
                                      background='white')
        checkbutton2.var = tk.BooleanVar(value=True)
        checkbutton2['variable'] = checkbutton2.var
        checkbutton2.place(x=620, y=435)

        def Error_Messagebox():  # 비밀번호가 조건에 맞지 않을 때 띄우는 에러
            messagebox.showinfo("에러", "ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ\n| 다시 확인해 주세요. |\nㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")  # 메시지 다시 만들기

        # 비번 조건 확인
        def button_hit():  # Sign up for SYI 눌렸을 때 반응하는 함수
            # 암호가 조건에 맞는지 확인하는 것
            chk_pw = str4.get()
            chk = True
            sum = 0
            for i in range(len(chk_pw)):
                if 'a' <= chk_pw[i] <= 'z' or 'A' <= chk_pw[i] <= 'Z':  # 암호가 모두 알파벳으로 돼 있다면
                    sum += 1
            if sum is len(chk_pw):
                chk = False  # False로 바꿈
            if len(chk_pw) < 8 or len(chk_pw) >= 15:  # 비밀번호의 길이가 8자 미만이거나 15자 이상이면 안된다.
                chk = False
            if chk is False:
                display4.delete(0, tk.END)
                Error_Messagebox()
            elif chk is True:
                clickMe()

        # 물음표 이미지 띄우는 부분
        def on_enter(event):
            label5.configure(text="Make it at least 8 characters.\nMake it at most 15 characters.\nAdd punctuation.")

        def on_leave(event):
            label5.configure(text="")

        que_image = PhotoImage(file=application_path + '/imagefile/questionmarkimage.gif')
        label_Queimage = tk.Label(self, image=que_image, borderwidth=0)
        label_Queimage.image = que_image
        label_Queimage.place(x=600, y=460)

        label5 = tk.Label(self, text="", width=0, background='white')
        label5.place(x=625, y=460)

        label_Queimage.bind("<Enter>", on_enter)
        label_Queimage.bind("<Leave>", on_leave)

        LabelWidget4 = tk.Label(self, text="Subscribe", background='white', font=FB)
        LabelWidget4.place(x=375, y=490)

        # subVar = IntVar(value=1)
        subscribe_checkbutton = tk.Checkbutton(self, onvalue=True, offvalue=False, background='white', variable=subVar2)
        # subscribe_checkbutton.var = tk.BooleanVar(value=True)
        subscribe_checkbutton.place(x=470, y=490)

        button = tk.Button(self, borderwidth=3, relief="flat", text="\tComplete\t", command=button_hit, fg="white",
                           background="#00b0f0", font=font_Cheack_B)
        button.place(x=475, y=540)

        def Empty():
            controller.show_frame("main")

        image_back = PhotoImage(file=application_path + '/imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=Empty, padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=235, y=540)


class Find_User_Info(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        image_user = PhotoImage(file=application_path + "/imagefile/OP_FIND_PWID2.png")
        user_image = Label(self, image=image_user, background="white", borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=115)

        # 아이디 찾기
        FU_ID_Email = StringVar()
        display1 = tk.Entry(self, width=20, textvariable=FU_ID_Email)
        display1.place(x=470, y=227)
        # 비번 찾기
        FU_PW_ID = StringVar()
        display2 = tk.Entry(self, width=20, textvariable=FU_PW_ID)
        display2.place(x=470, y=457)
        FU_PW_Email = StringVar()
        display3 = tk.Entry(self, width=20, textvariable=FU_PW_Email)
        display3.place(x=470, y=517)

        def Call_OR1():
            Email = FU_ID_Email.get()
            Delet()
            self.onReturn1(Email)

        def Call_OR2():
            ID = FU_PW_ID.get()
            Email = FU_PW_Email.get()
            Delet()
            self.onReturn23(ID, Email)

        button1 = tk.Button(self, text="   Enter   ", command=lambda: Call_OR1())
        button1.place(x=720, y=270)
        button2 = tk.Button(self, text="   Enter   ", command=lambda: Call_OR2())
        button2.place(x=720, y=557)

        def Delet():
            display1.delete(0, tk.END)
            display2.delete(0, tk.END)
            display3.delete(0, tk.END)

        def Empty():
            global UserInfo
            UserInfo = []
            Delet()
            controller.show_frame("StartPage")

        image_back = PhotoImage(file=application_path + '/imagefile/OP_button3_back.png')
        button_back = tk.Button(self, borderwidth=3, relief="flat", background='white',
                                command=Empty, padx=10, pady=10, image=image_back)
        button_back.image = image_back
        button_back.place(x=170, y=570)

        # 아이디찾기 부분에서 enter눌렀을 때 작동해야 하는 함수

        # PW찾기 부분에서 etner눌렀을때 작동해야 하는 함수

    def onReturn23(self, PW_id, PW_Email):
        global UserInfo
        FU_PW = Find_User.Find_User(PW_id, PW_Email)
        FU_PW.find_PW(UserInfo)

        if UserInfo:
            print(11111111111)
            print(UserInfo)
            if UserInfo[0] != 'None':
                print(200)
                self.controller.show_frame("Find_PW_S")
            else:
                print(404)
                self.controller.show_frame("Find_F")
        # clickMe() clickme처럼 이곳에 작동해야 하는 함수 추가하면 됨

    def onReturn1(self, ID_Email):
        global UserInfo
        FU_ID = Find_User.Find_User(None, ID_Email)
        FU_ID.find_ID(UserInfo)
        print(1111111111)
        if UserInfo:
            print(11111111111)
            print(UserInfo)
            if UserInfo[0] != 'None':
                print(200)
                self.controller.show_frame("Find_ID")
            else:
                print(404)
                self.controller.show_frame("Find_F")
        # clickMe() clickme처럼 이곳에 작동해야 하는 함수 추가하면 됨


class Find_ID(tk.Frame):
    def __init__(self, parent, controller):
        global UserInfo
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')


        def Show(event):
            print(1122)
            self.str1.set(UserInfo[0])

        """
        _widget = tk.LabelFrame(self, bd=0,background='white')  # 화면에 user의 아이디 혹은 존제하지 않음을 출력하기 위해 사용하는 Event를 사용하기 위해 추가
        _widget.pack(fill=BOTH, expand=1)
        _widget.bind("<Enter>", Show)
        """
        self.bind("<Enter>", Show)

        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)


        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력
        image_user = PhotoImage(file=application_path + "/imagefile/ID_S.png")
        user_image = Label(self, image=image_user, background="white", borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=150)

        self.str1 = StringVar()
        self.str1.set(" ")
        GetText1 = tk.Label(self, textvariable=self.str1, background='white', font=font_ID)
        GetText1.place(x=455, y=213)

        def Empty():
            global UserInfo
            UserInfo = []
            self.str1.set(" ")
            controller.show_frame("StartPage")

        button1 = tk.Button(self, borderwidth=3, relief="flat", text="  Check  ",
                            command=Empty,
                            fg="white", background="#00b0f0", font=font_Cheack_B)
        button1.place(x=500, y=520)


class Find_PW_S(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        image_user = PhotoImage(file=application_path + "/imagefile/PW_OK.png")
        user_image = Label(self, image=image_user, background="white", borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=150)

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력

        def Empty():
            global UserInfo
            UserInfo = []
            controller.show_frame("StartPage")

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력
        button1 = tk.Button(self, borderwidth=3, relief="flat", text="  Check  ",
                            command=Empty,
                            fg="white", background="#00b0f0", font=font_Cheack_B)
        button1.place(x=500, y=520)


class Find_F(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        image_user = PhotoImage(file=application_path + "/imagefile/PW_F.png")
        user_image = Label(self, image=image_user, background="white", borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=180)

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력

        def Empty():
            global UserInfo
            UserInfo = []
            controller.show_frame("StartPage")

        # DB에서 E-Mail 반환후 있으면 이거 없으면 오류 출력
        button1 = tk.Button(self, borderwidth=3, relief="flat", text="  Cheak  ",
                            command=Empty,
                            fg="white", background="#00b0f0", font=font_Cheack_B)
        button1.place(x=500, y=550)


class Mk_U_Suss(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(background='white')
        label = tk.Label(self, text="Sea your Info", font=controller.title_font, background='white')
        label.place(x=100, y=35)

        # 로그인 성공시 페이지
        image_user = PhotoImage(file=application_path + "/imagefile/Make_User_Successful.png")
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

        image_user = PhotoImage(file=application_path + "/imagefile/CH_USER_S.png")
        user_image = Label(self, image=image_user, background="white", borderwidth=0)
        user_image.image = image_user
        user_image.place(x=230, y=150)

        def Empty():
            controller.show_frame("main")

        button1 = tk.Button(self, borderwidth=3, relief="flat", text="  Cheak  ",
                            command=Empty,
                            fg="white", background="#00b0f0", font=font_Cheack_B)
        button1.place(x=500, y=520)

if __name__ == "__main__":
    app = Apps()
    app.mainloop()
