# -*-conding:utf-8-*-
import math
import tkinter as tk
#------------------------------------suanfa-------------------------
def Salinity(p,T,c):
    #-------------------计算盐度-------------------------------------------------
    '''
        R_T 一一被测海水样品与实用盐度为35的标准海水样品，在相同温度和一个标准大气压下电导率的比值;
        T 一 被测海水样品的温度，℃;
        R：现场测得的电导率与S=35,T=15℃，p=0时的标准海水电导率的比值
        R_p：现场测得的电导率与同一样品在相同温度和p=0条件下的电导率比值
        T_T：实用盐度为35的参考海水在温度为T（℃）时与其在15℃时电导率的比值
    '''
    if c <= 0:
        return 0
    else:
        T *= 1.00024
        a = [0.0080,-0.1692,25.3851,14.0941,-7.0261,2.7081]
        b = [0.0005,-0.0056,-0.0066,-0.0375,0.0636,-0.0144]
        # K = 0.0162
        A_1,A_2,A_3 = 2.070*pow(10,-5),-6.370*pow(10,-10),3.989*pow(10,-15)
        B_1,B_2,B_3,B_4 = 3.426*pow(10,-2),4.464*pow(10,-4),4.215*pow(10,-1),-3.107*pow(10,-3)
        C_0,C_1,C_2,C_3,C_4 = 0.6766097,2.00564*pow(10,-2),1.104259*pow(10,-4),-6.9698*pow(10,-7),1.0031*pow(10,-9)
        R = c/42.914
        val = 1+B_1*T+B_2*T**2+B_3*R+B_4*T*R
        if val:
            R_p = 1+(p*(A_1+p*(A_2+A_3*p)))/val
        val = R_p*(C_0+(T*(C_1+T*(C_2+T*(C_3+T*C_4)))))
        if val:
            R_T = R/val
        if R_T <=0:
            R_T = 0.000001
        sum1 = sum2 = 0.0
        for i in range(6):
            temp = pow(R_T,i/2.0)
            sum1 += a[i]*temp
            sum2 += b[i]*temp
        val = 1.0+0.0162*(T-15.0)
        if val:
            result = sum1+sum2*(T-15.0)/val
        else:
            result = -99.0
    return round(result,4)

        # T_T =C_0+C_1*T+C_2*T**2+C_3*T**3+C_4*T**4
        # R_p = 1+((A_1+A_2*p+A_3*p**2)*p)/(1+B_1*T+B_2*T**2+(B_3+B_4*T)*R)
        # R_T = R/(R_p*T_T)
        # #盐度
        # S = float(a_0+a_1*pow(R_T,1/2)+a_2*R_T+a_3*pow(R_T,3/2)+a_4*pow(R_T,2)+a_5*pow(R_T,5/2)+((T-15)/(1+K*(T-15)))*(b_0+b_1*pow(R_T,1/2)+b_2*R_T+b_3*pow(R_T,3/2)+b_4*pow(R_T,2)+b_5*pow(R_T,5/2)))
    # return round(S,4)
def Depth(d_type,p,latitude):             #由c转换来的
    '''
    :param d_type:fresh water or salt water
    :param p: 压力db
    :param latitude: 纬度
    :return: 深度
    '''
    if d_type == '0':            #淡水
        d = p*1.019716
    else:                                  #海水
        x = math.sin(latitude/57.29578)
        x *= x
        g = 9.780318*(1.0+(5.2788*10**(-3)+2.36*10**(-5)*x)*x)+1.092*pow(10,-6)*p #当地重力加速度
        d = (((-1.82*pow(10,-15)*p+2.279*pow(10,-10))*p-2.2512*pow(10,-5))*p+9.72659)*p
        if g:
            d/=g
    return round(d,0)
def density(p, T, c):
    # -------------------密度计算[kg/m^3]-------------------------------------------------
    #常数值设定
    S = Salinity(p,T,c)
    p/=100    #进行单位换算
    T = T*1.00024
    A0,A1,A2,A3,A4,A5 = 999.842594,6.793952*pow(10,-2),-9.095290*pow(10,-3),1.001685*pow(10,-4),-1.120083*pow(10,-6),6.536332*pow(10,-9)
    B0,B1,B2,B3,B4 = 8.24493*pow(10,-1),-4.0899*pow(10,-3),7.6438*pow(10,-5),-8.2467*pow(10,-7),5.3875*pow(10,-9)
    C0,C1,C2 = -5.72466*pow(10,-3),1.0227*pow(10,-4),-1.6546*pow(10,-6)
    D0 = 4.8314*pow(10,-4)
    E0,E1,E2,E3,E4 = 19652.21,148.4206,-2.327105,1.360477*pow(10,-2),-5.155288*pow(10,-5)
    F0,F1,F2,F3 = 54.6746,-0.603459,1.09987*pow(10,-2),-6.1670*pow(10,-5)
    G0,G1,G2 = 7.944*pow(10,-2),1.6483*pow(10,-2),-5.3009*pow(10,-4)
    H0,H1,H2,H3 = 3.239908,1.43713*pow(10,-3),1.16092*pow(10,-4),-5.77905*pow(10,-7)
    I0,I1,I2 = 2.2838*pow(10,-3),-1.0981*pow(10,-5),-1.6078*pow(10,-5)
    J0 = 1.91075*pow(10,-3)
    M0,M1,M2 = -9.9348*pow(10,-7),2.0816*pow(10,-8),9.1697*pow(10,-10)
    K0,K1,K2 = 8.50935*pow(10,-5),-6.12293*pow(10,-6),5.2787*pow(10,-8)
    if S <= 0:
        S = 0.000001
    density_w = A0+A1*T+A2*T**2+A3*T**3+A4*T**4+A5*T**5
    density = density_w+(B0+B1*T+B2*T**2+B3*T**3+B4*T**4)*S+(C0+C1*T+C2*T**2)*pow(S,3/2)+D0*S**2
    Kw = E0+E1*T+E2*T**2+E3*T**3+E4*T**4
    aw = H0+H1*T+H2*T**2+H3*T**3
    bw = K0+K1*T+K2*T**2
    k = Kw+(F0+F1*T+F2*T**2+F3*T**3)*S+(G0+G1*T+G2*T**2)*pow(S,3/2)+(aw+(I0+I1*T+I2*T**2)*S+J0*pow(S,3/2))*p+(bw+(M0+M1*T+M2*T**2)*S)*p**2
    val = 1-p/k
    if val:
        density = density/val-1000
    return round(density,4)
def sound_velocity(p,T,c):
    # -------------------计算声速[m/s]-------------------------------------------------
    T = T * 1.00024  # 由90定义温度转换为68定义温度
    S = Salinity(p, T, c)
    pr = 0.1019716*(p+10.1325)
    sd = S-35
    a = (((7.9851*pow(10,-6)*T-2.6045*pow(10,-4))*T-4.4532*pow(10,-2))*T+4.5721)*T+1449.14
    sv = (7.7711*pow(10,-7)*T-1.1244*pow(10,-2))*T+1.39799
    v0 = (1.69202*pow(10,-3)*sd+sv)*sd+a
    a = ((4.5283*pow(10,-8)*T+7.4812*pow(10,-6))*T-1.8607*pow(10,-4))*T+0.16072
    v1 = sv*sd+a
    a = (1.8563*pow(10,-9)*T-2.5294*pow(10,-7))*T+1.0268*pow(10,-5)
    sv = -1.294*pow(10,-7)*sd+a
    a = -1.9646*pow(10,-10)*T+3.5216*pow(10,-9)
    sv = (((-3.3603*pow(10,-12)*pr+a)*pr+sv)*pr+v1)*pr+v0
    return round(sv,4)
#---------------------end_suanfa-----------------------------------------------

#-----------------------子程序1，计算盐度，深度，密度，声速--------------------------
# -*-conding:utf-8-*-
def setup():
    #SDdV计算
    #创建应用程序窗口
    root = tk.Toplevel()
    #压强（db）
    varp = tk.StringVar()
    varp.set('')
    #温度（℃）
    varT = tk.StringVar()
    varT.set('')
    #电导率
    varc = tk.StringVar()
    varc.set('')
    #水的类型
    vard_type = tk.StringVar()
    vard_type.set('')
    #纬度
    varlatitude = tk.StringVar()
    varlatitude.set('')
    #水的盐度
    varS = tk.StringVar()
    varS.set('')
    #水的深度
    varDepth= tk.StringVar()
    varDepth.set('')
    #海水的密度
    vardensity= tk.StringVar()
    vardensity.set('')
    #海水的声速
    varV= tk.StringVar()
    varV.set('')

    root.title('衍生要素计算(S、d、D、V)')
    root.geometry('600x320')

    # 创建压强p标签及输入文本框
    labelp = tk.Label(root, text='p(压强db):')
    labelp.place(x=50, y=30, width=140, height=20)
    entryp = tk.Entry(root, textvariable=varp)
    entryp.place(x=190, y=30, width=60, height=20)

    # 创建温度T标签及输入文本框
    labelT = tk.Label(root, text='T(温度℃):')
    labelT.place(x=50, y=60, width=140, height=20)
    entryT = tk.Entry(root, textvariable=varT)
    entryT.place(x=190, y=60, width=60, height=20)

    # 创建电导率参数c标签及输入文本框
    labelc = tk.Label(root, text='c(电导率):')
    labelc.place(x=360, y=30, width=80, height=20)
    entryc = tk.Entry(root, textvariable=varc)
    entryc.place(x=440, y=30, width=60, height=20)

    # 创建水的类型d_type标签及输入文本框
    labeld_type = tk.Label(root, text='d_type(类型):')
    labeld_type.place(x=360, y=60, width=80, height=20)
    entryd_type = tk.Entry(root, textvariable=vard_type)
    entryd_type.place(x=440, y=60, width=60, height=20)
    #创建盐度（S）标签及文本框
    labelS = tk.Label(root, text='S(盐度):')
    labelS.place(x=20, y=200, width=130, height=20)
    varS = tk.StringVar()
    entryS = tk.Entry(root, textvariable=varS)
    entryS.place(x=150, y=200, width=120, height=20)

    # 创建Depth标签及文本框
    labelDepth = tk.Label(root, text='Depth（海水深度m）:')
    labelDepth.place(x=290, y=200, width=150, height=20)
    varDepth = tk.StringVar()
    entryDepth = tk.Entry(root, textvariable=varDepth)
    entryDepth.place(x=440, y=200, width=120, height=20)

    # 创建密度标签及文本框
    labeldensity = tk.Label(root, text='density(密度kg/m^3):')
    labeldensity.place(x=20, y=250, width=130, height=20)
    vardensity = tk.StringVar()
    entrydensity = tk.Entry(root, textvariable=vardensity)
    entrydensity.place(x=150, y=250, width=120, height=20)

    # 创建声速标签及文本框
    labelV = tk.Label(root, text='V(海水的声速m/s）:')
    labelV.place(x=290, y=250, width=150, height=20)
    varV = tk.StringVar()
    entryV = tk.Entry(root, textvariable=varV)
    entryV.place(x=440, y=250, width=120, height=20)
    #确认按钮事件处理函数
    def login():
        # 获取p,T,c
        p = float(entryp.get())
        T = float(entryT.get())
        c = float(entryc.get())
        d_type =entryd_type.get()

        #-------------- 计算盐度，深度，密度，声速---------------
        S = Salinity(p,T,c)
        D = Depth(d_type,p,latitude=27)
        d = density(p, T, c)
        V = sound_velocity(p,T,c)
        print(p,T,c)
        print(S,D,d,V)
        varS.set(S)
        varDepth.set(D)
        vardensity.set(d)
        varV.set(V)
    # 取消按钮的事件处理函数
    def cancel():
        # 清空用户输入的数值
        varp.set('')
        varT.set('')
        varc.set('')
        vard_type.set('')
        varS.set('')
        varDepth.set('')
        vardensity.set('')
        varV.set('')

    # 创建按钮组件，同时设置按钮事件处理函数
    buttonOk = tk.Button(root, text='Login', fg="blue", command=login)
    buttonOk.place(x=210, y=130, width=50, height=20)
    buttonCancel = tk.Button(root, text='Cancel', fg="blue", command=cancel)
    buttonCancel.place(x=340, y=130, width=50, height=20)
    #启动消息循环
    root.mainloop()
#------------------------end_子程序1--------------------------------------------
#------------------------子程序2:飓风浪相关参数换算---------------------------------
def JFL():#定义飓风浪计算函数
    root = tk.Toplevel()
    varVF = tk.StringVar()
    varVF.set('')
    varP0 = tk.StringVar()
    varP0.set('')
    varf = tk.StringVar()
    varf.set('')
    varR = tk.StringVar()
    varR.set('')
    root.title('飓风浪相关参数的计算')
    root.geometry('600x300')


    #创建VF标签及输入文本框
    labelVF=tk.Label(root, text='VF(风速m/s):')
    labelVF.place(x=50, y=30, width=140, height=20)
    entryVF =tk.Entry(root,textvariable=varVF)
    entryVF.place(x=190, y=30, width=60, height=20)

    #创建P0标签及输入文本框
    labelP0 = tk.Label(root, text='P0(飓风中心气压mmgh):')

    labelP0.place(x=50, y=60, width=140, height=20)
    entryP0=tk.Entry(root,textvariable=varP0)
    entryP0.place(x=190,y=60,width=60,height=20)

    #创建科氏力参数f标签及输入文本框
    labelf = tk.Label(root, text='f(科氏力参数):')
    labelf.place(x=360, y=30, width=80, height=20)
    entryf = tk.Entry(root,textvariable=varf)
    entryf.place(x=440, y=30, width=60, height=20)


    #创建飓风中心到最大风速的距离R标签及文本框
    labelR = tk.Label(root, text='R(距离KM):')
    labelR.place(x=360, y=60, width=80, height=20)
    entryR = tk.Entry(root,textvariable=varR)
    entryR.place(x=440, y=60, width=60, height=20)
    #创建Hmax标签及文本框
    labelHmax = tk.Label(root, text='Hmax（最大波高m）:')
    labelHmax.place(x=20, y=200, width=130, height=20)
    varHmax = tk.StringVar()
    entryHmax = tk.Entry(root,textvariable=varHmax)
    entryHmax.place(x=150, y=200, width=120, height=20)

    #创建Tmax标签及文本框
    labelTmax = tk.Label(root, text='Tmax（最大波长周期是s）:')
    labelTmax.place(x=290, y=200, width=150, height=20)
    varTmax = tk.StringVar()
    entryTmax = tk.Entry(root,textvariable=varTmax)
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
    buttonOk = tk.Button(root, text='Login', fg="blue",command=login)
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
    buttonCancel = tk.Button(root, text='Cancel',fg="blue", command=cancel)
    buttonCancel.place(x=340, y=130, width=50, height=20)

    #启动消息循环
    root.mainloop()
#------------------------end_子程序2--------------------------------------------
#------------------------子程序3：各种累积频率波高间的换算---------------------------
#各种累积频率波高间换算
#H_F:累积频率为F的波高(m)
#H:平均波高(m)
#H_*:相对水深,H_*=H/d,记为A
#d:水深(m)
#F:累积频率
def LJP():
    #创建应用程序窗口
    root = tk.Toplevel()
    varH1 = tk.StringVar()
    varH1.set('')
    varH2 = tk.StringVar()
    varH2.set('')
    varH_10 = tk.StringVar()
    varH_10.set('')
    vard2 = tk.StringVar()
    vard2.set('')
    varF = tk.StringVar()
    varF.set('')
    root.title('各种累积频率波高间换算')
    root.geometry('900x600')

    #创建第一个输入标签
    labelputin1 = tk.Label(root,text='请输入1/10大波的平均波高:')
    labelputin1.place(x=0,y=60)

    #创建第二个输入标签
    labelputin2 = tk.Label(root,text='请输入任一累积频率、波列的平均波高和水深:')
    labelputin2.place(x=0,y=350)
    #创建第一个输出标签
    labelputout1 = tk.Label(root,text='输出下面各值分别为:')
    labelputout1.place(x=450,y=20)
    #创建第一个输出标签
    labelputout2= tk.Label(root,text='输出下面各值分别为:')
    labelputout2.place(x=450,y=320)

    #创建H_1/10标签及其输入框
    labelH_10 = tk.Label(root,text='H_(1/10)大波的平均波高/m:')
    labelH_10.place(x=30,y=130,height=20)
    entryH_10 = tk.Entry(root,textvariable=varH_10)
    entryH_10.place(x=190,y=130,width=60,height=20)

    #创建d2标签及其输入框
    labeld2 = tk.Label(root,text='d(水深/m):')
    labeld2.place(x=30,y=440,width=100,height=20)
    entryd2 = tk.Entry(root,textvariable=vard2)
    entryd2.place(x=180,y=440,width=60,height=20)

    #创建H1标签及其输入框
    labelH1 = tk.Label(root,text='H(波列的平均波高/m):')
    labelH1.place(x=30,y=480,width=150,height=20)
    entryH1 = tk.Entry(root,textvariable=varH1)
    entryH1.place(x=180,y=480,width=60,height=20)

    #创建F标签及其输入框
    labelF = tk.Label(root,text='F(x%)累积频率):')
    labelF.place(x=30,y=400,width=130,height=20)
    entryF = tk.Entry(root,textvariable=varF)
    entryF.place(x=180,y=400,width=60,height=20)

    #--------------创建输出框---------------------

    #创建H2输出框
    labelH2 = tk.Label(root,text='H(波列的平均波高/m):')
    labelH2.place(x=310,y=60,width=120,height=20)
    varH2 = tk.StringVar()
    entryH2 = tk.Entry(root,textvariable=varH2)
    entryH2.place(x=530,y=60,width=60,height=20)
    #创建H1_(1/100)输出框
    labelH1_100 = tk.Label(root,text='H_(0.4%)=H_(1/100)大波的平均波高/m:')
    labelH1_100.place(x=310,y=100,width=220,height=20)
    varH1_100 = tk.StringVar()
    entryH1_100 = tk.Entry(root,textvariable=varH1_100)
    entryH1_100.place(x=530,y=100,width=60,height=20)
    #创建H_(1/3)输出框
    labelH1_6 = tk.Label(root,text='H_(13%)=H_(1/3)大波的平均波高/m:')
    labelH1_6.place(x=310,y=150,width=200,height=20)
    varH1_6 = tk.StringVar()
    entryH1_6= tk.Entry(root,textvariable=varH1_6)
    entryH1_6.place(x=530,y=150,width=60,height=20)
    #创建H_r输出框
    labelH_r = tk.Label(root,text='H_r均方根波高/m):')
    labelH_r.place(x=310,y=200,width=100,height=20)
    varH_r = tk.StringVar()
    entryH_r = tk.Entry(root,textvariable=varH_r)
    entryH_r.place(x=530,y=200,width=60,height=20)
    #创建H_(1%)输出框
    labelH_3= tk.Label(root,text='累积频率为1%的波高/m:')
    labelH_3.place(x=630,y=60,width=150,height=20)
    varH_3 = tk.StringVar()
    entryH_3 = tk.Entry(root,textvariable=varH_3)
    entryH_3.place(x=780,y=60,width=60,height=20)
    #创建H_(5%)输出框
    labelH_4 = tk.Label(root,text='累积频率为5%的波高/m:')
    labelH_4.place(x=630,y=100,width=150,height=20)
    varH_4 = tk.StringVar()
    entryH_4 = tk.Entry(root,textvariable=varH_4)
    entryH_4.place(x=780,y=100,width=60,height=20)
    #创建H_(13%)输出框
    labelH_5 = tk.Label(root,text='累积频率为13%的波高/m:')
    labelH_5.place(x=630,y=150,width=150,height=20)
    varH_5 = tk.StringVar()
    entryH_5 = tk.Entry(root,textvariable=varH_5)
    entryH_5.place(x=780,y=150,width=60,height=20)

    #创建Hp标签及其输出框
    labelHp = tk.Label(root,text='Hp(F对应的1/p大波的平均波高/m):')
    labelHp.place(x=310,y=360,width=200,height=20)
    varHp = tk.StringVar()
    entryHp = tk.Entry(root,textvariable=varHp)
    entryHp.place(x=530,y=360,width=60,height=20)
    #创建H7标签及其输出框
    labelH7 = tk.Label(root,text='H_(1/100)大波的平均波高/m:')
    labelH7.place(x=310,y=400,width=180,height=20)
    varH7 = tk.StringVar()
    entryH7 = tk.Entry(root,textvariable=varH7)
    entryH7.place(x=530,y=400,width=60,height=20)
    #创建H8标签及其输出框
    labelH8 = tk.Label(root,text='H_(1/10)大波的平均波高/m:')
    labelH8.place(x=310,y=440,width=170,height=20)
    varH8 = tk.StringVar()
    entryH8 = tk.Entry(root,textvariable=varH8)
    entryH8.place(x=530,y=440,width=60,height=20)
    #创建H9标签及其输出框
    labelH9 = tk.Label(root,text='H_(1/3)大波的平均波高/m:')
    labelH9.place(x=310,y=480,width=170,height=20)
    varH9 = tk.StringVar()
    entryH9 = tk.Entry(root,textvariable=varH9)
    entryH9.place(x=530,y=480,width=60,height=20)
    #创建H10标签及其输出框
    labelH10 = tk.Label(root,text='H_r均方根波高/m):')
    labelH10.place(x=310,y=520,width=120,height=20)
    varH10 = tk.StringVar()
    entryH10 = tk.Entry(root,textvariable=varH10)
    entryH10.place(x=530,y=520,width=60,height=20)
    #创建HF标签及其输出框
    labelHF = tk.Label(root,text='H_F(累积频率为F的波高/m):')
    labelHF.place(x=610,y=360,width=180,height=20)
    varHF = tk.StringVar()
    entryHF = tk.Entry(root,textvariable=varHF)
    entryHF.place(x=780,y=360,width=60,height=20)
    #创建H11标签及其输出框
    labelH11 = tk.Label(root,text='累积频率为1%的波高/m:')
    labelH11.place(x=630,y=400,width=130,height=20)
    varH11 = tk.StringVar()
    entryH11 = tk.Entry(root,textvariable=varH11)
    entryH11.place(x=780,y=400,width=60,height=20)
    #创建H12标签及其输出框
    labelH12 = tk.Label(root,text='累积频率为5%的波高/m:')
    labelH12.place(x=620,y=440,width=150,height=20)
    varH12 = tk.StringVar()
    entryH12 = tk.Entry(root,textvariable=varH12)
    entryH12.place(x=780,y=440,width=60,height=20)
    #创建H13标签及其输出框
    labelH13 = tk.Label(root,text='累积频率为13%的波高/m:')
    labelH13.place(x=610,y=480,width=180,height=20)
    varH13 = tk.StringVar()
    entryH13 = tk.Entry(root,textvariable=varH13)
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
    buttonOk = tk.Button(root,text='login1', fg="blue",command=login1)
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
    buttonOk = tk.Button(root, text='login2',fg="blue",command=login2)
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
    buttonCancel = tk.Button(root, text='Cancel1',fg="blue", command=Cancel1)
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
    buttonCancel = tk.Button(root,text='Cancel2',fg="blue", command=Cancel2)
    buttonCancel.place(x=500, y=550, width=50, height=20)
    #启动消息循环
    root.mainloop()
#------------------------end_子程序3--------------------------------------------
#-------------------------------创建应用程序主窗口---------------------------
def main():
    root = tk.Tk()
    #设置主窗口大小
    root.config(width=450)
    root.config(height=280)
    #设置主窗口标题
    root.title('海岸水文数据处理多用途集成工具系统')
    menubar = tk.Menu(root)
    fileMenu = tk.Menu(menubar, tearoff=0)  # 去掉顶端横线
    menubar.add_cascade(label='文件', menu=fileMenu)  # 添加一个子菜单 File
    fileMenu.add_command(label='新建' )
    fileMenu.add_command(label='打开')
    fileMenu.add_command(label='保存', accelerator="Ctrl+S")
    fileMenu.add_command(label='另存为')
    fileMenu.add_separator()  # 加分割线
    fileMenu.add_command(label='退出', command=quit)
    editMenu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label='编辑', menu=editMenu)
    editMenu.add_command(label='剪切')
    editMenu.add_command(label='复制')
    editMenu.add_command(label='粘贴')
    settingsMenu = tk.Menu(editMenu, tearoff=0)
    editMenu.add_cascade(label='设置', menu=settingsMenu)
    menubar.add_cascade(label='帮助')  # 添加一个子菜单 File
    root.config(menu=menubar)
    root.rowconfigure(0,weight=1)
    root.columnconfigure(0,weight=1)
    #----------------------------------------------------------

    #---------------------------设置弹窗-------------------------------
    # 单击按钮1，创建并弹出新窗口
    button1 = tk.Button(root, text='衍生要素计算(S、d、D、V)',command=setup)
    button1.place(x=120, y=40, height=40, width=200)
    button2 = tk.Button(root, text='飓风浪相关参数的计算', command=JFL)
    button2.place(x=120, y=100, height=40, width=200)
    button3 = tk.Button(root, text='各种累积频率波高间的换算', command=LJP)
    button3.place(x=120, y=160, height=40, width=200)
    #启动消息主循环
    root.mainloop()
if __name__ == '__main__':
    main()
