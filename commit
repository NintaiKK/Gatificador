import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from openpyxl import Workbook
from openpyxl import load_workbook

janela = tk.Tk()
janela.resizable(0,0)
janela.geometry('800x500')
janela.title('resGatados')

def opEnt():
    janela2 = tk.Toplevel()
    janela2.title('Cadastro de entrada')
    janela2.geometry('500x400')

    dtRsg = tk.Label(
        janela2,
        text = 'Data do resgate',)
    dtRsg.pack()

    dtEntr = tk.Entry(
        janela2,
        width = 15)
    dtEntr.pack()

    resRet = Combobox(janela2)
    resRet['values']= ('Resgate',
                       'Retorno')
    resRet.pack()
    
    cdReg = tk.Label(
        janela2,
        text = 'Código de registro')
    cdReg.pack()

    cdBtn = tk.Entry(
        janela2,
        width = 15)
    cdBtn.pack()

    ttrRsp = tk.Label(
        janela2,
        text = 'Tutor/Responsável')
    ttrRsp.pack()

    ttrEntr = tk.Entry(
        janela2,
        width = 15)
    ttrEntr.pack()

    tlf = tk.Label(
        janela2,
        text = 'Telefone do tutor')
    tlf.pack()

    tlfEntr = tk.Entry(
        janela2,
        width = 15)
    tlfEntr.pack()
    
    botao_voltar1 = tk.Button(janela2, text = 'Fechar a janela2', command = janela2.destroy)
    botao_voltar1.pack()

def opTr():
    janela3 = tk.Toplevel()
    janela3.title('Cadastro de triagem')
    janela3.geometry('200x200')
    botao_voltar2 = tk.Button(janela3, text = 'Fechar a janela3', command = janela3.destroy)
    botao_voltar2.pack()

def opSai():
    janela4 = tk.Toplevel()
    janela4.title('Cadastro de saída')
    janela4.geometry('200x200')
    botao_voltar3 = tk.Button(janela4, text = 'Fechar a janela4', command = janela4.destroy)
    botao_voltar3.pack()
    

a = tk.Frame()
b = tk.Frame()
c = tk.Frame()

lblVrd = tk.Label(
    master= a,
    height = 100,
    width = 45,
    text='OnlyCats',
    bg='grey')
lblVrd.pack()

lblSpcs = tk.Label(
    master = c,
    width = 25)
lblSpcs.pack()

btnCds = tk.Button(
    master = b,
    command = opEnt,
    width = 15,
    text = 'Entrada')
btnCds.pack()

lblSpc = tk.Label(
    master = b,
    width = 15)
lblSpc.pack()

btnTrg = tk.Button(
    command = opTr,
    master = b,
    width = 15,
    text = 'Triagem')
btnTrg.pack()

btnSpc = tk.Label(
    master = b,
    height = 1)
btnSpc.pack()

btnSd = tk.Button(
    command = opSai,
    master = b,
    width = 15,
    text = 'Saida')
btnSd.pack()
    

a.pack(side = LEFT)
c.pack(side = LEFT)
b.pack(side = LEFT)


janela.mainloop()
