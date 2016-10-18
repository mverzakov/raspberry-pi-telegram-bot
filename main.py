#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Simple Bot to reply to Telegram messages
# This program is dedicated to the public domain under the CC0 license.

"""
This Bot uses the Updater class to handle the bot.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""
import logging
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from decorators import access_required
import settings

# Enable logging
logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    bot.sendMessage(update.message.chat_id, text='')


def help(bot, update):
    bot.sendMessage(update.message.chat_id, text='')


@access_required
def echo(bot, update):
    message = update.message.text.lower()
    bot.sendMessage(update.message.chat_id, text=message)


@access_required
def torrent_file_handler(bot, update):
    document = update.message.document
    if not document.file_name.endswith('.torrent'):
        bot.sendMessage(update.message.chat_id,
                        text='It\'s not a torrent file!')
    else:
        custom_keyboard = [settings.TORRENT_DIRS.keys()]
        reply_markup = ReplyKeyboardMarkup(custom_keyboard)
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="Choose content type.",
                        reply_markup=reply_markup)


@access_required
def contact_handler(bot, update):
    id = update.message.contact.user_id
    if id not in settings.ALLOWED_IDS:
        settings.ALLOWED_IDS.append(id)
        text = u'User {} {} is now able to do things.'
    else:
        text = u'User {} {} already have an access to do things.'
    bot.sendMessage(update.message.chat_id, text=text.format(
        update.message.contact.first_name,
        update.message.contact.last_name))


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(settings.BOT_ID)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler([Filters.document], torrent_file_handler))
    dp.add_handler(MessageHandler([Filters.contact], contact_handler))
    dp.add_handler(MessageHandler([Filters.text], echo))


    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()