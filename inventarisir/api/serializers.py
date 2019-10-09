from rest_framework import serializers
from inventarisir.models import Barang, Karyawan


# Barang Serializer
class BarangListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = '__all__'


class BarangCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barang
        fields = '__all__'


# Karyawan Serializer
class KaryawanListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karyawan
        fields = '__all__'


class KaryawanCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Karyawan
        fields = '__all__'
