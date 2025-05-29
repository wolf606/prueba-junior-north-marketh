# Prueba de ingreso - Desarrollador Junior North Marketh

**Autor:** Luis Miguel Sanchez Pinilla

Este repositorio contiene la solución a tres ejercicios propuestos para la prueba de ingreso al cargo de Desarrollador Junior en North Marketh. Cada ejercicio aborda un nivel diferente de dificultad y utiliza distintas herramientas del ecosistema Python.

## 1. Scrapping Instagram

La API de Instagram le pone marcas a las cuentas y las bloquea si detecta scrapping. Tambien le pone marcas a los numeros de telefono y emails de las cuentas usadas al hacer scrapping. Las cuenatas del ejercicio contienen demasiados seguidores para hacer scrapping.

[Link Text](https://youtu.be/g5U48-J6Ugg)

---

## 1. Ejercicio básico de Python (Nivel Principiante)

**Propósito:**  
Crear una función llamada `numero_mas_frecuente(lista)` que reciba una lista de números enteros y devuelva el número que más veces se repite. Si hay más de uno con la misma frecuencia, devuelve el menor de ellos.

**Solución:**  
El archivo [`punto1.py`](punto1.py) implementa la función y contiene pruebas automáticas para verificar su correcto funcionamiento.

**Cómo ejecutar:**
```sh
python punto1.py
```
Si todo está correcto, verás el mensaje:  
`Todos los tests pasaron`

---

## 2. Automatización con scraping (Nivel Intermedio)

**Propósito:**  
Crear un script en Python que tome una palabra clave de búsqueda, ingrese a Mercado Libre Colombia, y extraiga los títulos y precios de los primeros 5 productos que coincidan. Permite cambiar fácilmente la palabra clave.

**Solución:**  
El archivo [`punto2.py`](punto2.py) realiza el scraping usando la librería estándar de Python y muestra los resultados en consola.

**Cómo ejecutar:**
```sh
python punto2.py <categoria_busqueda> <palabra_filtrar>
```
**Ejemplo:**
```sh
python punto2.py celular Samsung
```
Esto buscará los primeros 5 productos de la categoría "celular" que contengan la palabra "Samsung".

---

## 3. Consumo de API con interfaz y autenticación (Nivel Intermedio/Avanzado)

**Propósito:**  
Crear una aplicación gráfica en Python que muestre una ventana de login, valide el usuario contra una base de datos SQLite y, si el login es exitoso, muestre información obtenida de una API pública (Rick and Morty).

**Solución:**  
El archivo [`punto3.py`](punto3.py) implementa la interfaz gráfica con Tkinter, la autenticación con SQLite y el consumo de la API de Rick and Morty.

**Cómo ejecutar:**
```sh
python punto3.py
```
- Usuario por defecto: `admin`
- Contraseña por defecto: `Vienna22*`

Al iniciar sesión correctamente, se mostrará una ventana con la lista de personajes de Rick and Morty.

---

## Requisitos

- Python 3.x
- Acceso a internet (para el scraping y consumo de API)
- Las librerías utilizadas son parte de la biblioteca estándar de Python (no necesitas instalar paquetes adicionales).

---

**Luis Miguel Sanchez Pinilla**
