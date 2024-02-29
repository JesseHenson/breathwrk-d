# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

import time
import os
import base64
from gtts import gTTS #Import Google Text to Speech

LOGGER = get_logger(__name__)

TIME_TO_START_ROUND = 2
TIME_BETWEEN_BREATHS_IN = 3
TIME_BETWEEN_BREATHS_OUT = 2
TIME_TUMO_DEEP_IN = 2
TIME_TUMO_DEEP_IN_HOLD = 15
TIME_BETWEEN_ROUNDS = 2

"""
# Welcome to Beathwork'd 
## Custom AI Breathwork Exercises

> Pick a exercise to start
"""

def run():

  selected_exercise = st.selectbox('Breathing Exercize',[
    'Tumo Breathing', 
    'Box Breathing'
  ], index=None)

  if selected_exercise == 'Tumo Breathing':
    with st.form("Tumo Form"):
      hold_out_dur = st.number_input('How long would you like to hold out breath in seconds?',30,180,60)
      breaths_per_round = st.number_input('How many breaths per round?',30,100,30)
      rounds = st.number_input('How many rounds?',1,10,3)
      submitted = st.form_submit_button("Submit")
      if submitted:
        tumo_breathing(hold_out_dur, breaths_per_round, rounds)
  
  if selected_exercise == 'Box Breathing':
    with st.form("box Form"):
      seconds = st.number_input('How many seconds for each side of the box',4,20,6)
      total_time_in_min = st.number_input('How many minutes would you like to do the box breathing?', 1, 20, 3)
      submitted = st.form_submit_button("Submit")
      if submitted:
        box_breathing(seconds, total_time_in_min)





# ---------- Utility Functions -------------
def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true" style="display:none">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

def say(text):
    sound_file = f'{text}.mp3'
    sound = gTTS(text)
    sound.save(sound_file)
    autoplay_audio(sound_file)
    os.remove(sound_file)
    # autoplay_audio(sound_file)



# ------------- Breathing Exercizes --------------
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
  time.sleep(6)
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






if __name__ == "__main__":
    run()
