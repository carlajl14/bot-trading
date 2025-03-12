import yfinance as yf
import time
from Estrategia1 import Estrategia1

# Definir lista de activos y marco de tiempo
activos = [
    "EURUSD=X", "GRPUSD=X", "USDJPY=X", "USDCAD=X",
    "GC=F", "CL=F", "SI=F", "NG=F",
    "AAPL", "MSFT", "GOOGL", "AMZN", "IBE", "SAN", "TEF", "BBVA", "ITX", "REP", "IBE.MC", "SAN.MC", "TEF.MC", "BBVA.MC", "ITX.MC", "REP.MC", "BTC-USD", "ETH-USD", "ADA-USD", "SOL-USD", "DOGE-USD", "XRP-USD", "LTC-USD", "BNB-USD", "LINK-USD", "UNI-USD", "AAVE-USD", "MKR-USD", "COMP-USD", "SNX-USD", "YFI-USD", "UMA-USD", "CRV-USD", "SUSHI-USD", "1INCH-USD", "BAL-USD", "REN-USD", "KNC-USD", "OCEAN-USD", "BNT-USD", "LRC-USD", "GRT-USD", "MLN-USD", "BAND-USD", "RLC-USD", "STORJ-USD", "CVC-USD", "MANA-USD", "ENJ-USD", "BAT-USD", "CHZ-USD", "OGN-USD", "REEF-USD", "RVN-USD", "FIL-USD", "SKL-USD", "SXP-USD", "SAND-USD", "ANKR-USD", "CRV-USD", "1INCH-USD", "BAL-USD", "REN-USD", "KNC-USD", "OCEAN-USD", "BNT-USD", "LRC-USD", "GRT-USD", "MLN-USD", "BAND-USD", "RLC-USD", "STORJ-USD", "CVC-USD", "MANA-USD", "ENJ-USD", "BAT-USD", "CHZ-USD", "OGN-USD", "REEF-USD", "RVN-USD", "FIL-USD", "SKL-USD", "SXP-USD", "SAND-USD", "ANKR-USD",
    "BTC-EUR", "ETH-EUR", "ADA-EUR", "SOL-EUR", "DOGE-EUR", "XRP-EUR", "LTC-EUR", "BNB-EUR", "LINK-EUR", "UNI-EUR", "AAVE-EUR", "MKR-EUR", "COMP-EUR", "SNX-EUR", "YFI-EUR", "UMA-EUR", "CRV-EUR", "SUSHI-EUR", "1INCH-EUR", "BAL-EUR", "REN-EUR", "KNC-EUR", "OCEAN-EUR", "BNT-EUR", "LRC-EUR", "GRT-EUR", "MLN-EUR", "BAND-EUR", "RLC-EUR", "STORJ-EUR", "CVC-EUR", "MANA-EUR", "ENJ-EUR", "BAT-EUR", "CHZ-EUR", "OGN-EUR", "REEF-EUR", "RVN-EUR", "FIL-EUR", "SKL-EUR", "SXP-EUR", "SAND-EUR", "ANKR-EUR", "CRV-EUR", "1INCH-EUR", "BAL-EUR", "REN-EUR", "KNC-EUR", "OCEAN-EUR", "BNT-EUR", "LRC-EUR", "GRT-EUR", "MLN-EUR", "BAND-EUR", "RLC-EUR", "STORJ
]
marco_tiempo = "1h"

# Función para ejecutar la estrategia en diferentes activos y marcos de tiempo
def ejecutar_estrategia(activos: list, marco_tiempo: str, parametros_optimizados: list):
    """
    Ejecuta nuestra clase de Estrategia 1 para detectar oportunidades de inversión (señales)
    """

    while True:
        for activo in activos:
            # Descargar datos
            df = yf.download(activo, period="1y", interval=marco_tiempo)
            # Crear instancia de la estrategia
            estrategia = Estrategia1(df)
            estrategia.periodo_ma_rapido = parametros_optimizados[0]
            estrategia.periodo_ma_lento = parametros_optimizados[1]
            estrategia.periodo_rsi = parametros_optimizados[2]
            # Calcular la estrategia
            calculo_señal = estrategia.calcular()
            if calculo_señal is not False:
                # Imprimir señal generada
                print(f"Activo: {activo}, Marco de Tiempo: {marco_tiempo}, Señal Generada: {calculo_señal})
        
        # Esperar a volver a ejecutar
        print("\nEsperando...\n")
        time.sleep(60 * 60)

# Ejecutar la estrategia en diferentes activos
parametros_optimizados = [20, 50, 14]
ejecutar_estrategia(activos=activos, marco_tiempo=marco_tiempo, parametros_optimizados=parametros_optimizados)