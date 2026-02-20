# le chiffrement de César :
"""
>>> ord("A")
65
>>> ord("Z")
90
>>> ord("a")
97
>>> ord("z")
122
"""
def césar (ch,c):
    res = ""
    for i in range (len(ch)):
        rank = ord(ch[i])
        rank +=  c
        # if (ch[i].islower() and chr(rank)>"z") or (ch[i].isupper() and chr(rank)>"Z"):
        if (ch[i].upper()>="Z"): 
            rank -= 26
        res += chr(rank)
        return res              

txt = input("donner un text a crypter : ")
c = int(input("donner le decalage : "))
print(césar(txt,c))
