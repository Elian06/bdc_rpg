from Personnage import Personnage
from Decors import Decors
from Arme import Arme

#exemple d'utilisation de la classe Personnage

decors1 = Decors("Jungle", "Forêt tropicale", 3.55 )

arme1 = Arme("Épée légendaire", "", )

joueur1 = Personnage("Aragorn", "Guerrier", 10, 100, 15, 5)
joueur2 = Personnage("Gandalf", "Magicien", 10, 80, 5, 15)

joueur1.afficher_info()
joueur2.afficher_info()

joueur1.attaquer(joueur2)
joueur2.afficher_info()