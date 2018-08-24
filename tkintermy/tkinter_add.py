
# coding: utf-8

# In[ ]:


import tkinter


#创建操作窗口
root = tkinter.Tk()
root.title("操作窗口")
root.minsize(600, 400)
root.maxsize(600,400)
#创建输入框
label1 = tkinter.Label(root, text= "输入第一个数字：")
label1.place(relx = 0.13, rely = 0.20)
entry1 = tkinter.Entry(root)
entry1.place(relx = 0.29, rely = 0.20, width = 200, height = 20)
label2 = tkinter.Label(root, text= "输入第二个数字：")
label2.place(relx = 0.13, rely = 0.3)
entry2 = tkinter.Entry(root)
entry2.place(relx = 0.29, rely = 0.3, width = 200, height = 20)
#创建结果框
label3 = tkinter.Label(root, text= "计算结果为：")
label3.place(relx = 0.13, rely = 0.4)
text3 = tkinter.Text(root)
text3.place(relx = 0.29, rely = 0.4, width = 200, height = 40)
#创建按钮
button1 = tkinter.Button(root, text="计算")
button1.place(relx = 0.4, rely = 0.75, width = 80)

def result_add(self):
    number1 = entry1.get() #获取第一个输入框的值
    number2 = entry2.get() #获取第二个输入框的值
    result = float(number1) + float(number2)
    text3.delete('1.0','end')
    text3.insert('insert', result) #输入计算结果
    return

button1.bind("<ButtonRelease-1>", result_add ) #点击按钮时触发行为

root.mainloop()
    

