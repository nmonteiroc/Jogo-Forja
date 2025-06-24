class Pessoa:
    def __init__ (self, nome: str, email: str, endereco: str):
        self.nome = nome
        self.email = email
        self.endereco = endereco
        self.habilidades = [] # lista de habilidades deve ser vazia inicialmente

    def adicionar_habilidade(self, habilidade: str):
        if habilidade not in self.habilidades:
            self.habilidades.append(habilidade)
            print(f'Habilidade {habilidade} adicionada a {self.nome}')
        else:
            print(f'Habilidade {habilidade} já existente para {self.nome}')

    def listar_habilidades(self):
        return self.habilidades
        
    def __str__ (self):
        # formata a lista de habilidades em uma string separada por vírgulas
        habilidades_str = ', '.join(self.habilidades) if self.habilidades else 'Nenhuma habilidade'
        # garante que se a lista de habilidades estiver vazia, a mensagem "Nenhuma habilidade" será exibida em vez de uma string vazia
        return f'Nome: {self.nome}\nHabilidades: {habilidades_str}'

