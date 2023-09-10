from django.shortcuts import render

def mainpage(request):
    # You can add your view logic here
    # For example, you can retrieve data from models or perform other actions
    # Then, you can pass data to a template and render it
    
    context = {
        'message': 'Find whats New!',
    }
    
    return render(request, 'mainpage.html', context)

def itemlist(request):
  
    
    context = {
        'message': 'Find whats New!',
    }
    
    return render(request, 'itemlist.html', context)

def getstarted(request):
    # Define the context dictionary with data you want to pass to the template
    context = {
        'message': 'get started',  # Replace with your actual data
    }
    
    # Render the 'getstarted.html' template with the provided context
    return render(request, 'getstarted.html', context)