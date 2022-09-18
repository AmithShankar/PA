#this is the install file for the application
import subprocess
import os
subprocess.run(["pip", "install", "-r", "requirements.txt"])
os.system('main.py')

#https://pypi.org/project/SpeechRecognition/
#https://pypi.org/project/pyttsx3/
#https://pypi.org/project/PyAudio/
