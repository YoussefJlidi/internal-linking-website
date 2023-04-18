git remote add origin https://github.com/YoussefJlidi/internal-linking-SEO.git
git branch -M main
git push -u origin main

import requests
from bs4 import BeautifulSoup
import pandas as pd
import seaborn as sns

# Get the URL of the website to analyze
url = input("Enter the URL of the website to analyze: ")

# Retrieve the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Create a dictionary to store the number of incoming links for each page
incoming_links = {}

# Retrieve all links on the site
links = soup.find_all("a")
for link in links:
    href = link.get("href")
    if href:
        # Remove any parameters from the URL
        href = href.split("?")[0]
        # Add the number of incoming links for this page
        incoming_links[href] = incoming_links.get(href, 0) + 1

# Create a Pandas dataframe from the dictionary of incoming link counts
df = pd.DataFrame(list(incoming_links.items()), columns=["Page", "Number of incoming links"])
df = df.sort_values(by="Number of incoming links", ascending=False).head(10)

# Plot a horizontal bar chart with seaborn
sns.set(style="whitegrid")
sns.barplot(x="Number of incoming links", y="Page", data=df)
sns.despine(left=True, bottom=True)
plt.title("The 10 most linked pages on {}".format(url))
plt.xlabel("Number of incoming links")
plt.ylabel("Pages of the site")
plt.show()