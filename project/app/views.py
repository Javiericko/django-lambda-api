from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.

def index(request):
    context = {}

    if request.method == "POST" and "run_script" in request.POST: #using post here to avoid csrf display
        
        # import function to run
        from .fetch import fetch

        import pandas as pd

        # Endpoint to fetch data from
        url = 'https://api.usaspending.gov/api/v2/references/toptier_agencies/'

        # Call function
        # Call function to get results from the API
        r = fetch(url)
        results = r["results"]

        # Turn results into a DataFrame and then into formatted HTML
        ## Formatting is applied per column instead of globally to
        ## retain format of numeric ID column
        results = pd.DataFrame(results)

        comma_format = '{:,}'.format
        table = results.to_html(index=False)

        table = results.to_html(index=False, table_id="results-table", render_links=True,
                                formatters={
                                    "outlay_amount": comma_format,
                                    "obligated_amount": comma_format,
                                    "budget_authority_amount": comma_format,
                                    "current_total_budget_authority_amount": comma_format,
                                    "percentage_of_total_budget_authority": '{:,.2e}'.format
                                })

        # Return data on same page
        context = {
        "table":table,
        }
        return render(request, 'app/index.html', context)

    return render(request, 'app/index.html', context)

