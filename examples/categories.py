import asyncio

from kwork import Kwork


async def main() -> None:
    api = Kwork(login="login", password="password")

    try:
        categories = await api.get_categories()

        for parent in categories:
            print(f"\n{parent.name} (ID: {parent.id})")
            for sub in parent.subcategories or []:
                print(f"  └─ {sub.name} (ID: {sub.id})")

        dev_category = next((c for c in categories if "разработ" in (c.name or "").lower()), None)

        if dev_category and dev_category.subcategories:
            ids: list[int | str] = [s.id for s in dev_category.subcategories[:3] if s.id]
            projects = await api.get_projects(categories_ids=ids)

            print(f"\nПроектов в категории: {len(projects)}")
            for p in projects[:3]:
                print(f"  {p.title} | {p.price} руб. | {p.offers} предложений")
    finally:
        await api.close()


if __name__ == "__main__":
    asyncio.run(main())
