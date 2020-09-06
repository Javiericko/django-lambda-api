from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    context = {}

    if request.method == "POST" and "run_script" in request.POST: #using post here to avoid csrf display
        
        # Import function to run
        from .commands.fetch import fetch

        import pandas as pd

        # Endpoint to fetch data from
        url = "https://api.usaspending.gov/api/v2/references/toptier_agencies/"
        source = "From: USASpending.gov"

        # Call function to get results from the API
        r = fetch(url)
        results = r["results"]
        values = [d.values() for d in results]

        # Get the names of the columns and format them
        keys = results[0].keys()
        columns = [i.replace('_', ' ').title() for i in keys]

        # Turn results into a DataFrame and then into formatted HTML
        ## Formatting is applied per column instead of globally to
        ## retain format of numeric ID column
        results = pd.DataFrame(values, columns=columns)

        comma_format = '{:,}'.format
        table = results.to_html(index=False, table_id="results-table", render_links=True, classes="table table-striped table-bordered",
                                formatters={
                                    "Outlay Amount": comma_format,
                                    "Obligated Amount": comma_format,
                                    "Budget Authority Amount": comma_format,
                                    "Current Total Budget Authority Amount": comma_format,
                                    "Percentage Of Total Budget Authority": '{:,.2e}'.format
                                })

        # Return data on same page
        context = {
        "table":table,
        "source":source
        }
        return render(request, 'app/index.html', context)

    return render(request, 'app/index.html', context)

