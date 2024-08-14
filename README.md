# eBay Products Scraper

Этот проект является простым веб-скраппером, который извлекает информацию о продуктах с определенной страницы
eBay и сохраняет ее в текстовый файл.

## Описание

Скрипт загружает содержимое веб-страницы, ищет JSON-LD скрипт, парсит его, извлекает информацию о продуктах
и сохраняет полученные данные в файл `products.txt`.

### Используемые технологии

- `requests`: для загрузки содержимого веб-страницы.
- `BeautifulSoup`: для парсинга HTML-кода.
- `json`: для работы с данными в формате JSON.
- `fake_useragent`: для генерации случайных заголовков User-Agent, чтобы избежать блокировок со стороны веб-сайтов.

## Установка

1. Клонируйте репозиторий или загрузите файлы.
2. Убедитесь, что у вас установлен Python 3.11 или выше.
3. Установите зависимости, используя файл `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Использование

1. Запустите скрипт:

    ```bash
    python main.py
    ```

2. Скрипт скачает страницу, извлечет данные о продуктах и сохранит их в файл `products.txt`.

## Файлы

- `main.py`: основной скрипт, содержащий весь код.
- `products.txt`: файл, куда будут сохранены данные о продуктах.
- `requirements.txt`: файл, содержащий список всех необходимых зависимостей.

## Пример содержания `products.txt`

Файл `products.txt` будет содержать информацию о продуктах в следующем формате:

Name: HONDA CARBURETOR C70 CT70 ATC70 ASSY STANDARD PART PLUG & PLAY 
URL: https://www.ebay.com/...
Image: https://i.ebayimg.com/thumbs/images/g/....jpg
Price: 61.00 USD
Rating: 3.5
Review Count: 3