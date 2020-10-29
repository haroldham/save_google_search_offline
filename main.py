import requests


# Returns the HTML of the Google search results
def get_google_search_results(query):

    # The Google search endpoint.
    google_url = "https://www.google.com/search"

    # 'q' is the query (i.e. search term).
    parameters = {
        "q": query
    }

    # Returns Google's HTML response to the search query.
    return requests.get(url=google_url, params=parameters).text


# Saves the Google search result HTML to a file
def save_html_to_file(html, file):

    # Saves the HTML to a file.
    with open(file, 'w') as f:
        f.write(html)


# Get HTML of the Google search result page
google_search_results_html = get_google_search_results("python")

# Save Google search result HTML to a file
save_html_to_file(html=google_search_results_html, file='saved_google_results.html')
