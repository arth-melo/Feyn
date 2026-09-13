
import customtkinter as ctk

sinonimos_list = ['escassez', 'carência', 'falta', 'penúria']
respostaIA = [
    'míngua',
    'Substantivo feminino',
    'Míngua é quando falta alguma coisa que era necessária. Não é só "não ter" — é sentir a falta, ver o tanto diminuindo até quase acabar',
    'Pense numa torneira pingando cada vez mais devagar até quase parar: enquanto ainda cai água, mas pouca, essa água está "à míngua"',
    'à míngua de provas, o processo foi arquivado',
    'a família vivia à míngua depois da crise',
    'sem a renda rural, o comércio míngua',
    sinonimos_list,
    'A palavra "míngua" vem por derivação regressiva do verbo "minguar", que tem relação etimológica com o latim vulgar "minuāre" (ligado a "minuĕre", "diminuir").'
]

informacoes =  {
    'palavra' : respostaIA[0],
    'descricao' : respostaIA[1],
    'definicao' : respostaIA[2],
    'analogia' : respostaIA[3],
    'exemplo1' : respostaIA[4],
    'exemplo2' : respostaIA[5],
    'exemplo3' : respostaIA[6],
    'sinonimos' : respostaIA[7],
}
try:
    informacoes['etimologia'] = respostaIA[8]
except IndexError:
    informacoes['etimologia'] = 'etmologia não disponível'

app =ctk.CTk()
COLORS = {
    "bg": "#000000",
    "azul": "#828bc8",
    "Branco suave": "#f2f2f5",
    "Cinza azulado": "#626369",
    "azul escuro": "#233263",

}
app.configure(fg_color=COLORS["bg"])

#FUNDO PRETO
fundo = ctk.CTkFrame(master=app, width=500, height=400, corner_radius=50, fg_color=COLORS["bg"], border_width=0)
fundo.pack(padx=0, pady=0, fill="both", expand=True)

#FUNDO PRETO 2
fundo_preto2 = ctk.CTkFrame(master=fundo, width=500, height=400, corner_radius=20, fg_color=COLORS["bg"], border_width=0.8, border_color=COLORS["Branco suave"])
fundo_preto2.pack(
    padx=5, 
    pady=5,
    fill="both",
    expand=True,
        )
#FEYN
feyn_nome = ctk.CTkLabel(master=fundo_preto2, text="feyn", font=("Arial", 14, "bold"), text_color=COLORS["Branco suave"], height=1, width=1,)
feyn_nome.grid(
    row=0,
    column=0,
    pady=5,
    padx=(0,10),
    sticky="e")

#PALAVRA
palavra = ctk.CTkLabel(master=fundo_preto2, text=informacoes['palavra'], font=("Roboto", 17), text_color=COLORS["Branco suave"])
palavra.grid(
    row=0,
    column=0,
    pady=5,
    padx=20,
    sticky="w"

)


#DESCRICAO
descricao = ctk.CTkLabel(master=fundo_preto2, text=informacoes['descricao'], font=("Roboto", 10), text_color=COLORS["Cinza azulado"], width=1, height=1)

#DEFINICAO
definicao = ctk.CTkLabel(master=fundo_preto2, text=informacoes['definicao'], font=("Roboto", 12), fg_color=COLORS["azul escuro"], text_color=COLORS["Branco suave"], wraplength=400, justify="left", corner_radius=70, width=0, height=50)
definicao.grid(
    row=1,
    column=0,
    pady=(40,10),
    padx=20)

ECPUC = ctk.CTkLabel(master=fundo_preto2, text="EXPLIQUE COMO PARA UMA CRIANÇA", font=("Roboto", 10), text_color=COLORS["Cinza azulado"], height=1, width=1,)

#ANALOGIA
largura_container = fundo_preto2.cget("width")
pad_horizontal = 20 * 2
fonte_analogia = ctk.CTkFont(family="Roboto", size=12, slant="roman")
analogia_texto = ctk.CTkLabel(master=fundo_preto2, text="ANALOGIA", font=("Roboto", 10), text_color=COLORS["Cinza azulado"], height=1, width=1,)
analogia = ctk.CTkLabel(master=fundo_preto2, text=informacoes['analogia'], font=fonte_analogia, justify="left", wraplength= largura_container - pad_horizontal , height= 4)
analogia.grid(row = 2,column=0,pady=(35,0), padx=20, sticky="w")

#ONDE VOCÊ VÊ ESSA PALAVRA
onde_voce_ve = ctk.CTkLabel(master=fundo_preto2, text="ONDE VOCÊ VÊ ESSA PALAVRA", font=("Roboto", 10), text_color=COLORS["Cinza azulado"], height=1, width=1,)

#EXEMPLO1
exemplo1 = ctk.CTkLabel(master=fundo_preto2, text=informacoes['exemplo1'], font=("Roboto", 12), wraplength=400, justify="left", text_color=COLORS["azul"], height = 0)
exemplo1.grid(
    pady=(30,0),
    padx=20,
    row=3,
    column=0,
    sticky="w"
    )
#EXEMPLO2
exemplo2 = ctk.CTkLabel(master=fundo_preto2, text=informacoes['exemplo2'], font=("Roboto", 12), text_color=COLORS["azul"], wraplength=400, justify="left")
exemplo2.grid(
    pady=(8,0),
    padx=20,
    row=4,
    column=0,
    sticky="w"
    )

#EXEMPLO3
exemplo3 = ctk.CTkLabel(master=fundo_preto2, text=informacoes['exemplo3'], font=("Roboto", 12), text_color=COLORS["azul"], wraplength=400, justify="left")
exemplo3.grid(
    pady=0,
    padx=20,
    row=5,
    column=0,
    sticky="w"
    )

#ETIMOLOGIA
etm_text = ctk.CTkLabel(master=fundo_preto2, text='ETIMOLOGIA (COMPLEMENTAR)', font=("Roboto", 10), text_color = COLORS['Cinza azulado'])
wrap = largura_container -pad_horizontal
etimologia_font = ctk.CTkFont("Roboto", 11)
etimologia = ctk.CTkLabel(master=fundo_preto2, text=informacoes['etimologia'], font=etimologia_font, fg_color=COLORS['azul escuro'], width= etimologia_font.measure(informacoes['etimologia']) + 5 if etimologia_font.measure(informacoes['etimologia'])  < largura_container else  largura_container - pad_horizontal, wraplength= wrap, justify = 'left', height= etimologia_font.measure(informacoes['etimologia']) / wrap * 20)
etimologia.grid(
    pady=(20),
    padx=20,
    row = 6,
    column = 0,
    sticky = 'w')

#SINONIMOS
sin_text = ctk.CTkLabel(master=fundo_preto2, text='SINÔNIMOS', font=("Roboto", 10), text_color=COLORS['Cinza azulado'], height = 0)

#update das informações
app.update_idletasks()

y_sinonimoslabel = etimologia.winfo_y() + etimologia.winfo_height() + 10
#TODOS OS PLACES ---------------------------------------------------
# place EXPLIQUE COMO PARA UMA CRIANÇA
ECPUC.place(
    x=18,
    y=definicao.winfo_y() - 15
)

#place ANALOGIA
analogia_texto.place(
    x=18,
    y=analogia.winfo_y() - 15
)


#place ONDE VOCÊ VÊ
onde_voce_ve.place(
    x=18,
    y=exemplo1.winfo_y()- 15
)

#place DESCRIÇÃO
descricao.place(
x=20,
y=palavra.winfo_y() + palavra.winfo_height() - 3,
      )


#place ETIMOLOGIA
etm_text.place(
    x=18,
    y=etimologia.winfo_y() - 23
)


#place SINONIMOS
sin_text.place(
    x=18,
    y= y_sinonimoslabel
)

x_atual = 20
fonte_sinonimo = ctk.CTkFont(family="Roboto", size=10) 
# usando ctk font para que a fonte exibida seja a mesma medida no cálculo
for i, sinonimo in enumerate(sinonimos_list):
    tamanho = fonte_sinonimo.measure(sinonimo) + 20
    sinonimos_text = ctk.CTkLabel(
        master=fundo_preto2,
        text=sinonimo,
        font=("Roboto", 10),
        text_color=COLORS['azul'],
        fg_color=COLORS["azul escuro"],
        corner_radius=60,
        height = 20,
        width = tamanho
    )
    sinonimos_text.place(
        y = y_sinonimoslabel + 20,
        x=x_atual
    )
    x_atual = x_atual + tamanho + 10

largura_necessaria = fundo_preto2.winfo_reqwidth()
altura_necessaria = fundo_preto2.winfo_reqheight()
app.geometry(f"{largura_necessaria + 10}x{altura_necessaria + 50}")

app.mainloop()

