import tkinter as tk
import requests

window = tk.Tk()
window.title('词汇搜索')
window.geometry('675x350')

# # 图片封面
# canvas = tk.Canvas(window, height=500, width=900)
# image_file = tk.PhotoImage(file='C:\\Users\\user\\Desktop\\fm_rem.gif')
# image = canvas.create_image(0,0, anchor='nw', image=image_file)
# canvas.pack()

entry_usr_name = tk.Text(window, width=80, height=15)
entry_usr_name.place(x=15, y=0)

usr_input = tk.StringVar()
chat_input_area = tk.Entry(window, textvariable=usr_input)
chat_input_area.place(x=75, y=280)

def sc():
    entry_usr_name.delete('1.0', tk.END)    # 清空上次搜索内容

    url = "https://fanyi.baidu.com/sug"

    data = {
        "kw": "{}".format(usr_input.get())
    }
    resp = requests.post(url, data=data)    # 获取搜索内容

    inf = resp.json()   # 纪录搜索内容

    inf2 = inf.get("data")

    if inf2 == []:
        entry_usr_name.insert(tk.INSERT, "未查询到信息", '\n')   # 未查询到信息的提示
    else:
        for i in inf2:
            processing_inf = i.get("k"), i.get("v")
            entry_usr_name.insert(tk.INSERT, processing_inf, '\n')   # 插入最新搜索的内容
            entry_usr_name.insert(tk.INSERT, '\n')

button_login = tk.Button(window, text='搜索', command=sc)
button_login.place(x=250, y=275)

window.mainloop()