from django.shortcuts import render, get_object_or_404
from models.models import Locker

def locker_detail(request, locker_id):
    locker = get_object_or_404(Locker, pk=locker_id)
    compartments = locker.compartments.all()
    return render(request, 'locker_detail.html', {'locker': locker, 'compartments': compartments})
