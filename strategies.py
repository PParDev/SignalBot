def basic_strategy(df):
    signals = []
    for i in range(len(df)):
        if df['rsi'][i] < 30:
            signals.append('BUY')
        elif df['rsi'][i] > 70:
            signals.append('SELL')
        else:
            signals.append('')
    df['signal'] = signals
    return df
