import yfinance as yf
import time
from flask import Flask, request, jsonify
from Estrategia1 import Estrategia1

app = Flask(__name__)

# Definir lista de activos y marco de tiempo
activos = [
    "EURUSD=X", "GRPUSD=X", "USDJPY=X", "USDCAD=X",
    "GC=F", "CL=F", "SI=F", "NG=F",
    "AAPL", "MSFT", "GOOGL", "AMZN", "IBE", "SAN", "TEF", "BBVA", "ITX", "REP", "IBE.MC", "SAN.MC", "TEF.MC", "BBVA.MC", "ITX.MC", "REP.MC", "MRL.ES", "MRL.MC",
    "BTC-EUR", "ETH-EUR", "ADA-EUR", "SOL-EUR", "DOGE-EUR", "XRP-EUR", "LTC-EUR", "BNB-EUR", "LINK-EUR", "UNI-EUR", "AAVE-EUR", "MKR-EUR", "COMP-EUR", "SNX-EUR", "YFI-EUR", "UMA-EUR", "CRV-EUR", "SUSHI-EUR", "1INCH-EUR", "BAL-EUR", "REN-EUR", "KNC-EUR", "OCEAN-EUR", "BNT-EUR", "LRC-EUR", "GRT-EUR", "MLN-EUR", "BAND-EUR", "RLC-EUR", "STORJ-EUR", "CVC-EUR", "MANA-EUR", "ENJ-EUR", "BAT-EUR", "CHZ-EUR", "OGN-EUR", "REEF-EUR", "RVN-EUR", "FIL-EUR", "SKL-EUR", "SXP-EUR", "SAND-EUR", "ANKR-EUR"
]
marco_tiempo = "1h"

@app.route('/ejecutar_estrategia', methods=['POST'])
def ejecutar_estrategia():
    data = request.json
    parametros_optimizados = data['parametros_optimizados']
    
    resultados = []
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
            resultados.append({
                'activo': activo,
                'marco_tiempo': marco_tiempo,
                'señal': calculo_señal
            })
    
    return jsonify(resultados)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)