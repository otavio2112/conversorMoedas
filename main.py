#janela => 500 x 500
#título
#campos para selecionar as moedas de origem e de destino
#botão para converter
#lista de exebição com os nomes das moedas

#importar a biblioteca que vai fazer a janela
import customtkinter

#criar e configurar a janela
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela = customtkinter.CTk()
janela.geometry("500x500")

#criar os botões, textos e demais elementos
titulo = customtkinter.CTkLabel(janela, text = "Conversor de Moedas", font = ("", 30))
texto_moeda_origem = customtkinter.CTkLabel(janela, text = "Selecione a moeda de origem", font = ("", 15))
texto_moeda_de_destino = customtkinter.CTkLabel(janela, text = "Selecione a moeda de destino", font = ("", 15))
campo_moeda_origem = customtkinter.CTkOptionMenu(janela, values = ["USD", "EUR", "BRL", "BTC"], font = ("", 12))
campo_moeda_de_destino = customtkinter.CTkOptionMenu(janela, values = ["USD", "EUR", "BRL", "BTC"], font = ("", 12))
significado = customtkinter.CTkLabel(janela, text = "Significado:", font = ("", 15))

def converter_moeda():
    print("Converter moeda")

botao_converter = customtkinter.CTkButton(janela, text = "Converter", command = converter_moeda, font = ("", 15), hover_color = "#03256C")

lista_moedas = customtkinter.CTkScrollableFrame(janela)

moedas_disponiveis = ["USD = Dólar Americano", "EUR = Euro", "BRL = Real Brasileiro", "BTC = Bitcoin"]

for moeda in moedas_disponiveis:
    texto_moeda = customtkinter.CTkLabel(lista_moedas, text = moeda,font = ("", 14))
    texto_moeda.pack()

#moeda1 = customtkinter.CTkLabel(lista_moedas, text = "USD = Dólar Americano")
#moeda2 = customtkinter.CTkLabel(lista_moedas, text = "EUR = Euro")
#moeda3 = customtkinter.CTkLabel(lista_moedas, text = "BRL = Real Brasileiro")
#moeda4 = customtkinter.CTkLabel(lista_moedas, text = "BTC = Bitcoin")
#moeda1.pack()
#moeda2.pack()
#moeda3.pack()
#moeda4.pack()

#colocar os elementos criados na tela
titulo.pack(padx = 10, pady = 10)
texto_moeda_origem.pack(padx = 10, pady = 10)
campo_moeda_origem.pack(padx = 10, pady = 10)   
texto_moeda_de_destino.pack(padx = 10, pady = 10)
campo_moeda_de_destino.pack(padx = 10, pady = 10)
botao_converter.pack(padx = 10, pady = 10)
significado.pack(padx = 100, pady = 5)
lista_moedas.pack(padx = 10, pady = 10)



#rodar a janela
janela.mainloop()



