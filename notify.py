"""
Gui tin nhac Telegram (dung chay boi GitHub Actions, hoac chay tay de test).

Can 2 bien moi truong (GitHub Actions se lay tu Secrets):
    BOT_TOKEN   - token cua bot, lay tu @BotFather
    CHAT_ID     - id cuoc tro chuyen can gui den (xem huong dan trong README)
"""
import os
import sys

import requests

from message import build_message


def main():
    token = os.environ.get("BOT_TOKEN")
    chat_id = os.environ.get("CHAT_ID")

    if not token or not chat_id:
        print("Thieu BOT_TOKEN hoac CHAT_ID trong bien moi truong.", file=sys.stderr)
        sys.exit(1)

    text = build_message()
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    resp = requests.post(url, data={"chat_id": chat_id, "text": text})

    if resp.status_code != 200:
        print(f"Gui that bai: {resp.status_code} {resp.text}", file=sys.stderr)
        sys.exit(1)

    print("Da gui:")
    print(text)


if __name__ == "__main__":
    main()
