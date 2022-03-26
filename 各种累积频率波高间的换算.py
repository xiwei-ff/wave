#各种累积频率波高间换算
#H_F:累积频率为F的波高(m)
#H:平均波高(m)
#H_*:相对水深,H_*=H/d,记为A
#d:水深(m)
#F:累积频率
def LJP():
    import tkinter
    import tkinter.messagebox
    import math
    #创建应用程序窗口
    root = tkinter.Tk()
    varH1 = tkinter.StringVar()
    varH1.set('')
    varH2 = tkinter.StringVar()
    varH2.set('')
    varH_10 = tkinter.StringVar()
    varH_10.set('')
    vard2 = tkinter.StringVar()
    vard2.set('')
    varF = tkinter.StringVar()
    varF.set('')
    root.title('各种累积频率波高间换算')
    root.geometry('900x600')

    #创建第一个输入标签
    labelputin1 = tkinter.Label(root,text='请输入1/10大波的平均波高:')
    labelputin1.place(x=0,y=60)

    #创建第二个输入标签
    labelputin2 = tkinter.Label(root,text='请输入任一累积频率、波列的平均波高和水深:')
    labelputin2.place(x=0,y=350)
    #创建第一个输出标签
    labelputout1 = tkinter.Label(root,text='输出下面各值分别为:')
    labelputout1.place(x=450,y=20)
    #创建第一个输出标签
    labelputout2= tkinter.Label(root,text='输出下面各值分别为:')
    labelputout2.place(x=450,y=320)

    #创建H_1/10标签及其输入框
    labelH_10 = tkinter.Label(root,text='H_(1/10)大波的平均波高/m:')
    labelH_10.place(x=30,y=130,height=20)
    entryH_10 = tkinter.Entry(root,textvariable=varH_10)
    entryH_10.place(x=190,y=130,width=60,height=20)

    #创建d2标签及其输入框
    labeld2 = tkinter.Label(root,text='d(水深/m):')
    labeld2.place(x=30,y=440,width=100,height=20)
    entryd2 = tkinter.Entry(root,textvariable=vard2)
    entryd2.place(x=180,y=440,width=60,height=20)

    #创建H1标签及其输入框
    labelH1 = tkinter.Label(root,text='H(波列的平均波高/m):')
    labelH1.place(x=30,y=480,width=150,height=20)
    entryH1 = tkinter.Entry(root,textvariable=varH1)
    entryH1.place(x=180,y=480,width=60,height=20)

    #创建F标签及其输入框
    labelF = tkinter.Label(root,text='F(x%)累积频率):')
    labelF.place(x=30,y=400,width=130,height=20)
    entryF = tkinter.Entry(root,textvariable=varF)
    entryF.place(x=180,y=400,width=60,height=20)

    #--------------创建输出框---------------------

    #创建H2输出框
    labelH2 = tkinter.Label(root,text='H(波列的平均波高/m):')
    labelH2.place(x=310,y=60,width=120,height=20)
    varH2 = tkinter.StringVar()
    entryH2 = tkinter.Entry(root,textvariable=varH2)
    entryH2.place(x=530,y=60,width=60,height=20)
    #创建H1_(1/100)输出框
    labelH1_100 = tkinter.Label(root,text='H_(0.4%)=H_(1/100)大波的平均波高/m:')
    labelH1_100.place(x=310,y=100,width=220,height=20)
    varH1_100 = tkinter.StringVar()
    entryH1_100 = tkinter.Entry(root,textvariable=varH1_100)
    entryH1_100.place(x=530,y=100,width=60,height=20)
    #创建H_(1/3)输出框
    labelH1_6 = tkinter.Label(root,text='H_(13%)=H_(1/3)大波的平均波高/m:')
    labelH1_6.place(x=310,y=150,width=200,height=20)
    varH1_6 = tkinter.StringVar()
    entryH1_6= tkinter.Entry(root,textvariable=varH1_6)
    entryH1_6.place(x=530,y=150,width=60,height=20)
    #创建H_r输出框
    labelH_r = tkinter.Label(root,text='H_r均方根波高/m):')
    labelH_r.place(x=310,y=200,width=100,height=20)
    varH_r = tkinter.StringVar()
    entryH_r = tkinter.Entry(root,textvariable=varH_r)
    entryH_r.place(x=530,y=200,width=60,height=20)
    #创建H_(1%)输出框
    labelH_3= tkinter.Label(root,text='累积频率为1%的波高/m:')
    labelH_3.place(x=630,y=60,width=150,height=20)
    varH_3 = tkinter.StringVar()
    entryH_3 = tkinter.Entry(root,textvariable=varH_3)
    entryH_3.place(x=780,y=60,width=60,height=20)
    #创建H_(5%)输出框
    labelH_4 = tkinter.Label(root,text='累积频率为5%的波高/m:')
    labelH_4.place(x=630,y=100,width=150,height=20)
    varH_4 = tkinter.StringVar()
    entryH_4 = tkinter.Entry(root,textvariable=varH_4)
    entryH_4.place(x=780,y=100,width=60,height=20)
    #创建H_(13%)输出框
    labelH_5 = tkinter.Label(root,text='累积频率为13%的波高/m:')
    labelH_5.place(x=630,y=150,width=150,height=20)
    varH_5 = tkinter.StringVar()
    entryH_5 = tkinter.Entry(root,textvariable=varH_5)
    entryH_5.place(x=780,y=150,width=60,height=20)

    #创建Hp标签及其输出框
    labelHp = tkinter.Label(root,text='Hp(F对应的1/p大波的平均波高/m):')
    labelHp.place(x=310,y=360,width=200,height=20)
    varHp = tkinter.StringVar()
    entryHp = tkinter.Entry(root,textvariable=varHp)
    entryHp.place(x=530,y=360,width=60,height=20)
    #创建H7标签及其输出框
    labelH7 = tkinter.Label(root,text='H_(1/100)大波的平均波高/m:')
    labelH7.place(x=310,y=400,width=180,height=20)
    varH7 = tkinter.StringVar()
    entryH7 = tkinter.Entry(root,textvariable=varH7)
    entryH7.place(x=530,y=400,width=60,height=20)
    #创建H8标签及其输出框
    labelH8 = tkinter.Label(root,text='H_(1/10)大波的平均波高/m:')
    labelH8.place(x=310,y=440,width=170,height=20)
    varH8 = tkinter.StringVar()
    entryH8 = tkinter.Entry(root,textvariable=varH8)
    entryH8.place(x=530,y=440,width=60,height=20)
    #创建H9标签及其输出框
    labelH9 = tkinter.Label(root,text='H_(1/3)大波的平均波高/m:')
    labelH9.place(x=310,y=480,width=170,height=20)
    varH9 = tkinter.StringVar()
    entryH9 = tkinter.Entry(root,textvariable=varH9)
    entryH9.place(x=530,y=480,width=60,height=20)
    #创建H10标签及其输出框
    labelH10 = tkinter.Label(root,text='H_r均方根波高/m):')
    labelH10.place(x=310,y=520,width=120,height=20)
    varH10 = tkinter.StringVar()
    entryH10 = tkinter.Entry(root,textvariable=varH10)
    entryH10.place(x=530,y=520,width=60,height=20)
    #创建HF标签及其输出框
    labelHF = tkinter.Label(root,text='H_F(累积频率为F的波高/m):')
    labelHF.place(x=610,y=360,width=180,height=20)
    varHF = tkinter.StringVar()
    entryHF = tkinter.Entry(root,textvariable=varHF)
    entryHF.place(x=780,y=360,width=60,height=20)
    #创建H11标签及其输出框
    labelH11 = tkinter.Label(root,text='累积频率为1%的波高/m:')
    labelH11.place(x=630,y=400,width=130,height=20)
    varH11 = tkinter.StringVar()
    entryH11 = tkinter.Entry(root,textvariable=varH11)
    entryH11.place(x=780,y=400,width=60,height=20)
    #创建H12标签及其输出框
    labelH12 = tkinter.Label(root,text='累积频率为5%的波高/m:')
    labelH12.place(x=620,y=440,width=150,height=20)
    varH12 = tkinter.StringVar()
    entryH12 = tkinter.Entry(root,textvariable=varH12)
    entryH12.place(x=780,y=440,width=60,height=20)
    #创建H13标签及其输出框
    labelH13 = tkinter.Label(root,text='累积频率为13%的波高/m:')
    labelH13.place(x=610,y=480,width=180,height=20)
    varH13 = tkinter.StringVar()
    entryH13 = tkinter.Entry(root,textvariable=varH13)
    entryH13.place(x=780,y=480,width=60,height=20)


    #确认按钮1事件处理函数
    def login1():
        #获取H,d
        H_10 = float(entryH_10.get())
        H2 = (H_10)/2.03
        H1_100 = 2.66*H2
        H1_6 = 1.60*H2
        H_r = 1.13*H2
        H_3 = 2.42*H2
        H_4 = 1.95*H2
        H_5 = 1.61*H2
        varH2.set(round(H2,4))
        varH1_100.set(round(H1_100,4))
        varH1_6.set(round(H1_6,4))
        varH_r.set(round(H_r,4))
        varH_3.set(round(H_3,4))
        varH_4.set(round(H_4,4))
        varH_5.set(round(H_5,4))
    #创建按钮事件，同时设置按钮事件处理函数
    buttonOk = tkinter.Button(root,text='login1', fg="blue",command=login1)
    buttonOk.place(x=280, y=250, width=50, height=20)

    #确认按钮2事件处理函数
    def login2():
        #获取H,d
        H1 = float(entryH1.get())
        d2 = float(entryd2.get())
        F = float(entryF.get())
        A=float(H1/d2)
        w=math.log(F*0.01,math.e)
        e=1+(1/pow(2*math.pi,1/2))*A
        HF = H1*pow(((-4/math.pi)*(1+(1/pow(2*math.pi,1/2))*A)*math.log(F*0.01,math.e)),(1-A)/2)
        H7 = float(2.66*H1)
        H8 = float(2.03*H1)
        H9 = float(1.60*H1)
        H10 = float(1.13*H1)
        Hp = H1*(F/H1+(1-pow(math.erf(math.log(F*0.01,math.e)),1/2))/F*0.01)
        H11 = float(2042*H1)
        H12 = float(1.95*H1)
        H13 = float(1.61*H1)
        varHF.set(round(HF,4))
        varH7.set(round(H7,4))
        varH8.set(round(H8,4))
        varH9.set(round(H9,4))
        varH10.set(round(H10,4))
        varHp.set(Hp)
        varH11.set(round(H11,4))
        varH12.set(round(H12,4))
        varH13.set(round(H13,4))
    #创建按钮事件，同时设置按钮事件处理函数
    buttonOk = tkinter.Button(root, text='login2',fg="blue",command=login2)
    buttonOk.place(x=280, y=550, width=50, height=20)


    #取消按钮的事件处理函数
    def Cancel1():
        #清空用户输入的数值
        varH_10.set('')
        #vard1.set('')
        varH2.set('')
        varH1_100.set('')
        varH1_6.set('')
        varH_r.set('')
        varH_3.set('')
        varH_4.set('')
        varH_5.set('')
    buttonCancel = tkinter.Button(root, text='Cancel1',fg="blue", command=Cancel1)
    buttonCancel.place(x=500, y=250, width=50, height=20)


    #取消按钮的事件处理函数
    def Cancel2():
        #清空用户输入的数值
        varH1.set('')
        vard2.set('')
        varF.set('')
        varHF.set('')
        varH7.set('')
        varH8.set('')
        varH9.set('')
        varH10.set('')
        varHp.set('')
        varH11.set('')
        varH12.set('')
        varH13.set('')
    buttonCancel = tkinter.Button(root,text='Cancel2',fg="blue", command=Cancel2)
    buttonCancel.place(x=500, y=550, width=50, height=20)
    #启动消息循环
    root.mainloop()
if __name__ == '__main__':
    LJP()



