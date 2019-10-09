from django.urls import path
from .views import (
    BarangListView, BarangDetailView, BarangCreateView, BarangUpdateView, BarangDeleteView,
    KaryawanListView, KaryawanDetailView, KaryawanCreateView, KaryawanUpdateView, KaryawanDeleteView,
    InventarisListView, InventarisDetailView, InventarisCreateView, InventarisUpdateView, InventarisDeleteView,
)
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Url Route Barang
    path('barang/', BarangListView.as_view(), name='barang-list'),
    path('barang/<int:pk>/', BarangDetailView.as_view(), name='barang-detail'),
    path('barang/new/', BarangCreateView.as_view(), name='barang-create'),
    path('barang/<int:pk>/update/', BarangUpdateView.as_view(), name='barang-update'),
    path('barang/<int:pk>/delete/', BarangDeleteView.as_view(), name='barang-delete'),

    # Url Route Karyawan
    path('karyawan/', KaryawanListView.as_view(), name='karyawan-list'),
    path('karyawan/<int:pk>/', KaryawanDetailView.as_view(), name='karyawan-detail'),
    path('karyawan/new/', KaryawanCreateView.as_view(), name='karyawan-create'),
    path('karyawan/<int:pk>/update/', KaryawanUpdateView.as_view(), name='karyawan-update'),
    path('karyawan/<int:pk>/delete/', KaryawanDeleteView.as_view(), name='karyawan-delete'),

    # Url Route Inventaris
    path('inventaris/', InventarisListView.as_view(), name='inventaris-list'),
    path('inventaris/<int:pk>/', InventarisDetailView.as_view(), name='inventaris-detail'),
    path('inventaris/new/', InventarisCreateView.as_view(), name='inventaris-create'),
    path('inventaris/<int:pk>/update/', InventarisUpdateView.as_view(), name='inventaris-update'),
    path('inventaris/<int:pk>/delete/', InventarisDeleteView.as_view(), name='inventaris-delete'),
    path('inventaris/report/', views.inventaris_report, name='inventaris-print'),
]
