from django.shortcuts import render, redirect
from useri.models import Profil
from clienti.models import Client, Masina
from staff.models import Staff
from django.db.models import Q

def main(request):
    template = 'parkproject/main.html'
    title = 'Parcarea Zimbru'
    context = {
        'titlu': title,
    }
    response = render(request, template, context)
    return response


def search(request):
    template = 'parcare/parcare.html'
    search_profil = request.GET.get('search')
    if search_profil:
        profil = Profil.objects.filter(Q(user__username__icontains=search_profil) | Q(nume__icontains=search_profil) | Q(prenume__icontains=search_profil))
        client = Client.objects.filter(Q(profil__user__username__icontains=search_profil) | Q(profil__nume__icontains=search_profil) | Q(profil__prenume__icontains=search_profil))
        staff = Staff.objects.filter(Q(profil__user__username__icontains=search_profil) | Q(profil__nume__icontains=search_profil) | Q(profil__prenume__icontains=search_profil))
        masina = Masina.objects.filter(Q(profil__in=Profil.objects.filter(
                                            Q(user__username__icontains=search_profil) | 
                                            Q(nume__icontains=search_profil) | 
                                            Q(prenume__icontains=search_profil))))
        context = {
            'profil': profil, 'client': client, 'staff': staff, 'masina': masina,
        }
        return render(request, template, context)
    else:
        return redirect('parcare:parcare')
