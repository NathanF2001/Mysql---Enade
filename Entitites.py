class Participante():

    def __init__(self):
        self.idade = ""
        self.sexo = ""
        self.nota_geral = ""
        self.estado_civil = ""
        self.raca = ""
        self.nacionalidade = ""
        self.familia_participante = Familia()
        self.situacao_participante = Situacao()
        self.curso = Curso()
        self.escola_participante = Escola()
        self.bolsa_participante = Bolsa()
        self.preparacao_participante = Preparacao()
        self.id_participante = None
        self.id_familia = None
        self.id_situacao = None
        self.id_curso = None
        self.id_escola = None
        self.id_bolsa = None
        self.id_preparacao = None

    def set_idade(self,value):
        self.idade = value

    def set_sexo(self,value):
        self.sexo = value

    def set_nota_geral(self,value):
        self.nota_geral = value

    def set_estado_civil(self,value):
        self.estado_civil = value

    def set_raca(self,value):
        self.raca = value

    def set_nacionalidade(self,value):
        self.nacionalidade = value

    def anyempty(self):
        if (self.idade == "" or self.sexo == "" or self.nota_geral == "" or self.estado_civil == "" or self.raca == "" or 
        self.nacionalidade == ""):
            return True

        return False

    def transformList(self,list):
        self.idade = list[0]
        self.sexo = list[1]
        self.nota_geral = list[2]
        self.estado_civil = list[3]
        self.raca = list[4]
        self.nacionalidade = list[5]
        self.id_participante = list[6]
        self.id_familia = list[7]
        self.id_situacao = list[8]
        self.id_curso = list[9]
        self.id_escola = list[10]
        self.id_bolsa= list[11]
        self.id_preparacao = list[12]

    def to_map(self):
        return {
            "idade": self.idade,
            "sexo": self.sexo,
            "nota": self.nota_geral,
            "estado_civil": self.estado_civil,
            "raça": self.raca,
            "nacionalidade": self.nacionalidade,
            "id_participante": self.id_participante,
            "id_familia": self.id_familia,
            "id_situacao": self.id_situacao,
            "id_curso": self.id_curso,
            "id_escola": self.id_escola,
            "id_bolsa": self.id_bolsa,
            "id_preparacao": self.id_preparacao
        }

    def __str__(self):
        return f"""[
            idade: {self.idade},
            sexo: {self.sexo},
            nota_geral: {self.nota_geral},
            estado_civil: {self.estado_civil},
            raça: {self.raca},
            nacionalidade: {self.nacionalidade}
        ]"""

class Familia():

    def __init__(self):
        self.escolaridade_pai = ""
        self.escolaridade_mae = ""
        self.com_quem_participante_mora = ""
        self.quantidade_moradores = ""
        self.familia_cursou_superior = ""
        self.renda_familia = ""

    def set_escolaridade_pai(self,value):
        self.escolaridade_pai = value

    def set_escolaridade_mae(self,value):
        self.escolaridade_mae = value

    def set_com_quem_participante_mora(self,value):
        self.com_quem_participante_mora = value

    def set_quantidade_moradores(self,value):
        self.quantidade_moradores = value

    def set_familia_cursou_superior(self,value):
        self.familia_cursou_superior = value

    def set_renda_familia(self,value):
        self.renda_familia = value

    def anyempty(self):
        if (self.escolaridade_pai == "" or self.escolaridade_mae == "" or self.com_quem_participante_mora == "" or 
        self.quantidade_moradores == "" or self.familia_cursou_superior == "" or self.renda_familia == ""):
            return True
        
        return False

    def transformList(self,list):
        self.escolaridade_pai = list[0]
        self.escolaridade_mae = list[1]
        self.com_quem_participante_mora = list[2]
        self.quantidade_moradores = list[3]
        self.familia_cursou_superior = list[4]
        self.renda_familia = list[5]

    def to_map(self):
        return {
            "escolaridade_pai": self.escolaridade_pai,
            "escolaridade_mae": self.escolaridade_mae,
            "com_quem_mora": self.com_quem_participante_mora,
            "qt_moradores_participante": self.quantidade_moradores,
            "familia_cursou_superior": self.familia_cursou_superior,
            "renda_familia": self.renda_familia
        }

    def __str__(self):
        return f"""[
            escolaridade_pai: {self.escolaridade_pai},
            escolaridade_mae: {self.escolaridade_mae},
            com_quem_participante_mora: {self.com_quem_participante_mora},
            quantidade_moradores: {self.quantidade_moradores},
            familia_cursou_superior: {self.familia_cursou_superior},
            renda_familia: {self.renda_familia}
        ]"""

class Preparacao():

    def __init__(self):
        self.atividade_exterior = ""
        self.livro_lido_ano = ""
        self.horas_por_semana_estudada = ""
        self.estudou_idioma_estrangeiro = ""

    def set_atividade_exterior(self,value):
        self.atividade_exterior = value

    def set_livro_lido_ano(self,value):
        self.livro_lido_ano = value

    def set_horas_por_semana_estudada(self,value):
        self.horas_por_semana_estudada = value

    def set_estudou_idioma_estrangeiro(self,value):
        self.estudou_idioma_estrangeiro = value

    def anyempty(self):

        if (self.atividade_exterior == "" or self.livro_lido_ano == "" or self.horas_por_semana_estudada == "" 
        or self.estudou_idioma_estrangeiro == ""):
            return True
        return False

    def transformList(self,list):

        self.atividade_exterior = list[0]
        self.livro_lido_ano = list[1]
        self.horas_por_semana_estudada = list[2]
        self.estudou_idioma_estrangeiro = list[3]

    def to_map(self):
        return {
            "atividade_exterior": self.atividade_exterior,
            "livro_lido_ano": self.livro_lido_ano,
            "horas_por_semana_estudou": self.horas_por_semana_estudada,
            "estudou_idioma_estrangeiro": self.estudou_idioma_estrangeiro,
        }

    def __str__(self):
        return f"""[
            atividade_exterior: {self.atividade_exterior},
            livro_lido_ano: {self.livro_lido_ano},
            horas_por_semana_estudada: {self.horas_por_semana_estudada},
            estudou_idioma_estrangeiro: {self.estudou_idioma_estrangeiro},
        ]"""

class Situacao():

    def __init__(self):
        self.situacao_financeira = ""
        self.situacao_trabalho = ""

    def set_situacao_financeira(self,value):
        self.situacao_financeira = value

    def set_situacao_trabalho(self,value):
        self.situacao_trabalho = value

    def transformList(self,list):
        self.situacao_financeira = list[0]
        self.situacao_trabalho = list[1]

    def anyempty(self):
        if (self.situacao_financeira == "" or self.situacao_trabalho == ""):

            return True
        return False

    def to_map(self):
        return {
            "situação_financeira": self.situacao_financeira,
            "situação_trabalho": self.situacao_trabalho,
        }

    def __str__(self):
        return f"""[
            situacao_financeira: {self.situacao_financeira},
            situacao_trabalho: {self.situacao_trabalho},
        ]"""

class Curso():

    def __init__(self):
        self.ingresso_cota = ""
        self.motivo_curso = ""
        self.razao_instituicao = ""
        self.incentivou_graduacao = ""
        self.grupo_dificuldade = ""

    def set_ingresso_cota(self,value):
        self.ingresso_cota = value

    def set_motivo_curso(self,value):
        self.motivo_curso = value

    def set_razao_instituicao(self,value):
        self.razao_instituicao = value

    def set_incentivou_graduacao(self,value):
        self.incentivou_graduacao = value

    def set_grupo_dificuldade(self,value):
        self.grupo_dificuldade = value

    def anyempty(self):
        if (self.ingresso_cota == "" or self.motivo_curso == "" or self.razao_instituicao == "" or self.incentivou_graduacao == "" or 
        self.grupo_dificuldade == ""):
            
            return True

        return False

    def transformList(self,list):
        self.ingresso_cota = list[0]
        self.motivo_curso = list[1]
        self.razao_instituicao = list[2]
        self.incentivou_graduacao = list[3]
        self.grupo_dificuldade = list[4]

    def to_map(self):
        return {
            "ingresso_cota": self.ingresso_cota,
            "motivo_curso": self.motivo_curso,
            "razao_instituicao": self.razao_instituicao,
            "incentivou_graduacao": self.incentivou_graduacao,
            "grupo_dificuldade": self.grupo_dificuldade,
        }

    def __str__(self):
        return f"""[
            ingresso_cota: {self.ingresso_cota},
            motivo_curso: {self.motivo_curso},
            razao_instituicao: {self.razao_instituicao},
            incentivou_graduacao: {self.incentivou_graduacao},
            grupo_dificuldade: {self.grupo_dificuldade},
        ]"""

class Escola():

    def __init__(self):
        self.tipo_ensino_medio = ""
        self.modalidade_ensino_medio = ""
        self.regiao_ensino_medio = ""

    def set_tipo_ensino_medio(self,value):
        self.tipo_ensino_medio = value

    def set_modalidade_ensino_medio(self,value):
        self.modalidade_ensino_medio = value

    def set_regiao_ensino_medio(self,value):
        self.regiao_ensino_medio = value

    def transformList(self,list):
        self.tipo_ensino_medio = list[0]
        self.modalidade_ensino_medio = list[1]
        self.regiao_ensino_medio = list[2]

    def anyempty(self):
        if (self.tipo_ensino_medio == "" or self.modalidade_ensino_medio == "" or self.regiao_ensino_medio ==""):
            return True
        return False

    def to_map(self):
        return {
            'tipo_ensino_medio': self.tipo_ensino_medio,
            'modalidade_ensino_medio': self.modalidade_ensino_medio,
            'regiao_concluiu_ensino_medio': self.regiao_ensino_medio,
        }
    
    def __str__(self):
        return f"""[
            tipo_ensino_medio: {self.tipo_ensino_medio},
            modalidade_ensino_medio: {self.modalidade_ensino_medio},
            regiao_ensino_medio: {self.regiao_ensino_medio},
        ]"""

class Bolsa():

    def __init__(self):
        self.bolsa_estudos = ""
        self.bolsa_permanencia = ""
        self.bolsa_academica = ""

    def set_bolsa_estudos(self,value):
        self.bolsa_estudos = value

    def set_bolsa_permanencia (self,value):
        self.bolsa_permanencia  = value

    def set_bolsa_academica(self,value):
        self.bolsa_academica = value

    def anyempty(self):
        if (self.bolsa_academica == "" or self.bolsa_permanencia == "" or self.bolsa_academica == ""):

            return True

        return False

    def transformList(self,list):
        self.bolsa_estudos = list[0]
        self.bolsa_permanencia = list[1]
        self.bolsa_academica = list[2]

    def to_map(self):
        return {
            'bolsa_estudo': self.bolsa_estudos,
            'bolsa_permanencia': self.bolsa_permanencia,
            'bolsa_academica': self.bolsa_academica,
        }

    def __str__(self):
        return f"""[
            bolsa_estudos: {self.bolsa_estudos},
            bolsa_permanencia: {self.bolsa_permanencia},
            bolsa_academica: {self.bolsa_academica},
        ]"""
