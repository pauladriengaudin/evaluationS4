#le jeu des alumettes
import random
regle=int(input("pour avoir les regles du jeu, tappez 1, tapez un autre chiffre pour continuer : "))
if regle==1:
  print("vous pouvez enlever entre 1 et 3 allumettes par tour, le joueur qui enlève la dernière a perdu")
n=0
while n<9:
  n=int(input("entrez le nombre d'allumettes voulu (supérieur à 10) : "))
j=1
while n>0:
  print("")
  print("joueur",j)
  if j==1:
    a=0
    while a>3 or a<1:
      a=int(input("choisissez une nombre d'allumettes à enlever : "))
    n=n-a
    j=j+1
  elif j==2:
    r=(n-1)%4
    if r>0 :
      b=r
      print("joueur 2 enleve",b,"allumettes")
    else :
      b=random.randint(1,3)
      print("joueur 2 enleve",b,"allumettes")
    n=n-b
    j=j-1
  if n>0:
    print("il reste",n,"allumettes")
print("gagné joueur",j)
