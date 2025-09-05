import requests

# Base URL
url = "https://rickandmortyapi.com/api/character"

# Request API data
response = requests.get(url)
data = response.json()

# Start HTML structure
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rick and Morty Characters</title>
</head>
<body>
"""

for char in data["results"]: 
    html_content +=f"""
    <h1><strong>{char['name']}</strong></h1>
    <table> 
        <tr>
            <th> <img src="{char['image']}" width = "100" alt="{char['name']}"></th>
            <th><p><strong>Species:</strong> {char['species']}</p>     
            <p><strong>Status:</strong> {char['status']}</p>
            <p><strong>Origin:</strong> {char['origin']['name']}</p> 
        </tr>
    </table>
# End character cards


html_content += """

"""
# End HTML structure

# Write to HTML file
with open("rick_and_morty.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("HTML file created: rick_and_morty_strong.html")

