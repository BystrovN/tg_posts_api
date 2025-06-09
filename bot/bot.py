from telegram.ext import ApplicationBuilder

from .handlers import setup_handlers
from .config import BOT_TOKEN

import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(levelname)s - %(name)s - %(message)s')


def run_bot(token: str) -> None:
    app = ApplicationBuilder().token(token).build()
    setup_handlers(app)
    app.run_polling()


def main():
    run_bot(BOT_TOKEN)


if __name__ == '__main__':
    main()
