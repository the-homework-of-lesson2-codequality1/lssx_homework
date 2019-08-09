from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('calculation')
root.geometry('400x400')

#单位换算
change=1
def unit_1():
    global change
    change=1
def unit_2():
    global change
    change=2.54

#正方形
def counter4():
    global width3
    width3=float(e1.get())
    float(width3)
    width3_1=width3*change
    a='%.3f' % (width3_1)
    b=str(a)
    value='%.3f' % (width3_1**2)
    c=str(value)
    l1.config(text="你选择'正方形',边长:"+b+"cm,面积:"+c+"cm2.")

#圆
def counter3():
    global width3
    width3=float(e1.get())
    float(width3)
    width3_1=width3*change
    a='%.3f' % (width3_1)
    b=str(a)
    value='%.3f' % (3.14*width3_1**2)
    c=str(value)
    l1.config(text="你选择'圆形',直径:"+b+"cm,面积:"+c+"cm2.")

#长方形
def counter2():
    global width
    width=float(e1.get())
    global height
    height=float(e2.get())
    float(width)
    float(height)
    width_1=width*change
    height_1=height*change
    a='%.3f' % (width_1)
    b=str(a)
    c='%.3f' % (height_1)
    d=str(c)
    value=round(width_1*height_1,3)
    e=str(value)
    l1.config(text="你选择'长方形',长:"+b+"cm,高:"+d+",面积:"+e+"cm2.")

#三角形
def counter1():
    global width
    width=float(e1.get())
    global height
    height=float(e2.get())
    float(width)
    float(height)
    width_1=width*change
    height_1=height*change
    a='%.3f' % (width_1)
    b=str(a)
    c='%.3f' % (height_1)
    d=str(c)
    value='%.3f' % (width_1*height_1*0.5)
    e=str(value)
    l1.config(text="你选择'三角形',底边长:"+b+"cm,高:"+d+",面积:"+e+"cm2.")

l0=Label(root,text='请输入正方形边长/圆的直径/长方形的宽/三角形的底边长')
l0.pack()
e1=Entry(root)
e1.pack()

l2=Label(root,text='请输入长方形/三角形的高')
l2.pack()
e2=Entry(root)
e2.pack()
l1=Label(root,text='只能数字')
l1.pack()

l3=Label(root,text='请选择单位')
l3.pack()
b3=Button(root,text='cm',width=15,height=2,command=unit_1)
b3.pack()
b4=Button(root,text='inch',width=15,height=2,command=unit_2)
b4.pack()

menubar=Menu(root)
typemenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label='Type',menu=typemenu)

typemenu.add_command(label='正方形',command=counter4)
typemenu.add_command(label='圆',command=counter3)
typemenu.add_command(label='长方形',command=counter2)
typemenu.add_command(label='三角形',command=counter1)
typemenu.add_separator()
typemenu.add_command(label='Exit',command=root.quit)
root.config(menu=menubar)

mainloop()