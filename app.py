from flask import Flask, render_template, request
from duckduckgo_search import DDGS

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    search_results = []
    query = ""

    if request.method == "POST":
        query = request.form.get("query", "")
        if query:
            # Use DuckDuckGo search to get results
            try:
                with DDGS() as ddgs:
                    search_results = list(ddgs.text(query, max_results=3))
            except Exception as e:
                search_results = [
                    {"title": "Error", "body": f"Search error: {str(e)}", "href": "#"}
                ]

    return render_template("index.html", results=search_results, query=query)


if __name__ == "__main__":
    app.run(debug=True, port=5008, host="0.0.0.0", use_reloader=False)
