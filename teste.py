class Aluno:
    def __init__(self, nome, sobrenome, endereco, filiacao, emailResponsavel, RA, segmento, curso, turma, nomeUsuario, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.__endereco = endereco
        self.filiacao = filiacao
        self.emailResponsavel = emailResponsavel
        self.RA = RA
        self.segmento = self.validar_segmento(segmento)
        self.curso = self.validar_curso(self.segmento, curso)
        self.turma = turma
        self.nomeUsuario = nomeUsuario
        self.email = email
        self.__senha = senha
        self.cursos_adicionais = [] 

    @staticmethod
    def validar_segmento(segmento):
        segmento = segmento.strip().lower() 
        if segmento not in ["em", "superior"]:
            raise ValueError("Segmento inválido! Use apenas 'em' ou 'superior'.")
        return segmento
    
    @staticmethod
    def validar_curso(segmento, curso):
        curso = curso.strip().lower()
        cursos_em = ["mecatrônica", "eletromecânica", "informática"]
        cursos_superior = ["bacharel em ciências da computação", "bacharel em pedagogia"]

        if segmento == "em":
            if curso not in cursos_em:
                raise ValueError(f"Curso inválido para EM! Escolha entre: {', '.join(cursos_em)}.")
        elif segmento == "superior":
            if curso not in cursos_superior:
                raise ValueError(f"Curso inválido para Superior! Escolha entre: {', '.join(cursos_superior)}.")
        return curso 
    
    def solicitar_transferencia(self):
        print("Solicitação de Transferência")
        novo_segmento = input("Novo segmento (EM/Superior): ").strip().lower()
        if novo_segmento not in ["em", "superior"]:
            print("Segmento inválido. Transferência não realizada.")
            return
        novo_curso = input("Novo curso: ").strip().lower()
        try:
            novo_curso = self.validar_curso(novo_segmento, novo_curso)
            self.segmento = novo_segmento
            self.curso = novo_curso
            print(f"Transferência realizada com sucesso para o curso {self.curso} no segmento {self.segmento.upper()}.")
        except ValueError as e:
            print(e)

    def adicionar_curso_simultaneo(self):
        if self.segmento != "superior":
            print("Somente alunos do segmento Superior podem cursar dois cursos simultaneamente.")
            return

        if len(self.cursos_adicionais) >= 1:
            print("Você já está cursando o máximo permitido de dois cursos simultâneos.")
            return

        novo_curso = input("Escolha um curso adicional (bacharel em ciências da computação ou bacharel em pedagogia): ").strip().lower()
        try:
            novo_curso = self.validar_curso("superior", novo_curso)
            if novo_curso in self.cursos_adicionais or novo_curso == self.curso:
                print("Você já está matriculado neste curso.")
                return
            self.cursos_adicionais.append(novo_curso)
            print(f"Curso adicional '{novo_curso}' adicionado com sucesso.")
        except ValueError as e:
            print(e)
    
    @property 
    def endereco(self):
        return self.__endereco
    
    @endereco.setter 
    def endereco(self, novoEndereco):
        self.__endereco = novoEndereco

    @property 
    def senha(self):
        return self.__senha
    
    @senha.setter 
    def senha(self, novaSenha):
        self.__senha = novaSenha

    def __str__(self):
        return f"RA: {self.RA}, Nome: {self.nome} {self.sobrenome}"

    def editar(self):
        self.nome = input("Novo nome: ")
        self.sobrenome = input("Novo sobrenome: ")
        print("Dados atualizados com sucesso!")

    def desativar(self):
        self.nome = f"[Inativo] {self.nome}"


class Professor:
    def __init__(self, nome, sobrenome, cpf, endereco, formacao, disciplinas, segmento, turmas, nomeUsuario, email, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.__cpf = cpf
        self.__endereco = endereco
        self.formacao = formacao
        self.disciplinas = disciplinas
        self.segmento = segmento
        self.turmas = turmas
        self.nomeUsuario = nomeUsuario
        self.email = email
        self.__senha = senha

    @property
    def cpf(self):
        return self.__cpf
   
    @cpf.setter
    def cpf(self, novoCpf):
        self.__cpf = novoCpf

    @property
    def endereco(self):
        return self.__endereco
   
    @endereco.setter
    def endereco(self, novoEndereco):
        self.__endereco = novoEndereco

    @property
    def senha(self):
        return self.__senha
   
    @senha.setter
    def senha(self, novaSenha):
        self.__senha = novaSenha

    def __str__(self):
        return f"CPF: {self.__cpf}, Nome: {self.nome} {self.sobrenome}"

    def editar(self):
        self.nome = input("Novo nome: ")
        self.sobrenome = input("Novo sobrenome: ")
        self.__endereco = input("Novo endereço: ")
        self.formacao = input("Nova formação: ")
        self.email = input("Novo email: ")
        self.__senha = input("Nova senha: ")
        print("Dados atualizados com sucesso!")

    def desativar(self):
        self.nome = f"[Inativo] {self.nome}"


class Turma:
    def __init__(self, nome, segmento, ano, curso, alunos=None, professores=None, disciplinas=None):
        if alunos is None:
            alunos = []
        if professores is None:
            professores = []
        if disciplinas is None:
            disciplinas = []

        self.nome = nome
        self.segmento = segmento
        self.ano = ano
        self.curso = curso
        self.alunos = alunos
        self.professores = professores
        self.disciplinas = disciplinas

    def __str__(self):
        return f"Nome: {self.nome}, Segmento: {self.segmento}, Curso: {self.curso}, Ano: {self.ano}, Alunos: {len(self.alunos)}"

    def editar(self):
        self.nome = input("Novo nome da turma: ")
        print("Turma atualizada com sucesso!")

    def desativar(self):
        self.nome = f"[Inativa] {self.nome}"

    def validar_turma(self):
        if self.segmento.lower() == "em" and len(self.alunos) != 20:
            raise ValueError("Turmas do Ensino Médio devem ter exatamente 20 alunos.")
        elif self.segmento.lower() == "superior" and len(self.alunos) < 5:
            raise ValueError("Turmas do Ensino Superior devem ter no mínimo 5 alunos.")
        
    def adicionar_aluno(self, aluno):
        if aluno.segmento != self.segmento or aluno.curso != self.curso:
            raise ValueError("Segmento ou curso do aluno incompatível com a turma.")
        self.alunos.append(aluno)
        self.validar_turma()


class Disciplina:
    def __init__(self, id_disciplina, descricao, segmento, professor_titular):
        self.id_disciplina = id_disciplina
        self.descricao = descricao
        self.segmento = segmento
        self.professor_titular = professor_titular

    def __str__(self):
        return f"ID: {self.id_disciplina}, Descrição: {self.descricao}"

    def editar(self):
        self.descricao = input("Nova descrição: ")
        print("Disciplina atualizada com sucesso!")

    def desativar(self):
        self.descricao = f"[Inativa] {self.descricao}"

alunos = []
professores = []
turmas = []
disciplinas = []


def inserir_aluno():
    try:
        nome = input("Nome: ")
        sobrenome = input("Sobrenome: ")
        endereco = input("Endereço: ")
        filiacao = input("Filiação: ")
        emailResponsavel = input("Email do responsável: ")
        RA = input("RA: ")
        while not RA.isdigit():
            print("RA deve ser um número. Tente novamente.")
            RA = input("RA: ")
        segmento = None
        while segmento not in ["em", "superior"]:
            segmento = input("Segmento (EM/Superior): ").strip().lower()
            if segmento not in ["em", "superior"]:
                print("Segmento inválido! Por favor, insira 'em' ou 'superior'.")
        curso = None
        while curso is None:
            if segmento == "em":
                curso = input("Curso (Mecatrônica/Eletromecânica/Informática): ").strip().lower()
            elif segmento == "superior":
                curso = input("Curso (Bacharel em ciências da computação/Bacharel em pedagogia): ").strip().lower()
            try:
                curso = Aluno.validar_curso(segmento, curso)  
            except ValueError as e:
                print(e)
                curso = None  
        turma = input("Turma: ")
        while not turma.isdigit():
            print("Turma deve ser um número. Tente novamente.")
            turma = input("Turma: ")
        nomeUsuario = input("Nome de usuário: ")
        email = input("Email: ")
        senha = input("Senha: ")
        aluno = Aluno(nome, sobrenome, endereco, filiacao, emailResponsavel, RA, segmento, curso, turma, nomeUsuario, email, senha)
        return aluno
    except ValueError as e:
        print(f"Erro ao cadastrar aluno: {e}")
        return None


def inserir_professor():
    nome = input("Nome: ")
    sobrenome = input("Sobrenome: ")
    cpf = input("CPF: ")
    while not cpf.isdigit():
        print("CPF deve ser um número. Tente novamente.")
        cpf = input("CPF: ")
    endereco = input("Endereço: ")
    formacao = input("Formação: ")
    disciplinas = input("Disciplinas (separadas por vírgula): ").split(",")
    segmento = None
    while segmento not in ["em", "superior"]:
        segmento = input("Segmento (EM/Superior): ").strip().lower()
        if segmento not in ["em", "superior"]:
            print("Segmento inválido! Por favor, insira 'em' ou 'superior'.")
    turmas = input("Turmas (separadas por vírgula): ").split(",")
    nomeUsuario = input("Nome de usuário: ")
    email = input("Email: ")
    senha = input("Senha: ")
    return Professor(nome, sobrenome, cpf, endereco, formacao, disciplinas, segmento, turmas, nomeUsuario, email, senha)


def inserir_turma():
    nome = input("Nome da turma: ")
    
    segmento = None
    while segmento not in ["em", "superior"]:
        segmento = input("Segmento (EM/Superior): ").strip().lower()
        if segmento not in ["em", "superior"]:
            print("Segmento inválido! Por favor, insira 'em' ou 'superior'.")

    curso = None
    while not curso:
        curso = input("Curso: ").strip().lower()
        try:
            curso = Aluno.validar_curso(segmento, curso)
        except ValueError as e:
            print(e)
            curso = None

    ano = input("Ano: ")
    while not ano.isdigit():
        print("O ano deve ser um número. Tente novamente.")
        ano = input("Ano: ")

    turma = Turma(nome, segmento, ano, curso)

    while True:
        if not alunos:
            print("Nenhum aluno cadastrado. Adicione alunos no menu principal.")
            break
        print("\nAlunos disponíveis para adicionar à turma:")
        for idx, aluno in enumerate(alunos, start=1):
            print(f"{idx}. {aluno.nome} {aluno.sobrenome} (Segmento: {aluno.segmento.upper()})")
        escolha = input("Escolha o número do aluno para adicionar ou pressione Enter para encerrar: ").strip()
        if escolha == "":
            break
        elif escolha.isdigit():
            idx = int(escolha) - 1
            if 0 <= idx < len(alunos):
                aluno = alunos[idx]
                try:
                    turma.adicionar_aluno(aluno)
                    print(f"Aluno {aluno.nome} {aluno.sobrenome} adicionado à turma.")
                except ValueError as e:
                    print(f"Erro: {e}")
            else:
                print("Número inválido. Escolha novamente.")
        else:
            print("Entrada inválida. Escolha novamente.")

    try:
        turma.validar_turma()
        print("Turma não foi criada!")
        return turma
    except ValueError as e:
        print(f"Erro ao criar turma: {e}")
        return None

def inserir_disciplina():
    id_disciplina = input("ID da disciplina: ")
    while not id_disciplina.isdigit():
        print("O ID da disciplina deve ser um número. Tente novamente.")
        id_disciplina = input("ID da disciplina: ")
    descricao = input("Descrição: ")
    segmento = None
    while segmento not in ["em", "superior"]:
        segmento = input("Segmento (EM/Superior): ").strip().lower()
        if segmento not in ["em", "superior"]:
            print("Segmento inválido! Por favor, insira 'em' ou 'superior'.")
    professor_titular = input("Professor titular: ")
    return Disciplina(id_disciplina, descricao, segmento, professor_titular)

def exibir_menu():
    print("\nMENU PRINCIPAL:")
    print("1. Gerenciar Alunos")
    print("2. Gerenciar Professores")
    print("3. Gerenciar Turmas")
    print("4. Gerenciar Disciplinas")
    print("0. Sair")
    return input("Escolha uma opção: ")

def submenu(entidade):
    print(f"\nGerenciar {entidade}:")
    print("1. Inserir")
    print("2. Editar")
    print("3. Excluir")
    print("4. Desativar")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def submenu_aluno():
    print("\nGerenciar Aluno:")
    print("1. Inserir")
    print("2. Editar")
    print("3. Excluir")
    print("4. Desativar")
    print("5. Solicitar Transferência")
    print("6. Adicionar Curso Simultâneo")
    print("0. Voltar")
    return input("Escolha uma opção: ")

def listar_entidades(lista, tipo):
    if not lista:
        print(f"Nenhum {tipo} cadastrado.")
        return None
    for idx, item in enumerate(lista, 1):
        print(f"{idx}. {item}")
    escolha = input("Escolha pelo número ou pressione Enter para voltar: ")
    return int(escolha) - 1 if escolha.isdigit() else None

def gerenciar_entidades(lista, entidade, inserir_func):
    while True:
        opcao = submenu(entidade)
        if opcao == "1":
            lista.append(inserir_func())
            print(f"{entidade} inserido(a) com sucesso!")
        elif opcao == "2":
            idx = listar_entidades(lista, entidade)
            if idx is not None:
                lista[idx].editar()
        elif opcao == "3":
            idx = listar_entidades(lista, entidade)
            if idx is not None:
                del lista[idx]
                print(f"{entidade} excluído(a) com sucesso!")
        elif opcao == "4":
            idx = listar_entidades(lista, entidade)
            if idx is not None:
                lista[idx].desativar()
                print(f"{entidade} desativado(a) com sucesso!")
        elif opcao == "0":
            break

def gerenciar_alunos():
    while True:
        opcao = submenu_aluno()
        if opcao == "1":
            novo_aluno = inserir_aluno()
            if novo_aluno is not None: 
                alunos.append(novo_aluno)
                print("Aluno inserido com sucesso!")
            else:
                print("Falha ao inserir aluno.")
        elif opcao == "2":
            idx = listar_entidades(alunos, "Aluno")
            if idx is not None:
                alunos[idx].editar()
        elif opcao == "3":
            idx = listar_entidades(alunos, "Aluno")
            if idx is not None:
                del alunos[idx]
                print("Aluno excluído com sucesso!")
        elif opcao == "4":
            idx = listar_entidades(alunos, "Aluno")
            if idx is not None:
                alunos[idx].desativar()
                print("Aluno desativado com sucesso!")
        elif opcao == "5":
            idx = listar_entidades(alunos, "Aluno")
            if idx is not None:
                alunos[idx].solicitar_transferencia()
        elif opcao == "6":
            idx = listar_entidades(alunos, "Aluno")
            if idx is not None:
                alunos[idx].adicionar_curso_simultaneo()
        elif opcao == "0":
            break

while True:
    opcao_principal = exibir_menu()
    if opcao_principal == "1":
        gerenciar_alunos ()
    elif opcao_principal == "2":
        gerenciar_entidades(professores, "Professor", inserir_professor)
    elif opcao_principal == "3":
        gerenciar_entidades(turmas, "Turma", inserir_turma)
    elif opcao_principal == "4":
        gerenciar_entidades(disciplinas, "Disciplina", inserir_disciplina)
    elif opcao_principal == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida! Tente novamente.")
av3t_amandaeemily.py
3° trimestre - Roteiro para desenvolvimento do produto
Shirlei Magali Vendrami
•
11 de out. de 2024 (editado: 6 de dez. de 2024)
100 pontos
Data de entrega: 8 de dez. de 2024, 23:59
Conforme definido na aula do dia 13/11, a entrega deverá ser realizada através da postagem do link do repositório no github.

3° trimestre - roteiro para o desenvolvimento do produto.pdf
PDF
Comentários da turma
