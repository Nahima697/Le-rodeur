print("Le rodeur de la nuit")
print(
    "C'est Halloween, je dors profondement quand soudain à 3h du matin quelqu'un sonne à la porte, je regardes par la lorgnette et je vois un homme déguisé"
)
def security():
  print("Tu es en sécurité ici. Bien joué!")
  
def mort():
  print("Le tueur t'a trouvé, tu a été tuée. Game over")
  
def tel():
  rep = input("appeler la police ou papa")
  if (rep == "police"):
    security()
  else:
    print("Tu penses que Papa est un super héros? Trop tard")
    mort()

def alleraletage ():
  rep = input("On reste au rdc ou on cours à l'étage? rdc/étage")
  if (rep == "rdc"):
    rep=input("prendre le téléphone sur le plan de travail ou se cacher dans le placard à balai (Tel/placard")
    if(rep=="tel"):
      tel()
    elif(rep=="placard"): 
      print("prie pour ta survie")
      alleraletage()
  elif(rep == "étage"):
    rep = input("s'enfermer dans la salle de bain, sous le lit ou sauter par la fenêtre de la chambre,sdb/lit/fenêtre")
    if(rep == "sdb"):
      security()
    elif (rep == "lit"):
      print("trop facile ta cachette")
      mort()
    elif (rep == "fenêtre"):
      print("Tu t'es fais mal")
      security()


      
rep = input("ouvrir la porte? oui/non")
if (rep == "oui"):
  print("Le monsieur te poursuit dans la maison avec une hache. Tu n'as plus que tes yeux pour pleurer.")
  mort()
else:
  print("Qu'est ce qu'on fait?")
  rep = input("fermer les portes arrières et volets ou courir se cacher,fermer/ se cacher")
  if (rep == "se cacher"):
    print("Tu penses être en sécurité mais l'assassin n'est pas loin")
    print("Boum Bam Boum. Il est en train de défoncer la porte avec une hache!")
    print("Chiotte on est dans la mouise")
    alleraletage()

  else:
    tel()
