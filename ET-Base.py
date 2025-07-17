productos = {'C-123': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
             'C-111': ['lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
             'C-234': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
             'C-456': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
             'C-1222': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
             'C-477': ['lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
             'C-334': ['lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
             'C-2906': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050']}

stock = {'C-123': [387990,10], 
        'C-111': [327990,4], 
        'C-234': [424990,1],
        'C-456': [664990,21], 
        'C-477': [290890,32], 
        'C-334': [444990,7],
        'C-1222': [749990,2], 
        'C-2906': [349990,1]}

def stock_marca(lst_productos: dict, lst_stock: dict, marca_buscada: str) -> int:
        marca_buscada = [codigo]
        Datos = []
        codigo = input("\nIndique el codigo del modelo que desea consultar: ").strip("").lower()
        if codigo not in lst_productos and codigo not in lst_stock.items():
                print("\nEste Codigo No Se Encuentra En Nuestra Lista De Productos")
                return False
        elif codigo in lst_productos or lst_stock <= 0:
                print("\nStock Agotado")
        else:
                (productos[codigo] - ["Marca", "Tamaño", "Memoria RAM", "Tipo", "Capacidad", "Procesador", "Tarjeta Grafica"] == lst_productos)
                (stock[codigo] - ["Precio", "Stock"] == lst_stock)
                print(f"El Stock es de: ", stock[codigo] - [Datos[1]] )
                return True
def busqueda_precio(lst_productos: dict, lst_stock: dict, p_min: int, p_max: int) -> None:
        codigo = {}
        Precio, Stock = Datos
        Datos = []
        try:
                p_min = int(input("Indique Un Precio minimo: "))
                p_max = int(input("Indique Un Precio Maximo: "))
                if p_min <= 0 or p_max < p_min:
                        print("Datos Invalidos")
                        return
        except ValueError:
                print("Datos Invalido, Favor Ingrese Numeros")
                return
        else:
                (productos[codigo] - ["Marca", "Tamaño", "Memoria RAM", "Tipo", "Capacidad", "Procesador", "Tarjeta Grafica"] == lst_productos)
                (stock[codigo] - {"Precio": Precio, "Stock": Stock} == lst_stock)
                print(f"Estos Son Los Precios y Sus Modelos: ", stock[codigo] - [Datos[0]])
                return True
def actualizar_precio(lst_stock: dict, codigo: str, nuevo_precio: int) -> bool:
        codigo = input("Ingrese el codigo")
        nuevo_precio = int(input("Ingrese Un nuevo precio: "))
        for nuevo_precio in lst_stock.items(0):
                print
def main():
        productos = {}
        stock = {}
        while True:
                print("--MENU--\n")
                print("1.- Consultar Cantidad De Stock")
                print("2.- Buscar Productos Por Rango De Precio")
                print("3.- Actualizar Precio De Un Producto")
                print("4.- Salir Del Programa")
                op = input("Indique Una Accion Del Menú A Realizar: ")
                
                if op == "1":
                        stock_marca(stock and productos)
                elif op == "2":
                        busqueda_precio()
                elif op == "3":
                        actualizar_precio()
                elif op == "4":
                        print("Saliendo Del Programa")
                        break
                else:
                        print("Error, Dato u Seleccion Invalida")

if __name__ == "__main__":
        main()