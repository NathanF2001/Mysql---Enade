import mysql.connector
from mysql.connector import errorcode

class DAO():

    def __init__(self):

        self.cnx = mysql.connector.connect(user='your_user',password='your_password',
                              host='your_ip',database = "enade")
        self.cursor = self.cnx.cursor()


    def read_all(self):
        """
            Método que retorna as 100 primeiras linhas da tabela participante
        """

        self.cursor.execute("SELECT * from participante LIMIT 100")
        values = self.cursor.fetchall()

        return values

    def read_where(self,column,operation,value):
        """
            Método que retorna as 100 primeiras linhas da tabela participante com condição de alguma coluna
        """

        query = "SELECT * FROM participante WHERE %s %s %s LIMIT 100"%(column,operation,'%s')
        self.cursor.execute(query,(value,))
        values = self.cursor.fetchall()

        return values

    def fetch_situação_participante(self,values):
        """
            Método que procura id da tabela situação_participante de acordo com as suas colunas
        """

        self.cursor.execute("""
        SELECT id from situação_participante where Situação_financeira = 
        %(situação_financeira)s AND Situação_trabalho = %(situação_trabalho)s;""",values)
        find = self.cursor.fetchone()

        if (find == None):
            query = "INSERT INTO situação_participante(Situação_financeira,Situação_trabalho) VALUES (%(situação_financeira)s,%(situação_trabalho)s)"
            self.cursor.execute(query,values)     
            find= self.cursor.lastrowid
            self.save()
        else:
            find = find[0]

        return find

    def fetch_familia_participante(self,values):
        """
            Método que procura id da tabela familia_participante de acordo com as suas colunas
        """

        self.cursor.execute("""
        SELECT id from familia_participante where Escolaridade_pai = %(escolaridade_pai)s AND Escolaridade_mae = %(escolaridade_mae)s 
        AND Com_quem_participante_mora = %(com_quem_mora)s AND Quantidade_moradores_participante = %(qt_moradores_participante)s 
        AND Familia_cursou_superior = %(familia_cursou_superior)s AND Renda_familia = %(renda_familia)s;""",values)
        find = self.cursor.fetchone()

        if (find == None):
            query = """INSERT INTO familia_participante(Escolaridade_pai,Escolaridade_mae,Com_quem_participante_mora,
            Quantidade_moradores_participante,Familia_cursou_superior,Renda_familia) VALUES 
            (%(escolaridade_pai)s,%(escolaridade_mae)s,%(com_quem_mora)s,%(qt_moradores_participante)s,%(familia_cursou_superior)s,%(renda_familia)s)"""
            self.cursor.execute(query,values)     
            find = self.cursor.lastrowid
            self.save()
        else:
            find = find[0]

        return find

    def fetch_curso_participante(self,values):
        """
            Método que procura id da tabela curso de acordo com as suas colunas
        """

        self.cursor.execute("""
        SELECT id from curso where Ingressou_cota = %(ingresso_cota)s AND Motivo_ter_entrado_curso = %(motivo_curso)s AND 
        Razão_instituição = %(razao_instituicao)s AND Incetivou_graduação = %(incentivou_graduacao)s AND 
        Grupo_dificuldade = %(grupo_dificuldade)s""",values)
        find = self.cursor.fetchone()

        if (find == None):
            query = """INSERT INTO curso(Ingressou_cota,Motivo_ter_entrado_curso,Razão_instituição,Incetivou_graduação,Grupo_dificuldade) 
            VALUES (%(ingresso_cota)s,%(motivo_curso)s,%(razao_instituicao)s,%(incentivou_graduacao)s,%(grupo_dificuldade)s)"""
            self.cursor.execute(query,values)     
            find = self.cursor.lastrowid
            self.save()
        else:
            find = find[0]

        return find

    def fetch_preparacao_participante(self,values):
        """
            Método que procura id da tabela preparação_participante de acordo com as suas colunas
        """

        self.cursor.execute("""
        SELECT id from preparação_participante where Atividade_exterior = %(atividade_exterior)s AND Livro_lido_ano = %(livro_lido_ano)s AND 
        Horas_por_semana_estudou = %(horas_por_semana_estudou)s AND Estudou_idioma_estrangeiro = %(estudou_idioma_estrangeiro)s""",values)
        find = self.cursor.fetchone()

        if (find == None):
            query = """INSERT INTO preparação_participante(Atividade_exterior,Livro_lido_ano,Horas_por_semana_estudou,Estudou_idioma_estrangeiro) 
            VALUES (%(atividade_exterior)s,%(livro_lido_ano)s,%(horas_por_semana_estudou)s,%(estudou_idioma_estrangeiro)s)"""
            self.cursor.execute(query,values)
            find = self.cursor.lastrowid
            self.save()
        else:
            find = find[0]

        return find

    def fetch_escola_participante(self,values):
        """
            Método que procura id da tabela escola_participante de acordo com as suas colunas
        """

        self.cursor.execute("""
        SELECT id from escola_participante where Tipo_ensino_medio = %(tipo_ensino_medio)s AND 
        Modalidade_ensino_medio = %(modalidade_ensino_medio)s AND Regiao_concluiu_ensino_medio = %(regiao_concluiu_ensino_medio)s""",values)
        find = self.cursor.fetchone()

        if (find == None):
            query = """INSERT INTO escola_participante(Tipo_ensino_medio,Modalidade_ensino_medio,Regiao_concluiu_ensino_medio) 
            VALUES (%(tipo_ensino_medio)s,%(modalidade_ensino_medio)s,%(regiao_concluiu_ensino_medio)s)"""
            self.cursor.execute(query,values)     
            find = self.cursor.lastrowid
            self.save()
        else:
            find = find[0]

        return find

    def fetch_bolsa_participante(self,values):
        """
            Método que procura id da tabela bolsa_participante de acordo com as suas colunas
        """

        self.cursor.execute("""
        SELECT id from bolsa_participante where 
        Bolsa_de_estudo = %(bolsa_estudo)s AND Bolsa_permanência = %(bolsa_permanencia)s AND Bolsa_acadêmica = %(bolsa_academica)s""",values)
        find = self.cursor.fetchone()

        if (find == None):
            query = """INSERT INTO bolsa_participante(Bolsa_de_estudo,Bolsa_permanência,Bolsa_acadêmica) 
            VALUES (%(bolsa_estudo)s,%(bolsa_permanencia)s,%(bolsa_academica)s)"""
            self.cursor.execute(query,values)     
            find = self.cursor.lastrowid
            self.save()
        else:
            find = find[0]

        return find

    def search_situação_participante(self,id_sp):
        """
            Método que retorna as colunas de situação_participante de acordo com id
        """

        self.cursor.execute("""SELECT Situação_financeira,Situação_trabalho from situação_participante where id = %s;""",(id_sp,))
        find = self.cursor.fetchone()

        return find

    def search_familia_participante(self,id_fp):
        """
            Método que retorna as colunas de familia_participante de acordo com id
        """

        
        self.cursor.execute("""
        SELECT Escolaridade_pai,Escolaridade_mae,Com_quem_participante_mora,Quantidade_moradores_participante,Familia_cursou_superior,
        Renda_familia from familia_participante where id = %s;""",(id_fp,))
        find = self.cursor.fetchone()

        return find

    def search_curso_participante(self,id_cp):
        """
            Método que retorna as colunas de curso de acordo com id
        """

        self.cursor.execute("""SELECT Ingressou_cota, Motivo_ter_entrado_curso, Razão_instituição, Incetivou_graduação, Grupo_dificuldade from curso 
        where id = %s """,(id_cp,))
        find = self.cursor.fetchone()

        return find

    def search_preparacao_participante(self,id_pp):
        """
            Método que retorna as colunas de preparacao_participante de acordo com id
        """
        
        self.cursor.execute("""
        SELECT Atividade_exterior, Livro_lido_ano, Horas_por_semana_estudou,Estudou_idioma_estrangeiro from preparação_participante where 
        id = %s""",(id_pp,))
        find = self.cursor.fetchone()

        return find

    def search_escola_participante(self,id_ep):
        """
            Método que retorna as colunas de escola_participante de acordo com id
        """

        self.cursor.execute("""SELECT Tipo_ensino_medio,Modalidade_ensino_medio,Regiao_concluiu_ensino_medio from escola_participante where id = %s""",(id_ep,))
        find = self.cursor.fetchone()

        return find

    def search_bolsa_participante(self,id_bp):
        """
            Método que retorna as colunas de bolsa_participante de acordo com id
        """
        self.cursor.execute("""SELECT Bolsa_de_estudo, Bolsa_permanência, Bolsa_acadêmica from bolsa_participante where id = %s""",(id_bp,))
        find = self.cursor.fetchone()

        return find

    def insert_participante(self,values):
        """
            Método que insere um novo participante na tabela participante
        """

        query = """INSERT INTO participante(idade,Sexo,Nota_geral,Estado_civil,Raça,Nacionalidade,Familia_participante_id,
        Situação_participante_id,Curso_id,Escola_participante_id,Bolsa_participante_id,Preparação_participante_id) 
        VALUES (%(idade)s,%(sexo)s,%(nota)s,%(estado_civil)s,%(raça)s,%(nacionalidade)s,%(id_familia)s,%(id_situacao)s,%(id_curso)s,
        %(id_escola)s,%(id_bolsa)s,%(id_preparacao)s)"""
        self.cursor.execute(query,values)

        return self.cursor.lastrowid
        
    def delete_participante(self,id_participante):
        """
            Método que remove um participante na tabela participante
        """

        query = """DELETE FROM participante WHERE Id_participante = %s"""
        self.cursor.execute(query,(id_participante,))


    def update_participante_id(self,column,value,id_participante):
        """
            Método que atualiza os dados das chaves estrangeiras (id's) na tabela participante
        """

        query = "UPDATE participante SET %s = %s WHERE Id_participante = %s"%(column,"%(value)s","%(id_participante)s")
        self.cursor.execute(query,{"value": value,"id_participante": id_participante})

    def update_participante(self,value):
        """
            Método que atualiza os dados na tabela participante
        """

        query = """UPDATE participante SET idade = %(idade)s, Sexo = %(sexo)s,Nota_geral = %(nota)s,
        Estado_civil = %(estado_civil)s,Raça = %(raça)s,Nacionalidade = %(nacionalidade)s 
        WHERE Id_participante = %(id_participante)s"""
        self.cursor.execute(query,value)


    def save(self):
        """
            Método que salva alterações
        """
        self.cnx.commit()

    def dispose(self):
        self.cursor.close()
        self.cnx.close()