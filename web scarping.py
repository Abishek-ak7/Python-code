import requests

# Send a GET request to the website
url = "https://www.samsung.com/in/offer/online/samsung-fest/mobiles/"
response = requests.get(url)

# Get the HTML content of the response
html_content = response.content

# Print the HTML code
print(html_content)
