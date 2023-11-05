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
chen="Ayibobo Ayiti"
print("4-- ",chen[0]+chen[7],end="\n\n")