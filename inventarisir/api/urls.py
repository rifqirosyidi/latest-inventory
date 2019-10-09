from django.urls import path
from .views import (
    BarangCreateAPIView, BarangListAPIView,
    KaryawanCreateAPIView, KaryawanListAPIView
)
app_name = 'api-inventaris'
urlpatterns = [
    # Barang API
    path('barang/', BarangListAPIView.as_view(), name='barang-list'),
    path('barang/create/', BarangCreateAPIView.as_view(), name='barang-create'),

    # Karyawan API
    path('karyawan/', KaryawanListAPIView.as_view(), name='karyawan-list'),
    path('karyawan/create/', KaryawanCreateAPIView.as_view(), name='karyawan-create'),
]
