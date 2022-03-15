from facility.models import Facility
from facility.serializers import FacilitySerializer
from rest_framework import generics


class FacilityList(generics.ListCreateAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer


class FacilityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Facility.objects.all()
    serializer_class = FacilitySerializer