import asyncio

from kwork import Kwork


async def main() -> None:
    api = Kwork(login="login", password="password")

    try:
        me = await api.get_me()
        print(f"Авторизован: {me.username} | Баланс: {me.free_amount} {me.currency}")

        user = await api.get_user(user_id=1456898)
        print(f"Профиль: {user.username}, рейтинг: {user.rating}")

        connects = await api.get_connects()
        print(f"Коннекты: {connects.all_connects} (активных: {connects.active_connects})")

        dialogs = await api.get_all_dialogs()
        print(f"Диалогов: {len(dialogs)}")

        categories = await api.get_categories()
        print(f"Категорий: {len(categories)}")

        projects = await api.get_projects(categories_ids=[11, 79])
        print(f"Проектов: {len(projects)}")

        notifications = await api.get_notifications()
        print(f"Уведомления: {notifications}")
    finally:
        await api.close()


if __name__ == "__main__":
    asyncio.run(main())
