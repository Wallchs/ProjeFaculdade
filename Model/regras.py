class Usuarios(self):
    self.nome = nome
    self.rg = rg
    self.cpf = cpf
    self.idade = idade


    def validaUsuarios(self):
        if self.nome != nome:
            print(Usuário não cadastrado)

        if self.rg != rg:
            print(Usuário não possui RG)

        if self.cpf != cpf:
            print(Usuário não possui CPF)

        if self.idade < 18:
            print(Usuário é tem idade menor do que 18)
