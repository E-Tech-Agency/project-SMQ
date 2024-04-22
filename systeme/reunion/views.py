from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Meeting, Decision


from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404
from .serializers import MeetingSerializer,DecisionSerializer
from .models import*
from django.contrib.auth.decorators import login_required


# Afficher tous les Meet

@method_decorator(login_required(login_url='login'), name='dispatch')
class DashboardMeetAPIView(APIView):

    def get(self, request):
        meets = Meeting.objects.all()
        data = []
        for meet in meets:
            created_by_name = meet.created_by.first_name if meet.created_by else None
            updated_by_name = meet.updated_by.first_name if meet.updated_by else None
            created_at_str = meet.created_at.strftime('%Y-%m-%d %H:%M:%S') if meet.created_at else None
            updated_at_str = meet.updated_at.strftime('%Y-%m-%d %H:%M:%S') if meet.updated_at else None
            meet_data = {
                'id': meet.id,
                'created_by': created_by_name,
                'updated_by': updated_by_name,
                'created_at': created_at_str,
                'updated_at': updated_at_str,
            }
            data.append(meet_data)
        return Response(data, status=status.HTTP_200_OK)

# Ajouter un Meet
@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateMeetAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = MeetingSerializer(data=request.data)
        if serializer.is_valid():
            created_at = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            serializer.validated_data['created_at'] = created_at
            serializer.save(created_by=request.user)
            meet_data = serializer.data
            meet_data['created_by'] = request.user.first_name
            meet_data['created_at'] = created_at
            meet_data['id'] = serializer.instance.id 
            return Response(meet_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Modifier un Meet
@method_decorator(login_required(login_url='login'), name='dispatch')
class UpdateMeetAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def put(self, request, pk):
        meet = get_object_or_404(Meeting, pk=pk)
        serializer = MeetingSerializer(meet, data=request.data)
        if serializer.is_valid():
            updated_at = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            serializer.validated_data['updated_at'] = updated_at
            serializer.save(demandeur=request.user)
            meet_data = serializer.data
            meet_data['demandeur'] = request.user.first_name
            meet_data['updated_at'] = updated_at
            meet_data['evaluation_meet'] = serializer.instance.methode_calcul
            return Response(meet_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Afficher un Meet
@method_decorator(login_required(login_url='login'), name='dispatch')
class SingularMeetAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        meet = get_object_or_404(Meeting, pk=pk)
        serializer = MeetingSerializer(meet)
        serialized_data = serializer.data
        serialized_data['created_by'] = meet.demandeur.first_name 
        serialized_data['updated_by'] = meet.updated_by.first_name 
        serialized_data['created_at'] = meet.created_at.strftime('%Y-%m-%d %H:%M:%S') if meet.created_at else None
        serialized_data['updated_at'] = meet.updated_at.strftime('%Y-%m-%d %H:%M:%S') if meet.updated_at else None
        return Response(serialized_data)

# Supprimer un Meet
@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteMeetAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        meet = get_object_or_404(Meeting, pk=pk)
        meet.delete()
        return Response({"message": "Le fiche risk a été supprimé avec succès"}, status=status.HTTP_204_NO_CONTENT)
    

@method_decorator(login_required(login_url='login'), name='dispatch')

class MeetingMinutesAPIView(APIView):
    permission_classes = [IsAuthenticated]


    def get(self, request, meeting_id):
        try:
            meeting = Meeting.objects.get(pk=meeting_id)
            decisions = Decision.objects.filter(meeting=meeting)

            meeting_minutes = {
                'header': f"PV de Réunion - {meeting.type_reunion}",
                'date': meeting.date_previsionnelle,
                'lieu': meeting.lieu,
                'demandeur': meeting.demandeur.username,
                'participants': [participant.username for participant in meeting.participants.all()],
                'ordre_du_jour': meeting.ordre_du_jour,
                'decisions_prises': [decision.decision_text for decision in decisions]
            }

            return Response(meeting_minutes, status=status.HTTP_200_OK)
        except Meeting.DoesNotExist:
            return Response({'error': 'Réunion non trouvée'}, status=status.HTTP_404_NOT_FOUND)