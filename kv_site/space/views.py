from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from space.models import Place, Category
from django.db.models import Q


def index(request):
    places = Place.objects.all()
    context = {
        'title': 'Главная',
        'places': places,
    }

    return render(request, 'space/index.html', context)


def category(request, category_name):
    category = Category.objects.get(cname=category_name)

    category_places = Place.objects.filter(category=category)

    print(category)
    context = {
        'title': category.name,
        'places': category_places,
    } 

    return render(request, 'space/category.html', context)


def place(request, place_id):
    place = Place.objects.get(id=place_id)

    context = {
        'title': place.name,
        'place': place,
    }
    return render(request, 'space/place.html', context)


@login_required
def rate(request, place_id):
    place = Place.objects.get(id=place_id)

    rate_value = int(request.POST.get('rate'))
    current_rate = place.rate
    new_rate = float(current_rate + rate_value) / 2

    place.rate = new_rate
    place.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])