# 3. Install an external module and use it to perform an operation of your interest.

 #pip install pyjocks

import pyjokes
import pyttsx3
import time
#print(pyjokes.get_joke())
jock = pyjokes.get_joke()
print(jock)

def speak_offline(text: str, speed: int = 150):
    # Initialize the TTS engine
    engine = pyttsx3.init()
    
    # Configure properties (Optional)
    engine.setProperty('rate', speed)  # Speed of speech (words per minute)
    engine.setProperty('volume', 1.0)  # Volume (0.0 to 1.0)
    
    # Queue the text and play it
    engine.say(text)
    engine.runAndWait()
    
# Example execution
speak_offline(jock)
