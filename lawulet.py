from random import randrange

#input from users and save with pickle
surname=input("Antre epsedow pa mete espas ni let majiskil : ")
while " " in surname or surname.islower()==False:
    surname=input("Dezole ou mete espas oubyen let majiskil, re mete epsedo a: ")
print("*******************************")
print(f"{surname.upper()} Byenvini nan jwet la wulet la ",end="\n*******************************\n")
    
#ask the user for the magic number
magic_number=randrange(0,5)

luck=5 #luck variable
for i in range(luck):
    user_number=int(input("Antre yon nomb ant 0 et 5 : "))
    while user_number<0 or user_number>5:
        user_number=int(input("Ou antre yon nomb ki pa nan enteval la, re antre yon lot nomb: "))

    if(user_number>magic_number):
        luck-=1
        print(f"Ou antre yon nomb ki pi gwo ke nomb majik la. ou rete {luck} chans.")
    elif(user_number<magic_number):
        luck-=1
        print(f"Ou antre yon nomb ki pi piti ke nomb majik la. Ou rete {luck} chans.")
    else:
        print("Bravo ou jwenn nomb majik la!!")
        break
    if luck==0:
        print(f"Ou pedi!! Nomb majik la se {magic_number} ")
        break