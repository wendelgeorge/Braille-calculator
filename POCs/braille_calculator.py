# Author: Wendel George
# Date: 12/09/2021
# Description: Calculator in Braille

import pyttsx3  # pip install pyttsx3

engine = pyttsx3.init()

engine.say("Insira um valor: ")
engine.runAndWait()

n1 = int(input('Insira um valor: '))

engine.say("Insira um outro valor: ")
engine.runAndWait()

n2 = int(input('Insira um outro valor: '))

print('A multiplicação de {} e {} é igual a: {}'.format(n1, n2, n1*n2))

engine.say('A multiplicação de {} e {} é igual a: {}'.format(n1, n2, n1*n2))
engine.runAndWait()

engine.stop()

