from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    context = {}

    if request.method == "POST" and "run_script" in request.POST: #using post here to avoid csrf display
        
        # Import function to run
        from .commands.fetch import fetch

        # Call function to get results from the API
        source, table = fetch()

        # Return data on same page
        context = {
        "table":table,
        "source":source
        }
        return render(request, 'app/index.html', context)

    return render(request, 'app/index.html', context)

