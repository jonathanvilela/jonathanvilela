import mysql.connector
from tkinter import*
import mysql.connector
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from datetime import datetime






def bt1():
    Nome=str(caixa1.get())
    Idade=str(caixa2.get())
    CPF=str(caixa3.get())
    Telefone=str(caixa4.get())
    DiaMarcado=str(caixa5.get())

    now=datetime.now()
    horario=str(now.hour)
    minutos=str(now.minute)
    segundos=str(now.second)

    d=str(now.year)
    e=str(now.month)
    f=str(now.day)
    
    Hora=horario+':'+minutos+':'+segundos
    Ano=f+'/'+e+'/'+d
    
    

    declaracao = """INSERT INTO tbl_consultas
                (Nome,Idade,CPF,Telefone,DiaMarcado,Hora,Ano)
                VALUES ( """

    #dados='cliente','modelo',valor_fabrica)
    
    dados='\''+Nome+'\','+Idade+','+CPF+','+Telefone+',\''+DiaMarcado+'\',\''+Hora+'\',\''+Ano+'\')'

    sql= declaracao+dados

    print(sql)

    #criar conexão ao banco de dados
    con = mysql.connector.connect(host='localhost',database='db_consulta',user='root',password='kudlakjo28')

    if con.is_connected():
            db_info = con.get_server_info()
            print("Conectado ao servidor MySQL versão: ",db_info)

            cursor = con.cursor()
            cursor.execute("select database();") #saber qual banco está sendo usado
            linha = cursor.fetchone()#retorna a instrução acima (vá buscar uma linha)
            print("Conectado ao banco de dados: ",linha)

    criar_tabela_SQL = """CREATE TABLE tbl_consultas (
                                        Nome VARCHAR(70) NOT NULL,
                                        Idade INT(70) NOT NULL,
                                        CPF INT(70) NOT NULL,
                                        Telefone INT(70) NOT NULL,
                                        DiaMarcado VARCHAR(70) NOT NULL,
                                        Hora VARCHAR(70) NOT NULL,
                                        Ano VARCHAR(70) NOT NULL,
                                        PRIMARY KEY (Nome))"""
    #elementos foram adicionados (pelo programador) nesse espaço

    cursor = con.cursor()
    #cursor.execute(criar_tabela_SQL) #Apenas para criar tabela, depois de criada, comentar ele para nao dar error
    inserir_produtos = sql
    cursor.execute(inserir_produtos)
    con.commit() #comitar os dados na tabela, gravar os dados em definitivo
    print(cursor.rowcount,"registros inseridos na tabela!")


    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")



def bt2():

    Nome=str(caixa1.get())
    Idade=str(caixa2.get())
    CPF=str(caixa3.get())
    Telefone=str(caixa4.get())
    DiaMarcado=str(caixa5.get())

    now=datetime.now()
    horario=str(now.hour)
    minutos=str(now.minute)
    segundos=str(now.second)

    d=str(now.year)
    e=str(now.month)
    f=str(now.day)
    
    Hora=horario+':'+minutos+':'+segundos
    Ano=f+'/'+e+'/'+d
    
    

    declaracao = """INSERT INTO tbl_exames
                (Nome,Idade,CPF,Telefone,DiaMarcado,Hora,Ano)
                VALUES ( """

    #dados='cliente','modelo',valor_fabrica)
    
    dados='\''+Nome+'\','+Idade+','+CPF+','+Telefone+',\''+DiaMarcado+'\',\''+Hora+'\',\''+Ano+'\')'

    sql= declaracao+dados

    print(sql)

    #criar conexão ao banco de dados
    con = mysql.connector.connect(host='localhost',database='db_exames',user='root',password='kudlakjo28')

    if con.is_connected():
            db_info = con.get_server_info()
            print("Conectado ao servidor MySQL versão: ",db_info)

            cursor = con.cursor()
            cursor.execute("select database();") #saber qual banco está sendo usado
            linha = cursor.fetchone()#retorna a instrução acima (vá buscar uma linha)
            print("Conectado ao banco de dados: ",linha)

    criar_tabela_SQL = """CREATE TABLE tbl_exames (
                                        Nome VARCHAR(70) NOT NULL,
                                        Idade INT(70) NOT NULL,
                                        CPF INT(70) NOT NULL,
                                        Telefone INT(70) NOT NULL,
                                        DiaMarcado VARCHAR(70) NOT NULL,
                                        Hora VARCHAR(70) NOT NULL,
                                        Ano VARCHAR(70) NOT NULL,
                                        PRIMARY KEY (Nome))"""
    #elementos foram adicionados (pelo programador) nesse espaço

    cursor = con.cursor()
    #cursor.execute(criar_tabela_SQL) #Apenas para criar tabela, depois de criada, comentar ele para nao dar error
    inserir_produtos = sql
    cursor.execute(inserir_produtos)
    con.commit() #comitar os dados na tabela, gravar os dados em definitivo
    print(cursor.rowcount,"registros inseridos na tabela!")


    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")


def bt3():

    Nome=str(caixa1.get())
    Idade=str(caixa2.get())
    CPF=str(caixa3.get())
    Telefone=str(caixa4.get())
    DiaMarcado=str(caixa5.get())

    now=datetime.now()
    horario=str(now.hour)
    minutos=str(now.minute)
    segundos=str(now.second)

    d=str(now.year)
    e=str(now.month)
    f=str(now.day)
    
    Hora=horario+':'+minutos+':'+segundos
    Ano=f+'/'+e+'/'+d
    
    

    declaracao = """INSERT INTO tbl_Cirurgia
                (Nome,Idade,CPF,Telefone,DiaMarcado,Hora,Ano)
                VALUES ( """

    #dados='cliente','modelo',valor_fabrica)
    
    dados='\''+Nome+'\','+Idade+','+CPF+','+Telefone+',\''+DiaMarcado+'\',\''+Hora+'\',\''+Ano+'\')'

    sql= declaracao+dados

    print(sql)

    #criar conexão ao banco de dados
    con = mysql.connector.connect(host='localhost',database='db_Cirurgia',user='root',password='kudlakjo28')

    if con.is_connected():
            db_info = con.get_server_info()
            print("Conectado ao servidor MySQL versão: ",db_info)

            cursor = con.cursor()
            cursor.execute("select database();") #saber qual banco está sendo usado
            linha = cursor.fetchone()#retorna a instrução acima (vá buscar uma linha)
            print("Conectado ao banco de dados: ",linha)

    criar_tabela_SQL = """CREATE TABLE tbl_Cirurgia (
                                        Nome VARCHAR(70) NOT NULL,
                                        Idade INT(70) NOT NULL,
                                        CPF INT(70) NOT NULL,
                                        Telefone INT(70) NOT NULL,
                                        DiaMarcado VARCHAR(70) NOT NULL,
                                        Hora VARCHAR(70) NOT NULL,
                                        Ano VARCHAR(70) NOT NULL,
                                        PRIMARY KEY (Nome))"""
    #elementos foram adicionados (pelo programador) nesse espaço

    cursor = con.cursor()
    #cursor.execute(criar_tabela_SQL) #Apenas para criar tabela, depois de criada, comentar ele para nao dar error
    inserir_produtos = sql
    cursor.execute(inserir_produtos)
    con.commit() #comitar os dados na tabela, gravar os dados em definitivo
    print(cursor.rowcount,"registros inseridos na tabela!")


    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")


def bt4():

    Nome=str(caixa1.get())
    Idade=str(caixa2.get())
    CPF=str(caixa3.get())
    Telefone=str(caixa4.get())
    DiaMarcado=str(caixa5.get())

    now=datetime.now()
    horario=str(now.hour)
    minutos=str(now.minute)
    segundos=str(now.second)

    d=str(now.year)
    e=str(now.month)
    f=str(now.day)
    
    Hora=horario+':'+minutos+':'+segundos
    Ano=f+'/'+e+'/'+d
    
    

    declaracao = """INSERT INTO tbl_poscirurgico
                (Nome,Idade,CPF,Telefone,DiaMarcado,Hora,Ano)
                VALUES ( """

    #dados='cliente','modelo',valor_fabrica)
    
    dados='\''+Nome+'\','+Idade+','+CPF+','+Telefone+',\''+DiaMarcado+'\',\''+Hora+'\',\''+Ano+'\')'

    sql= declaracao+dados

    print(sql)

    #criar conexão ao banco de dados
    con = mysql.connector.connect(host='localhost',database='db_poscirurgico',user='root',password='kudlakjo28')

    if con.is_connected():
            db_info = con.get_server_info()
            print("Conectado ao servidor MySQL versão: ",db_info)

            cursor = con.cursor()
            cursor.execute("select database();") #saber qual banco está sendo usado
            linha = cursor.fetchone()#retorna a instrução acima (vá buscar uma linha)
            print("Conectado ao banco de dados: ",linha)

    criar_tabela_SQL = """CREATE TABLE tbl_poscirurgico (
                                        Nome VARCHAR(70) NOT NULL,
                                        Idade INT(70) NOT NULL,
                                        CPF INT(70) NOT NULL,
                                        Telefone INT(70) NOT NULL,
                                        DiaMarcado VARCHAR(70) NOT NULL,
                                        Hora VARCHAR(70) NOT NULL,
                                        Ano VARCHAR(70) NOT NULL,
                                        PRIMARY KEY (Nome))"""
    #elementos foram adicionados (pelo programador) nesse espaço

    cursor = con.cursor()
    #cursor.execute(criar_tabela_SQL) #Apenas para criar tabela, depois de criada, comentar ele para nao dar error
    inserir_produtos = sql
    cursor.execute(inserir_produtos)
    con.commit() #comitar os dados na tabela, gravar os dados em definitivo
    print(cursor.rowcount,"registros inseridos na tabela!")


    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão ao MySQL foi encerrada")



def bt5():



    
    
    def pesquisar():
        
        
        procura_coluna = str(caixa88.get())
        procura_elemento = str(caixa99.get())
        condicao = f"{procura_coluna} = \'{procura_elemento}\'"
        elemento_especifico = 'CPF'

        consulta_sql =( f" select {elemento_especifico} "
                        f" from tbl_consultas"     
                        f" where {condicao};")
        

        con = mysql.connector.connect(host='localhost',database='db_consulta',user='root',password='kudlakjo28')
        consulta_sql = "select * from tbl_consultas"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall() #vou pegar todas as linhas retornadas com o método fetchall e armazenar em linhas
        print("Número total de registros retornados: ",cursor.rowcount)

        print("\nMostrar os produtos cadastrados\n")

        for linha in linhas: 
            #print("Nome: ",linha[0])
            #print("Idade: ",linha[1])
            print("CPF ",linha[2])
            #print("Contato: ",linha[3])
            #print("Data Marcada: ",linha[4])
            #print("Horario: ",linha[5])
            #print("Data do Registro: ",linha[6],"\n")

        print(consulta_sql)
        

        #consulta_sql2 = (" select * from tbl_consultas where Nome = 'condicao';")
        #print(consulta_sql2)

        


            
        
    n= Toplevel()
    n.title("Buscar no banco")
    n.geometry("300x100")
    n.resizable(0,0)
    
    bt89=Button(n,text="Pesquisar",command=pesquisar,fg="green")
    bt89.config(height=1,width=10)
    bt89.place(x=215,y=40)
    
    text=Label(n,text="Buscar Coluna",fg="Blue")
    text.place(x=30,y=30)
    
    caixa88 = StringVar()
    caixa88Box = Entry(n, textvariable=caixa88)
    caixa88Box.place(x=120,y=30, width=90, height=25)

    caixa99 = StringVar()
    caixa99Box = Entry(n, textvariable=caixa99)
    caixa99Box.place(x=120,y=60, width=90, height=25)

    text=Label(n,text="Buscar Nome",fg="Blue")
    text.place(x=30,y=60)

    
    n.mainloop()



def bt22():

    try:
#criar conexão ao banco de dados
        con = mysql.connector.connect(host='localhost',database='db_consulta',user='root',password='kudlakjo28')

        consulta_sql = "select * from tbl_consultas"
        cursor = con.cursor()
        cursor.execute(consulta_sql)
        linhas = cursor.fetchall() #vou pegar todas as linhas retornadas com o método fetchall e armazenar em linhas
        print("Número total de registros retornados: ",cursor.rowcount)

        print("\nMostrar os produtos cadastrados\n")

        for linha in linhas:
            print("Nome: ",linha[0])
            print("Idade: ",linha[1])
            print("CPF ",linha[2])
            print("Contato: ",linha[3])
            print("Data Marcada: ",linha[4])
            print("Horario: ",linha[5])
            print("Data do Registro: ",linha[6],"\n")

    except mysql.connector.Error as erro:
        print("Erro ao acessar tabela MySQL: {}".format(erro))

    finally:
        if con.is_connected():
            cursor.close()
            con.close()
            print("Conexão ao MySQL foi encerrada")
    
        if con.is_connected():
            db_info = con.get_server_info()
            print("Conectado ao servidor MySQL versão: ",db_info)

    
    
        

j= Tk()

j.geometry('500x350')
j.resizable(0,0)
j.title('Clinica do Paraná')

text=Label(j,text="Digite seu nome",fg="blue")
text.place(x=20,y=30)

text=Label(j,text="Digite sua Idade",fg="blue")
text.place(x=20,y=80)

text=Label(j,text="Digite seu CPF", fg="blue")
text.place(x=250,y=30)

text=Label(j,text="Digite seu Telefone", fg="blue")
text.place(x=250,y=80)

text=Label(j,text="Digite Abaixo Para Quando a Data Do Procedimento", fg="blue")
text.place(x=110,y=120)

bt5=Button(j,text="Buscar no banco",command=bt5,fg="green")
bt5.config(height=2,width=22)
bt5.place(x=180,y=250)



#Caixas
caixa1 = StringVar()
caixa1Box = Entry(j, textvariable=caixa1)
caixa1Box.place(x=150,y=30, width=90, height=25)

caixa2 = StringVar()
caixa2Box = Entry(j, textvariable=caixa2)
caixa2Box.place(x=150,y=80, width=90, height=25)

caixa3 = StringVar()
caixa3Box = Entry(j, textvariable=caixa3)
caixa3Box.place(x=370,y=30, width=90, height=25)

caixa4 = StringVar()
caixa4Box = Entry(j, textvariable=caixa4)
caixa4Box.place(x=370,y=80, width=90, height=25)

caixa5 = StringVar()
caixa5Box = Entry(j, textvariable=caixa5)
caixa5Box.place(x=210,y=150, width=90, height=25)


bt1=Button(j,text="Cadastro Para Consulta",command=bt1,fg="green")
bt1.config(height=2,width=22)
bt1.place(x=47,y=200)

bt2=Button(j,text="Cadastro Para Exames",command=bt2,fg="green")
bt2.config(height=2,width=22)
bt2.place(x=300,y=200)

bt3=Button(j,text="Cadastro Para Cirurgia",command=bt3,fg="green")
bt3.config(height=2,width=22)
bt3.place(x=47,y=300)

bt4=Button(j,text="Cadastro Para Pós-Cirurgico",command=bt4,fg="green")
bt4.config(height=2,width=22)
bt4.place(x=300,y=300)

bt22=Button(j,text="Mostrar",command=bt22,fg="green")
bt22.config(height=1,width=10)
bt22.place(x=1,y=1)








j.mainloop()
