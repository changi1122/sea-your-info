from tkinter import *
from tkinter import ttk
from tkinter.font import *

# 창 설정 부분
root = Tk()
root.title("Sea your Info")
root.geometry('500x360')
root.iconbitmap(r'c:\Users\wonjoong\PycharmProjects\HelloWorld\schoolwork\sea_your_info.ico')
root.configure(background='white')
root.resizable(width=False, height=False)
# root.grid_columnconfigure(1, weight=1)#new
# root.grid_rowconfigure(1, weight=1)#new


# 회원가입 창
def register():
    win_reg = Tk()
    win_reg.title("회원가입")
    win_reg.geometry('300x300')
    win_reg.iconbitmap(r'c:\Users\wonjoong\PycharmProjects\HelloWorld\schoolwork\sea_your_info.ico')


# pack이 아니라 grid로 화면 띄우는법
###제일 위 마크 띄우는 부분###
icon_seayourinfo = PhotoImage(file="imagefile/sea_your_info.gif")
label_syiIcon = Label(root, image=icon_seayourinfo)
label_syiIcon.grid(row=0, columnspan=2, pady=25)  # columnspan은 여러 개의 칸을 묶는데 유용하다!!

###"SEA YOUR INFO"글자 들어가는 부분###
text_mainSyi = Label(root, text="SEA YOUR INFO", fg='blue', font='Times 14 bold italic', background='white')
text_mainSyi.grid(row=1, columnspan=2, pady=15)

###id입력하는 칸 부분###
# id_label = Label(root, text="ID").grid(row=2, column=0, sticky=W)
id_text = StringVar(root, value='아이디')

###pw입력하는 칸 부분###
id_textbox = ttk.Entry(root, width=20, textvariable=id_text, justify='center').grid(row=2, column=1, pady=6)
# pw_label = Label(root, text="Pw").grid(row=3, column=0, sticky=W)
pw_text = StringVar(root, value='비밀번호')
id_textbox = ttk.Entry(root, width=20, textvariable=pw_text, justify='center').grid(row=3, column=1, pady=6)

###Login버튼 부분###
#photo_button = PhotoImage(file='imagefile/enter.png') 로그인 버튼에 사진을 넣으려면 주석 해제
btn_login = Button(root, text="로그인", width=19, bg='#00B9FF', fg='white').grid(row=4, columnspan=2, pady=10)
btn_register = Button(root, text="회원가입", command=register, width=19, bg='#00B9FF', fg='white').grid(row=5, columnspan=2,
                                                                                                    pady=10)
###우측의 설명 부분### 아직 추가적으로 작업이 필요한 부분
text_explain_upper = Label(root, text="여기서부터")
text_explain_upper.grid(row=0,column=3)
text_explain_lower = Label(root, text="여기까지는 설명이 들어갈 부분입니다.")
text_explain_lower.grid(row=5, column=3)

root.mainloop()
