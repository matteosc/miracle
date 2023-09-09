from django.shortcuts import render
from utils.import_tools import import_articles, setprice
import speech_recognition
import pyttsx3




def home(request):
    """
    function respond to website rootHTTP request

    :param request:
    :return: index.html no db data yet
    """




    context={}
    return render(request, "restaurant/home.html", context)
