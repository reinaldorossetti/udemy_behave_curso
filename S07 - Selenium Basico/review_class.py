# Criamos uma classe com a palavra reservada "class", em seguida o nome da classe, e ":" no final


class NomeDaClasse:

    propriedade = 0  # variavel da classe

    def __init__(self, valor):
        self.variavel_de_instancia = valor

    def metodo(self):
        variavel_local = 1000  # somente enxergo dentro do metodo
        print(self.propriedade)  # se tiver só propriedade aqui seria uma variavel local
        print(self.variavel_de_instancia)
        print(variavel_local)


# Realiza a Instancia da classe, para ter acesso aos métodos.
# Atraves __init__ passamos o valor direto na instancia da classe.

objeto = NomeDaClasse(100)
objeto.propriedade = 10  # Mudando o valor da variavel da classe.
objeto.metodo()  # Realizando acesso a funcao/metodo da classe.

# resultado: 10, 100, 1000
