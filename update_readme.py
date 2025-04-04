import re
from scholarly import scholarly

# 🔹 Your Google Scholar name (ensure it's unique enough)
SCHOLAR_NAME = "Your Name"  # Change this to your Scholar profile name

def get_citation_count():
    """Fetch citation count from Google Scholar"""
    search_query = scholarly.search_author(SCHOLAR_NAME)
    author = next(search_query)  # Get first result
    author = scholarly.fill(author)  # Fetch full details
    return author.get("citedby", "N/A")  # Get citations count

def update_readme(citations):
    """Update README.md with the latest citation count"""
    with open("README.md", "r+", encoding="utf-8") as f:
        content = f.read()
        updated_content = re.sub(
            r"📚 Citations: \*\*(\d+)\*\*", 
            f"📚 Citations: **{citations}**", 
            content
        )
        f.seek(0)
        f.write(updated_content)
        f.truncate()

if __name__ == "__main__":
    citation_count = get_citation_count()
    print(f"Updating README with {citation_count} citations...")
    update_readme(citation_count)
