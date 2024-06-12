from django.db import models
from django.utils import timezone

class TypeVehicule(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom

class MarqueVehicule(models.Model):
    nom = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nom

class ProprietaireVehicule(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)

    def __str__(self):
        return self.nom

class Conducteur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    permis_conduire = models.CharField(max_length=50)
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Client(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    adresse = models.TextField()
    telephone = models.CharField(max_length=20)
    piece_identite = models.CharField(max_length=100, blank=True, null=True)
    permis_conduire = models.CharField(max_length=50, blank=True, null=True)
    fichierpiece_identite = models.FileField(upload_to='documentso/',blank=True, null=True)
    fichierpermis_conduire = models.FileField(upload_to='documentsoi/',blank=True, null=True)

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class Vehicule(models.Model):
    type = models.ForeignKey(TypeVehicule, on_delete=models.SET_NULL, null=True)
    marque = models.ForeignKey(MarqueVehicule, on_delete=models.SET_NULL, null=True)
    proprietaire = models.ForeignKey(ProprietaireVehicule, on_delete=models.SET_NULL, null=True)
    particulier = models.BooleanField(default=False)
    
    modele = models.CharField(max_length=100)
    annee = models.IntegerField()
    immatriculation = models.CharField(max_length=100, unique=True)
    date_achat = models.DateField()
    kilometrage = models.IntegerField()
    carburant = models.CharField(max_length=50)
    puissance = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    
    date_assurance = models.DateField()
    date_vidange = models.DateField()

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.immatriculation})"

    def alerte_assurance(self):
        return self.date_assurance < timezone.now()

    def alerte_vidange(self):
        return self.date_vidange < timezone.now()

class TypeDocument(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class Document(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    type_document = models.ForeignKey(TypeDocument, on_delete=models.SET_NULL, null=True)
    fichier = models.FileField(upload_to='documents/')
    date_expiration = models.DateField()

    def __str__(self):
        return f"{self.type_document.nom} pour {self.vehicule}"

class Entretien(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_entretien = models.DateField()
    type_entretien = models.CharField(max_length=100)
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f"Entretien de {self.vehicule} le {self.date_entretien}"

class Consommation(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_consommation = models.DateField()
    quantite = models.DecimalField(max_digits=10, decimal_places=2)
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    kilometrage = models.IntegerField()

    def __str__(self):
        return f"Consommation de {self.vehicule} le {self.date_consommation}"

class Alerte(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    type_alerte = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()

    def __str__(self):
        return f"Alerte {self.type_alerte} pour {self.vehicule}"

class Infraction(models.Model):
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
    type_infraction = models.CharField(max_length=100)
    date_infraction = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Infraction de {self.conducteur} le {self.date_infraction}"

class Affectation(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Affectation de {self.vehicule} à {self.conducteur}"

class TypeMission(models.Model):
    nom = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nom

class Mission(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    destination = models.CharField(max_length=200)
    motif = models.TextField()
    type_mission = models.ForeignKey(TypeMission, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Mission de {self.conducteur} avec {self.vehicule} vers {self.destination}"

class Panne(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_panne = models.DateField()
    nature_panne = models.CharField(max_length=200)
    description = models.TextField()
    date_reparation = models.DateField(null=True, blank=True)
    cout_reparation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Panne de {self.vehicule} le {self.date_panne}"

class Accident(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
    date_accident = models.DateField()
    circonstances = models.TextField()
    dommages = models.TextField()
    date_reparation = models.DateField(null=True, blank=True)
    cout_reparation = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Accident de {self.vehicule} le {self.date_accident}"

class ContratLocation(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    proprietaire = models.ForeignKey(ProprietaireVehicule, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    avec_chauffeur = models.BooleanField(default=False)
    conducteur = models.ForeignKey(Conducteur, on_delete=models.SET_NULL, null=True, blank=True)
    type_mission = models.ForeignKey(TypeMission, on_delete=models.SET_NULL, null=True, blank=True)
    date_debut = models.DateField()
    date_fin = models.DateField()
    montant = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Contrat de location pour {self.vehicule} de {self.date_debut} à {self.date_fin} pour {self.client}"

class Garantie(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    piece = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    fournisseur = models.CharField(max_length=100)

    def __str__(self):
        return f"Garantie pour {self.piece} du {self.date_debut} au {self.date_fin}"

class Versement(models.Model):
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_versement = models.DateField()

    def __str__(self):
        return f"Versement de {self.conducteur} le {self.date_versement}"
