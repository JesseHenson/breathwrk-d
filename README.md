# Welcome to streamlit

This is the app you get when you run `streamlit hello`, extracted as its own app.

Edit [Hello.py](./Hello.py) to customize this app to your heart's desire. ❤️

Check it out on [Streamlit Community Cloud](https://st-hello-app.streamlit.app/)



from google.colab import output
import time
import os
from gtts import gTTS #Import Google Text to Speech
from IPython.display import Audio #Import Audio method from IPython's Display Class

TIME_TO_START_ROUND = 2
TIME_BETWEEN_BREATHS_IN = 3
TIME_BETWEEN_BREATHS_OUT = 2
TIME_TUMO_DEEP_IN = 2
TIME_TUMO_DEEP_IN_HOLD = 15
TIME_BETWEEN_ROUNDS = 2


def say(text):
    sound_file = f'{text}.wav'
    sound = gTTS(text)
    sound.save(sound_file)
    display(Audio(f'/content/{sound_file}', autoplay=True) )
    os.remove(f'/content/{sound_file}')




def tumo_breathing(hold_out_dur=60, breaths_per_round=30, rounds=3):
  for round in range(rounds):

    say(f'round {round}')
    time.sleep(TIME_TO_START_ROUND)
    for breath in range(breaths_per_round):
      if breaths_per_round > 20 and breaths_per_round - breath == 10:
        say('10 breaths left')
        time.sleep(TIME_BETWEEN_BREATHS_IN)
        say('breathe out')
        time.sleep(TIME_BETWEEN_BREATHS_OUT)
      if breaths_per_round - breath == 5:
        say('5 breaths left')
        time.sleep(TIME_BETWEEN_BREATHS_IN)
        say('breathe out')
        time.sleep(TIME_BETWEEN_BREATHS_OUT)
      if breaths_per_round - breath == 1:
        say('last breath breath in as far as you can')
        time.sleep(TIME_BETWEEN_BREATHS_IN)
        say('breathe out all the way')
        time.sleep(TIME_BETWEEN_BREATHS_OUT)
      else:
        say('breathe in')
        time.sleep(TIME_BETWEEN_BREATHS_IN)
        say('breathe out')
        time.sleep(TIME_BETWEEN_BREATHS_OUT)

    # Hold breath out
    say(f'hold for {hold_out_dur} seconds')
    time.sleep(hold_out_dur-5)
    say(f'5 more seconds')
    time.sleep(5)


    # Hold In Deep Breath
    say('breathe in deep')
    time.sleep(TIME_TUMO_DEEP_IN)
    say(f'hold breath in for {TIME_TUMO_DEEP_IN_HOLD}')
    time.sleep(TIME_TUMO_DEEP_IN_HOLD)
    say(f'breathe out')
    time.sleep(TIME_BETWEEN_ROUNDS)
  say(f'breathing session complete')


def box_breathing(seconds, total_time_in_min):
  rounds = (60*total_time_in_min)//(seconds*4)
  say(f"Let's get started for {rounds} rounds of {seconds} second box-breathing")
  time.sleep(TIME_TO_START_ROUND)
  for round in range(rounds):
    if round == rounds:
      say(f'last round')
      time.sleep(1)
    say(f'breathe in')
    time.sleep(seconds)
    say(f'hold breath in')
    time.sleep(seconds)
    say(f'breathe out')
    time.sleep(seconds)
    say(f'hold breath out')
    time.sleep(seconds)
  say(f"Thank you so much for doing this breathing exercize with us!")


tumo_breathing(30, 30, 3)
# box_breathing(6, 1)
