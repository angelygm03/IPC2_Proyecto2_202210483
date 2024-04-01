import xml.etree.ElementTree as ET
from maqueta import Maqueta
from lista_maquetas import ListaMaquetas

def leer_archivo_xml(ruta):
    lista_maquetas = ListaMaquetas()
    tree = ET.parse(ruta)
    root = tree.getroot()
    for maqueta in root.findall('./maquetas/maqueta'):
        nombre = maqueta.find('nombre').text
        filas = int(maqueta.find('filas').text)
        columnas = int(maqueta.find('columnas').text)
        entrada = (int(maqueta.find('entrada/fila').text), int(maqueta.find('entrada/columna').text))
        objetivos = []
        for objetivo in maqueta.findall('objetivos/objetivo'):
            nombre_objetivo = objetivo.find('nombre').text
            fila_objetivo = int(objetivo.find('fila').text)
            columna_objetivo = int(objetivo.find('columna').text)
            objetivos.append((nombre_objetivo, fila_objetivo, columna_objetivo))
        estructura = maqueta.find('estructura').text.strip()
        maqueta_obj = Maqueta(nombre, filas, columnas, entrada, objetivos, estructura)
        for obj_nombre, obj_fila, obj_columna in objetivos:
            maqueta_obj.agregar_objetivo(obj_nombre, obj_fila, obj_columna)
        lista_maquetas.agregar_maq(maqueta_obj)
    return lista_maquetas

