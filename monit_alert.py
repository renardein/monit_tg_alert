#!/usr/bin/python3
# -*- coding: utf-8 -*- #

"""

 This script is used to send Telegram notifications
 when a Monit alert is raised.

 Author = Matei Ciobotaru
 Modifed = renardein
"""
import argparse
import telebot

bot = telebot.TeleBot('YOUR_TG_BOT_API_TOKEN')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--msg', dest='message')
    parser.add_argument('-c', '--chat', dest='chat')
    parser.add_argument('-t', '--thread', dest='thread')
    args = parser.parse_args()

bot.send_message(chat_id=args.chat, message_thread_id=args.thread, parse_mode='Markdown', text=args.message)