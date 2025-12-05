import asyncio
import logging

from kwork import Kwork

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger(__name__)


async def monitor(
    api: Kwork,
    categories_ids: list[int | str],
    interval: int = 60,
    min_price: int | None = None,
    max_price: int | None = None,
) -> None:
    seen: set[int] = set()

    while True:
        projects = await api.get_projects(
            categories_ids=categories_ids,
            price_from=min_price,
            price_to=max_price,
        )

        for p in projects:
            if p.id and p.id not in seen:
                seen.add(p.id)
                log.info("Новый: %s | %s руб. | %s предложений", p.title, p.price, p.offers)

        await asyncio.sleep(interval)


async def main() -> None:
    async with Kwork(login="login", password="password") as api:
        me = await api.get_me()
        log.info("Авторизован: %s", me.username)

        await monitor(api, categories_ids=[11, 79], interval=60, min_price=1000)


if __name__ == "__main__":
    asyncio.run(main())
