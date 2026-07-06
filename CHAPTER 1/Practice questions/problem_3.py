# 3. Install an external module and use it to perform an operation of your interest.

 #pip install pyjocks

# import pyjokes

# print(pyjokes.get_joke())


import pyttsx3

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
speak_offline("jay shree ram")
