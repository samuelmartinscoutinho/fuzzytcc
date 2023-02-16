from werkzeug.security import generate_password_hash
from fuzzytcc.ext.database import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    eadmin = db.Column(db.Boolean)
    
    def __init__(self, login:str, senha:str, email:str,eadmin:bool):
        self.login = login
        self.senha = generate_password_hash(senha)
        self.email = email
        self.eadmin = eadmin
        
class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    genero = db.Column(db.String)
    usuario= db.Column(db.Integer, db.ForeignKey(Usuario.id))
    usuario_relationship = db.relationship(Usuario)
    
    def __init__(self, nome:str, genero:str, usuario:Usuario):
        self.nome = nome
        self.genero = genero
        self.usuario = usuario
        
    
class Aluno(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    genero = db.Column(db.String)
    usuario= db.Column(db.Integer, db.ForeignKey(Usuario.id))
    usuario_relationship = db.relationship(Usuario)
    
    def __init__(self, nome:str, genero:str, usuario:Usuario):
        self.nome = nome
        self.genero = genero
        self.usuario = usuario
        
class Avaliacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idade = db.Column(db.Integer)
    altura = db.Column(db.Float)
    peso = db.Column(db.Float)
    imc = db.Column(db.Float)
    percentual_gordura = db.Column(db.Float)
    percentual_massa = db.Column(db.Float)
    efumante = db.Column(db.Boolean)
    ehipertenso = db.Column(db.Boolean)
    ediabetico = db.Column(db.Boolean)
    pratica_atividade = db.Column(db.Boolean)
    problemas_coluna = db.Column(db.Boolean)
    tratamento_osseo = db.Column(db.Boolean)
    tontura_frequente = db.Column(db.Boolean)
    valor_fuzzy = db.Column(db.String)
    aluno = db.Column(db.Integer, db.ForeignKey(Aluno.id))
    aluno_relationship = db.relationship(Aluno)
    
    def __init__(self, idade:int, altura:float, peso:float, imc:float,
                 percentual_gordura:float, percentual_massa:float, efumante:bool, ehipertenso:bool, ediabetico:bool,
                 pratica_atividade:bool, problemas_coluna:bool, tratamento_osseo:bool, tontura_frequente:bool, valor_fuzzy:str, aluno:Aluno):
        self.idade = idade
        self.altura = altura
        self.peso = peso
        self.imc = imc
        self.percentual_gordura = percentual_gordura
        self.percentual_massa = percentual_massa
        self.efumante = efumante
        self.ehipertenso = ehipertenso
        self.ediabetico = ediabetico
        self.pratica_atividade = pratica_atividade
        self.problemas_coluna = problemas_coluna
        self.tratamento_osseo = tratamento_osseo
        self.tontura_frequente = tontura_frequente
        self.valor_fuzzy = valor_fuzzy
        self.aluno = aluno
    
class Treino(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    treinos = db.Column(db.String)
    aluno = db.Column(db.Integer, db.ForeignKey(Aluno.id))
    aluno = db.relationship(Aluno)
    
    def __init__(self, treinos:str, aluno:Aluno):
        self.treinos = treinos
        self.aluno = aluno
    
class Regra(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    regra_portuges = db.Column(db.String)
    regra_fuzzy = db.Column(db.String)
    treino = db.Column(db.String)
    tempo = db.Column(db.Integer)
    imc = db.Column(db.Boolean)
    percentual_gordura = db.Column(db.Boolean)
    percentual_massa = db.Column(db.Boolean)
    efumante = db.Column(db.Boolean)
    ediabetico = db.Column(db.Boolean)
    ehipertenso = db.Column(db.Boolean)
    
    def __init__(self, regra_portugues:str, regra_fuzzy:str, treino:str, tempo:int, imc:bool, percentual_gordura:bool,
                 percentual_massa:bool, efumante:bool, ediabetico:bool, ehipertenso:bool):
        self.regra_portuges = regra_portugues
        self.regra_fuzzy = regra_fuzzy
        self.treino = treino
        self.tempo = tempo
        self.imc = imc
        self.percentual_gordura = percentual_gordura
        self.percentual_massa = percentual_massa
        self.efumante = efumante
        self.ediabetico = ediabetico
        self.ehipertenso = ehipertenso
        
class Pertinencia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    imc_baixo = db.Column(db.Float)
    imc_medio = db.Column(db.Float)
    imc_alto = db.Column(db.Float)
    percentual_gordura_baixo = db.Column(db.Float)
    percentual_gordura_medio = db.Column(db.Float)
    percentual_gordura_alto = db.Column(db.Float)
    percentual_massa_baixo = db.Column(db.Float)
    percentual_massa_medio = db.Column(db.Float)
    percentual_massa_alto = db.Column(db.Float)
    efumante = db.Column(db.Boolean)
    ediabetico = db.Column(db.Boolean)
    ehipertenso = db.Column(db.Boolean)
    
    def __init__(self, imc_baixo:float, imc_medio:float, imc_alto:float, percentual_gordura_baixo:float,percentual_gordura_medio:float,percentual_gordura_alto:float,
                 percentual_massa_baixo:float, percentual_massa_medio:float, percentual_massa_alto:float, efumante:bool, ediabetico:bool, ehipertenso:float):
        self.imc_baixo = imc_baixo
        self.imc_medio = imc_medio
        self.imc_alto = imc_alto
        self.percentual_gordura_baixo = percentual_gordura_baixo
        self.percentual_gordura_medio = percentual_gordura_medio
        self.percentual_gordura_alto = percentual_gordura_alto
        self.percentual_massa_baixo = percentual_massa_baixo
        self.percentual_massa_medio = percentual_massa_medio
        self.percentual_massa_alto = percentual_massa_alto
        self.efumante = efumante
        self.ediabetico = ediabetico
        self.ehipertenso = ehipertenso