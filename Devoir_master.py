'''
    MASTER STR (index, split, replace, lower, upper, title)
'''
# 1. Nan yon chenn karaktè, mete tout karaktè yo an miniskil.
chen="Jean Duckens SANNON"
print("1-- ",chen.lower(),end="\n\n")

# 2. Nan yon chenn karaktè, koupe chenn nan tout kote ki gen espas. Epi afiche yon lis ki gen chak eleman yo. Ekzanp: "Ayibobo Ayiti"  => ["Ayibobo", "Ayiti"]
chen="Ayibobo Ayiti"
print("2-- ",chen.split(),end="\n\n")


# 3. Nan yon chenn karaktè, mete tout premye lèt chak mo an majiskil.
chen="jean duckens sannon"
print("3-- ",chen.title(),end="\n\n")

#4 Nan yon chenn karaktè, rekipere premye lèt chak mo. Epi afiche yon nouvo chenn ak tout inisyal sa yo. Ekzanp: "Ayibobo Ayiti"  => "AA"
chen="Ayibobo Ayiti se pa nou"
chen=chen.split()
print("4-- ",end="")
for i in chen:
    print(i[0],end="")
print("\n")
    
#5 Ranplase tout karaktè "a" ki nan yon chenn pa "@".
chen="robertoagmail.com"
print("5-- ",end="")
for i in chen:
    if i=="a":
        print("@",end="")
    else:
        print(i,end="")
print("\n")

#6 Mete yon chenn karaktè devan dèyè, answit mete l an majiskil. Ekzanp: "Ayiti"  => "ITIYA"
chen="Ayiti"
chen=chen[::-1]
print("6-- ",chen.upper(),end="\n\n")

#7 Afiche endeks premye karaktè "a" ki nan yon chenn. Ekzanp:   "Ayiti kapab avanse" =>  7
chen="Ayiti kapab avanse"
print("7-- ",chen.index("a"),end="\n\n")

#8 Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil). Ekzanp:  "Ayiti kapab avanse" =>  42
chen="Ayiti kapab avanse"
a=0
for i in range(len(chen)):
    if chen[i]=="a" or chen[i]=="A":
        a+=i
print("8-- ",a,end="\n\n")

#9 Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil). Ekzanp:  "Ayiti kapab avanse" =>  [7,9,12,14]
chen="Ayiti kapab avanse"
a=[]
for i in range(len(chen)):
    if chen[i]=="a":
        a.append(i)
print("9-- ",a,end="\n\n")

#10 Retire tout espas ki nan yon chenn, epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo).
chen="Ayiti kapab avanse"
chen=chen.replace(" ", "")
print("10-- ",chen,end="\n\n")
