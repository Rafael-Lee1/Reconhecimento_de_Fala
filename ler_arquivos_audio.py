import speech_recognition as sr
#aqui voce le os arquivos de audio, transformando em textos.
rec = sr.Recognizer()
#nome do "seu arquivo de audio",salvo na pasta do projeto
with sr.AudioFile("audio.wav") as arquivo_audio:
    audio = rec.record(arquivo_audio)
    texto = rec.recognize_google(audio, language="pt-BR") #importante definir a lingua
    print(texto)