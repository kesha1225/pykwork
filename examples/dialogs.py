import asyncio
from datetime import datetime

from kwork import Kwork


def format_time(ts: int | None) -> str:
    return datetime.fromtimestamp(ts).strftime("%d.%m %H:%M") if ts else "—"


async def main() -> None:
    api = Kwork(login="login", password="password")

    try:
        me = await api.get_me()
        print(f"Авторизован: {me.username} | Непрочитанных: {me.unread_dialog_count}")

        dialogs = await api.get_all_dialogs()
        print(f"Всего диалогов: {len(dialogs)}\n")

        for d in dialogs[:5]:
            status = "🟢" if d.is_online else "⚫"
            unread = f" ({d.unread_count} новых)" if d.unread_count else ""
            msg = (d.last_message or "")[:50]
            print(f"{status} {d.username}{unread}")
            print(f"   {msg}... | {format_time(d.time)}\n")

        if dialogs and dialogs[0].username:
            messages = await api.get_dialog_with_user(dialogs[0].username)
            print(f"Диалог с {dialogs[0].username}:")
            for m in messages[-3:]:
                print(f"  {m.from_username}: {(m.message or '')[:60]}")
    finally:
        await api.close()


if __name__ == "__main__":
    asyncio.run(main())
