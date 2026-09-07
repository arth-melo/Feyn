
import customtkinter as ctk
sinonimos_list = ['sinonimo1', 'sinonimo2', 'sinonimo3']
respostaIA = ['míngua', 'Substantivo feminino', 'Míngua é quando falta alguma coisa que era necessária. Não é só "não ter" — é sentir a falta, ver o tanto diminuindo até quase acabar', 'Pense numa torneira pingando cada vez mais devagar até quase parar: enquanto ainda cai água, mas pouca, essa água está "à míngua"', "à mingua de", "viver à mingua", "minguar (verbo)", sinonimos_list, 'Derivação regressiva de "minguar", que tem relação etimológica com o latim vulgar minuāre (ligado a minuĕre, "diminuir") — segundo os dicionários consultados.']
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
app.geometry("500x450")
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
descricao.place(
x=18,
y=palavra.winfo_y() + palavra.winfo_height() + 28,
      )
 


#DEFINICAO
definicao = ctk.CTkLabel(master=fundo_preto2, text=informacoes['definicao'], font=("Roboto", 12), fg_color=COLORS["azul escuro"], text_color=COLORS["Branco suave"], wraplength=400, justify="left", corner_radius=70, width=0, height=50)
definicao.grid(
    row=1,
    column=0,
    pady=(40,10),
    padx=20)

ECPUC = ctk.CTkLabel(master=fundo_preto2, text="EXPLIQUE COMO PARA UMA CRIANÇA", font=("Roboto", 10), text_color=COLORS["Cinza azulado"], height=1, width=1,)
ECPUC.place(
    x=18,
    y=definicao.winfo_y() + definicao.winfo_height() + 60
)

#ANALOGIA
analogia_texto = ctk.CTkLabel(master=fundo_preto2, text="ANALOGIA", font=("Roboto", 10), text_color=COLORS["Cinza azulado"], height=1, width=1,)
analogia_texto.place(
    x=18,
    y=analogia_texto.winfo_y() + analogia_texto.winfo_height() + 155
)
analogia = ctk.CTkLabel(master=fundo_preto2, text=informacoes['analogia'], font=("Roboto", 12,'italic'), justify="left", wraplength=400)
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

onde_voce_ve.place(
    x=18,
    y=exemplo1.winfo_y() + exemplo1.winfo_height() + 213
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


etimologia = ctk.CTkLabel(master=fundo_preto2, text=informacoes.get('etimologia', 'etmologia não disponível'), font=("Roboto", 11), fg_color=COLORS['azul escuro'], width= 425, height= 60, wraplength= 400, justify = 'left')
etimologia.grid(
    pady=20,
    padx=20,
    row = 6,
    column = 0,
    sticky = 'w')

etm_text.place(
    x=18,
    y=etimologia.winfo_y() + etimologia.winfo_height() + 300
)

#SINONIMOS
sin_text = ctk.CTkLabel(master=fundo_preto2, text='SINÔNIMOS', font=("Roboto", 10), text_color=COLORS['Cinza azulado'], height = 0)
sin_text.place(
    x=18,
    y=analogia.winfo_y() + analogia.winfo_height() + 395
)

for i, sinonimo in enumerate(sinonimos_list):
    sinonimos_text = ctk.CTkLabel(
        master=fundo_preto2,
        text=sinonimo,
        font=("Roboto", 10),
        text_color=COLORS['azul'],
        fg_color=COLORS["azul escuro"],
        corner_radius=60,
        height = 20,
        width = len(sinonimo) * 5
    )
    sinonimos_text.place(
        y = 410,
        x  =(i ) * 75 + 20,
        )
app.mainloop()
