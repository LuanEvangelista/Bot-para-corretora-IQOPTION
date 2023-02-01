# Bot para Corretora IQOPTION

## Descrição
Este é um bot de negociação para a corretora IQOPTION escrito em Python utilizando a biblioteca IQOptionAPI. O objetivo deste bot é realizar negociações na plataforma IQOPTION com base em estratégias Martingale e Stop Loss / Stop Gain.

## Requisitos

Para rodar este bot é necessário ter o Python instalado em sua máquina e as seguintes bibliotecas:

<ul>
    <li>iqoptionapi</li>
    <li>datetime</li>
    <li>json</li>
    <li>sys</li>
    <li>time</li>
</ul>

## Instalação
1. Clone este repositório para sua máquina:

       $ git clone https://github.com/LuanEvangelista/Bot-para-corretora-IQOPTION
 
 2. Instale as dependências:
 
      $ pip install -r requirements.txt

## Como usar
Este script em Python foi escrito para ser usado com a corretora IQ Option. Ele usa a biblioteca iqoptionapi para se conectar à conta da corretora e colocar negociações automatizadas usando o método Martingale. O usuário precisa inserir suas credenciais de login na linha 27.

O script define três funções: stop, Martingale e Payout. A função stop verifica se a negociação atual atingiu o lucro esperado ou se atingiu o limite de perda. Se isso acontecer, a negociação é encerrada. 

A função Martingale ajusta o valor da negociação baseado no payout esperado e no valor de entrada. A função Payout retorna o payout esperado para o par de moedas selecionado.

No script, o usuário também define as variáveis ​​para o par de moedas, valor de entrada, quantidade de Martingale, limite de perda e limite de lucro. O script então se conecta à conta da corretora e começa a colocar negociações automatizadas usando o método Martingale. A negociação é encerrada se atingir o limite de lucro ou limite de perda ou se ocorrer algum erro na conexão com a conta da corretora.
