from django.contrib import admin

from .models import (
    TypeVehicule, MarqueVehicule, ProprietaireVehicule, Conducteur, Vehicule, 
    TypeDocument, Document, Entretien, Consommation, Alerte, Infraction, 
    Affectation, Mission, Panne, Accident, ContratLocation, Garantie, Versement, Client, TypeMission
)

class TypeVehiculeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

class MarqueVehiculeAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

class ProprietaireVehiculeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'adresse', 'telephone')
    search_fields = ('nom', 'adresse', 'telephone')

class ConducteurAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'permis_conduire', 'date_naissance', 'telephone', 'adresse')
    search_fields = ('nom', 'prenom', 'permis_conduire', 'telephone')
    list_filter = ('date_naissance',)

class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('type', 'marque', 'modele', 'immatriculation', 'proprietaire', 'particulier', 'date_achat', 'kilometrage')
    search_fields = ('modele', 'immatriculation')
    list_filter = ('type', 'marque', 'date_achat', 'particulier')

class TypeDocumentAdmin(admin.ModelAdmin):
    list_display = ('nom',)
    search_fields = ('nom',)

class DocumentAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'type_document', 'date_expiration')
    search_fields = ('vehicule__immatriculation', 'type_document__nom')
    list_filter = ('date_expiration',)

class EntretienAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'date_entretien', 'type_entretien', 'cout')
    search_fields = ('vehicule__immatriculation', 'type_entretien')
    list_filter = ('date_entretien',)

class ConsommationAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'date_consommation', 'quantite', 'cout', 'kilometrage')
    search_fields = ('vehicule__immatriculation',)
    list_filter = ('date_consommation',)

class AlerteAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'type_alerte', 'date_debut', 'date_fin')
    search_fields = ('vehicule__immatriculation', 'type_alerte')
    list_filter = ('date_debut', 'date_fin')

class InfractionAdmin(admin.ModelAdmin):
    list_display = ('conducteur', 'type_infraction', 'date_infraction')
    search_fields = ('conducteur__nom', 'type_infraction')
    list_filter = ('date_infraction',)

class AffectationAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'conducteur', 'date_debut', 'date_fin')
    search_fields = ('vehicule__immatriculation', 'conducteur__nom')
    list_filter = ('date_debut', 'date_fin')

class MissionAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'conducteur', 'date_debut', 'date_fin', 'destination')
    search_fields = ('vehicule__immatriculation', 'conducteur__nom', 'destination')
    list_filter = ('date_debut', 'date_fin')

class PanneAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'date_panne', 'nature_panne', 'date_reparation', 'cout_reparation')
    search_fields = ('vehicule__immatriculation', 'nature_panne')
    list_filter = ('date_panne', 'date_reparation')

class AccidentAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'conducteur', 'date_accident', 'circonstances', 'dommages', 'date_reparation', 'cout_reparation')
    search_fields = ('vehicule__immatriculation', 'conducteur__nom', 'circonstances')
    list_filter = ('date_accident', 'date_reparation')

class ContratLocationAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'proprietaire', 'date_debut', 'date_fin', 'montant')
    search_fields = ('vehicule__immatriculation', 'proprietaire__nom')
    list_filter = ('date_debut', 'date_fin')

class GarantieAdmin(admin.ModelAdmin):
    list_display = ('vehicule', 'piece', 'date_debut', 'date_fin', 'fournisseur')
    search_fields = ('vehicule__immatriculation', 'piece', 'fournisseur')
    list_filter = ('date_debut', 'date_fin')

class VersementAdmin(admin.ModelAdmin):
    list_display = ('conducteur', 'montant', 'date_versement')
    search_fields = ('conducteur__nom',)
    list_filter = ('date_versement',)
    
class ClientAdmin(admin.ModelAdmin):
    list_display = ('nom','prenom','adresse','telephone' ,'piece_identite','permis_conduire')
    search_fields = ('nom', 'prenom', 'piece_identite', 'permis_conduire')


admin.site.register(TypeVehicule, TypeVehiculeAdmin)
admin.site.register(MarqueVehicule, MarqueVehiculeAdmin)
admin.site.register(ProprietaireVehicule, ProprietaireVehiculeAdmin)
admin.site.register(Conducteur, ConducteurAdmin)
admin.site.register(Vehicule, VehiculeAdmin)
admin.site.register(TypeDocument, TypeDocumentAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(Entretien, EntretienAdmin)
admin.site.register(Consommation, ConsommationAdmin)
admin.site.register(Alerte, AlerteAdmin)
admin.site.register(Infraction, InfractionAdmin)
admin.site.register(Affectation, AffectationAdmin)
admin.site.register(Mission, MissionAdmin)
admin.site.register(Panne, PanneAdmin)
admin.site.register(Accident, AccidentAdmin)
admin.site.register(ContratLocation, ContratLocationAdmin)
admin.site.register(Garantie, GarantieAdmin)
admin.site.register(Versement, VersementAdmin)
admin.site.register(Client, ClientAdmin)

admin.site.register(TypeMission)
