#Question 1
def sup21(x):
  if x>=21:
    reponse=True
  else:
    reponse=False
  print(reponse)

sup21(2)

#Question 2
def pairs(l):
  rep=[]
  for i in l:
    if i%2==0:
      rep.append(i)
  print(rep)

pairs([1,2,3])

#question 3
def ajout4(l):
  list4=l
  list4.append(4)
  print(list4)

ajout4([])

#question 4
def to_strings(d):
  l=[]
  for i in d:
    x=i
    y=d[i]
    x=str(x)
    y=str(y)
    s=x,':',y
    s = "".join(s)
    l.append(s)
  print(l)

to_strings({1:2,2:3,3:4})

#question 5
def extremites(l):
  x=len(l)
  rep=[]
  for i in 0,1:
    rep.append(l[i])
  for i in x-2,x-1:
    rep.append(l[i])
  print(rep)

extremites(['a', 'b', 'c', 'd', 'e'])

#question 6

#question 7
def tri_et_inverse(l):
  rev=[]
  for i in reversed(l):
    rev.append(i)
  tri=sorted(l)
  print(tri,rev)

tri_et_inverse([2,1,3])

#question 8

#question 9
ville_nom_pays={'Paris':'France', 'Berlin':'Allemagne', 'Madrid':'Espagne' , 'Moscou':'Russie'}

to_strings(ville_nom_pays)
