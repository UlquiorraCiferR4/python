list = list(range(1,100))
target = int(input("donner le nombre a chercher : "))
begin = 0
end = len(list)
while not(end<begin ):
    index = int((end+begin)/2)
    if (list[index]==target):
        break
    elif (target > list[index]):
        begin = begin +1
    else:
        end = end - 1
if (end<begin):
    print("not found !")
else :
    print("found")
