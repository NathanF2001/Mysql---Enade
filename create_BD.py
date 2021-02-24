import mysql.connector
from mysql.connector import errorcode
import pandas as pd
import numpy as np

cnx = mysql.connector.connect(user='root',password='!user123#',
                              host='127.0.0.1',database = "enade")
cursor = cnx.cursor()

dataset = pd.read_csv("F:\Entrega Banco de dados\Create BD\dataset.csv",sep = ",")
dataset.replace({"M": "Masculino","F": "Feminino"})


def insert_situação_participante(values):

    cursor.execute("""
    SELECT id from situação_participante where Situação_financeira = %s AND Situação_trabalho = %s;""",values)
    find = cursor.fetchone()
    if (find == None):
        query = "INSERT INTO situação_participante(Situação_financeira,Situação_trabalho) VALUES (%s,%s)"
        cursor.execute(query,values)     
        situacao_id = cursor.lastrowid
    else:
        situacao_id = find[0]
    cnx.commit()
    return situacao_id

def insert_familia_participante(values):

    cursor.execute("""
    SELECT id from famila_participante where 
    Escolaridade_pai = %s AND Escolaridade_mae = %s AND Com_quem_participante_mora = %s AND
    Quantidade_moradores_participante = %s AND Familia_cursou_superior = %s AND Renda_familia = %s;""",values)
    find = cursor.fetchone()
    if (find == None):
        query = """INSERT INTO famila_participante(Escolaridade_pai,Escolaridade_mae,Com_quem_participante_mora,
        Quantidade_moradores_participante,Familia_cursou_superior,Renda_familia) VALUES (%s,%s,%s,%s,%s,%s)"""
        cursor.execute(query,values)     
        familia_id = cursor.lastrowid
    else:
        familia_id = find[0]
    cnx.commit()
    return familia_id

def insert_curso_participante(values):

    cursor.execute("""
    SELECT id from curso where 
    Ingressou_cota = %s AND Motivo_ter_entrado_curso = %s AND Razão_instituição = %s AND
    Incetivou_graduação = %s AND Grupo_dificuldade = %s""",values)
    find = cursor.fetchone()
    if (find == None):
        query = """INSERT INTO curso(Ingressou_cota,Motivo_ter_entrado_curso,Razão_instituição,Incetivou_graduação,Grupo_dificuldade) 
        VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(query,values)     
        curso_id = cursor.lastrowid
    else:
        curso_id = find[0]
    cnx.commit()
    return curso_id

def insert_preparacao_participante(values):
    cursor.execute("""
    SELECT id from preparação_participante where 
    Atividade_exterior = %s AND Livro_lido_ano = %s AND Horas_por_semana_estudou = %s AND
    Estudou_idioma_estrangeiro = %s""",values)
    find = cursor.fetchone()
    if (find == None):
        query = """INSERT INTO preparação_participante(Atividade_exterior,Livro_lido_ano,Horas_por_semana_estudou,Estudou_idioma_estrangeiro) 
        VALUES (%s,%s,%s,%s)"""
        cursor.execute(query,values)     
        preparacao_id = cursor.lastrowid
    else:
        preparacao_id = find[0]
    cnx.commit()
    return preparacao_id

def insert_escola_participante(values):
    cursor.execute("""
    SELECT id from escola_participante where 
    Tipo_ensino_medio = %s AND Modalidade_ensino_medio = %s AND Regiao_concluiu_ensino_medio = %s""",values)
    find = cursor.fetchone()
    if (find == None):
        query = """INSERT INTO escola_participante(Tipo_ensino_medio,Modalidade_ensino_medio,Regiao_concluiu_ensino_medio) 
        VALUES (%s,%s,%s)"""
        cursor.execute(query,values)     
        escola_id = cursor.lastrowid
    else:
        escola_id = find[0]
    cnx.commit()
    return escola_id

def insert_bolsa_participante(values):
    cursor.execute("""
    SELECT id from bolsa_participante where 
    Bolsa_de_estudo = %s AND Bolsa_permanência = %s AND Bolsa_acadêmica = %s""",values)
    find = cursor.fetchone()
    if (find == None):
        query = """INSERT INTO bolsa_participante(Bolsa_de_estudo,Bolsa_permanência,Bolsa_acadêmica) 
        VALUES (%s,%s,%s)"""
        cursor.execute(query,values)     
        bolsa_id = cursor.lastrowid
    else:
        bolsa_id = find[0]
    cnx.commit()
    return bolsa_id


def insert_participante(values):

    query = """INSERT INTO participante(idade,Sexo,Nota_geral,Estado_civil,Raça,Nacionalidade,Famila_participante_id,
    Situação_participante_id,Curso_id,Escola_participante_id,Bolsa_participante_id,Preparação_participante_id)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(query,values)     
    cnx.commit()
    

def inserir_dados(row):

    
    familia = (row["Escolaridade_pai"],row["Escolaridade_mae"],row["Com_quem_mora"],row["Qt_moradores_participante"],
    row["Familia_curso_superior"],row["Renda_família"])
    curso = (row["Ingresso_cota"],row["Motivo_curso"],row["Razao_instituicao"],row["Incentivou_graduação"],row["Grupo_dificuldade"])
    bolsa = (row["Bolsa_de_estudos"],row["Bolsa_permanência"],row["Bolsa_academica"])
    escola = (row["Tipo_ensino_medio"],row["Modalidade_ensino_medio"],row["Regiao_ensino_medio"])
    preparacao = (row["Atividade_exterior"],row["Livros_lidos"],row["horas/semana estudadas"],row["Estudo_idioma_estrangeiro"],)
    situacao = (row["Situação_financeira"],row["Situação_trabalho"])

    id_situacao = insert_situação_participante(situacao)
    id_familia = insert_familia_participante(familia)
    id_curso = insert_curso_participante(curso)
    id_preparacao = insert_preparacao_participante(preparacao)
    id_escola = insert_escola_participante(escola)
    id_bolsa = insert_bolsa_participante(bolsa)

    participante = (row["Idade"],row["Sexo"],row["Nota"],row["Estado_civil"],row["Raça/cor"],row["Nacionalidade"],id_familia,id_situacao,
    id_curso,id_escola,id_bolsa,id_preparacao)

    insert_participante(participante)



def popular():
    dataset.apply(lambda x: inserir_dados(x),axis = 1)

popular()

cnx.commit()
cursor.close()
cnx.close()



"""cnx = mysql.connector.connect(user='root',password='!user123#',
                              host='127.0.0.1',database = "enade")
cursor = cnx.cursor()






cnx.commit()

cursor.close()
cnx.close()"""
