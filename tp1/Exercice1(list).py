list1 = [17,38,10,25,72]

#list1 = []
#n = int(input("donner le nombre des entiers : "))
#while(n<0):
#    n = int(input("donner le nombre des entiers : "))

#for i in range (n):
#    var = int(input(f"donner la case {i+1} : "))
#    list1.append(var)
n = len(list1)

###################### trier une list ; #############################
for i in  range (len(list1)):
    for j in range (len(list1)):
        if (list1[i]>list1[j]):
            aux = list1[i]
            list1[i] = list1[j]
            list1[j] = aux

##################### adding element to  list #######################
print(list1)
list1.append(12)
print("element 12 added to 12")
##################### Reverse Element ###############################
list1 = list1[::-1]
list1.reverse()
print(list1)
##################### index of element in list ######################
for i in range (len(list1)):
    if (list1[i] == 17):
        print(f"element 17 at index {i}")
print(list1)
# la fonction predefinie
print(list1.index(17))
##################### Remove element from list ######################

list1 = [12,17,38,10,25,72]
list1.remove(38)  # not the index of the Element but the  element !! 
print(list1)

#################------ Show sub list ---------#####################

print(list1[1:3]) # to show two element remember that the second index of the list  is not going to  be shown that's why we didn't use list1[1:2] 


# to show the last two elements : 
print(list1[-2:])

#---------------- indesert element at a specific index : ----------##
list1.insert(3,10)
#         index,val
print(list1)
#------------- pop : remove the last element from the list --------##
list1.pop()
print(list1)

#---------------sum  of a list elements ---------------------------##
print(f"La Somme de tous les element de la list est : {sum(list1)}")

#--------------- suppremer l'element de 3eme indice
list1.pop(3)
print(list1)
