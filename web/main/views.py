from django.shortcuts import render
from .models import *
import random
# Create your views here.


questions = ["Автор", "Название", "Количество (text)", 'Адрес доставки (text)',
             'Способ доставки', 'Способ оплаты', 'Дополнительные пожелания', 'Ознакомлен с условиями доставки']

titles = {
    'main': 'Main',
    'reg': 'Регистрация',
    'grid': 'Таблицы',
    'regist': 'Регистрация',
    'orderForm': 'Форма заказа',
}

header_activ = {
    "activ": 'nav-link px-2 link-secondary',
    "nonactive": 'nav-link px-2 link-dark'
}

b1 = Book.objects.get(pk=1)
b2 = Book.objects.get(pk=2)
b3 = Book.objects.get(pk=3)
b4 = Book.objects.get(pk=4)


def main(request):
    ran = random.randint(1, 4)
    post = Book.objects.get(pk=ran)
    posts = Book.objects.all()
    return render(request, 'main/main.html', {"questions": questions, 'title': titles['main'],
                                              'activ': header_activ['activ'],
                                              'nonactiv': header_activ['nonactive'],
                                              'post': post,
                                              'posts': posts,

                                              })


def sec(request):
    return render(request, 'main/sec.html', {'title': titles['grid']})


def th(request):
    return render(request, 'main/th.html', {'title': titles['grid']})


def four(request):
    return render(request, 'main/four.html', {'title': titles['grid']})


def grid(request):
    return render(request, 'main/grids.html', {'title': titles['grid'],
                                               'activ': header_activ['activ'],
                                               'nonactiv': header_activ['nonactive']
                                               })


def reg(request):
    return render(request, 'main/reg.html', {'title': titles['regist'],
                                             'activ': header_activ['activ'],
                                             'nonactiv': header_activ['nonactive']
                                             })


def ank(request):
    return render(request, 'main/ank.html')


def getOrderForm(request):
    ran = random.randint(1, 4)
    post = Book.objects.get(pk=ran)
    return render(request, 'main/order_form.html', {'title': titles['orderForm'], 'post': post})


def getVideo(request):
    return render(request, 'main/video.html')


def get_book1(request):
    return render(request, 'main/book.html', {"book": b1})


def get_book2(request):
    return render(request, 'main/book.html', {"book": b2})


def get_book3(request):
    return render(request, 'main/book.html', {"book": b3})

def get_book4(request):
    return render(request, 'main/book.html', {"book": b4})