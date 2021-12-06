from iqoptionapi.stable_api import IQ_Option
import time
import json
from datetime import datetime
from dateutil import tz
import sys


def stop(lucro, gain, loss):
    if lucro <= float("-" + str(abs(loss))):
        print("Stop Loss batido!")
        sys.exit()

    if lucro >= float(abs(gain)):
        print("Stop Gain Batido!")
        sys.exit()


def Martingale(valor, payout):
    lucro_esperado = valor * payout #1.20
    perca = float(valor) # -2.00

    while True:
        if round(valor * payout, 2) > round(abs(perca) + lucro_esperado, 2):
            return round(valor, 2)
            break
        valor += 0.01


def Payout(par):
    #API.subscribe_strike_list(par, 1)
    #while True:
        #d = API.get_digital_payout(par)
        #if d != False:
            #d = round(int(d) / 100, 2)
            #break
        #time.sleep(1)
    #API.unsubscribe_strike_list(par, 1)
    d=round(int(API.get_digital_payout(par)) / 100, 2)
    

    return d


API = IQ_Option("USUARIO", "SENHA")  # Entrar Login e Senha
API.connect()
API.change_balance("PRACTICE")  # Real ou Practice -----------------------------------------------------------------------------

while True:
    if API.check_connect() == False:
        print("Erro ao conectar")
        API.connect
    else:
        print("Conectado com Sucesso")
        break
    time.sleep(3)


def timestamp_converter(x):  # Função para converter timestamp
    hora = datetime.strptime(datetime.utcfromtimestamp(x).strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    hora = hora.replace(tzinfo=tz.gettz("GMT"))

    return hora


def banca():
    return API.get_balance()


print("Banca:", banca())  # pega valor da Banca
par = "EURUSD"  #Moeda -------------------------------------------------------------------------------------------------------------------------------------
valor_entrada = (float(2))

valor_entrada_b = float(valor_entrada)

martingale = int(3) #Quantidade de gale -------------------------------------------------------------------------------------------------------------
martingale += 1

stop_loss = float(37)
print("Stop Loss:", stop_loss)
stop_gain = float(20)
print("Stop Gain:", stop_gain)

lucro = 0
valor = 0
payout = Payout(par)
print(payout)


while True:
    teste = timestamp_converter(API.get_server_timestamp())
    minutos = float((teste.strftime("%M.%S"))[1:])
    
    entrarHORA = True if (minutos >= 0.59 and minutos <= 1) or (minutos >= 1.59 and minutos <= 2) or (minutos >= 2.59 and minutos <= 3) or (minutos >= 3.59 and minutos <= 4) or (minutos >= 4.59 and minutos <= 5) or (minutos >= 5.59 and minutos <= 6) or (minutos >= 6.59 and minutos <= 7) or (minutos >= 7.59 and minutos <= 8) or (minutos >= 8.59 and minutos <= 9) or  minutos >= 9.59 else False

    dir = False

    velas = API.get_candles(par, 60, 3, API.get_server_timestamp())

    velas[0] = ( "g" if velas[0]["open"] < velas[0]["close"] else "r" if velas[0]["open"] > velas[0]["close"] else "d")
    velas[1] = ( "g" if velas[1]["open"] < velas[1]["close"] else "r" if velas[1]["open"] > velas[1]["close"] else "d")
    velas[2] = ( "g" if velas[2]["open"] < velas[2]["close"] else "r" if velas[2]["open"] > velas[2]["close"] else "d")

    cores = velas[0] + " " + velas[1] + " " + velas[2]
    print(cores)

    if cores.count("d") == 0:
        if cores.count("g") >= 3:
            dir = 'put'
        if cores.count("r") >= 3:
            dir = 'call'

    entrar = True if ( (dir == 'call' or dir == 'put') and entrarHORA == True) else False


    if entrar:
        print("\n\nIniciando Trade!", "\nData:", str(teste)[:-6])

        if valor > 0:  # Wins consecutivos adicionam metade do Gain na próxima entrada

            valor_entrada = 2 

        else:
            valor_entrada = 2

        print("Entrada:", valor_entrada)
        

        print("\nSentido:",dir)

        if dir:

            for i in range(martingale):

                status, id = API.buy_digital_spot_v2(par, valor_entrada, dir, 1)

                if status:
                    while True:
                        status, valor = API.check_win_digital_v2(id)

                        if status:
                            valor = (valor if valor > 0 else float("-" + str(abs( valor_entrada ))))
                            lucro += round(valor, 2)

                            print("Resultado: ", end="")
                            print("WIN /" if valor > 0 else "LOSS /",round(valor, 2), "/",round(lucro, 2),("/ " + str(i) + " GALE" if i > 0 else ""))

                            valor_entrada = Martingale(valor_entrada , payout)  # Martingale com metade do valor de entrada * o payout

                            stop(lucro, stop_gain, stop_loss)

                            break

                    if valor > 0:
                        break

                else:
                    print("\nERRO AO REALIZAR ORDEM\n\n")

        else:
            print("Analise Inconclusiva, foram encontrados candles neutros")
            time.sleep(1)
            entrar = False
