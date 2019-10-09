import csv
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Barang, Karyawan, Inventaris
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView
)

from .forms import KaryawanCreateForm, KaryawanUpdateForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


class BarangListView(LoginRequiredMixin, ListView):
    model = Barang
    context_object_name = 'list_barang'


class BarangDetailView(LoginRequiredMixin, DetailView):
    model = Barang
    context_object_name = 'barang'


class BarangCreateView(LoginRequiredMixin, CreateView):
    model = Barang
    fields = '__all__'


class BarangUpdateView(LoginRequiredMixin, UpdateView):
    model = Barang
    fields = '__all__'


class BarangDeleteView(LoginRequiredMixin, DeleteView):
    model = Barang
    success_url = '/barang'


# Karyawan Views Templates
class KaryawanListView(LoginRequiredMixin, ListView):
    model = Karyawan
    context_object_name = 'list_karyawan'


class KaryawanDetailView(LoginRequiredMixin, DetailView):
    model = Karyawan
    context_object_name = 'karyawan'


class KaryawanCreateView(LoginRequiredMixin, FormView):
    template_name = 'inventarisir/karyawan_form.html'
    form_class = KaryawanCreateForm
    success_url = '/karyawan'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class KaryawanUpdateView(LoginRequiredMixin, UpdateView):
    model = Karyawan
    success_url = '/karyawan'
    form_class = KaryawanUpdateForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class KaryawanDeleteView(LoginRequiredMixin, DeleteView):
    model = Karyawan
    success_url = '/karyawan'


# Inventaris Views Templates
class InventarisListView(LoginRequiredMixin, ListView):
    model = Inventaris
    context_object_name = 'list_inventaris'


class InventarisDetailView(LoginRequiredMixin, DetailView):
    model = Inventaris
    context_object_name = 'inventaris'


class InventarisCreateView(LoginRequiredMixin, CreateView):
    model = Inventaris
    fields = '__all__'


class InventarisUpdateView(LoginRequiredMixin, UpdateView):
    model = Inventaris
    fields = '__all__'


class InventarisDeleteView(LoginRequiredMixin, DeleteView):
    model = Inventaris
    success_url = '/inventaris'


def inventaris_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Inventaris_Report.csv"'

    query_set = Inventaris.objects.all()

    output = []

    for row in query_set:
        output.append([
            row.karyawan.nama,
            row.barang.nama
        ])

    writer = csv.writer(response)
    writer.writerow(['Nama Karyawan', 'Nama Barang'])
    # CSV Data
    writer.writerows(output)

    return response

