def remplir(l,n):
    exam = {
            "code":str,
            "libelle":str,
            "jour":int,
            "mois":int,
            "annee":int,
            "module":str
            }
    for i in range (n):
        l.append(exam)
        print(f"#### list[{i}]")
        l[i]["code"] = input("donner le code : ")
        l[i]["libelle"] = input("donne le libelle : ")
        l[i]["jour"] = int(input("donner le jour : "))
        l[i]["mois"] = int(input("donner le mois :"))
        l[i]["annee"] = int(input("donner l'annee : "))
        l[i]["module"] = f"{l[i]['code']} ,{l[i]['libelle']}"
    return l
def SmartRemplir(l,n):
    exam = {
            "code":str,
            "libelle":str,
            "jour":int,
            "mois":int,
            "annee":int,
            "module":str
            }
    for key in range (l.keys()):
        if (key in ["code","libelle"]):
            l[i][key] = input(f"donner le {key} : ")
        elif (key in ["jour","mois","annee"]):
            l[i][key] = int(input(f"donner le {key}"))
        else :
            for j in ["jour","mois","annee"]: 
                l[i][module] += f"{l[i][{j}]}"
    
def saisir():
    n = int(input("donner n :"))
    while not(n>0):
        n = int(input("donner n :"))
    return n

def afficher(l,n):
    for i in range (n):
        print(l[i])

l = []
n = saisir()
remplir(l,n)
afficher(l,n)
