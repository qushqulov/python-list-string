
emaillar = "ali@gmail.com,vali@mail.ru,karim@gmail.com"
ro_yxat = emaillar.split(",")
domenlar = []

for e in ro_yxat:
    domen = "@" + e.split("@")[1]
    if domen not in domenlar: 
        domenlar.append(domen)

print(domenlar)
