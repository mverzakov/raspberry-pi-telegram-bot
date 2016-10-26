# -*- coding: utf-8 -*-
from settings import ALLOWED_IDS


def access_required(func):
    def func_wrapper(bot, update):
        if update.message.from_user.id not in ALLOWED_IDS:
            bot.sendMessage(chat_id=update.message.chat_id,
                            text="It seems like you aren't allowed to use me.")
            text = ('But sudobot is open source software, which means you '
                    'can have your own! See my [GitHub repo]'
                    '(https://github.com/mverzakov/raspberry-pi-telegram-bot) '
                    'for details.')
            bot.sendMessage(chat_id=update.message.chat_id,
                            text=text, parse_mode='Markdown')
        else:
            return func(bot, update)
    return func_wrapper
