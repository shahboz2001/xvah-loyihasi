from django.shortcuts import render
from .models import *

def home(request):
    qidiruv_sozi = request.GET.get("searched")
    if qidiruv_sozi != "" and qidiruv_sozi is not None:
        t_s = Togri.objects.filter(soz=qidiruv_sozi)
        if t_s:
            n_s = Xato.objects.filter(t_soz=t_s[0])
        else:
            n_s = Xato.objects.filter(notogri=qidiruv_sozi)
            t_s = [n_s[0].t_soz]
            n_s = Xato.objects.filter(t_soz=t_s[0])
    data = {
        "togrisi": t_s[0],
        "notogrilar": n_s
    }
    return render(request, 'result.html', data)