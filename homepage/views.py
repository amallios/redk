from django.shortcuts import render


def landing(request):
    template_name = 'homepage/landing.html'
    return render(request, template_name)
