# AULA 14

class Pessoa:
    def __init__(self, nome, idade, endereco, cpf, sexo):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco
        self.cpf = cpf
        self.sexo = sexo

    def resumo(self):
        return f'Nome: {self.nome}, Idade: {self.idade}, Endereço: {self.endereco}, CPF: {self.cpf}, Sexo: {self.sexo}'


class Pai(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, sexo, esposa):
        super().__init__(nome, idade, endereco, cpf, sexo)
        self.esposa = esposa
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def resumo(self):
        return super().resumo() + f', Esposa: {self.esposa}, Filhos: {[filho.nome for filho in self.filhos]}'


class Mae(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, sexo, esposo):
        super().__init__(nome, idade, endereco, cpf, sexo)
        self.esposo = esposo
        self.filhos = []

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def resumo(self):
        return super().resumo() + f', Esposo: {self.esposo}, Filhos: {[filho.nome for filho in self.filhos]}'


class Filho(Pessoa):
    def __init__(self, nome, idade, endereco, cpf, sexo, pai, mae):
        super().__init__(nome, idade, endereco, cpf, sexo)
        self.pai = pai
        self.mae = mae

    def resumo(self):
        return super().resumo() + f', Pai: {self.pai.nome}, Mãe: {self.mae.nome}'
        
pai = Pai('João', 45, 'Aparecida de Goiânia', '123.456.789-01', 'Masculino', 'Maria')
mae = Mae('Maria', 37, 'Aparecida de Goiânia', '987.654.321-01', 'Feminino', 'João')
filho = Filho('Lucas', 19, 'Aparecida de Goiânia', '123.321.456-65', 'Masculino', pai, mae)

pai.adicionar_filho(filho)
mae.adicionar_filho(filho)

print(pai.resumo())
print(mae.resumo())
print(filho.resumo())

# Prof., usei uma ajuda da IA e vi q tem muitas maneiras de fzr o msm programa...
