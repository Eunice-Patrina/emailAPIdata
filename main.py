import requests
from send_email import send_email

api_key = "890603a55bfa47048e4490069ebee18c"
url = "https://newsapi.org/v2/everything?q=tesla&" \
      "sortBy=publishedAt&apiKey=" \
      "890603a55bfa47048e4490069ebee18c"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

message = " "

# Access the article titles and description
for article in content["articles"]:
    message += article["title"] + "\n" + article["description"] + 2*"\n"
    #print(article["title"])
    #print(article["description"])

message = message.encode("utf-8")
send_email(message)
