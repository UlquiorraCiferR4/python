auto = {'Mercedes':{"model":'C190','id':2},'Audi':{"model":'A9','id':3}}
# afficher les carecteristique de le voiture Mercedes
print("les carecteristique de le voiture Mercedes sont : ",auto.values())

# afficher les carecteristique de tous les voitures dans le dict 
for car in auto.items() : 
    print("Marque : ",car[0],' , model : ',car[1]["model"],',id : ',car[1]["id"])


#how to  append to  a dict
