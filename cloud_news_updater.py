import requests
from datetime import datetime

# === API Setup ===
API_KEY = "YOUR_GNEWS_API_KEY"  # Free tier available
query = "AWS OR Azure OR GCP site:timesofindia.indiatimes.com OR site:livemint.com"
url = f"https://gnews.io/api/v4/search?q={query}&lang=en&max=5&token={API_KEY}"

response = requests.get(url).json()
articles = response.get("articles", [])

# === Prepare Markdown ===
markdown = "## ☁️ Latest Cloud & DevOps News\n\n"
for article in articles:
    title = article["title"]
    link = article["url"]
    markdown += f"- [{title}]({link})\n"

markdown += f"\n*Last updated: {datetime.now().strftime('%d %b %Y, %H:%M IST')}*"

# === Write to README ===
with open("README.md", "r") as f:
    readme = f.read()

# Replace previous news block (between markers)
start_marker = "<!-- CLOUD_NEWS_START -->"
end_marker = "<!-- CLOUD_NEWS_END -->"

start = readme.find(start_marker)
end = readme.find(end_marker) + len(end_marker)

if start != -1 and end != -1:
    new_readme = readme[:start] + start_marker + "\n" + markdown + "\n" + readme[end:]
else:
    new_readme = readme + f"\n{start_marker}\n{markdown}\n{end_marker}\n"

with open("README.md", "w") as f:
    f.write(new_readme)
