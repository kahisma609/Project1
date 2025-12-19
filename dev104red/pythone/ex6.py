# # # ex6
# # # nbr = int(input("ENTER YOUR NUMBER "))
# # # cpt=0
# # # if nbr==0:
# # #   cpt=1
# # # else:
# # #    while nbr!=0 :
# # #       nbr=nbr//10
# # #       cpt+=1
# # # print(cpt)

# # # ex7

# # sum = 0
# # cpt= 0
# # for i in range(1, 101, 2):
# #   cpt += 1
# #   sum += i
# # print(f"la somme est:{sum} le nombre des impaires est : {cpt}")


# # # ex10
# # totale = 0
# # for i in range(8):
# #   client = int(input(f"saisie le nombres des client en {i+1} heur:  "))
# #   totale += client
# # print(f"le totale des client : {totale}")

# # # ex11
# cpt=0
# cpt1=0
# cptf=0
# cpth=0
# for i in range(3):
#   sexe=input("entrer votre sexe f ou h: ")
#   if sexe == "f":
#     cptf += 1
#   else:
#     cpth +=1
    
#   age=int(input("saisie votre age: "))
#   if age < 18 :
#     cpt+=1
#   else :
#     cpt1 +=1
# print(f"le nombre de femme est : {cptf} ")
# print(f"le nombre de homme est : {cpth} ")
# print(f"le nombre de mineur est : {cpt} ")
# print(f"le nombre de majeur est : {cpt1} ")

# # # ex13
note= float(input("saisie le premier note: "))
cpt=0
sum=0
while note!= -1:
    cpt += 1
    sum += note
    note= float(input("saisie l'autre note: "))
mo = sum/cpt
if mo < 10:
    print("faaible")
elif mo>10 and mo<14:
    print("moyenne")
else:
    print("bonne")