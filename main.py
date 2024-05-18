import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *


#config janela
janela = tk.Tk()
janela.resizable(0,0)
janela.geometry('800x500')
janela.title('Gatificador beta')

#config janela//
#tab config

tab = ttk.Notebook(janela)

tab.place(
    x=0,
    y=0,
    width=800,
    height=500)

psq=Frame(tab)
cds=Frame(tab)
vsl=Frame(tab)
edit=Frame(tab)

tab.add(psq,text='Recibo')
tab.add(cds,text='Cadastro')
tab.add(vsl,text='Visualizar')
tab.add(edit,text='Editar')
#tab config //
#aba pesquisa

PsqSpc = tk.Label(
    psq,
    height=2
)
PsqSpc.pack()

psqBar = tk.Entry(
    psq,
    width = 50
)
psqBar.pack()

PsqSpc2 = tk.Label(
    psq,
    height=1
)
PsqSpc2.pack()

btnPsq = tk.Button(
    psq,
    #command = ,
    text = 'Pesquisar'
)
btnPsq.pack()
#aba pesquisa//
#aba cadastro

lblCdsNr = tk.Label(
    cds,
    text='Resgate nº')
lblCdsNr.pack()

entryCdsNr = tk.Entry(
    cds,
    width=50)
entryCdsNr.pack()

lblCdsNm = tk.Label(
    cds,
    text='Nome')
lblCdsNm.pack()

entryCdsNm = tk.Entry(
    cds,
    width=50)
entryCdsNm.pack()

lblCdsCor = tk.Label(
    cds,
    text='Cor predominante')
lblCdsCor.pack()

entryCdsCor = tk.Entry(
    cds,
    width=50)
entryCdsCor.pack()

lblCdsPel = tk.Label(
    cds,
    text='Padrão de pelagem')
lblCdsPel.pack()

entryCdsPel = tk.Entry(
    cds,
    width=50)
entryCdsPel.pack()

lblFants = tk.Label(
    cds,
    height=2)
lblFants.pack()

lblTut = tk.Label(
    cds,
    text = 'Tutor'
)
lblTut.pack()

combo = Combobox(cds)
combo['values']= ('Indefinido',
                  'Tem tutor',
                  'Não tem tutor')
combo.pack()

btnCds = tk.Button(
    cds,
    #command=cadastrar,
    text = 'Cadastrar',
    width=20,
    height=2)
btnCds.pack()

lblSpcs = tk.Label(
    cds,
    height=1)
lblSpcs.pack()

btnLimp = tk.Button(
    cds,
    #command=limpar2,
    text = 'Limpar',
    width=20,
    height=2)
btnLimp.pack()
#cds //

janela.mainloop()
