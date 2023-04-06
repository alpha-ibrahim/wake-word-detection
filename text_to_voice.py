"""
Exxample script for generating and saving speech from text 
"""

import pyttsx3

# initialize the pyttsx3 engine
engine = pyttsx3.init()

# set the voice rate (default rate is 200)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)

# set the voice volume (default volume is 1)
volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.25)

# set the voice voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) # Here, we have selected the 1st female voice.

# say the text
text = "Activate"
engine.say(text)

# run the engine and wait for speech to finish
engine.runAndWait()

engine.save_to_file(text, 'speech.mp3')