from django.contrib import admin
from .models import Barang, Karyawan, Inventaris

# Register your models here.


class BarangAdmin(admin.ModelAdmin):
    list_display = ('kode', 'nama', 'jenis', 'keterangan')


class KarywawanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'nomor_handphone', 'alamat', 'email')


class InventarisAdmin(admin.ModelAdmin):
    list_display = ('barang', 'karyawan')


admin.site.register(Barang, BarangAdmin)
admin.site.register(Karyawan, KarywawanAdmin)
admin.site.register(Inventaris, InventarisAdmin)