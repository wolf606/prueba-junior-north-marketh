import sys
from urllib.request import urlopen, Request
from html.parser import HTMLParser

class ProductoParser(HTMLParser):
    def __init__(self, limite, palabra_clave):
        super().__init__()
        self.limite = limite
        self.palabra_clave = palabra_clave.lower()
        self.productos = []

        self.es_un_titulo = False
        self.es_un_precio = False
        self.found_real_price = False
        self.actual_titulo = ""
        self.actual_precio = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == "h3" and attrs_dict.get("class") == "poly-component__title-wrapper":
            self.es_un_titulo = True

        if tag == "div" and attrs_dict.get("class") == "poly-price__current":
            self.found_real_price = True

        if tag == "span" and attrs_dict.get("class") == "andes-money-amount__fraction":
            self.es_un_precio = True

    def handle_data(self, data):
        if len(self.productos) >= self.limite:
            return

        texto = data.strip()

        if self.es_un_titulo and texto and self.palabra_clave in texto.lower():
            self.actual_titulo = texto

        if self.found_real_price and self.es_un_precio and texto:
            self.actual_precio = texto
            if self.actual_titulo:
                self.productos.append((self.actual_titulo, self.actual_precio))
                self.actual_titulo = ""
                self.actual_precio = ""


    def handle_endtag(self, tag):
        if tag == "h3":
            self.es_un_titulo = False
        if tag == "div":
            self.found_real_price = False
        if tag == "span":
            self.es_un_precio = False


def find_products(palabra_clave_one: str, palabra_clave_two: str, limite: int = 5):
    url = f"https://listado.mercadolibre.com.co/{palabra_clave_one.replace(' ', '-')}"
    headers = {"User-Agent": "Mozilla/5.0"}

    req = Request(url, headers=headers)
    try:
        with urlopen(req) as response:
            html = response.read().decode("utf-8")
    except Exception as e:
        print("Error al realizar la solicitud:", e)
        return

    parser = ProductoParser(limite, palabra_clave_two)
    parser.feed(html)

    if not parser.productos:
        print("No se encontraron productos.")
        return
    
    for i, (titulo, precio) in enumerate(parser.productos, 1):
        print(f"{i}. {titulo}\n   ${precio}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python script.py <categoria_busqueda> <palabra_filtrar>")
        print("Ejemplo: python script.py celular Samsung")
        sys.exit(1)

    categoria = sys.argv[1]
    palabra = sys.argv[2]
    find_products(categoria, palabra)
