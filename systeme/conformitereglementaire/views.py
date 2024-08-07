from django.http import FileResponse
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from rest_framework import status
from .serializers import *
from .models import*
from django.contrib.auth.decorators import login_required


def get_piece_jointe_conformite(request, client_id):
    client = get_object_or_404(ExigenceReglementaire, id=client_id)
    piece_jointe_path = client.pieces_jointes.path
    return FileResponse(open(piece_jointe_path, 'rb'), content_type='application/pdf')
# Afficher tous les Exigences

@method_decorator(login_required(login_url='login'), name='dispatch')
class DashboardExigenceAPIView(APIView):

    def get(self, request):
        risques = ExigenceReglementaire.objects.all()
        data = []
        for risk in risques:
            created_by_name = risk.created_by.first_name if risk.created_by else None
            updated_by_name = risk.updated_by.first_name if risk.updated_by else None
            created_at_str = risk.created_at.strftime('%Y-%m-%d %H:%M:%S') if risk.created_at else None
            updated_at_str = risk.updated_at.strftime('%Y-%m-%d %H:%M:%S') if risk.updated_at else None
            risk_data = {
                'id': risk.id,
                'nom': risk.nom,
                'type_fiche': risk.type_fiche,
                'source': risk.source.designation,
                'type_decideur': risk.type_decideur,
                'exigence_dec': risk.exigence_dec,
                'created_by': created_by_name,
                'updated_by': updated_by_name,
                'created_at': created_at_str,
                'updated_at': updated_at_str,
            }
            if risk.exigence_dec:
                risk_data.update({
                    'nom_reglementation':risk.nom_reglementation,
                    'applicable':risk.applicable,
                    'plan_action':risk.plan_action.nom_action if risk.plan_action else None,
                    'pieces_jointes':risk.pieces_jointes.url if risk.pieces_jointes else None,
                })
            data.append(risk_data)
        return Response(data, status=status.HTTP_200_OK)

# Ajouter un Exigences
@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateExigenceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FicheExigenceReglementaireSerializer(data=request.data)
        if serializer.is_valid():
            created_at = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            serializer.validated_data['created_at'] = created_at
            serializer.save(created_by=request.user)
            risk_data = serializer.data
            risk_data['created_by'] = request.user.first_name
            risk_data['created_at'] = created_at
            return Response(risk_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Modifier un Exigences
@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateExigenceAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, pk):
        risk = get_object_or_404(ExigenceReglementaire, pk=pk)
        serializer = FicheExigenceReglementaireSerializer(risk, data=request.data)
        if serializer.is_valid():
            updated_at = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            serializer.validated_data['updated_at'] = updated_at
            serializer.save(updated_by=request.user)
            risk_data = serializer.data
            risk_data['updated_by'] = request.user.first_name
            risk_data['updated_at'] = updated_at
            return Response(risk_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Afficher un Exigences
@method_decorator(login_required(login_url='login'), name='dispatch')
class SingularExigenceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        risk = get_object_or_404(ExigenceReglementaire, pk=pk)
        serializer = FicheExigenceReglementaireSerializer(risk)
        serialized_data = serializer.data
        serialized_data['created_by'] = risk.created_by.first_name 
        serialized_data['updated_by'] = risk.updated_by.first_name if risk.updated_by else None
        serialized_data['created_at'] = risk.created_at.strftime('%Y-%m-%d %H:%M:%S') 
        serialized_data['updated_at'] = risk.updated_at.strftime('%Y-%m-%d %H:%M:%S') if risk.updated_at else None
        return Response(serialized_data)

# Supprimer un Exigences
@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteExigenceAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        fiche_risk = get_object_or_404(ExigenceReglementaire, pk=pk)
        fiche_risk.delete()
        return Response({"message": "Le fiche Exigence reglementaire a été supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)