import cv2
import numpy as np
import zbar

#agregar esta librerias

# Base de datos simple de productos de cafe
coffee_database = {
    "7441026000118": {"tipo": "Arábica", "origen": "Colombia", "tostado": "Medio", "tamaño": "250g"},
    "1123456789013": {"tipo": "Robusta", "origen": "Brasil", "tostado": "Fuerte", "tamaño": "500g"},
    # Agrega mas productos
}

def decode_barcodes(frame, processed_barcodes):
    # Convertir el frame a escala de grises
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Crear un objeto Scanner
    scanner = zbar.Scanner()

    # Escanear la imagen en busca de cidigos de barras
    symbols = scanner.scan(gray_frame)

    for symbol in symbols:
        barcode_info = symbol.data.decode("utf-8")
        if barcode_info not in processed_barcodes:
            processed_barcodes.add(barcode_info)
            print("Código de barras:", barcode_info)
            coffee_info = coffee_database.get(barcode_info)
            if coffee_info is not None:
                print("Tipo de café:", coffee_info["tipo"])
                print("Origen:", coffee_info["origen"])
                print("Nivel de tostado:", coffee_info["tostado"])
                print("Tamaño del paquete:", coffee_info["tamaño"])
                return True  # Se encontro un codigo de barras válido, devielve si
            else:
                print("Producto no encontrado en la base de datos")

    return False  # No se encontro un codigo de barras valido, devuelve False

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: No se pudo abrir la cámara.")
        return

    processed_barcodes = set()

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se pudo capturar el frame.")
            break

        if decode_barcodes(frame, processed_barcodes):
            break  # Si se encuentra un codigo de barras valido, salir del bucle, mal si break

        cv2.imshow('Barcode Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
    
#Este era el inicio de un codigo que puediera leer codigo de barras de un producto y presentara las caracteristicas.