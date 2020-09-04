from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    context = {}

    if request.method == 'POST' and 'run_script' in request.POST:
        # import function to run
        from .fetch import fetch
        import pandas as pd

        # Endpoint to fetch data from
        url = 'https://api.usaspending.gov/api/v2/references/toptier_agencies/'

        # Call function
        r = fetch(url)
        results = r["results"]

        # Turn results into a DataFrame and then to HTML
        results = pd.DataFrame(results)
        table = results.to_html(index=False)
        
        # Return data on same page
        context = {
        "table":table,
        }
        return render(request, 'app/index.html', context)

    return render(request, 'app/index.html', context)

