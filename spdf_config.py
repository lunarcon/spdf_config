symbol = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne', 'Na',
'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn',
'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se', 'Br', 'Kr', 'Rb', 'Sr',
'Y', 'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn', 'Sb',
'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce', 'Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd',
'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir',
'Pt', 'Au', 'Hg', 'Tl', 'Pb', 'Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th',
'Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf', 'Es', 'Fm', 'Md', 'No','Lr','Rf',
'Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Nh','Fl','Mc','Lv','Ts','Og']
lval,shl = {'s':0,'p':1,'d':2,'f':3},"spdf"
SUP= str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
def calc(z):
    lst=[2,8,8,18,18,32,32,0]
    for i in range(0,len(lst)):
        sm=0
        for g in range(0,i):
            if sm <= z:
                sm+= lst[g]
            else:
                break
        if sm >= z:
            return i
            break
while True:
    l,shls,sumn,st,sr,z = input("enter atomic number or symbol> "),["1s0"],0,[],"",1
    if l.capitalize() in symbol:
        for i in range(0,len(symbol)):
            if l.capitalize() == symbol[i]:
                z=i+1
    else:
        try:
            z = int(l)
        except:
            print("unknown element",l.capitalize())
            continue
    if z > 118 or z <= 0:
        print("out of range!")
        continue        
    for i in range(1,calc(z)+1):
        for n in range(0,len(shl)):
            if i + n > int(shls[-1][0]):
                if lval[shl[n]] + 1 <= i:
                    shls.append(str(i)+shl[n]+"0")
    for j in range(0,len(shls)-1):
        if int(shls[j][0]) + lval[shls[j][1]] > int(shls[j+1][0]) + lval[shls[j+1][1]]:
            shls[j],shls[j+1] = shls[j+1],shls[j]
    for i in range(0,len(shls)):
        for j in range(0,(2*(2*(lval[shls[i][1]])+1))):
            sumn += 1
            if sumn <= z:
                b,c = shls[i][0:2],shls[i][2]
                shls[i] = b + str(int(c)+1)
        if str(shls[i][2]) != '0':
            st.append(shls[i])
    for i in range(0,len(st)):
        st[i] = st[i][0:2] + st[i][2:len(st)].translate(SUP)
        sr+=st[i]
    try:
        sr=symbol[z-1]+" "+sr
    except:
        sr="Unknown Element "+sr
    print(sr)
