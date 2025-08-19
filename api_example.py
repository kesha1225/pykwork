import asyncio
import logging

from kwork import Kwork

logging.basicConfig(level=logging.INFO)


async def main() -> None:
    api = Kwork(login="login", password="password")

    # Если "Необходимо ввести последние 4 цифры номера телефона."
    # api = Kwork(login="login", password="password", phone_last="0102")

    # Можно использовать socks5 прокси
    # api = Kwork(login="login", password="password", proxy="socks5://208.113.220.250:3420")

    await api.get_me()
    # Получение своего профиля

    await api.get_user(user_id=1456898)
    # Получения профиля юзера

    await api.get_connects()
    # Получение ваших коннектов

    await api.get_all_dialogs()
    # Получения всех диалогов на аккаунте

    await api.get_dialog_with_user(user_name="username")
    # Получение всего диалога с указанным юзером

    await api.get_categories()
    # Получение категорий заказов на бирже, для дальнейшего
    # поиска проектов по их id

    await api.get_projects(categories_ids=[11, 79])
    # Получение проектов с биржи по id категорий,
    # которые можно получить из api.get_categories()

    await api.get_worker_orders()
    # Получение ваших выполненных и отменённых заказов, где вы - работник

    await api.get_payer_orders()
    # Получение ваших выполненных и отменённых заказов, где вы - заказчик

    await api.send_message(user_id=123, text="привет!")
    # Отправляет сообщение

    await api.delete_message(message_id=123)
    # Удаляет сообщение

    await api.set_typing(recipient_id=123)
    # У указанного recipient_id будет показываться что вы печатаете

    await api.set_offline()
    # Делает вас оффлайн

    await api.get_notifications()
    # Получает уведомления

    await api.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
