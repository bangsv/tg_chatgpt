import telebot
import openai
import time
import traceback

bot = telebot.TeleBot('Api key')
openai.api_key = "Api key"

# Choosing the gpt model
model_engine = "text-davinci-003"

def openai_answer(message):
    prompt = message.text
    max_tokens = 128
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return completion.choices[0].text

# A function that processes the /start command
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, '👋Hi, I am a bot assistant. Ask the question of interest')

# Receiving messages from the user
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, 'Message received' )
    text = openai_answer(message)
    bot.send_message(message.chat.id, f'You wrote: {message.text}' + "\nAnswer: " + text )

def start():
    try :
        print("Bot started")
        bot.polling(none_stop=True, interval=0)
    except:
        traceback_error_string=traceback.format_exc()
        with open("Error.Log", "a") as myfile:
            myfile.write("\r\n\r\n" + time.strftime("%c")+"\r\n<<ERROR polling>>\r\n"+ traceback_error_string + "\r\n<<ERROR polling>>")
        bot.stop_polling()
        time.sleep(15)
        start()

# Start Bot
start()
