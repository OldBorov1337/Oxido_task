import requests
import json
import os
from dotenv import load_dotenv 


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

openai_url = "https://api.openai.com/v1/chat/completions"

def read(*, filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        return file.read()

def gen_html_openai(*, article_text: str) -> str:
    prompt = (
        "Przekształć tekst tego artykułu do formatu HTML. Użyj odpowiednich znaczników, aby uporządkować tekst."
        " Wstaw znaczniki <img src='image_placeholder.jpg' alt='Opis obrazu'/> w miejscach, w których Twoim zdaniem"
        " powinien zostać umieszczony obraz. Dodaj podpis do obrazu za pomocą znacznika <figcaption>."
        " Nie dodawaj CSS и JavaScript. Umieść tylko код HTML помиędzy <body> и </body>."
        " ale bez samych znaczników <body>."
        "\n\nArtykuł:\n" + article_text
    )

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5
    }

    response = requests.post(openai_url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_data = response.json()
        gen_html = response_data["choices"][0]["message"]["content"]
        return gen_html
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None

def html_save(*, filename: str, html_content: str):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)

# Zadanie для dla chętnych
def create_for_szablon(*, file_tem: str, file_out: str, article: str):
    with open(file_tem, "r", encoding="utf-8") as file:
        html_tem = file.read()

    done_html = html_tem.replace(
        "<body>",
        f"<body>{article}"
    )

    with open(file_out, "w", encoding="utf-8") as file:
        file.write(done_html)

def main():
    article_text = read(filename="plik_do_pobrania.txt")
    gen_html = gen_html_openai(article_text=article_text)

    if gen_html:
        html_save(filename="artykul.html", html_content=gen_html)
        print("HTML successfully loaded in artykul.html")

        create_for_szablon(file_tem="szablon.html", file_out="podglad.html", article=gen_html)
        print("Full preview successfully created in podglad.html")
    else:
        print("Error: can't load HTML")

if __name__ == "__main__":
    main()
