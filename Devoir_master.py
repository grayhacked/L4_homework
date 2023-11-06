'''
    MASTER STR (index, split, replace, lower, upper, title)
'''
print("\tMASTER STR (index, split, replace, lower, upper, title)\n")
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

#6 Mete yon chnn kareaktè devan dèyè, answit mete l an majiskil. Ekzanp: "Ayiti"  => "ITIYA"
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

'''
    MASTER LIST (Union & Intersection & Lis comprehension)
'''
print("\tMASTER LIST (Union & Intersection & Lis comprehension)\n")

#1 Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
n=10
lis=[]
for i in range(n+1):
    if i%2==0:
        lis.append(i)
print("1-- ",lis,end="\n\n")

#2 Ou gen yon lis antye, konvèti l an yon lis chenn.
lis=[1,2,3,4,5,6,7,8,9]
for i in range(len(lis)):
    lis[i]=str(lis[i])
print("2-- ",lis,end="\n\n")

#3 Ou gen yon lis chenn ki an miniskil, konvèti an yon lis chenn majiskil
lis=["jean","duckens","sannon"]
for i in range(len(lis)):
    lis[i]=lis[i].upper()
print("3-- ",lis,end="\n\n")

#4 Ou gen yon lis, kreye yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
lis=[1,2,3,4,5,6,7,8,9]
lis2=[]
for i in range(len(lis)):
    if i%3==0:
        lis2.append(lis[i])
print("4-- ",lis2,end="\n\n")

#5 Ou gen lis eleman, kreye yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl. Ekzanp: [1,2,3,4,5,6,7,8,9] => [(1,2,3), (4,5,6), (7,8,9)]
lis=[1,2,3,4,5,6,7,8,9]
lis2=[]
for i in range(0,len(lis),3):
    lis2.append((lis[i],lis[i+1],lis[i+2]))
print("5-- ",lis2,end="\n\n")

#6 Ou gen yon lis, ki gen yon pakèt eleman ki repete. Konvèti l an yon lis, ki pa gen okenn doublon.
lis=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6]
lis2=[]
for i in lis:
    if i not in lis2:
        lis2.append(i)
print("6-- ",lis2,end="\n\n")

#7 Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis yo.
lis1=[1,2,3,4,5,6,7,8,9]
lis2=[2,4,9,10,11,12,13,14,15]
lis3=[]
for i in lis1:
    if i in lis2:
        lis3.append(i)
print("7-- ",lis3,end="\n\n")

#8 Ou gen 2 lis. Kreye yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.
list1=[1,2,3,4,5,6,7,8,9]
list2=[2,4,9,10,11,12,13,14,15]
list3=[]
for i in list1:
    if i not in list2:
        list3.append(i) 
for i in list2:
    if i not in list1:
        list3.append(i) 
print("8-- ",list3,end="\n\n")

#9 Ou gen yon diksyonè. Kreye yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman.
dic={"nom":"SANNON","prenom":"Jean Duckens","age":25,"sexe":"Masculin"}
lis1=[]
lis2=[]
for i in dic:
    lis1.append(i)
    lis2.append(dic[i])
print("9-- ",lis1)
print("    ",lis2,end="\n\n")

#10 Reyini 3 lis ansanm, san okenn doublon.
list1=[1,2,3,4,5,6,7,8,9]
list2=[2,4,9,10,11,12,13,14,15]
list3=[1,2,3,4,5,6,7,8,9]
list4=[]
for i in list1:
    if i not in list4:
        list4.append(i)
for i in list2:
    if i not in list4:
        list4.append(i)
for i in list3:
    if i not in list4:
        list4.append(i)
print("10-- ",list4,end="\n\n")


'''
    MASTER DICTIONNAIRE (isinstance, eval)
'''
print("\tMASTER DICTIONNAIRE (isinstance, eval)\n")

#1 Ou gen yon diksyonè. Rekipere tout valè yo, gras ak kle yo epi retounen yon lis valè.
dic={"nom":"SANNON","prenom":"Jean Duckens","age":25,"sexe":"Masculin"}
lis=[]
for i in dic:
    lis.append(dic[i])
print("1-- ",lis,end="\n\n")

#2 Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
user=input("2-- Tape yon valè: ")

if user.startswith("{") and user.endswith("}"):
    print("Ou gen akolad devan ak dèyè")
else:
    print("Ou pa gen akolad devan ak dèyè")
print("\n")

#3 Pakouri yon diksyonè, epi afiche tout kle yo.
dic={"nom":"SANNON","prenom":"Jean Duckens","age":25,"sexe":"Masculin"}
print("3-- ",dic.keys(),end="\n\n")

#4 Pakouri yon diksyonè, epi afiche tout valè yo.
dic={"nom":"SANNON","prenom":"Jean Duckens","age":25,"sexe":"Masculin"}
print("4-- ",dic.values(),end="\n\n")

#5 Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
dic={"nom":"SANNON","prenom":"Jean Duckens","age":25,"sexe":"Masculin"}
dic2={}
for i in dic:
    dic2[i]=dic[i]
print("5-- ",dic2,end="\n\n")

#6 Anndan yon diksyonè ki gen kle ak valè(valè yo ka nenpòt tip done). Ajoute yon underscore devan ak dèyè tout valè ki se chenn yo. Ekzanp: {"name": "Lub", "age": 14, "assets": ["laptop", "phone"]} -> {"name": "_Lub_", "age": 14, "assets": ["laptop", "phone"]}
dic={"nom":"SANNON","prenom":"Jean Duckens","age":25,"sexe":"Masculin"}
for i in dic:
    if isinstance(dic[i],str):
        dic[i]="_"+dic[i]+"_"
print("6-- ",dic,end="\n\n")

#7 Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman. Ekzanp: {"a": "12", "b": "abc", "c": "12r", "d":"90"} ->{"a": "12", "d":"90"}
dic={"a": "12", "b": "abc", "c": "12r", "d":"90"}
dic2={}
for i in dic:
    if dic[i].isdigit():
        dic2[i]=dic[i]
print("7-- ",dic2,end="\n\n")

#8 Pakouri yon disksyonè, pou w mete l sou fòm lis, kote chak eleman nan disksyonè sa, vin sou fòm tipl(kle, valè) anndan lis la. Ekzanp: {"a":1, "b": 2} ->[("a",1), ("b",2)]
dic={"a":1, "b": 2}
lis=[]
for i in dic:
    lis.append((i,dic[i]))
print("8-- ",lis,end="\n\n")

#9 Pakouri yon lis tipl, pou w mete l sou fòm diksyonè. Ekzanp: [("a",1), ("b",2)] -> {"a":1, "b": 2}
lis=[("a",1), ("b",2)]
dic={}
for i in lis:
    dic[i[0]]=i[1]
print("9-- ",dic,end="\n\n")

#10 Kole 2 diksyonè ansanm pou fè youn, kote si gen eleman ki gen menm kle ap konkatene valè, swivan kondisyon sa yo: - Antye: ADISYON -Chenn, lis, set: KONKATENASYON Rès eleman ki pa gen valè ki gen tip sa yo, pap nan nouvo diksyonè a.
dic1={"nom":"SANNON","prenom":"Jean Duckens","age":25,"sexe":"Masculin"}
dic2={"nom":"SANNON","prenom":"Jean Duckens","age":25,"sexe":"Masculin"}
dic3={}
for i in dic1:
    if type(dic1[i])==int:
        dic3[i]=dic1[i]+dic2[i]
    elif type(dic1[i])==str or type(dic1[i])==list or type(dic1[i])==set:
        dic3[i]=dic1[i]+dic2[i]
print("10-- ",dic3,end="\n\n")

'''
    MASTER FUNCTION CONCEPT
'''

print("\tMASTER FUNCTION CONCEPT\n")

#1 kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.
def env(mo):
    return mo[::-1]
print("1-- ",env("Ayiti kapab avanse"),end="\n\n")

#2 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik.
def kod(n):
    import random
    import string
    return "".join(random.choices(string.ascii_letters,k=n))
print("2-- ",kod(5),end="\n\n")

#3 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon.
def kod(n):
    import random
    import string
    return "".join(random.sample(string.ascii_letters,k=n))
print("3-- ",kod(5),end="\n\n")

#4 kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.
def kod(n):
    import random
    import string
    return "".join(random.sample(string.ascii_letters+string.digits,k=n))
print("4-- ",kod(5),end="\n\n")

#5 Ou gen yon lis chenn. Jenere yon SLUG apati chenn nan. Nan yon SLUG, tout karaktè ki akseptab yo se: alfanimerik ak "-"
def slug(chenn):
    import re
    return re.sub(r"\W+","-",chenn)
print("5-- ",slug("Ayiti kapab avanse"),end="\n\n")

#6 Kreye yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil
def separe(mo,symbol_vigil):
    return symbol_vigil.join(mo)
print("6-- ",separe("Ayiti kapab avanse",","),end="\n\n")

#7 Kreye yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè. ekzanp: "ALO" -> "0-11-14"
def kripte(mo):
    import string
    lis=[]
    for i in mo:
        lis.append(string.ascii_lowercase.index(i))
    return "-".join(str(i) for i in lis)
print("7-- ",kripte("alo"),end="\n\n")

#8 Kreye yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè. ekzanp: "0-11-14" -> "ALO"
def dekripte(mo):
    import string
    lis=mo.split("-")
    return "".join(string.ascii_lowercase[int(i)] for i in lis)
print("8-- ",dekripte("0-11-14"),end="\n\n")

#9 Kreye yon fonksyon ki ap pran 2 paramèt, epi ki pèmite valè yo. Answit li retounen tou 2 valè yo sou fòm Tuple.
def permut(a,b):
    return (b,a)
print("9-- ",permut(2,3),end="\n\n")

#10 Kreye yon fonksyon ki ap pran yon non an paramèt, epi ki retounen inisyal yo. Atansyon ak non konpoze ak tirè yo. ekzanp: "Jean-Baptiste Jean" -> "JBJ"
def inisyal(nom):
    import re
    lis=re.split(r"\W+",nom)
    return "".join(i[0] for i in lis)
print("10-- ",inisyal("Jean-Baptiste Jean"),end="\n\n")