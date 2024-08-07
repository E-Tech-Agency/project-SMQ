from rest_framework import serializers
from ..modelsRH.models2 import *

class ResponsableFormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponsableFormation
        fields = ['id','nom', 'prenom', 'username', 'email', 'pieces_jointes','is_user']


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = ['id','nom', 'prenom', 'username', 'email' ,'pieces_jointes', 'employe','is_user','formations_concernees']


class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ['id','nom', 'prenom', 'username', 'email', 'pieces_jointes','is_user']

class FormationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formation
        fields = ['id','intitule_formation','statut','type_formation', 'organisme_formation', 'theme_formation','date_debut_formation','date_fin_formation', 'responsable_validation','responsable_formation', 'participants', 'pieces_jointes', 'parametre_validation', 'date_cloture']
        
