import requests
from bs4 import BeautifulSoup

# Получает HTML-код страницы
url = "https://quotes.toscrape.com"
response = requests.get(url)

# Использует BeautifulSoup для парсинга HTML(вычитал из инета ;d)
soup = BeautifulSoup(response.text, "html.parser")

# Извлекаеn и выводиn все цитаты на странице которые найдет
quotes = soup.find_all("span", class_="text")
for quote in quotes:
    print(quote.text)
