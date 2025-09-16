import ccxt
import pandas as pd

# Conexión a Binance Testnet
binance = ccxt.binance({
    'apiKey': 'W5ZVmuh6F4lhzxc05Nnj7Kq7CxYcOr0LcbjevaXm2LaYLv5nbvawVihmSfiD0a9m',
    'secret': '2mHRgu1giwg29AAWZzctbygihW5Pq48Od0HVdcwmxyBgeT9DN47iXvPRjWhNYsRh',
    'enableRateLimit': True,
})
binance.set_sandbox_mode(True)  # Activamos modo testnet

# Traer 100 velas de BTC/USDT en timeframe de 1 hora
ohlcv = binance.fetch_ohlcv('BTC/USDT', timeframe='1h', limit=100)

# Convertir a DataFrame
df = pd.DataFrame(ohlcv, columns=['timestamp','open','high','low','close','volume'])

# Convertir timestamp a fecha legible
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

print(df.tail())
