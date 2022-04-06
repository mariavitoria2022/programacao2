class Pessoa:

    # construtor com parâmetros opcionais
    def __init__(self, nome="", email="", tel=""):
        self.nome = nome
        self.email = email
        self.telefone = tel

    # método que expressa o objeto em forma de string        
    def __str__(self):
        return "\n" + self.nome + ", email: " + \
        self.email + ", " + self.telefone

if __name__ == "__main__":

    # criar objetos e informar alguns valores depois
    maria = Pessoa()    
    maria.nome = "Maria Vitoria da Silva"
    maria.email = "marparkminiekookiesilva@gmail.com"
 
    # criar objeto já informando valores
    marlete = Pessoa("Marlete de Andrade da Silva", "marlete@gmail.com", "33342473")
    
    # criar objeto e informar alguns valores
    chico = Pessoa("Francisco da Silva", "chico@gmail.com")

    # exibir os dados de teste
    print(maria, marlete, chico)