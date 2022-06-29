from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as bs
import requests

# Create your views here.
def index(request):
    return render(request, 'index.html')

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        # for searching we will be using web scrapping
        url = 'https://www.ask.com/web?q='+search
        response = requests.get(url)
        soup = bs(response.text, 'lxml')
        
        result_list = soup.find_all('div', {'class':'PartialSearchResults-item'})
        
        final_result = []
        
        for result in result_list:
            title = result.find(class_='PartialSearchResults-item-title').text
            res_url = result.find('a').get('href')
            res_desc = result.find(class_ = 'PartialSearchResults-item-abstract').text
            
            final_result.append((title, res_url, res_desc))
            
        context = {
            'final_result':final_result
        }
        
        return render(request, 'search.html', context)
        
    else:
        return redirect(index)
    
