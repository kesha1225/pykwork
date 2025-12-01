# pykwork

Асинхронная обёртка над API фриланс-биржи [kwork.ru](https://kwork.ru/)

## Установка

```bash
uv add kwork
```

или последняя версия:

```bash
uv add git+https://github.com/kesha1225/pykwork
```

## Быстрый старт

```python
import asyncio
from kwork import Kwork

async def main():
    api = Kwork(login="login", password="password")

    try:
        me = await api.get_me()
        print(f"{me.username} | {me.free_amount} {me.currency}")
    finally:
        await api.close()

asyncio.run(main())
```

📖 **[Полный туториал](docs/tutorial.md)** — API, боты, прокси, примеры

## Contributors

- [@iamlostshe](https://github.com/iamlostshe)
