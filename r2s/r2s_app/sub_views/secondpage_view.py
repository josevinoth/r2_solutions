from django.shortcuts import render


def second_page_view(request):

    return render(request, "r2s_app/second_page.html")