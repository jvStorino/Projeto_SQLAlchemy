from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Criando engine      (db+driver    //usuario:senha @ servidor : porta / database  
engine = create_engine('mysql+pymysql://root:Ekko1403$@localhost:3306/cinema')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

'''
try:
    # Criando conexão com o banco de dados
    with engine.connect() as connection:
        resultado = connection.exec_driver_sql('SELECT * FROM filmes;')

        # Selecionando as tabelas de filmes
        for linha in resultado:
            print(linha)

except Exception as e:
    print(f"Erro: {e}")
'''

# Entidades
class Filmes(Base):
    __tablename__ = 'filmes'

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)
    
    def __repr__(self):
        return f"Filme: {self.titulo} - Genero: {self.genero}"

#SQL

# Insert
'''
data_insert = Filmes(titulo = 'Superman', genero = 'Ficção', ano = '1978')
session.add(data_insert)
'''

# Update
'''
session.query(Filmes).filter(Filmes.genero=='Drama').update({'genero':'hahaha'})
'''

# Delete
'''
session.query(Filmes).filter(Filmes.titulo=='Superman').delete()
'''

# Commit das mudanças
session.commit()

# Select
data = session.query(Filmes).all()
print(data)

# Fechando o DB
session.close()