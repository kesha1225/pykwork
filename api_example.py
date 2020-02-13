from kwork import Kwork
from kwork.types import User, Actor
import logging
import asyncio

logging.basicConfig(level=logging.INFO)


async def main():
    api = Kwork(login="login", password="password")

    # Можно использовать socks5 прокси
    # api = Kwork(login="login", password="password", proxy="socks5://208.113.220.250:3420")

    me: Actor = await api.get_me()
    # Получение своего профиля
    print(me)

    user: User = await api.get_user(user_id=1456898)
    # Получения профиля юзера
    print(user)

    all_dialogs = await api.get_all_dialogs()
    # Получения всех диалогов на аккаунте
    print(all_dialogs)

    dialog_with_user = await api.get_dialog_with_user(user_name="username")
    # Получение всего диалога с указанным юзером
    print(dialog_with_user)

    categories = await api.get_categories()
    # Получение категорий заказов на бирже, для дальнейшего
    # поиска проектов по их id
    print(categories)

    projects = await api.get_projects(categories_ids=[11, 79])
    # Получение проектов с биржи по id категорий,
    # которые можно получить из api.get_categories()
    print(projects)

    worker_orders = await api.get_worker_orders()
    # Получение ваших выполненных и отменённых заказов, где вы - работник
    print(worker_orders)

    payer_order = await api.get_payer_orders()
    # Получение ваших выполненных и отменённых заказов, где вы - заказчик
    print(payer_order)

    await api.send_message(user_id=123, text="привет!")
    # Отправляет сообщение

    await api.delete_message(message_id=123)
    # Удаляет сообщение

    await api.set_typing(recipient_id=123)
    # У указанного recipient_id будет показываться что вы печатаете

    await api.set_offline()
    # Делает вас оффлайн

    notifications = await api.get_notifications()
    # Получает уведомления
    print(notifications)

    await api.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
