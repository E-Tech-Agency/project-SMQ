from django.db import models
from django.contrib.auth.models import User
from action.models import ActionPrincipale
from RH.modelsRH.models2 import Participant

class type(models.Model):
    nom = models.CharField(max_length=255) 

    def __str__(self):
        return self.nom


class Meeting(models.Model):
    
    demandeur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='demandeur_reunion', limit_choices_to={'groups__name': 'Employe'})
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='reunion_updated', null=True)
    created_at = models.DateTimeField(null=True, default=None)
    updated_at = models.DateTimeField(null=True, default=None)
    date_previsionnelle = models.DateField()
    TYPES = [
        ('Team Meeting', 'Team Meeting'),
        ('Client Meeting', 'Client Meeting'),
        ('Project Meeting', 'Project Meeting'),
        ('One-on-One', 'One-on-One'),
        ('Brainstorming', 'Brainstorming'),
    ]
    type_reunion = models.CharField(max_length=50, choices=TYPES,default=None)
    lieu = models.CharField(max_length=100)
    ordre_du_jour = models.TextField()
    participants = models.ManyToManyField(Participant, related_name='meetings_attended')
    piece_jointe = models.FileField(upload_to='meeting_attachments/', blank=True, null=True)
    commentaire = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Réunion demandée par {self.demandeur.first_name} le {self.date_previsionnelle}"
    

class Decision(models.Model):
    meeting = models.ForeignKey(Meeting ,on_delete=models.CASCADE,null=True)
    decision_text = models.TextField()  
    action_prise = models.ForeignKey(ActionPrincipale,on_delete=models.CASCADE)

    def __str__(self):
        return self.decision_text
