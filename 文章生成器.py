import tkinter
import random,readJSON
from tkinter import INSERT

data = readJSON.读JSON文件("data.json")
名人名言 = data["famous"] # a 代表前面垫话，b代表后面垫话
前面垫话 = data["before"] # 在名人名言前面弄点废话
后面垫话 = data['after']  # 在名人名言后面弄点废话
废话 = data['bosh'] # 代表文章主要废话来源

xx = "学生会退会"

重复度 = 2

def 洗牌遍历(列表):
    global 重复度
    池 = list(列表) * 重复度
    while True:
        random.shuffle(池)
        for 元素 in 池:
            yield 元素

下一句废话 = 洗牌遍历(废话)
下一句名人名言 = 洗牌遍历(名人名言)

def 来点名人名言():
    global 下一句名人名言
    xx = next(下一句名人名言)
    xx = xx.replace(  "a",random.choice(前面垫话) )
    xx = xx.replace(  "b",random.choice(后面垫话) )
    return xx

def 另起一段():
    xx = ". "
    xx += "\r\n"
    xx += "    "
    return xx
def run():
    xx =  entry.get()
    for x in xx:
        tmp = str()
        while ( len(tmp) < 6000 ) :
            分支 = random.randint(0,100)
            if 分支 < 5:
                tmp += 另起一段()
            elif 分支 < 20 :
                tmp += 来点名人名言()
            else:
                tmp += next(下一句废话)
        tmp = tmp.replace("x",xx)
        entry2.insert(INSERT,tmp)
        print(tmp)



#生成主窗口对象
root = tkinter.Tk()
#创建标签 并且添加到主窗口中
root.title("文章生成器")
root.geometry("500x500+200+100")
label = tkinter.Label(root,text = '主题')
label.grid(row = 0,column = 0)

#创建输入框，并且添加到主窗口中
entry = tkinter.Entry(root)
entry.grid(row = 0,column = 1)


#创建按钮，并且添加到主窗口中
btn1 = tkinter.Button(root,text = '按钮1',command = run)
btn1.grid(row = 1,column = 1)

entry2 = tkinter.Text(root, width=50, height=30, undo=True, autoseparators=False)
entry2.grid(row = 2,column = 1)

#保持主窗口一直消息循环中。。
root.mainloop()