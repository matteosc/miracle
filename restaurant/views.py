from django.shortcuts import render

def home(request):
    """
    function respond to website rootHTTP request

    :param request:
    :return: index.html no db data yet
    """

    context={}
    return render(request, "restaurant/home.html", context)
