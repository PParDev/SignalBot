import pandas as pd

def backtest_strategy(df, initial_balance=1000):
	balance = initial_balance
	position = 0  # 0: sin posición, 1: comprado
	entry_price = 0
	trades = []
	for i in range(len(df)):
		signal = df['signal'][i]
		close = df['close'][i]
		if signal == 'BUY' and position == 0:
			position = 1
			entry_price = close
			trades.append({'type': 'BUY', 'price': close, 'index': i})
		elif signal == 'SELL' and position == 1:
			profit = close - entry_price
			balance += profit
			trades.append({'type': 'SELL', 'price': close, 'index': i, 'profit': profit})
			position = 0
	# Si queda posición abierta, la cerramos al último precio
	if position == 1:
		profit = df['close'].iloc[-1] - entry_price
		balance += profit
		trades.append({'type': 'SELL', 'price': df['close'].iloc[-1], 'index': len(df)-1, 'profit': profit})
	# Estadísticas
	total_trades = len([t for t in trades if t['type'] == 'SELL'])
	wins = len([t for t in trades if t.get('profit', 0) > 0])
	losses = len([t for t in trades if t.get('profit', 0) <= 0])
	total_profit = balance - initial_balance
	results = {
		'final_balance': balance,
		'total_trades': total_trades,
		'wins': wins,
		'losses': losses,
		'total_profit': total_profit,
		'trades': trades
	}
	return results
