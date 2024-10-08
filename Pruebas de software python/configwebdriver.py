from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

try:
	# Utiliza WebDriverManager para obtener el chromedriver
	service = Service(ChromeDriverManager().install())

	# Inicializa Chrome con el servicio
	driver = webdriver.Chrome(service=service)

	# Abre una página web
	driver.get("https://www.google.com")

except WebDriverException as e:
	print(f"Error al iniciar el WebDriver: {e}")

finally:
	# Cierra el navegador si está abierto
	try:
		driver.quit()
	except:
		pass
