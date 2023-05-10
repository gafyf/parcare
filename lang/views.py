from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.translation import get_language, activate, gettext
from staff.models import Staff
from clienti.models import Masina

def lang(request):
    trans = translate(language='en')
    staff = Staff.objects.all()
    masina = Masina.objects.all()
    print('asta e', masina)
    print('asta e', staff)
    return render(request, 'lang.html', {'trans': trans, 'masina': masina, 'staff': staff})

def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = gettext('Traducere text')
    finally:
        activate(cur_language)
    return text