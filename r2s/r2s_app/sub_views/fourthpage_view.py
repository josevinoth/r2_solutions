from django.shortcuts import render


def fourth_page_view(request):

    return render(request, "r2s_app/fourth_page.html")