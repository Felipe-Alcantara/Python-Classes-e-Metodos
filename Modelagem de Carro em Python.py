# Classe em Python
# Uma classe é um modelo para criar objetos em Python. Ela define atributos e métodos que serão compartilhados por todos os objetos criados a partir desta classe.

# Definição da classe 'car'
class car:
    # Método construtor da classe
    # Este método é chamado automaticamente quando um novo objeto é criado a partir desta classe
    def __init__(self, cor, modelo, preco):
        # Atributos da classe
        # Estes são os dados que cada objeto criado a partir desta classe irá armazenar
        self.cor = cor
        self.modelo = modelo
        self.preco = preco

    # Método da classe
    # Este é um comportamento que todos os objetos criados a partir desta classe podem realizar
    def ligar(self):
        print(f"Ligando o carro: {self.modelo}")

# Criação de um objeto da classe 'car'
# Um novo objeto 'musta' é criado com a cor "preto", o modelo "mustang" e o preço "10000"
musta = car("preto", "mustang", "10000")

# Chamada de método do objeto
# O método 'ligar()' é chamado no objeto 'musta', que imprime "Ligando o carro: mustang"
musta.ligar()
