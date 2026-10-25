from selenium import webdriver

browser = webdriver.Firefox()

# browser.get("https://google.com")

# assert "Google" in browser.title

browser.get("http://localhost:8000")

assert "Congratulations!" in browser.title
print("OK")