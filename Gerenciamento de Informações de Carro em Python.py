# Definição da classe 'carro'
class carro:
    # Método construtor da classe
    # Este método é chamado automaticamente quando um novo objeto é criado a partir desta classe
    def __init__(self, marca, portas, placa, rodou):
        # Atributos da classe
        # Estes são os dados que cada objeto criado a partir desta classe irá armazenar
        self.marca = marca
        self.portas = portas
        self.placa = placa
        self.rodou = rodou

    # Método da classe para exibir as informações do carro
    def exibir(self):
        print(self.marca, self.portas, self.placa, self.rodou)

    # Método da classe para exibir a quilometragem do carro
    def quanto_rodou(self):
        print(f"Já rodou {self.rodou}")

    # Método da classe para exibir o número de portas do carro
    def portasnbr(self):
        print(f"Este carro tem {self.portas} portas")

    # Método da classe para indicar que o carro está funcionando
    def funcionando(self):
        print("Está funcionando")

# Criação de um objeto da classe 'carro'
# Um novo objeto 'carro1' é criado com a marca "Jeep", 4 portas, a placa "94irt4" e que rodou "300KM"
carro1 = carro("Jeep", "4", "94irt4", "300KM")

# Chamada de método do objeto
# O método 'exibir()' é chamado no objeto 'carro1', que imprime as informações do carro
carro1.exibir()