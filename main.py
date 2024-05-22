import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from openpyxl import Workbook



#config janela
janela = tk.Tk()
janela.resizable(0,0)
janela.geometry('800x500')
janela.title('resGatados')

#config janela//
#criar/abre planilha
wb = Workbook()#TESTAR
planilha = wb.active#TESTAR
#criar/abre planilha//
#config defs
def cadastroRsg():

  getRsg = entryRsg.get()
  getNm  = entryCdsNm.get()
  getQtd = entryRsgQtd.get()
  getOrg = entryCdsOrg.get()

  planilha['B2'] = getRsg
  planilha['C2'] = getNm
  planilha['D2'] = getQtd
  planilha['E2'] = getOrg

  wb.save('resGatados.xlsx')
#tab config

tab = ttk.Notebook(janela)

tab.place(
    x=0,
    y=0,
    width=800,
    height=500)

rgs=Frame(tab)
gato=Frame(tab)
ttr=Frame(tab)

tab.add(rgs,text='Resgatador')
tab.add(gato,text='Gato')
tab.add(ttr,text='Tutor')
#tab config //
#aba resgatador

lblRsg = tk.Label(
    rgs,
    text='Resgatador')
lblRsg.pack()

entryRsg = tk.Entry(
    rgs,
    width=50)
entryRsg.pack()

lblCdsNm = tk.Label(
    rgs,
    text='Número')
lblCdsNm.pack()

entryCdsNm = tk.Entry(
    rgs,
    width=50)
entryCdsNm.pack()

lblRsgQtd = tk.Label(
    rgs,
    text='Quantidade de Resgatados')
lblRsgQtd.pack()

entryRsgQtd = tk.Entry(
    rgs,
    width=50)
entryRsgQtd.pack()

lblCdsOrg = tk.Label(
    rgs,
    text='De onde veio')
lblCdsOrg.pack()

entryCdsOrg = tk.Entry(
    rgs,
    width=50)
entryCdsOrg.pack()

lblFants = tk.Label(
    rgs,
    height=2)
lblFants.pack()

btnCds = tk.Button(
    rgs,
    command=cadastroRsg,
    text = 'Cadastrar',
    width=20,
    height=2)
btnCds.pack()

lblSpcs = tk.Label(
    rgs,
    height=1)
lblSpcs.pack()

btnLimp = tk.Button(
    rgs,
    #command=limpar2,
    text = 'Limpar',
    width=20,
    height=2)
btnLimp.pack()
#aba resgatador //
#aba gato

lblCor = tk.Label(
    gato,
    text='Cor da pelagem'
)
lblCor.pack()

cor = Combobox(gato)
cor['values']= ('Branco',
                  'Preto',
                  'Frajola',
                  'Siames',
                  'Escaminha',
                  'Tricolor',
                  'Tigrado',
                  'Tigrado com branco',
                  'Cinza',
                  'Laranja',
                  'Cinza com branco',
                  'Laranja com branco',
                  'Outros')
cor.pack()

lblCorOlhos = tk.Label(
    gato,
    text='Cor dos olhos'
)
lblCorOlhos.pack()

corOlho = Combobox(gato)
corOlho['values']= ('Amarelo',
                    'Verde',
                    'Azul',
                    'Um de cada cor')
corOlho.pack()

lblSex = tk.Label(
    gato,
    text='Sexo')
lblSex.pack()

sexo = Combobox(gato)
sexo['values']= ('Macho',
                 'Fêmea',
                 'Não identificado')
sexo.pack()

lblId = tk.Label(
    gato,
    text='Idade')
lblId.pack()

id = Combobox(gato)
id['values']= ('Bebê',
               'Filhote',
               'Adulto',)
id.pack()

lblObs = tk.Label(
    gato,
    text='Observações')
lblObs.pack()

entryObs = tk.Entry(
    gato,
    width=50)
entryObs.pack()

lblFant1 = tk.Label(
    gato,
    height=2)
lblFant1.pack()

btnCds1 = tk.Button(
    gato,
    #command=cadastroRsg,
    text = 'Cadastrar',
    width=20,
    height=2)
btnCds1.pack()

lblSpc1 = tk.Label(
    gato,
    height=1)
lblSpc1.pack()

btnLimp1 = tk.Button(
    gato,
    #command=limpar2,
    text = 'Limpar',
    width=20,
    height=2)
btnLimp1.pack()
#aba gato //
#aba tutor

lblTut = tk.Label(
    ttr,
    text='Tem tutor?')
lblTut.pack()

tut = Combobox(ttr)
tut['values'] = ('Sim',
                 'Não')
tut.pack()

lblTut = tk.Label(
    ttr,
    text='Tutor')
lblTut.pack()

entryTut = tk.Entry(
    ttr,
    width=50)
entryTut.pack()

tutNr = tk.Label(
    ttr,
    text='Número')
tutNr.pack()

entryNr = tk.Entry(
    ttr,
    width=50)
entryNr.pack()

lblFant2 = tk.Label(
    ttr,
    height=2)
lblFant2.pack()

btnCds2 = tk.Button(
    ttr,
    #command=cadastrar,
    text = 'Cadastrar',
    width=20,
    height=2)
btnCds2.pack()

lblSpc2 = tk.Label(
    ttr,
    height=1)
lblSpc2.pack()

btnLimp2 = tk.Button(
    ttr,
    #command=limpar2,
    text = 'Limpar',
    width=20,
    height=2)
btnLimp2.pack()

janela.mainloop()
