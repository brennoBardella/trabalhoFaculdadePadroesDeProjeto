class AppleTV:
    def on(self):
        print("Apple TV ligada")

    def off(self):
        print("Apple TV desligada")

    def play(self, movie):
        print(f"Reproduzindo '{movie}' na Apple TV")

    def stop(self):
        print("Reprodução parada na Apple TV")

    def connectToNetwork(self, network):
        print(f"Apple TV conectada à rede '{network}'")

class TV:
    def on(self):
        print("TV ligada")

    def off(self):
        print("TV desligada")

    def setInputChannel(self, channel):
        print(f"Canal de entrada ajustado para {channel} na TV")

class SoundSystem:
    def on(self):
        print("Sistema de som ligado")

    def off(self):
        print("Sistema de som desligado")

    def setVolume(self, volume):
        print(f"Volume ajustado para {volume} no sistema de som")

class HomeEntertainmentFacade:
    def __init__(self):
        self.apple_tv = AppleTV()
        self.tv = TV()
        self.sound_system = SoundSystem()

    def turnOn(self):
        print("Ligando todos os dispositivos...")
        self.tv.on()
        self.sound_system.on()
        self.sound_system.setVolume(15)
        self.apple_tv.on()
        self.apple_tv.connectToNetwork("Home WiFi")
        print("Todos os dispositivos ligados")

    def turnOff(self):
        print("Desligando todos os dispositivos...")
        self.apple_tv.off()
        self.tv.off()
        self.sound_system.off()
        print("Todos os dispositivos desligados")

    def watchMovie(self, movie):
        print(f"Iniciando o filme '{movie}'...")
        self.tv.setInputChannel("HDMI1")
        self.apple_tv.play(movie)
        print(f"Filme '{movie}' pronto para assistir!")

    def endMovie(self):
        print("Encerrando o filme...")
        self.apple_tv.stop()
        print("Filme encerrado")

home_entertainment = HomeEntertainmentFacade()
home_entertainment.turnOn()
home_entertainment.watchMovie("Inception")
home_entertainment.endMovie()
home_entertainment.turnOff()
