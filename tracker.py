from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with the URL of the product you want to track
product_url = "https://www.amazon.com/product/123456"

# Set up Chrome webdriver
driver = webdriver.Chrome()

# Go to the product page
driver.get(product_url)

# Wait for the price element to load
wait = WebDriverWait(driver, 10)
price_element = wait.until(EC.presence_of_element_located((By.ID, "priceblock_ourprice")))

# Get the product price
price = price_element.text

# Print the price
print(f"The current price is ${price}")

# Close the webdriver
driver.quit()
