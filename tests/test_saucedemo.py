import pytest
from utils.helpers import login
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.login
def test_login(driver):
    login(driver, "standard_user", "secret_sauce")
    
    assert "inventory.html" in driver.current_url

    title = driver.find_element(By.CLASS_NAME, "title").text #chequea que esté el texto al agregar .text
    assert title == "Products"

@pytest.mark.catalogo
def test_catalogo_productos(driver):
    login(driver, "standard_user", "secret_sauce")
    
    title = driver.find_element(By.CLASS_NAME, "title").text #chequea que esté el texto al agregar .text
    assert title == "Products"


    # validar productos
    productos = driver.find_elements(By.CSS_SELECTOR, "[data-test='inventory-item']")
    #el CCS_SELECTOR captura cualquier tipo de etiqueta, que no esté definida

    assert len(productos) > 0 #chequea que haya algo mayor a cero y valida que tenga productos
    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    assert nombre == "Sauce Labs Backpack"

@pytest.mark.carrito
def test_agregar_al_carrito(driver):
    login(driver, "standard_user", "secret_sauce")
    wait = WebDriverWait(driver, 10)
    

    nombre_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name").text

    #agregar producto, voy a buscar cualquier boton que diga "add to cart"
    bnt_add = wait.until(
        EC.element_to_be_clickable((By.XPATH,"//button[contains(text(),'Add to cart')]"))
    )
    bnt_add.click()

    #validar contador de agregado al carrito
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert badge.text == "1"

    driver.find_element(By.CLASS_NAME,"shopping_cart_link").click()

    #validar productos dentro del carrito
    producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_carrito == nombre_producto

@pytest.mark.menu
def test_check_menu(driver):

    login(driver, "standard_user", "secret_sauce")

    wait = WebDriverWait(driver, 10)

    # abrir menú
    driver.find_element(By.ID, "react-burger-menu-btn").click()

    # esperar menú visible
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "bm-menu"))
    )

    # items esperados
    menu_items = {
        "inventory_sidebar_link": "All Items",
        "about_sidebar_link": "About",
        "logout_sidebar_link": "Logout",
        "reset_sidebar_link": "Reset App State"
    }

    # recorrer y validar
    for element_id, expected_text in menu_items.items():

        element = wait.until(
            EC.visibility_of_element_located((By.ID, element_id))
        )

        assert element.text == expected_text

