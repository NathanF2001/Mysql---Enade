from Repository import DAO

class Controll():

    def __init__(self):
        pass

    def updateInfo(self,index,participante):
        pass

    def getAllrow(self):
        banco = DAO()
        values = banco.read_all()
        banco.dispose()

        return values

    def filter_row(self,coluna,operação,valor):

        banco = DAO()
        values = banco.read_where(coluna,operação,valor)
        banco.dispose()


        return values
        
    def get_allInfoParticipante(self,participante):
        banco = DAO()

        familia_participante = banco.search_familia_participante(participante.id_familia)
        situacao_participante = banco.search_situação_participante(participante.id_situacao)
        curso_participante = banco.search_curso_participante(participante.id_curso)
        preparacao_participante = banco.search_preparacao_participante(participante.id_preparacao)
        escola_participante = banco.search_escola_participante(participante.id_escola)
        bolsa_participante = banco.search_bolsa_participante(participante.id_bolsa)

        participante.familia_participante.transformList(familia_participante)
        participante.situacao_participante.transformList(situacao_participante)
        participante.curso.transformList(curso_participante)
        participante.preparacao_participante.transformList(preparacao_participante)
        participante.escola_participante.transformList(escola_participante)
        participante.bolsa_participante.transformList(bolsa_participante)

        banco.dispose()

        return participante

    def check_empty(self,participante):
        if (participante.anyempty() or participante.familia_participante.anyempty() or participante.situacao_participante.anyempty() or
        participante.curso.anyempty() or participante.preparacao_participante.anyempty() or participante.escola_participante.anyempty() 
        or participante.bolsa_participante.anyempty()):
            return True

        return False
    
    def insert_data(self, participante):

        banco = DAO()
        participante.id_familia = banco.fetch_familia_participante(participante.familia_participante.to_map())
        participante.id_situacao = banco.fetch_situação_participante(participante.situacao_participante.to_map())
        participante.id_curso = banco.fetch_curso_participante(participante.curso.to_map())
        participante.id_preparacao = banco.fetch_preparacao_participante(participante.preparacao_participante.to_map())
        participante.id_escola = banco.fetch_escola_participante(participante.escola_participante.to_map())
        participante.id_bolsa = banco.fetch_bolsa_participante(participante.bolsa_participante.to_map())

        id_participante = banco.insert_participante(participante.to_map())

        banco.save()
        banco.dispose()

    def remove_data(self,id_participante):
        banco = DAO()

        banco.delete_participante(id_participante)

        banco.save()
        banco.dispose()

    def update_data(self,participante):

        banco = DAO()

        id_familia = banco.fetch_familia_participante(participante.familia_participante.to_map())
        id_situacao = banco.fetch_situação_participante(participante.situacao_participante.to_map())
        id_curso = banco.fetch_curso_participante(participante.curso.to_map())
        id_preparacao = banco.fetch_preparacao_participante(participante.preparacao_participante.to_map())
        id_escola = banco.fetch_escola_participante(participante.escola_participante.to_map())
        id_bolsa = banco.fetch_bolsa_participante(participante.bolsa_participante.to_map())

        if id_familia != participante.id_familia:
            banco.update_participante_id("Familia_participante_id",id_familia,participante.id_participante)
            participante.id_familia = id_familia
        if id_situacao != participante.id_situacao:
            banco.update_participante_id("Situação_participante_id",id_situacao,participante.id_participante)
            participante.id_situacao = id_situacao
        if id_curso != participante.id_curso:
            banco.update_participante_id("Curso_id",id_curso,participante.id_participante)
            participante.id_curso = id_curso
        if id_preparacao != participante.id_preparacao:
            banco.update_participante_id("Preparação_participante_id",id_preparacao,participante.id_participante)
            participante.id_preparacao = id_preparacao
        if id_escola != participante.id_escola:
            banco.update_participante_id("Escola_participante_id",id_escola,participante.id_participante)
            participante.id_escola = id_escola
        if id_bolsa != participante.id_bolsa:
            banco.update_participante_id("Bolsa_participante_id",id_bolsa,participante.id_participante)
            participante.id_bolsa = id_bolsa

        banco.update_participante(participante.to_map())

        banco.save()
        banco.dispose()

        return participante