class GameStudio:
    def __init__ (self, nome: str, link: str):
        self.nome = nome
        self.link = link
        self.__jogos = [] #convenção: __ indica privado
        self.__ativo = False # Atributo booleano privado __ativo, inicializado como False

    def adicionar_jogo(self, nome_jogo: str, esta_lancado: bool):
        """
        Adiciona um jogo à lista do GameStudio.
        'esta_lancado' deve ser um booleano (True para lançado, False para em desenvolvimento).
        """
        jogo_info = {"nome": nome_jogo, "lançado": esta_lancado}
        self.__jogos.append(jogo_info)
        status = "lançado" if esta_lancado else "em desenvolvimento"
        print(f"Jogo '{nome_jogo}' foi adicionado ao GameStudio '{self.nome}' e está {status}.")
        
    def acessar_jogo(self, nome_jogo: str):
        """
        Acessa e retorna as informações de um jogo específico pelo nome.
        Retorna None se o jogo não for encontrado.
        """
        for jogo in self.__jogos:
            if jogo["nome"] == nome_jogo:
                status = 'Lançado' if jogo["lançado"] else 'Em desenvolvimento'
                print(f"Informação do jogo '{nome_jogo}': Status - {status}")
                return jogo
        print(f"Jogo '{nome_jogo}' não encontrado no GameStudio '{self.nome}'.")
        return None
    
    def listar_jogos(self):
        """
        Lista todos os jogos do GameStudio, mostrando o nome e o status.
        """
        if not self.__jogos:
            print(f"Não há jogos cadastrados no GameStudio '{self.nome}'.")
            return

        print(f"---Jogos do GameStudio '{self.nome}':---")
        for jogo in self.__jogos:
            status = 'Lançado' if jogo["lançado"] else 'Em desenvolvimento'
            print(f"- Nome: {jogo['nome']} (Status: {status})")
        print("---Fim da lista de jogos---")

    def set_ativo(self, estado: bool):
        """
        Define o status de ativação do GameStudio.
        'estado' deve ser um booleano (True para ativo, False para inativo).
        """
        if isinstance(estado, bool):  # Corrigido de 'insistance' para 'isinstance'
            self.__ativo = estado  # Corrigido de 'self. ativo' para 'self.__ativo'
            status = "Ativo" if self.__ativo else "Inativo"
            print(f"O studio '{self.nome}' foi definido como {status}.")
        else:
            print("Erro: O estado deve ser um booleano (True ou False).")

    def get_ativo(self):
        """
        Retorna o status de ativação do GameStudio.
        """
        return self.__ativo

    def __str__(self):
        status_studio = "Ativo" if self.__ativo else "Inativo"
        return (f"Game Studio: {self.nome}\nLink: {self.link}\nStatus: {status_studio}")
    