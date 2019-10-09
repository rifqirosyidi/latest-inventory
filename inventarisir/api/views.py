from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView
)
from .serializers import (
    BarangCreateSerializer, BarangListSerializer,
    KaryawanCreateSerializer, KaryawanListSerializer
)
from inventarisir.models import Barang, Karyawan


# Barang API View
class BarangListAPIView(ListAPIView):
    queryset = Barang.objects.all()
    serializer_class = BarangListSerializer
    search_fields = ['kode', 'nama']
    filter_backends = (filters.SearchFilter,)


class BarangCreateAPIView(CreateAPIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Barang.objects.all()
    serializer_class = BarangCreateSerializer


# Karyawan API View
class KaryawanListAPIView(ListAPIView):
    queryset = Karyawan.objects.all()
    serializer_class = KaryawanListSerializer
    search_fields = ['nama']
    filter_backends = (filters.SearchFilter,)


class KaryawanCreateAPIView(CreateAPIView):

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Karyawan.objects.all()
    serializer_class = KaryawanCreateSerializer
