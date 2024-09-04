from company_models import Session, Company, Project, Task, Team, Employee, Finance, Departament, Budget, Resource


def adauga_finance():
    venituri = int(input("Adaugati veniturile: "))
    cheltuieli = int(input("Adaugati cheltuielile: "))
    finante = Finance(venituri=venituri, cheltuieli=cheltuieli)
    session.add(finante)
    session.commit()
    print("Finantele au fost adaugate")



def adauga_resursa():
    nume = input("Adaugati numele resursei: ")
    tip = input("Adaugati tip-ul resursei: ")
    disponibilitate = input("Adaugati disponibilitatea resursei: ")
    cost = int(input("Adaugati costul resursei: "))
    companie_nume = input("Adaugati numele companiei din care face parte resursa : ")
    companie = session.query(Company).filter_by(nume=companie_nume).first()
    if not companie:
        print(f"Compania {companie_nume} nu exista: ")
        return
    resursa = Resource(nume=nume, tip=tip, disponibilitate=disponibilitate, cost=cost, company=companie)
    session.add(resursa)
    session.commit()



def adauga_angajat():
    nume = input("Adaugati numele angajatului: ")
    rol = input("Adaugati rol-ul angajatului: ")
    salariu = input("Adaugati salariul angajatului: ")

    echipa_nume = input("Adaugati echipa din care face parte angajatul: ")
    echipa = session.query(Team).filter_by(nume=echipa_nume).first()
    if not echipa:
        print(f"Nu exista nici o echipa cu numele {echipa_nume}")
        return

    companie_nume = input("Adaugati numele companiei din care face parte angajatul: ")
    companie = session.query(Company).filter_by(nume=companie_nume).first()
    if not companie:
        print(f"Compania {companie_nume} nu exista: ")
        return

    task_title = input("Adaugati titlul task-ului pe care o sa il aiba angajatul: ")
    task = session.query(Task).filter_by(titlu=task_title).first()
    if not task:
        print(f"Task-ul {task_title} nu exista: ")
        return

    angajat = Employee(nume=nume, rol=rol, salariu=salariu, echipa=echipa, company=companie, task=task)
    session.add(angajat)
    session.commit()



def adauga_proiect():
    nume = input("Adaugati numele proiectului: ")
    descriere = input("Adaugati descrierea proiectului: ")
    data_inceput = input("Adaugati data de inceput: ")
    data_sfarsit = input("Adaugati data de sfarsit: ")

    # Fetching the Budget object instead of just a buget value
    buget_cost = int(input("Adaugati bugetul: "))
    buget = session.query(Budget).filter_by(buget=buget_cost).first()
    if not buget:
        print(f"Bugetul {buget_cost} nu exista. Adaugati bugetul mai intai.")
        return

    departament_nume = input("Introduceti numele departamentului din care face parte proiectul: ")
    departament = session.query(Departament).filter_by(nume=departament_nume).first()
    if not departament:
        print(f"Departamentul {departament_nume} nu exista.")
        return

    # Creating the Project object and assigning the Budget object
    proiect = Project(nume=nume, descriere=descriere, data_inceput=data_inceput, data_sfarsit=data_sfarsit, budget=buget, departament=departament)
    session.add(proiect)
    session.commit()
    print(f"Proiectul {nume} a fost adaugat cu succes.")



def adauga_buget():
    buget = input("Introduceti bugetul: ")
    budget = Budget(buget=buget)
    session.add(budget)
    session.commit()



def adauga_departament():
    nume = input("Introduceti numele departamentului: ")
    companie_nume = input("Adaugati numele companiei din care face parte departamenul: ")
    companie = session.query(Company).filter_by(nume=companie_nume).first()
    if not companie:
        print(f"Compania {companie_nume} nu exista: ")
        return

    departament = Departament(nume=nume, company=companie)
    session.add(departament)
    session.commit()



def adauga_echipa():
    nume = input("Introduceti numele echipei: ")

    proiect_nume = input("Introduceti numele proiectului din care face parte echipa: ")
    proiect = session.query(Project).filter_by(nume=proiect_nume).first()
    if not proiect:
        print(f"Proiectul {proiect_nume} nu exista.")
        return

    departament_nume = input("Introduceti numele departamentului din care face parte echipa: ")
    departament = session.query(Departament).filter_by(nume=departament_nume).first()
    if not departament:
        print(f"Task-ul {departament_nume} nu exista: ")
        return

    echipa = Team(nume=nume, proiect=proiect, departament=departament)
    session.add(echipa)
    session.commit()



def adauga_task():
    titlu = input("Introduceti titlul task-ului: ")
    descriere = input("Introduceti descrierea task-ului: ")
    termen_limita = input("Introduceti termenul limita: ")
    status = input("Introduceti statusul: ")

    proiect_nume = input("Introduceti numele proiectului din care face parte echipa: ")
    proiect = session.query(Project).filter_by(nume=proiect_nume).first()
    if not proiect:
        print(f"Proiectul {proiect_nume} nu exista.")
        return

    task = Task(titlu=titlu, descriere=descriere, termen_limita=termen_limita, status=status, proiect=proiect)
    session.add(task)
    session.commit()



def stergere_proiect():
    nume = input("Introduceti numele proiectului pe care doriti sa il stergeti: ")
    proiect = session.query(Project).filter_by(nume = nume).first()
    if not proiect:
        print(f"Proiectul {nume} nu a fost gasit.")
        return

    session.delete(proiect)
    session.commit()
    print(f"Proiectul {nume} a fost sters cu succes.")



def stergere_task():
    titlu = input("Introduceti titlul task-ului pe care doriti sa il stergeti: ")
    task = session.query(Task).filter_by(titlu=titlu).first()
    if not task:
        print(f"Task-ul {titlu} nu a fost gasit.")
        return

    session.delete(task)
    session.commit()
    print(f"Task-ul {titlu} a fost sters cu succes.")



def stergere_team():
    nume = input("Introduceti numele echipei pe care doriti sa o stergeti: ")
    team = session.query(Team).filter_by(nume=nume).first()
    if not team:
        print(f"Echipa {nume} nu a fost gasita.")
        return

    session.delete(team)
    session.commit()
    print(f"Echipa {nume} a fost sters cu succes.")



def stergere_employee():
    nume = input("Introduceti numele angajatului pe care doriti sa il stergeti: ")
    employee = session.query(Employee).filter_by(nume=nume).first()
    if not employee:
        print(f"Angajatul {nume} nu a fost gasit.")
        return

    session.delete(employee)
    session.commit()
    print(f"Angajatul {nume} a fost sters cu succes.")



def actualizare_proiect():
    nume = input("Introduceti numele proiectului pe care doriti sa il actualizati: ")
    proiect = session.query(Project).filter_by(nume=nume).first()
    if not proiect:
        print(f"Proiectul {nume} nu a fost gasit.")
        return
    choice = input("Ce doriti sa actualizati la proiect ? (nume, descriere, data_inceput sau data_sfarsit): ")
    if choice == "nume":
        nume_nou = input("Introduceti valoarea noua: ")
        proiect.nume = nume_nou
        session.commit()
        print("Valoarea a fost schimbata cu succes")
    elif choice == "descriere":
        descriere_noua = input("Introduceti valoarea noua: ")
        proiect.descriere = descriere_noua
        session.commit()
        print("Valoarea a fost schimbata cu succes")
    elif choice == "data_inceput":
        data_inceput_noua = input("Introduceti valoarea noua: ")
        proiect.data_inceput = data_inceput_noua
        session.commit()
        print("Valoarea a fost schimbata cu succes")
    elif choice == "data_sfarsit":
        data_sfarsit_noua = input("Introduceti valoarea noua: ")
        proiect.data_sfarsit = data_sfarsit_noua
        session.commit()
        print("Valoarea a fost schimbata cu succes")
    else:
        print("Nu ati introduc o valoare corespunzatoare")



def actualizare_task():
    titlu = input("Introduceti titlul task-ului pe care doriti sa il actualizati: ")
    task = session.query(Task).filter_by(titlu=titlu).first()
    if not task:
        print(f"Task-ul {titlu} nu a fost gasit.")
        return

    choice = input("Ce doriti sa actualizati la task ? (titlu, descriere, termen_limita sau status ): ")
    if choice == "titlu":
        titlu_nou = input("Introduceti valoarea noua: ")
        task.titlu = titlu_nou
        session.commit()
        print("Valoarea a fost schimbata cu succes")
    elif choice == "descriere":
        descriere_noua = input("Introduceti valoarea noua: ")
        task.descriere = descriere_noua
        session.commit()
        print("Valoarea a fost schimbata cu succes")
    elif choice == "termen_limita":
        termen_limita_nou = input("Introduceti valoarea noua: ")
        task.termen_limita = termen_limita_nou
        session.commit()
        print("Valoarea a fost schimbata cu succes")
    elif choice == "status":
        status_nou = input("Introduceti valoarea noua: ")
        task.status = status_nou
        session.commit()
        print("Valoarea a fost schimbata cu succes")
    else:
        print("Nu ati introduc o valoare corespunzatoare")



def actualizare_team():
    nume = input("Introduceti numele echipei pe care doriti sa o actualizati: ")
    team = session.query(Team).filter_by(nume=nume).first()
    if not team:
        print(f"Echipa {nume} nu a fost gasita.")
        return
    nume_nou = input("Introduceti numele nou al echipei: ")
    team.nume = nume_nou
    session.commit()
    print("Numele a fost schimbat cu succes!")



def actualizare_angajat():
    nume = input("Introduceti numele angajatului pe care doriti sa il actualizati: ")
    employee = session.query(Employee).filter_by(nume=nume).first()
    if not employee:
        print(f"Angajatul {nume} nu a fost gasit.")
        return

    choice = input("Ce doriti sa actualizati la angajat ? (nume, rol, salariu sau echipa ): ")
    if choice == "nume":
        nume_nou = input("Introduceti valoarea noua: ")
        employee.nume = nume_nou
        session.commit()
        print("Valoarea a fost schimbata cu succes")
    elif choice == "rol":
        rol_nou = input("Introduceti valoarea noua: ")
        employee.rol = rol_nou
        session.commit()
        print("Valoarea a fost schimbata cu succes")
    elif choice == "salariu":
        salariu_nou = input("Introduceti valoarea noua: ")
        employee.salariu = salariu_nou
        session.commit()
        print("Valoarea a fost schimbata cu succes")
    elif choice == "echipa":
        id_team_nou = input("Introduceti id-ul unei noi echipe: ")
        team = session.query(Team).filter_by(id=id_team_nou).first()
        if not team:
            print("Echipa nu exista:")
            return
        employee.echipa_id = team.id
        session.commit()



def generare_raport():
    choice = int(input("Ce raport doriti sa generati (1. Stare / 2. Financiar): "))
    if choice == 1:
        departamente = session.query(Departament).all()
        print("Departamente active:")
        for departament in departamente:
            print(f"Nume: {departament.nume} ")

        proiecte = session.query(Project).all()
        print("Proiectele active:")
        for proiect in proiecte:
            print(f"Nume: {proiect.nume}\nDescriere: {proiect.descriere}\nData Inceput: {proiect.data_inceput}\nData Sfarsit: {proiect.data_sfarsit}\nBuget_id: {proiect.budget_id}\nDepartament_id: {proiect.departament_id}\n")

        tasks = session.query(Task).all()
        print("Active tasks:")
        for task in tasks:
            print(f"Titlu: {task.titlu}\nDescriere: {task.descriere}\nTermen Limita: {task.termen_limita}\nStatus: {task.status}\nProiect_id: {task.proiect_id}\n")

        employees = session.query(Employee).all()
        print("Angajatii activi:")
        for employee in employees:
            print(f"Nume: {employee.nume}\nRol: {employee.rol}\nSalariu: {employee.salariu}\nEchipa_id: {employee.echipa_id}\nCompany_id: {employee.company_id}\nTask_id: {employee.task_id}\n")

        teams = session.query(Team).all()
        print("Echipele active:")
        for team in teams:
            print(f"Nume: {team.nume}\nProiect_id: {team.proiect_id}\nDepartament_id: {team.departament_id}\n")

    elif choice == 2:
        finances = session.query(Finance).order_by(Finance.id.desc()).first()
        if not finances:
            print("Finantele nu au fost adaugate.")
        else:
            print(f"Venituri: {finances.venituri}\nCheltuieli: {finances.cheltuieli}")



def meniu():
    while True:
        print("\n --- Meniu Companie ---")
        print("1. Adauga_angajat")
        print("2. Adauga Proiect")
        print("3. Adauga Departament")
        print("4. Adauga Echipa")
        print("5. Adauga Task")
        print("6. Adauga Buget")
        print("7. Adauga Resursa")
        print("8. Adauga Finance")
        print("9. Stergere Proiect")
        print("10. Stergere Task")
        print("11. Stergere Team")
        print("12. Stergere Employee")
        print("13. Actualizare Proiect")
        print("14. Actualizare Task")
        print("15. Actualizare Team")
        print("16. Actualizare Employee")
        print("17. Generare Raport")
        print("18. Exit()")

        optiune = int(input("Alegeti o optiune: "))

        if optiune == 1:
            adauga_angajat()
        elif optiune == 2:
            adauga_proiect()
        elif optiune == 3:
            adauga_departament()
        elif optiune == 4:
            adauga_echipa()
        elif optiune == 5:
            adauga_task()
        elif optiune == 6:
            adauga_buget()
        elif optiune == 7:
            adauga_resursa()
        elif optiune == 8:
            adauga_finance()
        elif optiune == 9:
            stergere_proiect()
        elif optiune == 10:
            stergere_task()
        elif optiune == 11:
            stergere_team()
        elif optiune == 12:
            stergere_employee()
        elif optiune == 13:
            actualizare_proiect()
        elif optiune == 14:
            actualizare_task()
        elif optiune == 15:
            actualizare_team()
        elif optiune == 16:
            actualizare_angajat()
        elif optiune == 17:
            generare_raport()
        elif optiune == 18:
            print("La revedere!")
            exit()
        else:
            print("Optiune invalida. Incercati din nou!")



if __name__ == "__main__":
    session = Session()
    companie = Company(nume=input("Introdu numele companiei: "))
    session.add(companie)
    meniu()
    session.close()
