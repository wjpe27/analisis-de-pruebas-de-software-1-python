from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar el controlador del navegador (por ejemplo, Chrome) usando WebDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
	# Abrir una página web
	driver.get("https://www.amazon.com")

	# Esperar hasta que la página se haya cargado completamente
	wait = WebDriverWait(driver, 10)
	wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

	# Pausar el script para resolver el CAPTCHA manualmente
	print("Por favor, resuelve el CAPTCHA manualmente si aparece.")
	time.sleep(30)  # Pausa de 30 segundos para resolver el CAPTCHA

	# Verificar si el elemento está dentro de un iframe
	iframes = driver.find_elements(By.TAG_NAME, "iframe")
	for iframe in iframes:
		driver.switch_to.frame(iframe)
		try:
			search_box = driver.find_element(By.ID, "twotabsearchtextbox")
			break
		except:
			driver.switch_to.default_content()
	else:
		# Si no se encuentra en ningún iframe, buscar en el contexto principal
		search_box = wait.until(EC.presence_of_element_located((By.ID, "twotabsearchtextbox")))

	# Realizar una búsqueda
	search_box.send_keys("laptop")
	search_box.submit()

	# Verificar si los resultados de la búsqueda contienen la palabra "laptop"
	wait.until(EC.title_contains("laptop"))

	# Pausar el script para visualizar los resultados
	print("Búsqueda realizada. Visualizando los resultados...")
	time.sleep(30)  # Pausa de 30 segundos para visualizar los resultados

finally:
	# Cerrar el navegador
	driver.quit()