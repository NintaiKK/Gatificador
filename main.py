import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from openpyxl import Workbook
from openpyxl import load_workbook

#config janela
janela = tk.Tk()
janela.resizable(0,0)
janela.geometry('800x500')
janela.title('resGatados')

def cadastroRsg():
  
  try:
        wb = load_workbook('resGatados.xlsx')
  except FileNotFoundError:
        wb = Workbook()

  planilha = wb.active

  getRsg = entryRsg.get()
  getNm  = entryCdsNm.get()
  getQtd = entryRsgQtd.get()
  getOrg = entryCdsOrg.get()
  getVol = entryVol.get()

  planilha.append(['Resgatador', 'Número do resgatador', 'Quantidade de resgatados', 'Origiem', 'Voluntário'])
  planilha.append([getRsg, getNm, getQtd, getOrg, getVol])

  wb.save('resGatados.xlsx')
  
  entryRsg.delete(0, tk.END)
  entryCdsNm.delete(0, tk.END)
  entryRsgQtd.delete(0, tk.END)
  entryCdsOrg.delete(0, tk.END)
  entryVol.delete(0, tk.END)

  messagebox.showinfo('Sucesso!', 'Resgatador cadastrado, não esqueça de cadastrar os gatos!')

def cadastroTutor():
  
  try:
        wb = load_workbook('resGatados.xlsx')
  except FileNotFoundError:
        wb = Workbook()

  planilha = wb.active

  getCor = cor.get()
  getCO  = corOlho.get()
  getSexo = sexo.get()
  getId = id.get()
  getObs = entryObs.get()
  getTut = tut.get()
  getNmTut  = entryTut.get()
  getNrTut = entryNr.get()

  planilha.append(['Cor', 'Cor dos olhos','Sexo', 'Idade', 'Observações', 'Tem tutor?', 'Tutor', 'Número Tutor'])
  planilha.append([getCor, getCO, getSexo, getId, getObs, getTut, getNmTut, getNrTut])

  wb.save('resGatados.xlsx')

  entryTut.delete(0, tk.END)
  entryNr.delete(0, tk.END)
  

  messagebox.showinfo('Sucesso!', 'Gato cadastrado com sucesso!')

def cadastroData():
  try:
        wb = load_workbook('resGatados.xlsx')
  except FileNotFoundError:
        wb = Workbook()

  planilha = wb.active

  getData = entryData.get()
  
  planilha.append([getData])

  wb.save('resGatados.xlsx')

  entryData.delete(0, tk.END)
  

  messagebox.showinfo('Sucesso!', 'Data cadastrada com sucesso!')

def cadastroSaida():
  try:
        wb = load_workbook('resGatados.xlsx')
  except FileNotFoundError:
        wb = Workbook()

  planilha = wb.active

  getIde - entryIde.get()
  getMot = mot.get()
  getObs = entryObs.get()
  getNmTut = entryNmTut.get()
  getNrTut = entryNrTut.get()

  planilha.append(['Id coleira', 'Motiva da saída', 'Observações', 'Tutor', 'Número do tutor'])
  planilha.append([getIde, getMot, getObs, getNmTut, getNrTut])

  wb.save('resGatados.xlsx')

  entryIde.delete(0, tk.END)
  entryObs.delete(0, tk.END)
  entryNmTut.delete(0, tk.END)
  entryNrTut.delete(0, tk.END)
  
  messagebox.showinfo('Sucesso!', 'Data cadastrada com sucesso!')
#tab config

#tab
#separar entrada e saída#######################
tab = ttk.Notebook(janela)

tab.place(
    x=0,
    y=0,
    width=800,
    height=500)

data=Frame(tab)
rgs=Frame(tab)
gato=Frame(tab)
saida=Frame(tab)

tab.add(data,text='Data')
tab.add(rgs,text='Resgatador')
tab.add(gato,text='Gato')
tab.add(saida,text='Saída')
#tab config //
#aba data
lblData = tk.Label(
  data,
  text='Data do cadastro')
lblData.pack()

entryData = tk.Entry(
  data,
  width=50)
entryData.pack()

lblFantl = tk.Label(
    data,
    height=2)
lblFantl.pack()

btnCds = tk.Button(
    data,
    command=cadastroData,
    text = 'Cadastrar',
    width=20,
    height=2)
btnCds.pack()
#aba data//
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

lblVol = tk.Label(
    rgs,
    text='Voluntário')
lblVol.pack()

entryVol = tk.Entry(
  rgs,
  width=50)
entryVol.pack()

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

lblTut = tk.Label(
    gato,
    text='Tem tutor?')
lblTut.pack()

tut = Combobox(gato)
tut['values'] = ('Sim',
                 'Não')
tut.pack()

lblTut = tk.Label(
    gato,
    text='Tutor')
lblTut.pack()

entryTut = tk.Entry(
    gato,
    width=50)
entryTut.pack()

tutNr = tk.Label(
    gato,
    text='Número')
tutNr.pack()

entryNr = tk.Entry(
    gato,
    width=50)
entryNr.pack()

lblFant2 = tk.Label(
    gato,
    height=2)
lblFant2.pack()

btnCds2 = tk.Button(
    gato,
    command=cadastroTutor,
    text = 'Cadastrar',
    width=20,
    height=2)
btnCds2.pack()
#aba gato//
#aba saída
lblIde = tk.Label(
  saida,
  text='Id da coleira')
lblIde.pack()

entryIde = tk.Entry(
  saida,
  width=50)
entryIde.pack()

lblSai = tk.Label(
  saida,
  text='Motivo da saída')
lblSai.pack()

mot = Combobox(saida)
mot['values'] = ('Adotado',
                 'Identificado',
                 'Lar temporário',
                 'Outro')
mot.pack()

lblObs = tk.Label(
  saida,
  text='Observações')
lblObs.pack()

entryObs = tk.Entry(
  saida,
  width=50)
entryObs.pack()

lblNmTut = tk.Label(
    saida,
    text='Nome do novo tutor')
lblNmTut.pack()

entryNmTut = tk.Entry(
    saida,
    width=50)
entryNmTut.pack()

tutNr = tk.Label(
    saida,
    text='Número do novo tutor')
tutNr.pack()

entryNrTut = tk.Entry(
    saida,
    width=50)
entryNrTut.pack()

lblFanti = tk.Label(
    saida,
    height=2)
lblFanti.pack()

btnCdsi = tk.Button(
    saida,
    command=cadastroData,
    text = 'Cadastrar',
    width=20,
    height=2)
btnCdsi.pack()
    
#aba saída//

janela.mainloop()
