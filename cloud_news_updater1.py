import requests
from datetime import datetime

API_KEY = "YOUR_GNEWS_API_KEY"
MAX_ARTICLES = 5

query = (
    "AWS OR Azure OR GCP "
    "site:aws.amazon.com OR site:azure.microsoft.com OR site:cloud.google.com "
    "OR site:timesofindia.indiatimes.com OR site:livemint.com"
)

url = f"https://gnews.io/api/v4/search?q={query}&lang=en&max={MAX_ARTICLES}&token={API_KEY}"

response = requests.get(url)
data = response.json()
articles = data.get("articles", [])

markdown = "## ☁️ Latest Cloud & DevOps News\n\n"
for article in articles:
    title = article["title"]
    link = article["url"]
    source = article.get("source", {}).get("name", "")
    markdown += f"- [{title}]({link}) - _{source}_\n"

markdown += f"\n*Last updated: {datetime.now().strftime('%d %b %Y, %H:%M IST')}*"

# Update README
with open("README.md", "r") as f:
    readme = f.read()

start_marker = "<!-- CLOUD_NEWS_START -->"
end_marker = "<!-- CLOUD_NEWS_END -->"

start = readme.find(start_marker)
end = readme.find(end_marker) + len(end_marker)

new_readme = readme[:start] + start_marker + "\n" + markdown + "\n" + readme[end:]

with open("README.md", "w") as f:
    f.write(new_readme)

print("✅ README updated with latest cloud news!")
