from bs4 import BeautifulSoup
import requests
import os
import datetime

web = 'https://www.getonbrd.com/empleos/programacion'
resultado = requests.get(web)
contenido = resultado.text

soup = BeautifulSoup(contenido, 'lxml')

contenedor = soup.find('ul', class_='sgb-results-list')

fecha_limpia = datetime.date.today()
try:
  fecha = str(fecha_limpia) + ".txt"
  archivo = open(fecha, 'x')
except:
  print("El archivo de hoy ya está creado, se creará otro")
  fecha = str(fecha_limpia) + "-2.txt"
  archivo = open(fecha, 'x')

ofertasRemotas = contenedor.find_all('div', class_='remote')
for oferta in ofertasRemotas:
  caracteristicas = oferta.find('span', class_='color-hierarchy3').get_text()
  if str(caracteristicas).startswith('Junior'):
    print("Oferta encontrada")
    try:
      titulo = oferta.find('h3', class_='gb-results-list__title').get_text()
      archivo.write(titulo + '\n')
    except:
      archivo.write("Oferta sin título\n")
    archivo.write(caracteristicas + '\n')
    enlace = oferta.find('a', class_='gb-results-list__item', href=True)
    archivo.write(str(enlace['href']) + '\n')
    fecha = oferta.find('div', class_='gb-results-list__date').get_text()
    archivo.write(fecha + '\n')
    archivo.write('----------------------------\n')

print("Fin de ofertas, cerrando.")
archivo.close()