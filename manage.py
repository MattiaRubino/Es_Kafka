from db import DestinationSession,DESTINATION_DB
from model import Document,Log_change
from sqlalchemy import create_engine,update,event,select,delete
from sqlalchemy.orm import sessionmaker,session
import  pandas as pd


session = DestinationSession()

def add_document():
    i = input("inserisci valori author,title_book,date,e_mail separati da virgola = ")
    elem = i.split(",")
    new_document = Document(author = elem[0], title_book = elem[1], date = elem[2], e_mail = elem[3])
    session.add(new_document)
    session.commit()
    print("\nDocument creato")


def delete_document():
    del_document = input("Inserisci l'id_document : ")
    if(del_document.isnumeric()):
        session.query(Document).filter(Document.id_document == del_document).delete()
        session.commit()
        print("\nDocument eliminato")
    else:
        print("valore id_document inserito non corretto")

def set_document():
    set_d = input("Inserisci l'id_document : ")
    if set_d.isnumeric():
        while True:
            while True:
                campo_modifica = input(" inserisci nome colonna da modificare: ")
                if any([x in campo_modifica for x in ['author','title_book','date','e_mail']]):
                   break
                else:
                    print("Valore inserito non corretto")

            modifica = input(" inserisci nuovo dato: ")
            up_doc = '''UPDATE documents SET %s ='%s' WHERE id_document=%s''' % (campo_modifica, modifica, set_d)
            session.execute(up_doc)
            session.commit()
            print("\nDocument modificato")
            new_modifica = input("inserisci y per continuare a modificare altro per uscire")
            if (new_modifica != "y"):
                break
    else:
        print("valore id_document inserito non corretto")

def search_document():
    search= input("Inserisci l'id_document : ")
    x = session.query(Document).filter(Document.id_document == search).all()
    print(x[0])

def view_document():
    destination_engine = create_engine(DESTINATION_DB).connect()
    df = pd.read_sql_table("documents", DESTINATION_DB)
    print(df)
