class Decors:
    def __initialize__(self, nom, categorie, poids):
        self.nom = nom
        self.categorie = categorie
        self.poids = poids
        
    
    def afficher_info_decors(self):
        print(f"Nom : {self.nom}")
        print(f"Catégorie : {self.categorie}")
        print(f"Poids : {self.poids}")
        
        pass