import logging
from datetime import datetime

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes, Application

from .config import POST_TG_COMMAND
from .posts_api import fetch_posts, fetch_post_detail

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Используй /{POST_TG_COMMAND} чтобы увидеть список постов')


async def posts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        posts = await fetch_posts()
        logger.info(f'Fetched {len(posts)} posts')
    except Exception as e:
        logger.error(f'Error fetching posts: {e}')
        await update.message.reply_text('Ошибка при получении постов')
        return

    if not posts:
        await update.message.reply_text('Нет доступных постов')
        return

    keyboard = [[InlineKeyboardButton(post['title'], callback_data=str(post['id']))] for post in posts]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Выбери пост:', reply_markup=reply_markup)


async def post_detail(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    post_id = query.data

    try:
        post = await fetch_post_detail(post_id)
    except Exception as e:
        logger.error(f'Error fetching post ID {post_id}: {e}')
        await query.edit_message_text(text='Ошибка при получении поста')
        return

    text = (
        f"Текст: {post['content']}\n\n"
        f"Создан: {datetime.strptime(post['created_at'], '%Y-%m-%dT%H:%M:%S.%fZ').strftime('%Y-%m-%d %H:%M:%S')}"
    )
    await query.edit_message_text(text=text)


def setup_handlers(app: Application):
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler(POST_TG_COMMAND, posts_command))
    app.add_handler(CallbackQueryHandler(post_detail))
