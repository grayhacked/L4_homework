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