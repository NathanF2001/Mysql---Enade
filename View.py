from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Entitites import *
from Controll import *

class Screen():

    def __init__(self,interface):
        self.interface = interface
        self.controll = Controll()
        self.participante = Participante()
        self.List_columns()
        self.filter_options()
        self.buttons()
        #self.inputs_data()
        pass

    def List_columns(self):
        frame1 = LabelFrame(self.interface,text= "Visualização")
        frame1.place(height=250,width =980)

        self.tree = ttk.Treeview(frame1)
        self.tree.place(height = 220,width = 980)

        treescrolly =   Scrollbar(frame1,orient ="vertical",command = self.tree.yview)
        treescrollx = Scrollbar(frame1,orient="horizontal",command= self.tree.xview)
        self.tree.configure(xscrollcommand =treescrollx.set,yscrollcommand =treescrolly.set)
        treescrollx.pack(side="bottom",fill="x")
        treescrolly.pack(side="right",fill="y")

    def filter_options(self):

        frame_filter = Frame(self.interface)
        frame_filter.place(height = 100,width = 980,y = 250)

        coluna = ""
        input_coluna = self.dropdown("Coluna",['Idade','Sexo','Nota_geral','Estado_civil','Raça','Nacionalidade',"Id_participante",
        'Famila_participante_id','Situação_participante_id','Curso_id','Escola_participante_id','Bolsa_participante_id',
        'Preparação_participante_id'],frame_filter,0,0.01,rely_dd = 0.20)


        operador = ""
        input_operador = self.dropdown("Operador",["=",">",">=","<","<="],frame_filter,0,0.33,rely_dd = 0.20)

        variavel = ""
        variavel_label = Label(frame_filter,text ="Valor",font = ('calibre',12,"bold"))
        variavel_input = Entry(frame_filter,textvariable = variavel ,font = ('calibre',12),width = 20)
        variavel_label.place(y=0,relx = 0.66,rely = 0.20)
        variavel_input.place(y = 25,relx = 0.66,rely = 0.20)

        button_filtrar = Button(frame_filter, text = "Filtrar",font = ("calibri",16,"bold"),
        command = lambda: self.filter_action(input_coluna.get(),input_operador.get(),variavel_input.get()))
        button_filtrar.place(height = 30,width = 100,relx = 0.87,rely = 0.42)



    def filter_action(self,coluna,operation,valor):
        
        valores = self.controll.filter_row(coluna,operation,valor)

        self.update_tree(valores)
        

    def update_tree(self,items):

        self.tree.delete(*self.tree.get_children())
        for row in items:
            self.tree.insert("","end",values = row)

    
    def get_data(self):
        curItem = self.tree.selection()

        if curItem == ():
            return None

        # Pegar valores da linha selecionada
        values_participante = self.tree.item(curItem)["values"]
        self.participante.transformList(values_participante)

        return curItem

    def get_InfoParticipante(self):

        curItem = self.get_data()
        if curItem ==None:
            return None
        self.participante = self.controll.get_allInfoParticipante(self.participante)

        return curItem


    def selectItem(self):
        
        curItem = self.tree.selection()
        values = self.tree.item(curItem)["values"]
        self.participante.set_idade(values[0])
        self.participante.set_sexo(values[1])
        self.participante.set_nota_geral(values[2])
        self.participante.set_estado_civil(values[3])
        self.participante.set_raca(values[4])
        self.participante.set_nacionalidade(values[5])
        index = self.tree.index(curItem)
        self.update_data(curItem)

    def buttons(self):

        frame1 = Frame(self.interface)
        frame1.place(height = 50,width = 980,y = 350)

        button_adicionar = Button(frame1, text = "Adicionar participante",font = ("calibri",16,"bold"),
        command= lambda: self.inputs_data())
        button_adicionar.place(height = 30,width = 230,relx = 0.01,rely = 0.01)

        button_consulta = Button(frame1, text = "Consultar participante",font = ("calibri",16,"bold"),command = lambda: self.read_data())
        button_consulta.place(height = 30,width = 230,relx = 0.25,rely = 0.01)

        button_deletar = Button(frame1, text = "Remover participante",font = ("calibri",16,"bold"),command = lambda: self.remove_item())
        button_deletar.place(height = 30,width = 230,relx = 0.49,rely = 0.01)

        button_atualizar = Button(frame1, text = "Atualizar participante",font = ("calibri",16,"bold"),
        command = lambda: self.update_data())
        button_atualizar.place(height = 30,width = 230,relx = 0.73,rely = 0.01)

    def remove_item(self):
        item = self.get_data()
        if item == None:
            return messagebox.showinfo(title = "Não foi possível procurar", message = "Selecione um participante")

        #Operation BD
        self.controll.remove_data(self.participante.id_participante)

        self.tree.delete(item)

        messagebox.showinfo(title = "Sucesso", message = "Dados removido com sucesso")

    def inputs_data(self):
        self.participante = Participante()

        self.frame = Frame(self.interface)
        self.frame.place(height = 250,width = 980,y=400)

        self.notebook = ttk.Notebook(self.frame)

        frame_participante = self.form_participante()
        frame_familia_participate = self.form_familia()
        frame_preparacao = self.form_preparacao()
        frame_curso = self.form_curso()
        frame_escola = self.form_escola_participante()
        frame_bolsa = self.form_bolsa()
        frame_situacao = self.form_situacao()

        self.notebook.add(frame_participante,text="Participante")
        self.notebook.add(frame_familia_participate,text = "Família")
        self.notebook.add(frame_preparacao,text = "Preparação")
        self.notebook.add(frame_curso,text = "Curso")
        self.notebook.add(frame_escola,text = "Escola")
        self.notebook.add(frame_bolsa,text = "Bolsa")
        self.notebook.add(frame_situacao,text = "Situação")

        self.notebook.place(height = 200,width = 980)

        button = Button(self.frame,text = "Adicionar",font = ("calibri",16,"bold"),command= lambda: self.add_participante())
        button.place(height = 30,width = 100,x =850,y = 160)

    def add_participante(self):

        validate = self.controll.check_empty(self.participante)
        if (validate):
            messagebox.showinfo(title = "Não foi possível adicionar", message = "Preencha todos os campos")
            return 
        
        self.controll.insert_data(self.participante)

        messagebox.showinfo(title = "Sucesso", message = "Dados adicionados com sucesso")


    def update_data(self):

        self.frame = Frame(self.interface)
        self.frame.place(height = 250,width = 980,y=400)

        self.notebook = ttk.Notebook(self.frame)
        
        curItem = self.get_InfoParticipante()
        if curItem == None:
            return messagebox.showinfo(title = "Não foi possível procurar", message = "Selecione um participante")
    
        frame_participante = self.form_participante()
        frame_familia_participate = self.form_familia()
        frame_preparacao = self.form_preparacao()
        frame_curso = self.form_curso()
        frame_escola = self.form_escola_participante()
        frame_bolsa = self.form_bolsa()
        frame_situacao = self.form_situacao()



        self.notebook.add(frame_participante,text="Participante")
        self.notebook.add(frame_familia_participate,text = "Família")
        self.notebook.add(frame_preparacao,text = "Preparação")
        self.notebook.add(frame_curso,text = "Curso")
        self.notebook.add(frame_escola,text = "Escola")
        self.notebook.add(frame_bolsa,text = "Bolsa")
        self.notebook.add(frame_situacao,text = "Situação")

        self.notebook.place(height = 200,width = 980)

        button = Button(self.frame,text = "Atualizar",font = ("calibri",16,"bold"),command = lambda: self.set_list(curItem))
        button.place(height = 30,width = 100,x =850,y = 160)

    def read_data(self):
        self.frame = Frame(self.interface)
        self.frame.place(height = 250,width = 980,y=400)

        self.notebook = ttk.Notebook(self.frame)
        
        curItem = self.get_InfoParticipante()
        if curItem == None:
            return messagebox.showinfo(title = "Não foi possível procurar", message = "Selecione um participante")
    
        frame_participante = self.read_participante()
        frame_familia_participate = self.read_familia()
        frame_preparacao = self.read_preparacao()
        frame_curso = self.read_curso()
        frame_escola = self.read_escola_participante()
        frame_bolsa = self.read_bolsa()
        frame_situacao = self.read_situacao()


        self.notebook.add(frame_participante,text="Participante")
        self.notebook.add(frame_familia_participate,text = "Família")
        self.notebook.add(frame_preparacao,text = "Preparação")
        self.notebook.add(frame_curso,text = "Curso")
        self.notebook.add(frame_escola,text = "Escola")
        self.notebook.add(frame_bolsa,text = "Bolsa")
        self.notebook.add(frame_situacao,text = "Situação")

        self.notebook.place(height = 200,width = 980)


    def set_list(self,id):

        self.participante = self.controll.update_data(self.participante)

        self.tree.item(id,text = "",values = (self.participante.idade,
        self.participante.sexo,self.participante.nota_geral,self.participante.estado_civil,self.participante.raca,self.participante.nacionalidade,
        self.participante.id_participante,self.participante.id_familia,self.participante.id_situacao,self.participante.id_curso,
        self.participante.id_escola,self.participante.id_bolsa,self.participante.id_preparacao))
        messagebox.showinfo(title = "Sucesso", message = "Dados atualizados com sucesso")


    def form_participante(self):
        
        frame_participante = Frame(self.notebook)
        frame_participante.place(height = 150,width = 980,rely= 270)
    
        idade = IntVar(value= self.participante.idade)
        nota = StringVar(value= self.participante.nota_geral)
        
        idade_label = Label(frame_participante,text ="Idade",font = ('calibre',12,"bold"))
        idade_input = Entry(frame_participante,textvariable = idade,font = ('calibre',8),width = 42)
        idade_label.place(y=0,relx = 0.01)
        idade_input.place(y = 25,relx = 0.01)
        idade_input.bind("<KeyRelease>", lambda x: self.participante.set_idade(idade_input.get()))
    

        sexo_input = self.dropdown("Sexo",["Masculino","Feminino"],frame_participante,60,0.01)
        sexo_input.bind("<<ComboboxSelected>>", lambda x: self.participante.set_sexo(sexo_input.get()))
        sexo_input.set(self.participante.sexo)

        nota_geral_label = Label(frame_participante,text ="Nota Geral",font = ('calibre',12,"bold"))
        nota_geral_input = Entry(frame_participante,textvariable = nota,font = ('calibre',8),width = 42)
        nota_geral_label.place(y=0,relx = 0.33)
        nota_geral_input.place(y = 25,relx = 0.33)
        nota_geral_input.bind("<KeyRelease>", lambda x: self.participante.set_nota_geral(nota_geral_input.get()))

        estado_civil_input = self.dropdown("Estado Civil",
        [
            "Solteiro(a)",
            "Casado(a)",
            "Separado(a) judicialmente/divorciado(a)",
            "Viúvo(a)",
            "Outro(a)"],frame_participante,60,0.33)
        estado_civil_input.bind("<<ComboboxSelected>>", lambda x: self.participante.set_estado_civil(estado_civil_input.get()))
        estado_civil_input.set(self.participante.estado_civil)

        raca_input = self.dropdown("Raça",
        [
            "Branca",
            "Preta",
            "Amarela",
            "Parda",
            "Indígena",
            "Não quis declarar"],frame_participante,0,0.66)
        raca_input.bind("<<ComboboxSelected>>", lambda x: self.participante.set_raca(raca_input.get()))
        raca_input.set(self.participante.raca)

        nacionalidade_input = self.dropdown("Nacionalidade",
        [
            "Brasileira",
            "Brasileira naturalizada",
            "Estrangeira"],frame_participante,60,0.66)
        nacionalidade_input.bind("<<ComboboxSelected>>", lambda x: self.participante.set_nacionalidade(nacionalidade_input.get()))
        nacionalidade_input.set(self.participante.nacionalidade)

        
        return frame_participante

    def form_familia(self):

        frame_familia = Frame(self.notebook)
        frame_familia.place(height = 150,width = 980)


        input_escolaridade_pai = self.dropdown("Escolaridade pai",
        [
            "Nenhuma",
            "Ensino Fundamental",
            "Ensino Médio",
            "Ensino Superior"],frame_familia,0,0.01)
        input_escolaridade_pai.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.familia_participante.set_escolaridade_pai(input_escolaridade_pai.get()))
        input_escolaridade_pai.set(self.participante.familia_participante.escolaridade_pai)

        input_escolaridade_mae = self.dropdown("Escolaridade mãe",
        [
            "Nenhuma",
            "Ensino Fundamental",
            "Ensino Médio",
            "Ensino Superior"],frame_familia,60,0.01)
        input_escolaridade_mae.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.familia_participante.set_escolaridade_mae(input_escolaridade_mae.get()))
        input_escolaridade_mae.set(self.participante.familia_participante.escolaridade_mae)

        input_com_quem_participante_mora = self.dropdown("Com quem participante mora",
        [
            "Em casa ou apartamento, sozinho",
            "Em casa ou apartamento, com pais e/ou parentes",
            "Em casa ou apartamento, com cônjuge e/ou filhos",
            "Em casa ou apartamento, com outras pessoas ",
            "Em alojamento universitário da própria instituição",
            "Em outros tipos de habitação individual ou coletiva"],frame_familia,
        0,0.33)
        input_com_quem_participante_mora.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.familia_participante.set_com_quem_participante_mora(input_com_quem_participante_mora.get()))
        input_com_quem_participante_mora.set(self.participante.familia_participante.com_quem_participante_mora)

        input_renda_familia = self.dropdown("Renda Família", 
        [
            "Até 1.5 salário mínimo",
            "De 1.5 a 3 salários mínimos",
            "De 3 a 4.5 salários mínimos",
            "De 4.5 a 6 salários mínimos",
            "De 6 a 10 salários mínimos",
            "De 10 a 30 salários mínimos",
            "Acima de 30 salários mínimos"],frame_familia,60,0.33)
        input_renda_familia.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.familia_participante.set_renda_familia(input_renda_familia.get()))
        input_renda_familia.set(self.participante.familia_participante.renda_familia)

        input_quantidadde_moradores_participante = self.dropdown("Qtº moradores participante",
        ["Nenhuma","Uma","Duas","Três","Quatro","Cinco","Seis","Sete ou mais"],frame_familia,0,0.66)
        input_quantidadde_moradores_participante.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.familia_participante.set_quantidade_moradores(input_quantidadde_moradores_participante.get()))
        input_quantidadde_moradores_participante.set(self.participante.familia_participante.quantidade_moradores)

        input_familia_cursou_superior = self.dropdown("Família cursou Superior",["Sim","Não"],frame_familia,
        60,0.66)
        input_familia_cursou_superior.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.familia_participante.set_familia_cursou_superior(input_familia_cursou_superior.get()))
        input_familia_cursou_superior.set(self.participante.familia_participante.familia_cursou_superior)
        

        return frame_familia


    def form_preparacao(self):

        frame_preparacao = Frame(self.notebook)
        frame_preparacao.place(height = 150,width = 980)

        input_atividade_exterior = self.dropdown("Atividade exterior",
        [
            "Não",
            "Programa Ciência sem fronteiras",
            "Programa de intercâmbio financiado pelo governo Federal",
            "Programa de intercâmbio financiado pelo governo Estadual",
            "Programa de intercâmbio da instituição",
            "Outro intercâmbio não institucional"],frame_preparacao,0,0.01)
        input_atividade_exterior.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.preparacao_participante.set_atividade_exterior(input_atividade_exterior.get()))
        input_atividade_exterior.set(self.participante.preparacao_participante.atividade_exterior)

        input_livro_lido_ano = self.dropdown("Livros lido no ano",
        [
            "Nenhum",
            "Um ou dois",
            "De três a cinco",
            "De seis a oito",
            "Mais de oito"],frame_preparacao,60,0.01)
        input_livro_lido_ano.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.preparacao_participante.set_livro_lido_ano(input_livro_lido_ano.get()))
        input_livro_lido_ano.set(self.participante.preparacao_participante.livro_lido_ano)

        input_horas_por_semana_estudada = self.dropdown("Horas por semana estudada",
        [
            "Nenhuma, apenas assistiu as aulas",
            "De uma a três",
            "De quatro a sete",
            "De oito a doze",
            "Mais de Doze"],frame_preparacao,0,0.33)
        input_horas_por_semana_estudada.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.preparacao_participante.set_horas_por_semana_estudada(input_horas_por_semana_estudada.get()))
        input_horas_por_semana_estudada.set(self.participante.preparacao_participante.horas_por_semana_estudada)
        

        input_estudou_idioma_estrangeiro = self.dropdown("Estudou idioma estrangeiro",
        [
            "Não",
            "Modalidade presencial",
            "Modalidade semipresencial",
            "Modalidade presencial e semipresencial",
            "Modalidade a distância"],frame_preparacao,60,0.33)
        input_estudou_idioma_estrangeiro.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.preparacao_participante.set_estudou_idioma_estrangeiro(input_estudou_idioma_estrangeiro.get()))
        input_estudou_idioma_estrangeiro.set(self.participante.preparacao_participante.estudou_idioma_estrangeiro)

        return frame_preparacao

    def form_curso (self):

        frame_curso = Frame(self.notebook)
        frame_curso.place(height = 150,width = 980)

        input_ingresso_cota = self.dropdown("Ingresso por cota",
        [
            "Nenhuma",
            "Por critério étnico-racial",
            "Por critério de renda",
            "Por ter estudado em escola pública ou em particular com bolsa de estudos",
            "Por sistema que combina dois ou mais critéios anteriores",
            "Por sistema diferentes dos anteriores"],
        frame_curso,0,0.01)
        input_ingresso_cota.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.curso.set_ingresso_cota(input_ingresso_cota.get()))
        input_ingresso_cota.set(self.participante.curso.ingresso_cota)

        input_motivo_curso = self.dropdown("Motivo curso", 
        [
            "Inserção no mercado de trabalho",
            "Influência familiar",
            "Valorização profissional",
            "Prestígio Social",
            "Vocação",
            "Oferecido na modalidade a distância",
            "Baixa concorrência para ingresso",
            "Outro motivo"],frame_curso,60,0.01)
        input_motivo_curso.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.curso.set_motivo_curso(input_motivo_curso.get()))
        input_motivo_curso.set(self.participante.curso.motivo_curso)

        input_razao_instituicao = self.dropdown("Razão instituição", 
        [
            "Gratuidade",
            "Preço da mensalidade",
            "Proximidade da minha residência",
            "Proximidade do meu trabalho",
            "Facilidade de acesso",
            "Qualidade/reputação",
            "Foi a única onde tive aprovação",
            "Possibilidade de ter bolsa de estudo",
            "Outro motivo"],frame_curso,0,0.33)
        input_razao_instituicao.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.curso.set_razao_instituicao(input_razao_instituicao.get()))
        input_razao_instituicao.set(self.participante.curso.razao_instituicao)

        input_incentivou_graduacao = self.dropdown("Incentivou graduação",
        [
            "Ninguém",
            "Pais",
            "Outro membros da família",
            "Professores",
            "Líder ou representante religioso",
            "Colegas/Amigos",
            "Outras pessoas"],frame_curso,60,0.33)
        input_incentivou_graduacao.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.curso.set_incentivou_graduacao(input_incentivou_graduacao.get()))
        input_incentivou_graduacao.set(self.participante.curso.incentivou_graduacao)
        
        input_grupo_dificuldade = self.dropdown("Grupo dificuldade", 
        [
            "Não teve dificuldade",
            "Não recebeu apoio para enfrentar dificuldades",
            "Pais",
            "Avós",
            "Irmãos,primos ou tios",
            "Líder ou representante religioso",
            "Colegas de curso ou amigos",
            "Professores do curso",
            "Profissionais do serviço de apoio ao estudante da IES",
            "Colegas de trabalho",
            "Outro grupo"],frame_curso,0,0.66)
        input_grupo_dificuldade.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.curso.set_grupo_dificuldade(input_grupo_dificuldade.get()))
        input_grupo_dificuldade.set(self.participante.curso.grupo_dificuldade)

        return frame_curso

    def form_escola_participante (self):

        frame_escola = Frame(self.notebook)
        frame_escola.place(height = 150,width = 980)

        input_tipo_ensino_medio = self.dropdown("Tipo de ensino médio",
        [
            "Todo em escola pública",
            "Todo em escola privada(particular)",
            "Todo no exterior",
            "A maior parte na escola pública",
            "A maior parte em escola privada(particular)",
            "Parte no Brasil parte no exterior"],frame_escola,0,0.01)
        input_tipo_ensino_medio.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.escola_participante.set_tipo_ensino_medio(input_tipo_ensino_medio.get()))
        input_tipo_ensino_medio.set(self.participante.escola_participante.tipo_ensino_medio)

        input_modalidade_ensino_medio = self.dropdown("Modalidade ensino médio",
        ["Ensino médio tradicional",
        "Profissionalizante técnico",
        "Profissionalizante magistério",
        "Educação de Jovens e Adultos e/ou supletivo",
        "Outra modalidade"],frame_escola,60,0.01)
        input_modalidade_ensino_medio.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.escola_participante.set_modalidade_ensino_medio(input_modalidade_ensino_medio.get()))
        input_modalidade_ensino_medio.set(self.participante.escola_participante.modalidade_ensino_medio)

        input_regiao_concluiu_ensino_medio = self.dropdown("Região concluiu ensino médio", 
        [
            "Norte",
            "Nordeste",
            "Sudeste",
            "Sul",
            "Centro-Oeste"],frame_escola,0,0.33)
        input_regiao_concluiu_ensino_medio.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.escola_participante.set_regiao_ensino_medio(input_regiao_concluiu_ensino_medio.get()))
        input_regiao_concluiu_ensino_medio.set(self.participante.escola_participante.regiao_ensino_medio)

        return frame_escola
        
    def form_bolsa(self):
        frame_bolsa = Frame(self.notebook)
        frame_bolsa.place(height = 150,width = 980)

        input_bolsa_estudos = self.dropdown("Bolsa de estudos",
        [
        "Nenhum, curso gratuito",
        "Nenhum, porém curso não gratuito",
        "ProUni integral",
        "ProUni parcial, apenas",
        "FIES, apenas",
        "Prouni parcial e FIES",
        "Bolsa oferecida por governo",
        "Bolsa oferecida pela instituição",
        "Bolsa oferecida por outra entidade",
        "Finaciamento da instituição",
        "Finaciamento bancário"],
        frame_bolsa,0,0.01)
        input_bolsa_estudos.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.bolsa_participante.set_bolsa_estudos(input_bolsa_estudos.get()))
        input_bolsa_estudos.set(self.participante.bolsa_participante.bolsa_estudos)

        input_bolsa_permanencia = self.dropdown("Bolsa permanência",
        [
            "Nenhum",
            "Auxílio Moradia",
            "Auxílio alimentação",
            "Auxílio moradia e alimentação",
            "Auxílio Permanência",
            "Outro tipo de auxílio"],
        frame_bolsa,60,0.01)
        input_bolsa_permanencia.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.bolsa_participante.set_bolsa_permanencia(input_bolsa_permanencia.get()))
        input_bolsa_permanencia.set(self.participante.bolsa_participante.bolsa_permanencia)

        input_bolsa_academica = self.dropdown("Bolsa acadêmica",
        [
            "Nenhum",
            "Bolsa de iniação científica",
            "Bolsa de extensão",
            "Bolsa de monitoria/tutoria",
            "Bolsa PET",
            "Outro tipo de bolsa acadêmica"],
        frame_bolsa,0,0.33)
        input_bolsa_academica.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.bolsa_participante.set_bolsa_academica(input_bolsa_academica.get()))
        input_bolsa_academica.set(self.participante.bolsa_participante.bolsa_academica)

        return frame_bolsa

    def form_situacao(self):
        frame_situacao = Frame(self.notebook)
        frame_situacao.place(height = 150,width = 980)


        input_situacao_financeira = self.dropdown("Situação Financeira",
        ["Não tem renda, gastos financiados por programas governamentais",
        "Não tem renda, gastos financiados pela família ou por outra pessoa",
        "Tem renda, mas recebe ajuda da família ou de outra pessoa para financiar os gastos",
        "Tem renda e não precisa de ajuda para financiar os gastos",
        "Tem renda e contribue com sustento da família",
        "Principal sustento da família"],frame_situacao,0,0.01)
        input_situacao_financeira.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.situacao_participante.set_situacao_financeira(input_situacao_financeira.get()))
        input_situacao_financeira.set(self.participante.situacao_participante.situacao_financeira)

        input_situacao_trabalho = self.dropdown("Situação de Trabalho",
        ["Não está trabalhando",
        "Trabalha eventualmente",
        "Trabalho até 20 horas semanais",
        "Trabalho de 21 a 39 horas semanais",
        "Trabalho 40 horas semanais ou mais"],
        frame_situacao,60,0.01)
        input_situacao_trabalho.bind("<<ComboboxSelected>>", 
        lambda x: self.participante.situacao_participante.set_situacao_trabalho(input_situacao_trabalho.get()))
        input_situacao_trabalho.set(self.participante.situacao_participante.situacao_trabalho)

        return frame_situacao

    def dropdown(self,label_text,categories,frame,y_dd,relx_dd,width = 39,rely_dd = 0):

        label = Label(frame,text =label_text,font = ('calibre',12,"bold"))
        input_ = ttk.Combobox(frame,values = categories,font = ('calibre',8),width = width)
        label.place(y= y_dd,relx = relx_dd,rely = rely_dd)
        input_.place(y = y_dd + 25,relx = relx_dd,rely = rely_dd)

        return input_


    def main(self):
        self.tree["column"] = ['Idade','Sexo','Nota_geral','Estado_civil','Raça','Nacionalidade',"Id_participante",'Famila_participante_id',
        'Situação_participante_id','Curso_id','Escola_participante_id','Bolsa_participante_id','Preparação_participante_id']
        self.tree["show"] = "headings"


        for coluna in self.tree["columns"]:
            self.tree.column(coluna,width = 15)
            self.tree.heading(coluna,text=coluna)

        items = self.controll.getAllrow()
        for row in items:
            self.tree.insert("","end",values = row)

    def Label_participante(self,frame,title,data,y_lp,rel_lp):

        label_title = Label(frame,text =title,font = ('calibre',12,"bold"))
        label_data = Label(frame,text = data,font = ('calibre',8))
        label_title.place(y=y_lp,relx = rel_lp)
        label_data.place(y = y_lp + 25,relx = rel_lp,anchor = "nw")

    def read_participante(self):
        
        frame_participante = Frame(self.notebook)
        frame_participante.place(height = 150,width = 980,rely= 270)
    
        
        self.Label_participante(frame_participante,"Idade",self.participante.idade,0,0.01)
    
        self.Label_participante(frame_participante,"Sexo",self.participante.sexo,60,0.01)

        self.Label_participante(frame_participante,"Nota Geral",self.participante.nota_geral,0,0.33)

        self.Label_participante(frame_participante,"Estado_Civil",self.participante.estado_civil,60,0.33)

        self.Label_participante(frame_participante,"Raça",self.participante.raca,0,0.66)

        self.Label_participante(frame_participante,"Nacionalidade",self.participante.nacionalidade,60,0.66)

        return frame_participante

    def read_familia(self):

        frame_familia = Frame(self.notebook)
        frame_familia.place(height = 150,width = 980)

        self.Label_participante(frame_familia,"Escolaridade pai",self.participante.familia_participante.escolaridade_pai,0,0.01)

        self.Label_participante(frame_familia,"Escolaridade mãe", self.participante.familia_participante.escolaridade_mae,60,0.01)

        self.Label_participante(frame_familia,"Com quem participante mora", self.participante.familia_participante.com_quem_participante_mora,
        0,0.33)

        self.Label_participante(frame_familia,"Renda Família",self.participante.familia_participante.renda_familia,60,0.33)

        self.Label_participante(frame_familia,"Qtº moradores participante",self.participante.familia_participante.quantidade_moradores,
        0,0.66)

        self.Label_participante(frame_familia,"Família cursou Superior",self.participante.familia_participante.familia_cursou_superior,60,0.66)
        
        return frame_familia


    def read_preparacao(self):

        frame_preparacao = Frame(self.notebook)
        frame_preparacao.place(height = 150,width = 980)

        self.Label_participante(frame_preparacao,"Atividade exterior",self.participante.preparacao_participante.atividade_exterior,0,0.01)
        
        self.Label_participante(frame_preparacao,"Livros lido no ano",self.participante.preparacao_participante.livro_lido_ano,60,0.01)

        self.Label_participante(frame_preparacao,"Horas por semana estudada", self.participante.preparacao_participante.horas_por_semana_estudada,
        0,0.33)

        self.Label_participante(frame_preparacao,"Estudou idioma estrangeiro", self.participante.preparacao_participante.estudou_idioma_estrangeiro,
        60,0.33)

        return frame_preparacao

    def read_curso (self):

        frame_curso = Frame(self.notebook)
        frame_curso.place(height = 150,width = 980)

        self.Label_participante(frame_curso,"Ingresso por cota",self.participante.curso.ingresso_cota,0,0.01)
        
        self.Label_participante(frame_curso,"Motivo curso", self.participante.curso.motivo_curso,60,0.01)

        self.Label_participante(frame_curso,"Razão instituição",self.participante.curso.razao_instituicao,0,0.33)

        self.Label_participante(frame_curso,"Incentivou graduação",self.participante.curso.incentivou_graduacao,60,0.33)

        self.Label_participante(frame_curso,"Grupo dificuldade",self.participante.curso.grupo_dificuldade,0,0.66)


        return frame_curso

    def read_escola_participante (self):

        frame_escola = Frame(self.notebook)
        frame_escola.place(height = 150,width = 980)

        self.Label_participante(frame_escola,"Tipo de ensino médio",self.participante.escola_participante.tipo_ensino_medio,0,0.01)
        
        self.Label_participante(frame_escola,"Modalidade ensino médio",self.participante.escola_participante.modalidade_ensino_medio,60,0.01)

        self.Label_participante(frame_escola,"Região concluiu ensino médio",self.participante.escola_participante.regiao_ensino_medio,0,0.33)

        return frame_escola
        
    def read_bolsa(self):
        frame_bolsa = Frame(self.notebook)
        frame_bolsa.place(height = 150,width = 980)

        self.Label_participante(frame_bolsa,"Bolsa de estudos",self.participante.bolsa_participante.bolsa_estudos,0,0.01)
        
        self.Label_participante(frame_bolsa,"Bolsa permanência", self.participante.bolsa_participante.bolsa_permanencia,60,0.01)

        self.Label_participante(frame_bolsa,"Bolsa acadêmica", self.participante.bolsa_participante.bolsa_academica,0,0.33)

        return frame_bolsa

    def read_situacao(self):
        frame_situacao = Frame(self.notebook)
        frame_situacao.place(height = 150,width = 980)


        self.Label_participante(frame_situacao,"Situação Financeira",self.participante.situacao_participante.situacao_financeira,0,0.01)
        
        self.Label_participante(frame_situacao,"Situação de Trabalho",self.participante.situacao_participante.situacao_trabalho,60,0.01)


        return frame_situacao

        

root = Tk()
t = Screen(root)
t.main()
root.title("")
root.geometry("980x610")
root.mainloop()