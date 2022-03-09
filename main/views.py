from django.shortcuts import render
from .forms import CalcForm, RandForm
from .services import solve_equation, get_color


def index(request):
    return render(request, 'main/index.html')


def page1(request):

    if request.method == 'POST':
        form = CalcForm(request.POST)
        if form.is_valid():
            a = int(form.cleaned_data['a'])
            b = int(form.cleaned_data['b'])
            c = int(form.cleaned_data['c'])
            ans = solve_equation(a, b, c)
            return render(request, 'main/page1.html', {'form': form, 'ans': ans})
    else:
        form = CalcForm()
    return render(request, 'main/page1.html', {'form': form})


def page2(request):

    if request.method == 'POST':
        form = RandForm(request.POST)
        if form.is_valid():
            ans = get_color()
            return render(request, 'main/page2.html', {'form': form, 'ans': ans})
    else:
        form = RandForm()
    return render(request, 'main/page2.html', {'form': form})