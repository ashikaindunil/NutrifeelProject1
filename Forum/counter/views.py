from django.shortcuts import render
# rK4rdAPamyplSpSxAw2srw==lIdANJ7P5l08Vehp
# Create your views here.
# def home(request):
#     return render(request,'home1.html')

# Create your views here.
def Nhome(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'rK4rdAPamyplSpSxAw2srw==lIdANJ7P5l08Vehp'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home1.html', {'api': api})
    else:
        return render(request, 'home1.html', {'query': 'Enter a valid query'})
