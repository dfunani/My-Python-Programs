from django.shortcuts import render
from rest_framework.mixins import RetrieveModelMixin
from .models import Clubs
from .serializers import ClubsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class GetClub(APIView):
    def get(self, request, pk, format=None):
        club = Clubs.objects.get(pk=pk)
        serializer = ClubsSerializer(club)
        return Response(serializer.data)


class GetClubList(APIView):
    def get(self, request, format=None):
        clubs = Clubs.objects.all()
        serializer = ClubsSerializer(clubs, many=True)
        return Response(serializer.data)
