from telegram import Bot
import asyncio
bot = Bot(token='8268690696:AAGEOq8ZtzEUsSv_2gQahE4d4edM5F1iZ6A')
async def Enviar():
    await bot.send_message(chat_id='5999033875', text='Señal de COMPRA en BTC a $40,000')

if __name__ == "__main__":
    asyncio.run(Enviar())