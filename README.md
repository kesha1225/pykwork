Простая асинхронная обёртка над закрытым api для фриланс биржи kwork.ru


https://api.kwork.ru/
все доступные методы тут, можно запрашивать их через api_request
```python3
await self.api_request(
            method="post", api_method="actor", token=await self.token
)
```


## Установка

Стабильная версия:
```
pip install kwork
```

Последняя версия:
```
pip install https://github.com/kesha1225/pykwork/archive/master.zip --upgrade
```

## Обзор

Список доступных методов можно посмотреть [здесь](./api_example.py)

Пример простого api запроса:

```python3
from kwork import Kwork
from kwork.types import Actor
import logging
import asyncio

logging.basicConfig(level=logging.INFO)


async def main():
    api = Kwork(login="login", password="password")
    me: Actor = await api.get_me()
    # Получение своего профиля
    print(me)
    await api.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

```

### pykwork предоставляет возможность создания ботов для мгновенных ответов потециальным покупателям


Пример бота с тремя хендлерами для ответов:

```python3
from kwork import KworkBot
from kwork.types import Message
import logging
import asyncio

logging.basicConfig(level=logging.INFO)

bot = KworkBot(login="login", password="password")

@bot.message_handler(on_start=True)
async def simple_handle(message: Message):
    """
    Отвечаем только если это первое сообщение от юзера
    """
    text = ("Здравствуйте, рад что вы обратились именно ко мне,"
            " опишите ваше желание подробнее!")
    await message.answer_simulation(text)


@bot.message_handler(text_contains="бот")
async def bot_handler(message: Message):
    """
    Отвечаем если текст сообщения содержит слово бот
    """
    text = "Вам нужен бот? Можете посмотреть на примеры уже сделанных:..."
    await message.answer_simulation(text)


@bot.message_handler(text="привет")
async def bot_handler(message: Message):
    """
    Отвечаем только если текст такой же как параметр text
    """
    text = "И вам привет!"
    await message.answer_simulation(text)


async def run():
    """
    Запускаем бота
    """
    await bot.run_bot()


loop = asyncio.get_event_loop()
loop.run_until_complete(run())

```

## Примечание

Получая ошибку "Подтвердите что вы не робот" просто ставьте прокси.

Kwork может банить по ip, но в основном pykwork предотвращает это, даже
если вас забанили, не пугайтесь, аккаунты они не банят, просто перезайдите
с vpn/tor/proxy. Если вас каким то чудом забанили, но вам нужно продолжить 
использовать бота - воспользуйтесь прокси (socks5/socks4):

```python3
from kwork import Kwork
from kwork.types import User, Actor
import logging
import asyncio

logging.basicConfig(level=logging.INFO)


async def main():
    api = Kwork(login="login", password="password", proxy="socks5://208.113.220.250:3420")

    me: Actor = await api.get_me()
    print(me)

    await api.close()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

``` 

Получая ошибку "Необходимо ввести последние 4 цифры номера телефона." используйте параметр phone_last
```
api = Kwork(login="login", password="password", phone_last="0102")
```

Если вдруг какие - то методы перестанут работать или работают неправильно -
пишите отчёты в issue