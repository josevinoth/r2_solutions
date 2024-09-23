from django.shortcuts import render


def third_page_view(request):

    return render(request, "r2s_app/third_page.html")