import yfinance as yf # pip install yfinance
import os
import time

# Listas de símbolos para diferentes categorías

# Divisas: Representan pares de monedas
divisas = [
    "EURUSD=X", 
    "GRPUSD=X",
    "USDJPY=X",
    "USDCAD=X"
]

# Materias Primas: Incluyen productos básicos como metales y energéticas
materias_primas = [
    "GC=F",
    "CL=F",
    "SI=F",
    "NG=F"
]

# Acciones: Empresas que cotizan en bolsa
acciones = [
    "AAPL",
    "MSFT",
    "GOOGL",
    "AMZN"
]

# Criptomonedas: Monedas digitales y sus valores exresadas en dólares estadounidenses
criptomonedas = [
    "BTC-USD",
    "ETH-USD",
    "ADA-USD",
    "SOL-USD"
]

# Intervalos de tiempo para los datos históricos
intervalos = ["1m", "1h", "1d"]

# Fecha de inicio y fecha final para los datos históricos
fecha_inicio = "2023-01-01"
fech_final = "2024-08-01"

#Función para obtener datos históricos
def obtener_datos(simbolos: list, fecha_inicio: str, fech_final: str, intervalos: list) -> dict:
    """
        Método que descarfa datos históricos para un conjunto de instrumentos financieros.
    """

    datos = {}

    for simbolo in simbolos:
        datos[simbolo] = {}
        for intervalo in intervalos:
            print(f"Descargando datos para {simbolo} con intervalo {intervalo}...")
            if intervalo == "1m":
                df = yf.download(tickers=simbolo, interval=intervalo, multi_level_index=False)
            else:
                df = yf.download(tickers=simbolo, start=fecha_inicio, end= fech_final, interval=intervalo)
            datos[f"{simbolo}"][f"{intervalo}"] = df
        time.sleep(0.25)
    
    return datos

# Obtener datos históricos para cada categoría
datos_divisas = obtener_datos(simbolos=divisas, fecha_inicio=fecha_inicio, fech_final=fech_final, intervalos=intervalos)
datos_materias_primas = obtener_datos(simbolos=materias_primas, fecha_inicio=fecha_inicio, fech_final=fech_final, intervalos=intervalos)
datos_acciones = obtener_datos(simbolos=acciones, fecha_inicio=fecha_inicio, fech_final=fech_final, intervalos=intervalos)
datos_criptomonedas = obtener_datos(simbolos=criptomonedas, fecha_inicio=fecha_inicio, fech_final=fech_final, intervalos=intervalos)

# Guardar los datos en archivos csv
if not os.path.isdir("datos"):
    os.mkdir("datos")

datos_conjuntos = {"acciones": datos_acciones, "divisas": datos_divisas, "materias_primas": datos_materias_primas, "criptomonedas": datos_criptomonedas}

# Iterar en cada conjunto de datos
for tipo_activo, conjunto_datos in datos_conjuntos.items():
    # Iterar en cada instrumento
    for ticker, datos_dict in conjunto_datos.items():
        # Iterar en cada intervalo de tiempo
        for intervalo, datos_df in datos_dict.items():
            # Revisar si existe subcarpeta para este tipo de activo
            if not os.path.isdir(f"datos/{tipo_activo}"):
                os.mkdir(f"datos/{tipo_activo}")
            # Revisar si este activo ya existe dentro de esta categoría
            if not os.path.isdir(f"datos/{tipo_activo}/{ticker}"):
                os.mkdir(f"datos/{tipo_activo}/{ticker}")
            datos_df.to_csv(f"datos/{tipo_activo}/{ticker}/{intervalo}.csv")