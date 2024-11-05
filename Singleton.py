class Configuracao:
    _instancia = None
    _configuracoes = {} 

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(Configuracao, cls).__new__(cls)
        return cls._instancia

    def __init__(self):

        if not hasattr(self, "_inicializado"):
            self._inicializado = True 
            self._configuracoes = {} 

    @staticmethod
    def obterInstancia():
        if Configuracao._instancia is None:
            Configuracao()
        return Configuracao._instancia

    def obterConfiguracao(self, chave):
        return self._configuracoes.get(chave, None)

    def definirConfiguracao(self, chave, valor):
        self._configuracoes[chave] = valor

config = Configuracao.obterInstancia()
config.definirConfiguracao("db_url", "localhost:7777")
config.definirConfiguracao("db_usuario", "admin")

print(config.obterConfiguracao("db_url"))
print(config.obterConfiguracao("db_usuario"))

config2 = Configuracao.obterInstancia()
print(config2.obterConfiguracao("db_url"))
print(config is config2)