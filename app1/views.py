from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item
from .forms import ItemForm, LocationForm
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'app1/home.html')

@login_required
def item_list(request):
    query = request.GET.get('q')

    if query:
        items = Item.objects.filter(
            Q(name__icontains=query) |
	    Q(location__name__icontains=query) |   # ✅ FIXED
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

@login_required
def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)

    return render(request, 'app1/edit_item.html', {'form': form})

@login_required
def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('item_list')

    return render(request, 'app1/confirm_delete.html', {'item': item})
