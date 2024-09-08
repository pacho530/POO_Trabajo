# registro de usuario
import speech_recognition as sr
class Usuario:
    def __init__(self):
        self.nombre = None
        self.fecha_de_nacimiento = None
        self.estado_civil = None

    def reconocimiento_de_voz(self):
        recognizer = sr.recognizers()
        with sr.Microphone() as source:
            print("hable ahora...")
            audio = recognizer.listen(source)




