from tkinter import *
from back import calculadora
from back import fatorial

#///////////////////////////////////// Config base app /////////////////////////////////////
#Configuracoes base da tela da aplicaçao
app = Tk()
app.title('Calculadora')#Titulo do aplicativo
app.geometry('320x500')#Largura x Altura
app.minsize(320,500)#Largura x Altura minima
app.maxsize(320,500)#Largura x Altura maxima
icon = PhotoImage(file='Calculadora\imagem\icones\icon_app.png')#Icone do programa
app.iconphoto(True,icon)#Permite a troca do icone padrao pelo de sua escolha

def fechar_programa():
    app.quit()

#///////////////////////////////////// CORES PRE-DEFINIDAS /////////////////////////////////////
#Cores em hexadecimal
cor1 = '#ffffff' #Branco
cor2 = '#000000' #Preto
cor3 = '#f49619' #Laranja
cor4 = '#333333' #cinza escuro
cor5 = '#a4a4a4' #Cinza claro

#///////////////////////////////////// Criacao do display e corpo /////////////////////////////////////
#Display calculadora
display = Frame(app, width=320, height=80, bg=cor2)
display.grid(row=0, column=0)

#Corpo calculadora
body = Frame(app, width=320, height=420, bg=cor2)
body.grid(row=1, column=0)

#Display calculadora
digitos = Entry(display,
                width=24, 
                relief=FLAT, 
                fg=cor1,
                bg=cor2,
                font=('futura', 18, 'bold'), 
                justify=RIGHT)
digitos.place(x=0,y=40)
#/////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////// BARRA DE MENU E OPCOES /////////////////////////////////////
img_open_branco = PhotoImage(file='Calculadora\imagem\icones\open_white.png')
img_open_preto = PhotoImage(file='Calculadora\imagem\icones\open_black.png')
img_close = PhotoImage(file='Calculadora\imagem\icones\close_white.png')

#///////////////////////////////////// imagens menu /////////////////////////////////////
img_modo_claro = PhotoImage(file='Calculadora\imagem\icones\modo_claro.png')
img_modo_escuro = PhotoImage(file='Calculadora\imagem\icones\modo_escuro.png')
img_sobre = PhotoImage(file='Calculadora\imagem\icones\sobre.png')
img_fechar = PhotoImage(file='Calculadora\imagem\icones\close_app.png')

def Menu():
    menu = Frame(app, width=230, height=500)
    menu.configure(bg=cor4)
    menu.place(x=0, y=0)

    def close():
        menu.destroy()
    #botao fechar
    botao_menu_fechar = Button(menu, image=img_close, border=0, bg=cor4, activebackground=cor4, command=close)
    botao_menu_fechar.place(x=15, y=15)

    Button(menu, image=img_modo_claro, border=0, bg=cor4, activebackground=cor4, command=lambda:tema('Light'), justify=CENTER).place(x=60, y=155)
    Button(menu, image=img_modo_escuro, border=0, bg=cor4, activebackground=cor4, command=lambda:tema('Dark'), justify=CENTER).place(x=50, y=205)
    Button(menu, image=img_sobre, border=0, bg=cor4, activebackground=cor4, command=janela_sobre, justify=CENTER).place(x=80, y=255)
    Button(menu, image=img_fechar, border=0, bg=cor4, activebackground=cor4, command=fechar_programa, justify=CENTER).place(x=50, y=305)

botao_menu_abrir = Button(app,command=Menu, image=img_open_branco, border=0, bg=cor2, activebackground=cor1)
botao_menu_abrir.place(x=15, y=15)

#/////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////// Janela sobre o app /////////////////////////////////////
def janela_sobre():
    # Cria uma nova janela
    sobre = Toplevel()
    sobre.geometry('394x315')
    

    # Função para fechar a janela
    def fechar_janela():
        sobre.destroy()
    
    # Carrega a imagem
    img_mesa3 = PhotoImage(file='Calculadora\imagem\icones\img_box.png')
    
    # Cria um label com a imagem
    imagem = Label(sobre, image=img_mesa3,border=0,justify=CENTER)
    imagem.pack(anchor='center',pady=8)#Posiciona o imagem na tela
        
    # Cria um botão para fechar a janela
    botao_fechar = Button(sobre, text='Fechar', command=fechar_janela,relief=FLAT, font=('Arial', 13, 'bold'),activebackground=cor1)
    botao_fechar.pack(anchor='center',padx=20,pady=10)#Posiciona o botao na tela
    
    # Exibe a janela
    sobre.mainloop()
#/////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////// TEMA CLARO /////////////////////////////////////
#Imagens botoes tema tema claro
#primeira fileira
wht_mod = PhotoImage(file='Calculadora\imagem\claro\Ativo 1.png')
wht_exp = PhotoImage(file='Calculadora\imagem\claro\Ativo 2.png')
wht_fat = PhotoImage(file='Calculadora\imagem\claro\Ativo 3.png')
wht_del = PhotoImage(file='Calculadora\imagem\claro\Ativo 4.png')

#Imagens botoes tema tema claro
#segunda fileira
wht_ac = PhotoImage(file='Calculadora\imagem\claro\Ativo 5.png')
wht_porcent = PhotoImage(file='Calculadora\imagem\claro\Ativo 6.png')
wht_div = PhotoImage(file='Calculadora\imagem\claro\Ativo 7.png')
wht_mult = PhotoImage(file='Calculadora\imagem\claro\Ativo 8.png')

#Imagens botoes tema tema claro
#terceira fileira
wht_7 = PhotoImage(file='Calculadora\imagem\claro\Ativo 9.png')
wht_8 = PhotoImage(file='Calculadora\imagem\claro\Ativo 10.png')
wht_9 = PhotoImage(file='Calculadora\imagem\claro\Ativo 11.png')
wht_menos = PhotoImage(file='Calculadora\imagem\claro\Ativo 12.png')

#Imagens botoes tema tema claro
#quarta fileira
wht_4 = PhotoImage(file='Calculadora\imagem\claro\Ativo 13.png')
wht_5 = PhotoImage(file='Calculadora\imagem\claro\Ativo 14.png')
wht_6 = PhotoImage(file='Calculadora\imagem\claro\Ativo 15.png')
wht_mais = PhotoImage(file='Calculadora\imagem\claro\Ativo 16.png')

#Imagens botoes tema tema claro
#quinta fileira
wht_1 = PhotoImage(file='Calculadora\imagem\claro\Ativo 17.png')
wht_2 = PhotoImage(file='Calculadora\imagem\claro\Ativo 18.png')
wht_3 = PhotoImage(file='Calculadora\imagem\claro\Ativo 19.png')

#Imagens botoes tema tema claro
#sexta fileira
wht_0 = PhotoImage(file='Calculadora\imagem\claro\Ativo 20.png')
wht_vig = PhotoImage(file='Calculadora\imagem\claro\Ativo 21.png')
wht_res = PhotoImage(file='Calculadora\imagem\claro\Ativo 22.png')
#/////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////// TEMA ESCURO /////////////////////////////////////
#Imagens botoes tema escuro
#primeira fileira
img_mod = PhotoImage(file='Calculadora\imagem\Ativo 2.png')
img_exp = PhotoImage(file='Calculadora\imagem\Ativo 3.png')
img_fat = PhotoImage(file='Calculadora\imagem\Ativo 4.png')
img_del = PhotoImage(file='Calculadora\imagem\Ativo 5.png')

#Imagens botoes
#segunda fileira
img_ac = PhotoImage(file='Calculadora\imagem\Ativo 6.png')
img_porcent = PhotoImage(file='Calculadora\imagem\Ativo 7.png')
img_div = PhotoImage(file='Calculadora\imagem\Ativo 8.png')
img_mult = PhotoImage(file='Calculadora\imagem\Ativo 9.png')

#Imagens botoes
#terceira fileira
img_7 = PhotoImage(file='Calculadora\imagem\Ativo 10.png')
img_8 = PhotoImage(file='Calculadora\imagem\Ativo 11.png')
img_9 = PhotoImage(file='Calculadora\imagem\Ativo 12.png')
img_menos = PhotoImage(file='Calculadora\imagem\Ativo 13.png')

#Imagens botoes
#quarta fileira
img_4 = PhotoImage(file='Calculadora\imagem\Ativo 14.png')
img_5 = PhotoImage(file='Calculadora\imagem\Ativo 15.png')
img_6 = PhotoImage(file='Calculadora\imagem\Ativo 16.png')
img_mais = PhotoImage(file='Calculadora\imagem\Ativo 17.png')

#Imagens botoes
#quinta fileira
img_1 = PhotoImage(file='Calculadora\imagem\Ativo 18.png')
img_2 = PhotoImage(file='Calculadora\imagem\Ativo 19.png')
img_3 = PhotoImage(file='Calculadora\imagem\Ativo 20.png')

#Imagens botoes
#sexta fileira
img_0 = PhotoImage(file='Calculadora\imagem\Ativo 21.png')
img_vig = PhotoImage(file='Calculadora\imagem\Ativo 22.png')
img_res = PhotoImage(file='Calculadora\imagem\Ativo 23.png')
#/////////////////////////////////////////////////////////////////////////////////////////////////

#Funcoes para os botoes
def botao_click(num):
    digitos.insert(END, num)

def botao_del():
    # Obtém o texto atual do display
    display_text = digitos.get()

    # Remove o último caractere do texto
    novo_texto = display_text[:-1]

    # Atualiza o texto no display
    digitos.delete(0, END)
    digitos.insert(0, novo_texto)

def botao_apagar():
    digitos.delete(0,END)


def calcular():
    expressao = digitos.get()
    if '!' in (expressao):
        resultado = fatorial(expressao)
    else:
        resultado = calculadora(expressao)
    digitos.delete(0, END)
    digitos.insert(0, resultado)

#/////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////// Criando os botoes da calculadora /////////////////////////////////////                              
#Botoes calculadora
#Primeira Filieira
mod = Button(body, 
             image=img_mod,
             bg=cor2,
             command=lambda:botao_click('M'),
             activebackground=cor2,
             relief=FLAT,
             border=0,
)
mod.place(x=16, y=0)

exp = Button(body, 
             image=img_exp,
             bg=cor2,
             command=lambda:botao_click('^'),
             activebackground=cor2,
             relief=FLAT,
             border=0,
)
exp.place(x=92, y=0)

fat = Button(body, 
             image=img_fat,
             bg=cor2,
             command=lambda:botao_click('!'),
             activebackground=cor2,
             relief=FLAT,
             border=0,
)
fat.place(x=168, y=0)

delet = Button(body, 
             image=img_del,
             bg=cor2,
             command=botao_del,
             activebackground=cor2,
             relief=FLAT,
             border=0,
)
delet.place(x=244, y=0)

#Botoes calculadora
#Segunda Fileira
apagar = Button(body, 
             image=img_ac,
             bg=cor2,
             command=botao_apagar,
             activebackground=cor2,
             relief=FLAT,
             border=0,
)
apagar.place(x=16, y=68)

porcent = Button(body, 
             image=img_porcent,
             bg=cor2,
             command=lambda:botao_click('%'),
             activebackground=cor2,
             relief=FLAT,
             border=0,
)
porcent.place(x=92, y=68)

division = Button(body, 
                image=img_div,
                bg=cor2,
                command=lambda:botao_click('/'),
                activebackground=cor2,
                relief=FLAT,
                border=0,
)
division.place(x=168, y=68)

mult = Button(body,
             image=img_mult,
             bg=cor2,
             command=lambda:botao_click('x'),
             activebackground=cor2,
             relief=FLAT,
             border=0,
)
mult.place(x=244, y=68)

#Botoes calculadora
#Terceira Fileira
sete = Button(body,
            image=img_7,
            bg=cor2,
            command=lambda:botao_click(7),
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
sete.place(x=16, y=137)

oito = Button(body,
            image=img_8,
            bg=cor2,
            command=lambda:botao_click(8),
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
oito.place(x=92, y=137)

nove = Button(body, 
            image=img_9,
            bg=cor2,
            command=lambda:botao_click(9),
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
nove.place(x=168, y=137)

menos = Button(body, 
            image=img_menos,
            bg=cor2,
            command=lambda:botao_click('-'),
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
menos.place(x=244, y=137)

#Botoes calculadora
#Quarta Fileira
quatro = Button(body, 
            image=img_4,
            bg=cor2,
            command=lambda:botao_click(4),
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
quatro.place(x=16, y=206)

cinco = Button(body, 
            image=img_5,
            bg=cor2,
            command=lambda:botao_click(5),
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
cinco.place(x=92, y=206)

seis = Button(body, 
            image=img_6,
            bg=cor2,
            command=lambda:botao_click(6),
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
seis.place(x=168, y=206)

mais = Button(body, 
            image=img_mais,
            bg=cor2,
            command=lambda:botao_click('+'),
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
mais.place(x=244, y=206)

#Botoes calculadora
#Quinta Fileira
um = Button(body, 
            image=img_1,
            bg=cor2,
            command=lambda:botao_click(1),
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
um.place(x=16, y=275)

dois = Button(body, 
            image=img_2,
            bg=cor2,
            command=lambda:botao_click(2),
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
dois.place(x=92, y=275)

tres = Button(body, 
            image=img_3,
            bg=cor2,
            command=lambda:botao_click(3),
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
tres.place(x=168,y=275)

#Botoes calculadora
#Sexta Fileira
zero = Button(body, 
            image=img_0,
            bg=cor2,
            command=lambda:botao_click(0),
            activebackground=cor2,
            relief=FLAT,
            border=0,

)
zero.place(x=16, y=344)

vig = Button(body, 
            image=img_vig,
            bg=cor2,
            command=lambda: botao_click('.'),
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
vig.place(x=168, y=344)

res = Button(body, 
            image=img_res,
            bg=cor2,
            command=calcular,
            activebackground=cor2,
            relief=FLAT,
            border=0,
)
res.place(x=244, y=275)
#/////////////////////////////////////////////////////////////////////////////////////////////////

#///////////////////////////////////// Parametros para a troca de tema a/////////////////////////////////////  
def tema(modo):
        if modo == 'Light':#parametros para modo claro
            botao_menu_abrir.config(bg=cor1, image=img_open_preto)
            digitos.config(bg=cor1, foreground=cor2)#Trocando os digitos para claro
            body.config(bg=cor1)#Trocando o corpo para claro
            display.config(bg=cor1)#Trocando a cor do display para claro
            mod.config(bg=cor1, image=wht_mod, activebackground=cor1)#Troca da cor de fundo e da imagem
            exp.config(bg=cor1, image=wht_exp, activebackground=cor1)#Troca da cor de fundo e da imagem
            fat.config(bg=cor1, image=wht_fat, activebackground=cor1)#Troca da cor de fundo e da imagem
            delet.config(bg=cor1, image=wht_del, activebackground=cor1)#Troca da cor de fundo e da imagem
            apagar.config(bg=cor1, image=wht_ac, activebackground=cor1)#Troca da cor de fundo e da imagem
            porcent.config(bg=cor1, image=wht_porcent, activebackground=cor1)#Troca da cor de fundo e da imagem
            division.config(bg=cor1, image=wht_div, activebackground=cor1)#Troca da cor de fundo e da imagem
            mult.config(bg=cor1, image=wht_mult, activebackground=cor1)#Troca da cor de fundo e da imagem
            sete.config(bg=cor1, image=wht_7, activebackground=cor1)#Troca da cor de fundo e da imagem
            oito.config(bg=cor1, image=wht_8, activebackground=cor1)#Troca da cor de fundo e da imagem
            nove.config(bg=cor1, image=wht_9, activebackground=cor1)#Troca da cor de fundo e da imagem
            menos.config(bg=cor1, image=wht_menos, activebackground=cor1)#Troca da cor de fundo e da imagem
            quatro.config(bg=cor1, image=wht_4, activebackground=cor1)#Troca da cor de fundo e da imagem
            cinco.config(bg=cor1, image=wht_5, activebackground=cor1)#Troca da cor de fundo e da imagem
            seis.config(bg=cor1, image=wht_6, activebackground=cor1)#Troca da cor de fundo e da imagem
            mais.config(bg=cor1, image=wht_mais, activebackground=cor1)#Troca da cor de fundo e da imagem
            um.config(bg=cor1, image=wht_1, activebackground=cor1)#Troca da cor de fundo e da imagem
            dois.config(bg=cor1, image=wht_2, activebackground=cor1)#Troca da cor de fundo e da imagem
            tres.config(bg=cor1, image=wht_3, activebackground=cor1)#Troca da cor de fundo e da imagem
            zero.config(bg=cor1, image=wht_0, activebackground=cor1)#Troca da cor de fundo e da imagem
            vig.config(bg=cor1, image=wht_vig, activebackground=cor1)#Troca da cor de fundo e da imagem
            res.config(bg=cor1, image=wht_res, activebackground=cor1)#Troca da cor de fundo e da imagem

        elif modo == 'Dark':#parametros para modo Escuro
            botao_menu_abrir.config(bg=cor2, image=img_open_branco)
            digitos.config(bg=cor2, foreground=cor1)#Trocando os digitos para escuro
            body.config(bg=cor2)#Trocando o corpo para escuro
            display.config(bg=cor2)#Trocando o display para escuro
            mod.config(bg=cor2, image=img_mod, activebackground=cor2)#Troca da cor de fundo e da imagem
            exp.config(bg=cor2, image=img_exp, activebackground=cor2)#Troca da cor de fundo e da imagem
            fat.config(bg=cor2, image=img_fat, activebackground=cor2)#Troca da cor de fundo e da imagem
            delet.config(bg=cor2, image=img_del, activebackground=cor2)#Troca da cor de fundo e da imagem
            apagar.config(bg=cor2, image=img_ac, activebackground=cor2)#Troca da cor de fundo e da imagem
            porcent.config(bg=cor2, image=img_porcent, activebackground=cor2)#Troca da cor de fundo e da imagem
            division.config(bg=cor2, image=img_div, activebackground=cor2)#Troca da cor de fundo e da imagem
            mult.config(bg=cor2, image=img_mult, activebackground=cor2)#Troca da cor de fundo e da imagem
            sete.config(bg=cor2, image=img_7, activebackground=cor2)#Troca da cor de fundo e da imagem
            oito.config(bg=cor2, image=img_8, activebackground=cor2)#Troca da cor de fundo e da imagem
            nove.config(bg=cor2, image=img_9, activebackground=cor2)#Troca da cor de fundo e da imagem
            menos.config(bg=cor2, image=img_menos, activebackground=cor2)#Troca da cor de fundo e da imagem
            quatro.config(bg=cor2, image=img_4, activebackground=cor2)#Troca da cor de fundo e da imagem
            cinco.config(bg=cor2, image=img_5, activebackground=cor2)#Troca da cor de fundo e da imagem
            seis.config(bg=cor2, image=img_6, activebackground=cor2)#Troca da cor de fundo e da imagem
            mais.config(bg=cor2, image=img_mais, activebackground=cor2)#Troca da cor de fundo e da imagem
            um.config(bg=cor2, image=img_1, activebackground=cor2)#Troca da cor de fundo e da imagem
            dois.config(bg=cor2, image=img_2, activebackground=cor2)#Troca da cor de fundo e da imagem
            tres.config(bg=cor2, image=img_3, activebackground=cor2)#Troca da cor de fundo e da imagem
            zero.config(bg=cor2, image=img_0, activebackground=cor2)#Troca da cor de fundo e da imagem
            vig.config(bg=cor2, image=img_vig, activebackground=cor2)#Troca da cor de fundo e da imagem
            res.config(bg=cor2, image=img_res, activebackground=cor2)#Troca da cor de fundo e da imagem
#/////////////////////////////////////////////////////////////////////////////////////////////////
app.mainloop()