from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from space.models import Card
from space.forms import ContactUsForm


def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'space/inedx.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('space:index'))
    else:
        form = ContactUsForm()
    context = {
        'title': 'Свяжитесь с нами',
        'form': form,
    }
    return render(request, 'space/contact.html', context)


def museums(request):
    cards = Card.objects.filter(is_online=False)
    min_id = 0
    if len(cards) != 0:
        min_id = min([c.id for c in cards])

    context = {
        'title': 'Музеи & Планетарии',
        'cards': cards,
        'min_id': min_id,
    }
    return render(request, 'space/museums.html', context)


def onlines(request):
    cards = Card.objects.filter(is_online=True)
    min_id = min([c.id for c in cards])

    context = {
        'title': 'Онлайн Экскурсии',
        'cards': cards,
        'min_id': min_id,
    }
    return render(request, 'space/onlines.html', context)


def place(request, card_id):
    card = Card.objects.get(id=card_id)
    context = {
        'title': card.name,
        'card': card,
    }
    return render(request, 'space/place.html', context)