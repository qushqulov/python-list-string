
gap = "olol radar makka non"
sozlar = gap.split()
palindromlar = []

for s in sozlar:
    if s == s[::-1]:
        palindromlar.append(s)

print(palindromlar)
