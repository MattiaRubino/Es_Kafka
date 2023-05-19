from db import DestinationSession
from model import Document,Log_change
from sqlalchemy import create_engine,update,event,select
from sqlalchemy.orm import sessionmaker,session
from confluent_kafka import Producer
import time,datetime
import manage
import logging
import json
import threading
from convert_data import convert_datetime_to_utc_string

with open('starter.txt') as f:
    last_producer = int(f.readline())
    f.close()

logging.basicConfig(format='%(message)s', level = logging.INFO, filename='producer.log',filemode='w' )
logger = logging.getLogger()

session = DestinationSession()
def receipt(err,msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        message = msg.value().decode('utf-8')
        logger.info(message)


def prod():
      p=Producer({'bootstrap.servers':'localhost:9092'})
      global last_producer
      while True:
          last_row = session.execute(select(Log_change.id_change).order_by(Log_change.id_change.desc())).first()
          last_row = int(last_row[0])
          sql = ('SELECT * from Log_change where id_change > %s') % last_producer
          results = session.execute(sql)
          while last_producer<last_row :
              for record in results:
                   print("\n", record)
                   last_producer= int(record[3])
                   data = {
                       'id_document': record[0],
                       'type_chage': record[1],
                       'date_change': convert_datetime_to_utc_string(record[2]),
                       'id_change': record[3],
                                     }
                   m = json.dumps(data)
                   p.poll(1)
                   p.produce('my-topic', m.encode('utf-8'),callback=receipt)
                   p.flush()
                   f = open("starter.txt", "w")
                   f.write(str(record[3]))
                   f.close()
                   time.sleep(30)




def menu():
    while True:
        while True:
            print("\n-----Gestione Document-----")
            print("\n1 - Crea Document")
            print("2 - Elimina  Document")
            print("3 - Cerca Document")
            print("4 - Update  Document")
            print("5 - Visualizza  Documents")
            print("6 - Esci")
            choice_Document = input("Scegli l'opzione con un numero: ")
            if any([x in choice_Document for x in ['1', '2', '3', '4', '5', '6']]):
                break
            else:
                print("Valore inserito non corretto")

        if choice_Document == '1':
            manage.add_document()
        elif choice_Document == '2':
            manage.delete_document()
        elif choice_Document == '3':
            manage.search_document()
        elif choice_Document == '4':
            manage.set_document()
        elif choice_Document == '5':
            manage.view_document()
        elif choice_Document == '6':
            break

if __name__=='__main__':
    threading.Thread(target = menu).start()
    threading.Thread(target=prod).start()
