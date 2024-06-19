#janela => 500 x 500
#título
#campos para selecionar as moedas de origem e de destino
#botão para converter
#lista de exebição com os nomes das moedas

#importar a biblioteca que vai fazer a janela
import customtkinter
from pegar_moedas import nomes_moedas, conversoes_disponiveis
from pegar_cotacao import pegar_cotacao_moeda

#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.geometry("5000x5000")
janela.title("Conversor de moedas do BARBOSA")
janela.iconbitmap("money.ico")

dic_conversoes_disponiveis = conversoes_disponiveis()

#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text = "Conversor de Moedas", font = ("", 30))
texto_moeda_origem = customtkinter.CTkLabel(janela, text = "Selecione a moeda de origem", font = ("", 15))
texto_moeda_de_destino = customtkinter.CTkLabel(janela, text = "Selecione a moeda de destino", font = ("", 15))

def carregar_moedas_destino(moeda_selecionada):
    lista_moedas_destino = dic_conversoes_disponiveis[moeda_selecionada]
    campo_moeda_de_destino.configure(values = lista_moedas_destino)
    campo_moeda_de_destino.set(lista_moedas_destino[0])

campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values = list(dic_conversoes_disponiveis.keys()), command = carregar_moedas_destino, font = ("", 12))
campo_moeda_de_destino = customtkinter.CTkOptionMenu(janela, values = ["Selecione uma moeda de origem"], font = ("", 12))
significado = customtkinter.CTkLabel(janela, text = "Significado:", font = ("", 15))

def converter_moeda():
    moeda_origem = campo_moeda_origem.get()
    moeda_destino = campo_moeda_de_destino.get()
    if moeda_origem and moeda_destino:
        cotacao = pegar_cotacao_moeda(moeda_origem, moeda_destino)
        texto_cotacao_moeda.configure(text = f"1 {moeda_origem} = {cotacao} {moeda_destino}")

botao_converter = customtkinter.CTkButton(janela, text = "Converter", command = converter_moeda, font = ("", 15), hover_color = "#03256C")

lista_moedas = customtkinter.CTkScrollableFrame(janela)

texto_cotacao_moeda = customtkinter.CTkLabel(janela, text = "", font = ("", 20), text_color = "#53D8FB")

moedas_disponiveis = nomes_moedas()
for codigo_moeda in moedas_disponiveis:
    nome_moeda = moedas_disponiveis[codigo_moeda]
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text = f"{codigo_moeda}: {nome_moeda}",font = ("", 14))
    texto_moeda.pack()


#colocar os elementos criados na tela
titulo.pack(padx = 10, pady = 10)
texto_moeda_origem.pack(padx = 10, pady = 10)
campo_moeda_origem.pack(padx = 10, pady = 10)   
texto_moeda_de_destino.pack(padx = 10, pady = 10)
campo_moeda_de_destino.pack(padx = 10, pady = 10)
botao_converter.pack(padx = 10, pady = 10)
texto_cotacao_moeda.pack(padx = 10, pady = 10)
significado.pack(padx = 100, pady = 5)
lista_moedas.pack(padx = 10, pady = 10)

#rodar a janela
janela.mainloop()