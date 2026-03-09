class Employe:

    def __init__(self, numeroPermis, nom, prenom):
        self.numeroPermis = numeroPermis
        self.nom = nom
        self.prenom = prenom
        self.voitureService = None

    def afficherInformations(self):
        print("Permis :", self.numeroPermis)
        print("Nom :", self.nom)
        print("Prenom :", self.prenom)
        if self.voitureService != None:
            print("Voiture :", self.voitureService.matricule)
        else:
            print("Aucune voiture assignée")

    def affecterVoiture(self, voiture):
        if self.voitureService != None:
            print("Cet employé a déjà une voiture")
            return
        if voiture.chauffeur != None:
            print("Cette voiture est déjà assignée")
            return
        self.voitureService = voiture
        voiture.chauffeur = self
        print("Voiture assignée")

    def retirerVoiture(self):
        if self.voitureService == None:
            print("Aucune voiture à retirer")
            return
        self.voitureService.chauffeur = None
        self.voitureService = None
        print("Voiture retirée")