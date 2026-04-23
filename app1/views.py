from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm, LocationForm
from django.db.models import Q

# Create your views here.
@login_required
def item_list(request):
    query = request.GET.get('q')

    if query:
        items = Item.objects.filter(
            Q(name__icontains=query) |
            Q(location__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        items = Item.objects.all()

    return render(request, 'app1/item_list.html', {
        'items': items,
        'query': query
    })

@login_required
def add_location(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_item')  # go back to item form
    else:
        form = LocationForm()

    return render(request, 'app1/add_location.html', {'form': form})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()

    return render(request, 'app1/add_item.html', {'form': form})