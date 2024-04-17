# Definição da classe 'Computador'
class Computador:
    # Método construtor da classe
    # Este método é chamado automaticamente quando um novo objeto é criado a partir desta classe
    def __init__(self, marca, ram, placa):
        # Atributos da classe
        # Estes são os dados que cada objeto criado a partir desta classe irá armazenar
        self.marca = marca
        self.ram = ram
        self.placa = placa

    # Método da classe para ligar o computador
    def ligar(self):
        print("Estou ligando")

    # Método da classe para desligar o computador
    def desligar(self):
        print("estou desligando")

    # Método da classe para exibir as informações do computador
    def exibir(self):
        print(self.marca, self.ram, self.placa)

# Criação de objetos da classe 'Computador'
# Três novos objetos são criados com diferentes marcas, quantidades de RAM e placas gráficas
computador1 = Computador("Asus", "12GB", "GTX 650 1GB")
computador2 = Computador("Gigabyte", "30GB", "GTX 950 TI")
computador3 = Computador("AMD", "64GB", "RTX 1080 Super")

# Impressão das informações de cada computador
print(computador1.marca, computador1.ram, computador1.placa)
print(computador2.marca, computador2.ram, computador2.placa)
print(computador3.marca, computador3.ram, computador3.placa)

print()

# Criação de um novo objeto da classe 'Computador' e exibição de suas informações usando o método 'exibir'
comp4 = Computador("Aa", "349GB", "GTXSLa")
comp4.exibir()
