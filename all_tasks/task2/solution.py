import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict


def get_animal_count():
    base_url = "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    counts = defaultdict(int)
    alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'К', 'Л', 'М',
                'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш',
                'Щ', 'Э', 'Ю', 'Я']

    for letter in alphabet:
        print(f"Обрабатываем букву: {letter}")
        url = f"https://ru.wikipedia.org/wiki/Категория:{letter}"
        page_count = 0

        while url:
            response = requests.get(url)
            if response.status_code != 200:
                break
            soup = BeautifulSoup(response.text, 'html.parser')
            animal_list = soup.find('div', class_='mw-category')
            if animal_list:
                animals = animal_list.find_all('li')
                page_count += len(animals)

            next_page = soup.find('a', string='Следующая страница')
            url = f"https://ru.wikipedia.org{next_page['href']}" if next_page else None

        counts[letter] = page_count

    return counts


def write_to_csv(counts):
    with open('beasts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for letter in sorted(counts.keys()):
            writer.writerow([letter, counts[letter]])


def main():
    animal_counts = get_animal_count()
    write_to_csv(animal_counts)
    print("Результаты записаны в beasts.csv")


if __name__ == "__main__":
    main()