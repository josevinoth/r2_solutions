from django.shortcuts import render


def first_page_view(request):

    return render(request, "r2s_app/first_page.html")