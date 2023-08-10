from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML file
with open("Amazon.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all div elements with class "a-section a-spacing-small a-spacing-top-small"
product_divs = soup.find_all("div", class_="a-section a-spacing-small a-spacing-top-small")

# Initialize empty lists to store product names and prices
product_names = []
product_prices = []

# Loop through each product div and extract the product name and price
for div in product_divs:
    # Find the span element with class "a-size-medium a-color-base a-text-normal" for the product name
    product_name_span = div.find("span", class_="a-size-medium a-color-base a-text-normal")
    product_name = product_name_span.get_text(strip=True) if product_name_span else " "

    # Find the span element with class "a-price-whole" for the product price
    product_price_span = div.find("span", class_="a-price-whole")
    product_price = product_price_span.get_text(strip=True) if product_price_span else " "

    # Append the product name and price to the respective lists
    product_names.append(product_name)
    product_prices.append(product_price)

# Create a DataFrame from the lists
data = {
    "Product Name": product_names,
    "Product Price": product_prices
}
df = pd.DataFrame(data)

# Write the DataFrame to an Excel file
output_file = "amazon_products.xlsx"
df.to_excel(output_file, index=False)

print(f"Data written to {output_file}")
