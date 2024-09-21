from django.shortcuts import render


def home_view(request):

    return render(request, "r2s_app/home_page.html")