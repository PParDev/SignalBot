import pandas as pd
import ta

def add_indicators(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    df['ema50'] = ta.trend.EMAIndicator(df['close'], window=50).ema_indicator()
    return df
