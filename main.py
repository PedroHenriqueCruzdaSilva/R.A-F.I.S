# Our main file.

import speech_recognition as sr

# Cria um Reconhecedor
r = sr.Recognizer()

# Abrir o Microfone para captura de audio
with sr.Microphone() as source:
  while True:
    audio = r.listen(source) # Define Microfone como fonte de áudio

    print(r.recognize_google(audio, language='pt'))
