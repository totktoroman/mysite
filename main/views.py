from django.shortcuts import render

import requests
from bs4 import BeautifulSoup
# Create your views here.
def homePageView(request):
    return render(request, 'main/main.html')
def about(request):
    return render(request, 'main/about.html')
