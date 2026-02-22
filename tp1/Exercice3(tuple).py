MOIS = (
    ("janvier",31),
    ("fevrier",28),
    ("mars",31),
    ("avril",30),
    ("mai",31),
    ("juin",30),
    ("juillet",31),
    ("aout",31),
    ("septembre",30),
    ("octouber",31),
    ("novembre",30),
    ("decembre",31)
)
jours = int(input("donner le nombre des jours : "))
s = 0
month = -1
while (jours>s):
    month +=1
    s +=  MOIS[month][1] 
    
print(f"the month that passes {jours} est {MOIS[month][0]}")

