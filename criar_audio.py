import speech_recognition as sr
#aqui voce cria o arquivo de audio.
rec = sr.Recognizer()
#use (seu mic padrao).Para o padrao do pc, deixe em branco ou use "device_index=0"
with sr.Microphone(device_index=0) as microfone:
    rec.adjust_for_ambient_noise(microfone)
    print("Pode começar a falar")
    audio = rec.listen(microfone)

# salvar o audio
with open("audio.wav", "wb") as arquivo:
    arquivo.write(audio.get_wav_data())

# extensões audio suportadas desta biblioteca
# raw
# wav
# aiff
# flac
#Se precisar reconhecer outras extensões ,usar outra biblioteca do Python para converter
