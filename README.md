## Automatización de SAUCEDEMO.COM

Proyecto automatización con Selenium y Chrome de la web SAUCEDEMO.COM

# Autor: Mario Alejandro Rotella
# Comisión: 26142

## Tecnologías

- Python 3.12
- Selenium
- WebDriver Manager

# Instalación
pip install -r requirements.txt

# Ejecución pruebas
python3 -m pytest .\tests\test_saucedemo.py -v --html=reporte.html

### Pruebas individuales
- python3 -m pytest -m login -v
- python3 -m pytest -m catalogo -v 
- python3 -m pytest -m carrito -v
- python3 -m pytest -m menu -v
