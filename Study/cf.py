# coding:utf-8

"This is a program to match the chemical equation"

import numpy as np
from fractions import Fraction
from fractions import gcd
import copy

# periodic table of the elements
periodictable = {"H" :1 , "He":2 , "Li":3 , "Be":4 , "B" :5 , "C" :6 , "N" :7 , "O" :8 , "F" :9 , "Ne":10,
                 "Na":11, "Mg":12, "Al":13, "Si":14, "P" :15, "S" :16, "Cl":17, "Ar":18, "K" :19, "Ca":20,
                 "Sc":21, "Ti":22, "V" :23, "Cr":24, "Mn":25, "Fe":26, "Co":27, "Ni":28, "Cu":29, "Zn":30,
                 "Ga":31, "Ge":32, "As":33, "Se":34, "Br":35, "Kr":36, "Rb":37, "Sr":38, "Y" :39, "Zr":40,
                 "Nb":41, "Mo":42, "Tc":43, "Ru":44, "Rh":45, "Pd":46, "Ag":47, "Cd":48, "In":49, "Sn":50,
                 "Sb":51, "Te":52, "I" :53, "Xe":54, "Cs":55, "Ba":56, "La":57, "Ce":58, "Pr":59, "Nd":60, 
                 "Pm":61, "Sm":62, "Eu":63, "Gd":64, "Tb":65, "Dy":66, "Ho":67, "Er":68, "Tm":69, "Yb":70,
                 "Lu":71, "Hf":72, "Ta":73, "W" :74, "Re":75, "Os":76, "Lr":77, "Pt":78, "Au":79, "Hg":80, 
                 "TI":81, "Pb":82, "Bi":83, "Po":84, "At":85, "Rn":86, "Fr":87, "Ra":88, "Ac":89, "Th":90,
                 "Pa":91, "U" :92, "Np":93, "Pu":94, "Am":95, "Cm":96, "Bk":97, "Cf":98, "Es":99, "Fm":100,
                 "Md":101,"No":102,"Lr":103,"Rf":104,"Db":105,"Sg":106,"Bh":107,"Hs":108,"Mt":109}    

# velence table of the elements
Valencedynamic = {"H":[1 , -1] , "Cu":[1 , 2] , "Fe":[2 , 3 , 4 , 5 , 6 , 8] , "Mn":[2 , 3 , 4 , 6 , 7] , 
                  "Cl":[-1 , 1 , 3 , 4 , 5 , 6 , 7] , "S":[-2 , 2 , 4 , 6] , "C":[2 , 4] , "Si":[2 , 4] , 
                  "Ge":[2 , 4] , "Sn":[2 , 4] , "Pb":[2 , 4] , "N":[-3 , 1 , 2 , 3 , 4 , 5] , 
                  "P":[-3 , 1 , 3 , 4 , 5] , "Au":[1 , 3] , "Hg":[1 , 2],"In":[1 , 3] ,
                  "TI":[1 , 3] , "Ti":[2 , 3 , 4] ,"Zr":[2 , 3 , 4] , "Ce":[3 , 4] , "Hf":[3 , 4] ,
                  "Th":[3 , 4] , "As":[-3 , 3 , 5] , "Sb":[-3 , 3 , 5] , "Bi":[3 , 5] , "V":[2 , 3 , 4 , 5] ,
                  "Nb":[2 , 3 , 4 , 5] , "Ta":[2 , 3 , 4 , 5] , "Pa":[3 , 4 , 5] , "Se":[-2 , 2 , 4 , 6] ,
                  "Te":[-2 , 2 , 4 , 6] , "Po":[2 , 4 , 6] , "Cr":[2 , 3 , 6] , "Mo":[2 , 3 , 4 , 5 , 6] ,
                  "W":[2 , 3 , 4 , 5 , 6] , "U":[3 , 4 , 5 , 6] , "Br":[-1 , 1 , 3 , 5 , 7] ,
                  "I":[-1 , 1 , 3 , 5 , 7] , "Tc":[4 , 5 , 6 , 7] ,"Re":[4 , 5 , 6 , 7] ,
                  "Np":[3 , 4 , 5 , 6 , 7] , "Pu":[3 , 4 , 5 , 6 , 7] , 
                  "Ru":[2 , 3 , 4 , 5 , 6 , 7 , 8] ,"Os":[2 , 3 , 4 , 5 , 6 , 8] , "Co":[2 , 3 , 4] ,
                  "Ni":[2 , 3 , 4] , "Pd":[2 , 3 , 4] , "Rh":[2 , 3 , 4 , 5 , 6] , "Ir":[2 , 3 , 4 , 5 , 6] ,
                  "Pt":[2 , 3 , 4 , 5 , 6]}

valencestatic = {"Li":1 , "Na":1 , "K" :1 , "Rb":1 , "Cs":1 , "Ag":1 , "NH4":1,
                "Ca":2 , "Mg":2 , "Be":2 , "Sr":2 , "Ba":2 , "Zn":2 , "Ra":2,
                "B" :3 , "Al":3 , "Sc":3 , "Ga":3 , "Y" :3 , "La":3 , "Pr":3 , "Nd":3 , "Pm":3 , "Sm":3 ,
                "Eu":3 , "Gd":3 , "Tb":3 , "Dy":3 , "Ho":3 , "Er":3 , "Tm":3 , "Yb":3 , "Lu":3 , "Ac":3 ,
                "Si":4 ,
                "F" :-1, "NO3":-1, "OH":-1, "ClO":-1, "HCO3":-1, "HSO4":-1, "ClO3":-1,
                "O" :-2, "SO4":-2,"CO3":-2,"SO3":-2,"MnO4":-2,
                "PO4":-3}
'''
元素周期表
主族元素    
类金属 
▪ 硼 ( 5)    ▪ 硅 ( 14)   ▪ 锗 ( 32)   ▪ 砷 ( 33)   ▪ 锑 ( 51)
▪ 碲 ( 52)   ▪ 钋 ( 84)           
金属元素    
碱金属 
▪ 锂 ( 3)    ▪ 钠 ( 11)   ▪ 钾 ( 19)   ▪ 铷 ( 37)   ▪ 铯 ( 55)
▪ 钫 ( 87)               
碱土金属    
▪ 铍 ( 4)    ▪ 镁 ( 12)   ▪ 钙 ( 20)   ▪ 锶 ( 38)   ▪ 钡 ( 56)
▪ 镭 ( 88)               
其他金属    
▪ 铝 ( 13)   ▪ 铟 ( 49)   ▪ 镓 ( 31)   ▪ 锡 ( 50)   ▪ 铊 ( 81)
▪ 铅 ( 82)   ▪ 铋 ( 83)   ▪ Uut ( 113)    ▪ Uuq ( 114)    ▪ Uup ( 115)
▪ Uuh ( 116)    ▪ Uus ( 117)            
非金属元素   
稀有气体    
▪ 氦 ( 2)    ▪ 氖 ( 10)   ▪ 氩 ( 18)   ▪ 氪 ( 36)   ▪ 氙 ( 54)
▪ 氡 ( 86)   ▪ Uuo ( 118)            
卤族元素    
▪ 氟 ( 9)    ▪ 氯 ( 17)   ▪ 溴 ( 35)   ▪ 碘 ( 53)   ▪ 砹 ( 85)
其他元素    
▪ 氢 ( 1)    ▪ 碳 ( 6)    ▪ 氮 ( 7)    ▪ 氧 ( 8)    ▪ 磷 ( 15)
▪ 硫 ( 16)   ▪ 硒 ( 34)           
副族元素    
金属元素    
镧系  
▪ 镧 ( 57)   ▪ 铈 ( 58)   ▪ 镨 ( 59)   ▪ 钕 ( 60)   ▪ 钷 ( 61)
▪ 钐 ( 62)   ▪ 铕 ( 63)   ▪ 钆 ( 64)   ▪ 铽 ( 65)   ▪ 镝 ( 66)
▪ 钬 ( 67)   ▪ 铒 ( 68)   ▪ 铥 ( 69)   ▪ 镱 ( 70)   ▪ 镥 ( 71)
锕系  
▪ 锕 ( 89)   ▪ 钍 ( 90)   ▪ 镤 ( 91)   ▪ 铀 ( 92)   ▪ 镎 ( 93)
▪ 钚 ( 94)   ▪ 镅 ( 95)   ▪ 锔 ( 96)   ▪ 锫 ( 97)   ▪ 锎 ( 98)
▪ 锿 ( 99)   ▪ 镄 ( 100)  ▪ 钔 ( 101)  ▪ 锘 ( 102)  ▪ 铹 ( 103)
过渡金属    
▪ 钪 ( 21)   ▪ 钛 ( 22)   ▪ 钒 ( 23)   ▪ 铬 ( 24)   ▪ 锰 ( 25)
▪ 铁 ( 26)   ▪ 钴 ( 27)   ▪ 镍 ( 28)   ▪ 铜 ( 29)   ▪ 锌 ( 30)
▪ 钇 ( 39)   ▪ 锆 ( 40)   ▪ 铌 ( 41)   ▪ 钼 ( 42)   ▪ 锝 ( 43)
▪ 钌 ( 44)   ▪ 铑 ( 45)   ▪ 钯 ( 46)   ▪ 银 ( 47)   ▪ 镉 ( 48)
▪ 铪 ( 72)   ▪ 钽 ( 73)   ▪ 钨 ( 74)   ▪ 铼 ( 75)   ▪ 锇 ( 76)
▪ 铱 ( 77)   ▪ 铂 ( 78)   ▪ 金 ( 79)   ▪ 钅卢 ( 104) ▪ 钅杜 ( 105)
▪ 钅喜 ( 106) ▪ 钅波 ( 107) ▪ 钅黑 ( 108) ▪ 钅麦 ( 109) ▪ 鐽 ( 110)
▪ 錀 ( 111)  ▪ 鎶 ( 112)  ▪ 汞 ( 80)   
'''

# The Function to calculate the attributes of the molecule
def CalcMolecules(smc,amc,elemset):
    slen = len(smc)

    ss = (smc.replace('(','')).replace(')','')
    if not ss.isalnum() :
        print("Invalid molecule input")
        exit(0)

    j = 0
    elem = ''
    while (j < slen) :
        idx = j
        if elem == '' and smc[idx].isdigit():
            print("Digit unexpected") 
            exit(0)        
     
        if smc[j] != '(' :
            elem = smc[idx:idx+2]
            try:
                periodictable[elem]
                j += 2
            except:
                elem = smc[idx]
                try:
                    periodictable[elem]
                    j += 1
                except:
                    print("Invalid element input")
                    exit(0)
            
            idx = j
            while (j < slen) and (smc[j].isdigit()):
                j += 1
            if idx == j :
                elemnum = 1
            else:
                elemnum = int(smc[idx:j])
            amc.append([elem,elemnum])
            elemset.add(elem)
        else:
            j += 1
            idx = j
            while (j < slen) and (smc[j] != ')') :
                j += 1
            locsmc = smc[idx:j]
            locamc = []
            CalcMolecules(locsmc,locamc,elemset)
        
            if (smc[j] != ')') :
                print(") expected")
                exit(0)

            j += 1
            if j >= slen :
                print("Digits expected")
                exit(0)

            if not smc[j].isdigit() :
                print("Digits expected")
                exit(0)

            idx = j
            while (j < slen) and (smc[j].isdigit()) :
                j += 1

            mul = int(smc[idx:j])

            for a in locamc :
                a[1] = a[1] * mul
                amc.append(a)

def printequation(Lequmolecules,Requmolecules,y) :
    ss = ""
    equidx = 0
    for Lidx in Lequmolecules :
        if ss == "" :
            if int(round(y[equidx])) > 1 :
                ss += str(str(int(round(y[equidx]))) + Lidx)
            else :
                ss += str(Lidx)
        else :
            if int(round(y[equidx])) > 1 :
                ss += str(" + " + str(str(int(round(y[equidx]))) + Lidx))
            else :
                ss += str(" + " + Lidx)
        equidx += 1

    ss += " = "
    for Ridx in Requmolecules :
        if ss[-2] == "=" :
            if int(round(y[equidx])) > 1 :
                ss += str(str(int(round(y[equidx]))) + Ridx)
            else :
                ss += str(Ridx)
        else :
            if int(round(y[equidx])) > 1 :
                ss += str(" + " + str(str(int(round(y[equidx]))) + Ridx))
            else :
                ss += str(" + " + Ridx)
        equidx += 1

    print("The matched equation is : ",ss)
    print("\n")

def BalanceEquation() :
    # check the equation
    equlist = inputmsg.split("=")
    if len(equlist) != 2 :
        print("Invalid equation input")
        exit(0)

    # split the molecules in the equation
    Lequmolecules = [x.strip() for x in equlist[0].split("+")]
    Requmolecules = [x.strip() for x in equlist[1].split("+")]

    Lequlist = [] 
    Requlist = []
    Lelemset = set()
    Relemset = set()
    for i in Lequmolecules:
        Lmoleattr = []
        CalcMolecules(i,Lmoleattr,Lelemset)
        Lequlist.append(Lmoleattr)
    for i in Requmolecules:
        Rmoleattr = []
        CalcMolecules(i,Rmoleattr,Relemset)
        Requlist.append(Rmoleattr)

    if Lelemset != Relemset :
        print("Elements unmatched")
        exit(0)

    myfunc = []
    myresu = []
    for esidx in Lelemset :
        mypow = []
        for midx in Lequlist :
            enum = 0
            for elidx in midx :
                if esidx == elidx[0] :
                    enum += elidx[1]
            mypow.append(enum)
        for midx in Requlist :
            enum = 0 
            for elidx in midx :
                if esidx == elidx[0] :
                    enum += elidx[1]
            mypow.append(-enum)
        myfunc.append(mypow)

    tfunc = []
    for tt in myfunc :
        if tfunc != [] :
            bingo = 1
            for ff in tfunc :
                k = 0
                ab = 0
                okflag = 0
                while k < len(tt) :
                    if tt[k] != 0 and ff[k] != 0 :
                        tm = tt[k] / ff[k]
                        if ab == 0 :
                            ab = tm
                        else :
                            if ab != tm :
                                okflag = 1
                                break
                    elif (tt[k] != 0 and ff[k] == 0) or (tt[k] == 0 and ff[k] != 0 ) :
                        okflag = 1
                        break
                    k += 1
                if okflag == 0 : break
            if okflag == 1 :
                tfunc.append(tt)            
        else :
            tfunc.append(tt)

    myfunc = tfunc
    for tt in myfunc :
        myresu.append(0)

    myfunclen = len(myfunc[0])
    myresulen = len(myresu)
    while myfunclen < myresulen :
        myfunc.pop()
        myresu.pop()
        myresulen -= 1

    if len(myfunc[0]) == len(myresu) :
        myresu.pop()
        myfunc.pop()

    if len(myfunc[0]) == len(myresu) + 1 :
        for mfidx,mf in enumerate(myfunc) :
            myresu[mfidx] -= mf[len(mf)-1]
            mf.pop()
        x = np.linalg.solve(myfunc,myresu)
        y = [ Fraction(n).limit_denominator() for n in x]
        y.append(Fraction(1,1))
        ydenolist = [ n.denominator for n in y ]
        for i,yd in enumerate(ydenolist) :
            if i == 0 :
                a = yd
            else :
                b = yd
                a = a * b / gcd(a,b)
        y = [int(n*a) for n in y]
        printequation(Lequmolecules,Requmolecules,y)
    elif len(myfunc[0]) == len(myresu) + 2 :
        print("\n","More equations, you should choose the correct one")
        for i in range(10) :
            for j in range(10) :
                tempfunc = copy.deepcopy(myfunc)
                tempresu = copy.deepcopy(myresu)
                bkflag = 0
                for k,mf in enumerate(tempfunc) :
                    tempresu[k] = tempresu[k] - mf[-1] * (j+1)
                    mf.pop()
                    tempresu[k] = tempresu[k] - mf[-1] * (i+1)
                    mf.pop()
                x = np.linalg.solve(tempfunc,tempresu)
                for k in x :
                    if k != 0 :
                        bkflag = 1
                        break
                if bkflag == 1 : 
                    y = [ Fraction(n).limit_denominator() for n in x]
                    y.append(Fraction(i+1))
                    y.append(Fraction(j+1))
                    ydenolist = [ n.denominator for n in y ]
                    for k,yd in enumerate(ydenolist) :
                        if k == 0 :
                            a = yd
                        else :
                            b = yd
                            a = a * b / gcd(a,b)
                    y = [int(n*a) for n in y]
                    printequation(Lequmolecules,Requmolecules,y)
    else :
        print("Not support yet")
        exit(0)

# input the chemical equation
inputmsg = input("Please input the chemical equation : ")

while (inputmsg != "q") :
    BalanceEquation()
    inputmsg = input("Please input the chemical equation : ")