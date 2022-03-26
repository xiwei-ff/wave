
def JFL():#定义飓风浪计算函数
    import tkinter
    import tkinter.messagebox
    import math
    #创建应用程序窗口
    global gDialog
    root = tkinter.Tk()
    varVF = tkinter.StringVar()
    varVF.set('')
    varP0 = tkinter.StringVar()
    varP0.set('')
    varf = tkinter.StringVar()
    varf.set('')
    varR = tkinter.StringVar()
    varR.set('')
    root.title('飓风浪相关参数的计算')
    root.geometry('600x300')


    #创建VF标签及输入文本框
    labelVF=tkinter.Label(root, text='VF(风速m/s):')
    labelVF.place(x=50, y=30, width=140, height=20)
    entryVF =tkinter.Entry(root,textvariable=varVF)
    entryVF.place(x=190, y=30, width=60, height=20)

    #创建P0标签及输入文本框
    labelP0 = tkinter.Label(root, text='P0(飓风中心气压mmgh):')

    labelP0.place(x=50, y=60, width=140, height=20)
    entryP0=tkinter.Entry(root,textvariable=varP0)
    entryP0.place(x=190,y=60,width=60,height=20)

    #创建科氏力参数f标签及输入文本框
    labelf = tkinter.Label(root, text='f(科氏力参数):')
    labelf.place(x=360, y=30, width=80, height=20)
    entryf = tkinter.Entry(root,textvariable=varf)
    entryf.place(x=440, y=30, width=60, height=20)


    #创建飓风中心到最大风速的距离R标签及文本框
    labelR = tkinter.Label(root, text='R(距离KM):')
    labelR.place(x=360, y=60, width=80, height=20)
    entryR = tkinter.Entry(root,textvariable=varR)
    entryR.place(x=440, y=60, width=60, height=20)
    #创建Hmax标签及文本框
    labelHmax = tkinter.Label(root, text='Hmax（最大波高m）:')
    labelHmax.place(x=20, y=200, width=130, height=20)
    varHmax = tkinter.StringVar()
    entryHmax = tkinter.Entry(root,textvariable=varHmax)
    entryHmax.place(x=150, y=200, width=120, height=20)

    #创建Tmax标签及文本框
    labelTmax = tkinter.Label(root, text='Tmax（最大波长周期是s）:')
    labelTmax.place(x=290, y=200, width=150, height=20)
    varTmax = tkinter.StringVar()
    entryTmax = tkinter.Entry(root,textvariable=varTmax)
    entryTmax.place(x=440, y=200 ,width=120, height=20)


    #确认按钮事件处理函数
    def login():
        #获取VF,P0,f,R
       VF = entryVF.get()
       P0 = entryP0.get()
       f = entryf.get()
       R = entryR.get()
       α=float(1.0)
       P0=float(P0)
       ΔP=(1013.3-P0)*0.75
       R=float(R)
       f=float(f)
       VF=float(VF)
       Umax=float(0.447*(14.5*pow(ΔP,1/2)-R*0.31*f))#计算海面上10m高程处最大梯度风速m/s
       if  VF==0:                         #判断飓风是静止还是移动
               UR=0.865*Umax
       elif VF >0:
               UR=0.865*Umax+0.5*VF
       Hmax=5.03*math.exp(R*ΔP/4700)*(1+0.29*α*VF/pow(UR,1/2))
       Tmax=8.6*math.exp(R*ΔP/9400)*(1+0.145*α*VF/pow(UR,1/2))
       print(Hmax)
       print(Tmax)
       varHmax.set(round(Hmax,6))
       varTmax.set(round(Tmax,6))
    #创建按钮组件，同时设置按钮事件处理函数
    buttonOk = tkinter.Button(root, text='Login', fg="blue",command=login)
    buttonOk.place(x=210, y=130, width=50, height=20)

    #取消按钮的事件处理函数
    def cancel():
        #清空用户输入的数值
        varVF.set('')
        varP0.set('')
        varf.set('')
        varR.set('')
        varHmax.set('')
        varTmax.set('')
    buttonCancel = tkinter.Button(root, text='Cancel',fg="blue", command=cancel)
    buttonCancel.place(x=340, y=130, width=50, height=20)

    #启动消息循环
    root.mainloop()
if __name__ == '__main__':
    JFL()