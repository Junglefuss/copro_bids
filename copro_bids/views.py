from django.shortcuts import render

from .models import Project, Bid, Teammate


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'copro_bids/project_list.html', {'projects': projects})
