from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

hostname = "127.0.0.1"
username = "root"
password = ""
port = 3306
database = "companie"

DATABASE_URL = f'mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}'

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Project(Base):
    __tablename__ = "Projects"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nume = Column(String(50), nullable=False)
    descriere = Column(String(200), nullable=False)
    data_inceput = Column(String(20), nullable=False)
    data_sfarsit = Column(String(20), nullable=False)

    #Relatie one to one cu buget
    budget_id = Column(Integer, ForeignKey('budget.id'), unique=True)
    budget = relationship("Budget", back_populates="project")

    #Relatie one to many cu sarcini
    task = relationship("Task", back_populates="proiect")

    #Relatie many to one cu Departament
    departament_id = Column(Integer, ForeignKey('departamente.id'))
    departament = relationship("Departament", back_populates="proiect")

    #Relatie one to many cu echipe
    echipa = relationship("Team", back_populates="proiect")

    def __repr__(self):
        return (f"<Project(nume = '{self.nume}', descriere = {self.descriere}), data_inceput = {self.data_inceput}, data_sfarsit = {self.data_sfarsit},"
                f"buget = {self.budget_id}, department = {self.departament_id})>")


class Budget(Base):
    __tablename__ = "budget"
    id = Column(Integer, primary_key=True, autoincrement=True)
    buget = Column(Integer, nullable=False)

    #Relatie one to one cu Project
    project = relationship("Project", back_populates="budget", uselist=False)

    def __repr__(self):
        return f"<Budget(buget = '{self.buget}')>"


class Company(Base):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nume = Column(String(20), nullable=False)

    #Relatie one to many cu departament
    departament = relationship("Departament", back_populates="company", cascade="all, delete-orphan")

    #Relatie one to many cu angajati
    angajati = relationship("Employee", back_populates="company", cascade="all, delete-orphan")

    #Relatie one to many cu resurse
    resurse = relationship("Resource", back_populates="company", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Company(nume = '{self.nume}')>"


class Departament(Base):
    __tablename__ = "departamente"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nume = Column(String(20), nullable=False)

    #Relatie one to many cu echipe
    echipa = relationship("Team", back_populates="departament")

    #Relatie one to many cu project
    proiect = relationship("Project", back_populates="departament", cascade="all, delete-orphan")

    # Relatie many to one cu company
    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship("Company", back_populates="departament")

    def __repr__(self):
        return f"<Departament(nume = '{self.nume}'), company_id = {self.company_id}>"


class Employee(Base):
    __tablename__ = "angajati"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nume = Column(String(20), nullable=False)
    rol = Column(String(20), nullable=False)
    salariu = Column(Integer, nullable=False)

    #Relatie many to one cu echipe
    echipa_id = Column(Integer, ForeignKey('echipe.id'))
    echipa = relationship("Team", back_populates="angajat")

    #Relatie many to one cu company
    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship("Company", back_populates="angajati")

    # Relatie one to one cu sarcini
    task_id = Column(Integer, ForeignKey('sarcini.id'), unique=True)
    task = relationship("Task", back_populates="angajat")

    def __repr__(self):
        return (f"<Employee(nume = '{self.nume}'), rol = '{self.rol}'), salariu = {self.salariu},"
                f"company_id = {self.company_id}, task_id = {self.task_id}, echipa_id = {self.echipa_id})>")


class Finance(Base):
    __tablename__ = "finante"
    id = Column(Integer, primary_key=True, autoincrement=True)
    venituri = Column(Integer, nullable=False)
    cheltuieli = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Finance(venituri = {self.venituri}, cheltuieli = {self.cheltuieli})>"


class Resource(Base):
    __tablename__ = "resurse"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nume = Column(String(20), nullable=False)
    tip = Column(String(20), nullable=False)
    disponibilitate = Column(String(20), nullable=False)
    cost = Column(Integer, nullable=False)

    #Relatie many to one cu company
    company_id = Column(Integer, ForeignKey('company.id'))
    company = relationship("Company", back_populates="resurse")

    def __repr__(self):
        return f"<Resource(nume = {self.nume}, tip = {self.tip}, disponibilitate = {self.disponibilitate}, cost = {self.cost}, company_id = {self.company_id})>"

class Task(Base):
    __tablename__ = "sarcini"
    id = Column(Integer, primary_key=True, autoincrement=True)
    titlu = Column(String(20), nullable=False)
    descriere = Column(String(200), nullable=False)
    termen_limita = Column(String(20), nullable=False)
    status = Column(String(20), nullable=False)

    #Relatie one to one cu angajat
    angajat = relationship("Employee", back_populates="task", uselist=False)

    #Relatie Many to one cu proiect
    proiect_id = Column(Integer, ForeignKey('Projects.id'))
    proiect = relationship("Project", back_populates="task")

    def __repr__(self):
        return (f"<Task(titlu = {self.titlu}, descriere = {self.descriere}, termen_limita = {self.termen_limita}, status = {self.status},"
                f"proiect_id = {self.proiect_id})>")

class Team(Base):
    __tablename__ = "echipe"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nume = Column(String(20), nullable=False)

    #Relatie one to many cu angajati
    angajat = relationship("Employee", back_populates="echipa")

    #Relatie many to one cu proiecte
    proiect_id = Column(Integer, ForeignKey('Projects.id'))
    proiect = relationship("Project", back_populates="echipa")

    #Relatie many to one cu departament
    departament_id = Column(Integer, ForeignKey('departamente.id'))
    departament = relationship("Departament", back_populates="echipa")

    def __repr__(self):
        return f"<Team(nume = '{self.nume}', proiect_id = {self.proiect_id}, departament_id = {self.departament_id})>"

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)