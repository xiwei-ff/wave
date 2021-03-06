import math
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