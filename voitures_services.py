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

class Voiture:
    def __init__(self, matricule, annee, marque, kilometrage):
        self.matricule = matricule
        self.annee = annee
        self.marque = marque
        self.kilometrage = kilometrage
        self.chauffeur = None

    def afficherInformations(self):
        print("Matricule :", self.matricule)
        print("Année :", self.annee)
        print("Marque :", self.marque)
        print("Kilométrage :", self.kilometrage)
        if self.chauffeur != None:
            print("Chauffeur :", self.chauffeur.nom)
        else:
            print("Aucun chauffeur")

E1 = Employe(numeroPermis="P123", nom="Dupont", prenom="Jean")
E2 = Employe(numeroPermis="P456", nom="Martin", prenom="Claire")

V1 = Voiture(matricule="AA111", annee=2020, marque="Toyota", kilometrage=15000)
V2 = Voiture(matricule="BB222", annee=2019, marque="Honda", kilometrage=20000)
V3 = Voiture(matricule="CC333", annee=2022, marque="BMW", kilometrage=5000)

E1.afficherInformations()
E2.afficherInformations()

V1.afficherInformations()
V2.afficherInformations()
V3.afficherInformations()

E1.affecterVoiture(V1)
E2.affecterVoiture(V2)

E1.afficherInformations()
E2.afficherInformations()

E1.retirerVoiture()

E1.afficherInformations()
V1.afficherInformations()

E1.affecterVoiture(V2)