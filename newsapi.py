import json
import requests

API_KEY = "8bb6b5be10b94056a36693f09b331359"
URL = "https://newsapi.org/v2/everything"

params = {
    "q": "technology",  # Искать новости по ключевому слову
    "language": "en",  # Язык новостей
    "sortBy": "publishedAt",  # Сортировка по дате публикации
    "pageSize": 3,  # Количество новостей в ответе
    "apiKey": API_KEY  # API-ключ
}

response = requests.get(URL, params=params)

data = response.json()
articles = data.get("articles", [])

for i, article in enumerate(articles, 1):
    print(f"{i}. {article['title']}")
    print(f"   Источник: {article['source']['name']}")
    print(f"   Опубликовано: {article['publishedAt']}")
    print(f"   Ссылка: {article['url']}\n")

with open("news_data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Новости сохранены в файл news_data.json")