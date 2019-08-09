from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('calculation')
root.geometry('400x650')


#正方形
def counter4_cm():
    global width3
    width3=float(e1.get())
    float(width3)
    a='%.3f' % (width3)
    b=str(a)
    value='%.3f' % (width3**2)
    c=str(value)
    l1.config(text="你选择'正方形',边长:"+b+"cm,面积:"+c+"cm2.")
def counter4_inch():
    global width3
    width3=float(e1.get())
    float(width3)
    width3_1=width3*2.54
    a='%.3f' % (width3_1)
    b=str(a)
    value='%.3f' % (width3_1**2)
    c=str(value)
    l1.config(text="你选择'正方形',边长:"+b+"cm,面积:"+c+"cm2.")


#圆
def counter3_cm():
    float(width3)
    a='%.3f' % (width3)
    b=str(a)
    value='%.3f' % (3.14*width3**2)
    c=str(value)
    l1.config(text="你选择'圆形',直径:"+b+"cm,面积:"+c+"cm2.")
def counter3_inch():
    global width3
    width3=float(e1.get())
    float(width3)
    width3_1=width3*2.54
    a='%.3f' % (width3_1)
    b=str(a)
    value='%.3f' % (3.14*width3_1**2)
    c=str(value)
    l1.config(text="你选择'圆形',直径:"+b+"cm,面积:"+c+"cm2.")



#长方形
def counter2_cm():
    global width
    width=float(e1.get())
    global height
    height=float(e2.get())
    float(width)
    float(height)
    a='%.3f' % (width)
    b=str(a)
    c='%.3f' % (height)
    d=str(c)
    value=round(width*height,3)
    e=str(value)
    l1.config(text="你选择'长方形',长:"+b+"cm,高:"+d+",面积:"+e+"cm2.")
def counter2_inch():
    float(width)
    float(height)
    a='%.3f' % (width*2.54)
    b=str(a)
    c='%.3f' % (height*2.54)
    d=str(c)
    value='%.3f' % (width*height*2.54**2)
    e=str(value)
    l1.config(text="你选择'长方形',长:"+b+"cm,高:"+d+",面积:"+e+"cm2.")



#三角形
def counter1_cm():
    global width
    width=float(e1.get())
    global height
    height=float(e2.get())
    float(width)
    float(height)
    a='%.3f' % (width)
    b=str(a)
    c='%.3f' % (height)
    d=str(c)
    value='%.3f' % (width*height*0.5)
    e=str(value)
    l1.config(text="你选择'三角形',底边长:"+b+"cm,高:"+d+",面积:"+e+"cm2.")
def counter1_inch():
    global width
    width=float(e1.get())
    global height
    height=float(e2.get())
    float(width)
    float(height)
    a='%.3f' % (width*2.54)
    b=str(a)
    c='%.3f' % (height*2.54)
    d=str(c)
    value='%.3f' % (0.5*width*height*2.54**2)
    e=str(value)
    l1.config(text="你选择'三角形',长:"+b+"cm,高:"+d+",面积:"+e+"cm2.")



l0=Label(root,text='请输入三角形的底边长/长方形的宽/正方形边长/圆的直径')
l0.pack()
e1=Entry(root)
e1.pack()

l2=Label(root,text='请输入长方形/三角形的高')
l2.pack()
e2=Entry(root)
e2.pack()
l1=Label(root,text='只能数字')
l1.pack()

l3=Label(root,text='请选择单位（三角形）')
l3.pack()
b3=Button(root,text='cm',width=15,height=2,command=counter1_cm)
b3.pack()
b4=Button(root,text='inch',width=15,height=2,command=counter1_inch)
b4.pack()
l4=Label(root,text='请选择单位（长方形）')
l4.pack()
b3=Button(root,text='cm',width=15,height=2,command=counter2_cm)
b3.pack()
b4=Button(root,text='inch',width=15,height=2,command=counter2_inch)
b4.pack()
l5=Label(root,text='请选择单位（正方形）')
l5.pack()
b3=Button(root,text='cm',width=15,height=2,command=counter4_cm)
b3.pack()
b4=Button(root,text='inch',width=15,height=2,command=counter4_inch)
b4.pack()
l6=Label(root,text='请选择单位（圆形）')
l6.pack()
b3=Button(root,text='cm',width=15,height=2,command=counter3_cm)
b3.pack()
b4=Button(root,text='inch',width=15,height=2,command=counter3_inch)
b4.pack()

mainloop()
