from rest_framework.views import APIView
from .models import Clubs
from .serializers import clubSerializer, matchSerializer
from rest_framework.response import Response
from django.http import Http404
import datetime
import json


class ClubsViewSet(APIView):
    queryset = Clubs.objects.all()

    def get(self, request, format=None):
        clubs = Clubs.objects.all()
        serializer = clubSerializer(clubs, many=True)
        return Response(serializer.data)


class ClubResultsView(APIView):
    queryset = Clubs.objects.all()

    def get_object(self, pk):
        try:
            return Clubs.objects.get(pk=pk)
        except Clubs.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        club = self.get_object(pk)
        serializer = matchSerializer(club)
        result = []
        for res in serializer.data['matches']:
            result.append(serializer.data['matches'][res]) if datetime.date.fromisoformat(
                serializer.data['matches'][res]['match_start'].split(" ")[0]) <= datetime.date.today() else None
        result.sort(
            key=lambda a: a['match_start'])
        return Response(result[-5:])


class ClubFixturesView(APIView):
    queryset = Clubs.objects.all()

    def get_object(self, pk):
        try:
            return Clubs.objects.get(pk=pk)
        except Clubs.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        club = self.get_object(pk)
        serializer = matchSerializer(club)
        result = []
        for res in serializer.data['matches']:
            result.append(serializer.data['matches'][res]) if datetime.date.fromisoformat(
                serializer.data['matches'][res]['match_start'].split(" ")[0]) > datetime.date.today() else None
        result.sort(
            key=lambda a: a['match_start'])
        return Response(result[0:5])
