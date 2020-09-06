import requests
import pandas as pd

# Endpoint to fetch data from
url = "https://api.usaspending.gov/api/v2/references/toptier_agencies/"
source = "From: USASpending.gov"

def fetch():
    r = requests.get(url).json()

    # Reponse is a single key dictionary with a list of nested dictionaries.
    # We are using Python 3.6 so dictionaries are still unordered. 
    # From Python 3.7 dictionaries are ordered, but as of this comment Zappa 
    # does not support Python past 3.6.
    
    ## Get list of dictionaries from first key
    results = r[list(r.keys())[0]]

    ## Get list of values for each dictionary in results
    values = [d.values() for d in results]

    ## Get the names of the columns from first nested dictionary and format them
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

    return source, table