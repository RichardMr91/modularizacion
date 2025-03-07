import modulo_base
if __name__ == "__main__":
    print("Archivo ejecutándose directamente")
else:
    print("Archivo ejecutándose a través de importación. El archivo se llama:", __name__)