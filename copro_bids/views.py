from django.shortcuts import render

from .models import Project, Bid, Teammate


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'copro_bids/project_list.html', {'projects': projects})


def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'copro_bids/project_form.html', {'form': form})


def project_edit(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            project = form.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'copro_bids/project_form.html', {'form': form})


def teammate_create(request):
    if request.method == 'POST':
        form = TeammateForm(request.POST)
        if form.is_valid():
            teammate = form.save()
            return redirect('teammate_detail', pk=teammate.pk)


def teammate_list(request):
    teammates = Teammate.objects.all()
    return render(request, 'copro_bids/teammate_list.html', {'teammates': teammates})


def teammate_detail(request, pk):
    teammate = Teammate.objects.get(id=pk)
    return render(request, 'copro_bids/teammate_detail.html', {'teammate': teammate})


def teammate_edit(request, pk):
    teammate = Teammate.objects.get(pk=pk)
    if request.method == 'POST':
        form = TeammateForm(request.POST, instance=teammate)
        if form.is_valid():
            teammate = form.save()
            return redirect('teammate_detail', pk=teammate.pk)
    else:
        form = TeammateForm(instance=teammate)
    return render(request, 'copro_bids/teammate_form.html', {'form': form})


def teammate_delete(request, pk):
    teammate = Teammate.objects.get(id=pk)
    return redirect('teammate_list')


def bid_create(request):
    if request.method == 'POST':
        form = BidForm(request.POST)
        if form.is_valid():
            bid = form.save()
            return redirect('bid_detail', pk=song.pk)


def bid_detail(request, pk):
    bid = Bid.objects.get(id=pk)
    return render(request, 'copro_bids/bid_detail.html', {'bid': bid})


def bid_edit(request, pk):
    bid = Bid.objects.get(pk=pk)
    if request.method == 'POST':
        bid = BidForm(request.POST, instance=bid)
        if form.is_valid():
            project = form.save()
            return redirect('bid_detail', pk=song.pk)
    else:
        form = BidForm(instance=bid)
    return render(request, 'copro_bids/bid_form.html', {'form': form})
