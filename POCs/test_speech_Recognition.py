import speech_recognition as sr     # pip install SpeechRecognition

#   Caso dê problema no pyAudio, instalar as seguintes linhas:
#   $ pip install pipwin
#   $ pipwin install pyaudio

#Cria um reconhecedor
r = sr.Recognizer()

#Ler o microfone
mic = sr.Microphone()

with mic as fonte:
    r.adjust_for_ambient_noise(fonte)
    print("Fale alguma coisa")
    audio = r.listen(fonte)
    print("Enviando para reconhecimento")
    try:
        text = r.recognize_google(audio, language = "pt-BR")
        print("Você disse: {}".format(text))
    except:
        print("Não entendi o que você disse.")
