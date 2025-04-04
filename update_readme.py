import requests
import os
import re

API_KEY = os.getenv("SERPAPI_KEY")  # Fetch API key from GitHub Secrets
AUTHOR_ID = "KKS2dsQAAAAJ"  # Replace with your Google Scholar ID

def get_citation_count():
    """Fetch citation count from SerpAPI"""
    url = f"https://serpapi.com/search.json?engine=google_scholar_author&author_id={AUTHOR_ID}&api_key={API_KEY}"
    
    response = requests.get(url).json()
    citations = response["cited_by"]["table"][0]["citations"]
    h_index = response["cited_by"]["table"][1]["h_index"]
    i10_index = response["cited_by"]["table"][2]["i10_index"]

    return citations, h_index, i10_index

def update_readme(citations, h_index, i10_index):
    """Update README.md with the latest citation stats"""
    with open("README.md", "r+", encoding="utf-8") as f:
        content = f.read()
        updated_content = re.sub(r"📊 Citations: \*\*(\d+)\*\*", f"📊 Citations: **{citations}**", content)
        updated_content = re.sub(r"📈 h-index: \*\*(\d+)\*\*", f"📈 h-index: **{h_index}**", updated_content)
        updated_content = re.sub(r"🏅 i10-index: \*\*(\d+)\*\*", f"🏅 i10-index: **{i10_index}**", updated_content)

        f.seek(0)
        f.write(updated_content)
        f.truncate()

if __name__ == "__main__":
    citations, h_index, i10_index = get_citation_count()
    print(f"Updating README with Citations: {citations}, h-index: {h_index}, i10-index: {i10_index}")
    update_readme(citations, h_index, i10_index)
