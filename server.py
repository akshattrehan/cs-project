from telebot import telegram_bot

update_id = None

def make_reply(msg):
    if msg is not None:
        reply = "Okay"

    return reply

while True:
    print(" .... ")
    updates = bot.get_updates(offset = update_id)
    updates = updates["result"]

    if updates:
        for item in updates:
            update_id = item["update-id"]

            try:
                message = item["message"]["text"]

            except:
                message = None

            from_ = item["message"]["from"]["id"]
            reply = make_reply(message)
            bot.send_message(reply, from_)