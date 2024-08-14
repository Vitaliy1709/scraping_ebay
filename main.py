import requests
from bs4 import BeautifulSoup
import json
from fake_useragent import UserAgent


def get_page_content(url):
    userAgent = UserAgent()
    headers = {
        'User-Agent': userAgent.random
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")
        return None


def parse_json_ld(content):
    soup = BeautifulSoup(content, "html.parser")
    json_ld_scripts = soup.find_all("script", type="application/ld+json")

    if len(json_ld_scripts) > 1:
        json_ld_content = json.loads(json_ld_scripts[1].string)
        return json_ld_content.get("about", {}).get("offers", {}).get("itemOffered", [])
    else:
        print("JSON-LD script not found.")
        return None


def save_products_to_file(products, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for product in products:
            name = product.get("name")
            url = product.get("url")
            image = product.get("image")
            price = product.get("offers", {}).get("price")
            price_currency = product.get("offers", {}).get("priceCurrency")
            rating_value = product.get("aggregateRating", {}).get("ratingValue", "N/A")
            review_count = product.get("aggregateRating", {}).get("reviewCount", "N/A")

            file.write(f"Name: {name}\n")
            file.write(f"URL: {url}\n")
            file.write(f"Image: {image}\n")
            file.write(f"Price: {price} {price_currency}\n")
            file.write(f"Rating: {rating_value}\n")
            file.write(f"Review Count: {review_count}\n")
            file.write("=" * 50 + "\n")


def main():
    url = "https://www.ebay.com/b/Motorcycle-Scooter-Parts-Accessories-with-Vintage-Part/10063/bn_562672"
    content = get_page_content(url)

    if content:
        products = parse_json_ld(content)
        if products:
            filename = "products.txt"
            save_products_to_file(products, filename)
            print(f"Products have been saved to {filename}")
        else:
            print("No products found.")
    else:
        print("Failed to retrieve content.")


if __name__ == "__main__":
    main()
