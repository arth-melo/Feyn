import tkinter as tk

import customtkinter as ctk
import keyboard as ky
from PIL import Image, ImageDraw, ImageTk

from consultaApi import consulta
from script import copiar

# ---------- paleta baseada no design do card de vocabulário ----------
COLORS = {
    "bg": "#0b0d14",
    "card_gradient_topo": "#000000",
    "card_gradient_base": "#0d0d19",
    "bubble_blue": "#3d55e8",
    "text_white": "#f2f2f5",
    "text_gray": "#8b8fa3",
}

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Captura de texto")
app.geometry("500x360")
app.minsize(400, 300)
app.configure(fg_color=COLORS["bg"])
app.overrideredirect(True)  # remove a moldura nativa (barra de título do Windows)

# torna a cor de fundo da janela transparente (recurso do Windows), então só o
# card arredondado fica visível — some com o retângulo escuro ao redor dele
app.attributes("-transparentcolor", COLORS["bg"])

app.update_idletasks()
CARD_PAD = 20
CARD_W = app.winfo_width() - CARD_PAD * 2
CARD_H = app.winfo_height() - CARD_PAD * 2
CORNER_RADIUS = 24


def _hex_para_rgb(cor_hex):
	cor_hex = cor_hex.lstrip("#")
	return tuple(int(cor_hex[i:i + 2], 16) for i in (0, 2, 4))


def cor_gradiente(t, topo=COLORS["card_gradient_topo"], base=COLORS["card_gradient_base"]):
	"""Interpola a cor do degradê numa posição vertical t (0 = topo, 1 = base)."""
	t = max(0.0, min(1.0, t))
	r0, g0, b0 = _hex_para_rgb(topo)
	r1, g1, b1 = _hex_para_rgb(base)
	r = int(r0 + (r1 - r0) * t)
	g = int(g0 + (g1 - g0) * t)
	b = int(b0 + (b1 - b0) * t)
	return f"#{r:02x}{g:02x}{b:02x}"


def gerar_card_gradiente(width, height, radius):
	"""Gera a imagem do card: fundo em degradê vertical preto -> #0D0D19, com
	cantos arredondados mascarados na cor de fundo da janela (que já é
	transparente pra o Windows, então os cantos somem visualmente)."""
	gradiente = Image.new("RGB", (width, height))
	draw = ImageDraw.Draw(gradiente)
	for y in range(height):
		cor = _hex_para_rgb(cor_gradiente(y / max(height - 1, 1)))
		draw.line([(0, y), (width, y)], fill=cor)

	mascara = Image.new("L", (width, height), 0)
	ImageDraw.Draw(mascara).rounded_rectangle(
		[0, 0, width - 1, height - 1], radius=radius, fill=255
	)

	fundo = Image.new("RGB", (width, height), COLORS["bg"])
	resultado_img = Image.composite(gradiente, fundo, mascara)
	return ImageTk.PhotoImage(resultado_img)


# ---------- canvas com o degradê no lugar do antigo CTkFrame sólido ----------
card_canvas = tk.Canvas(
	app, width=CARD_W, height=CARD_H, highlightthickness=0, bg=COLORS["bg"]
)
card_canvas.place(x=CARD_PAD, y=CARD_PAD)

card_img = gerar_card_gradiente(CARD_W, CARD_H, CORNER_RADIUS)
card_canvas.create_image(0, 0, anchor="nw", image=card_img)
card_canvas.image = card_img  # mantém referência viva (evita garbage collection)

# botão de fechar customizado, já que a barra nativa não existe mais
btn_fechar = ctk.CTkButton(
    card_canvas,
    text="✕",
    width=28,
    height=28,
    fg_color="transparent",
    hover_color=COLORS["bubble_blue"],
    text_color=COLORS["text_gray"],
    font=ctk.CTkFont(size=13),
    command=app.destroy,
)
card_canvas.create_window(CARD_W - 16, 16, anchor="ne", window=btn_fechar)

titulo = ctk.CTkLabel(
    card_canvas,
    text="Feyn",
    text_color=COLORS["text_white"],
    fg_color="transparent",
    bg_color=cor_gradiente(40 / CARD_H),
    font=ctk.CTkFont(family="Georgia", size=22, weight="bold"),
)
card_canvas.create_window(CARD_W // 2, 40, anchor="center", window=titulo)

status = ctk.CTkLabel(
    card_canvas,
    text="Pressione Alt+A para capturar o texto selecionado",
    text_color=COLORS["text_gray"],
    fg_color="transparent",
    bg_color=cor_gradiente(76 / CARD_H),
    font=ctk.CTkFont(size=12),
)
card_canvas.create_window(CARD_W // 2, 76, anchor="center", window=status)

secao_resposta = ctk.CTkLabel(
    card_canvas,
    text="RESPOSTA",
    text_color=COLORS["text_gray"],
    fg_color="transparent",
    bg_color=cor_gradiente(108 / CARD_H),
    font=ctk.CTkFont(size=11, weight="bold"),
    anchor="w",
)
card_canvas.create_window(24, 108, anchor="nw", window=secao_resposta)

# textbox no estilo "balão" azul do design, mesma função de antes
resultado = ctk.CTkTextbox(
    card_canvas,
    wrap="word",
    fg_color=COLORS["bubble_blue"],
    text_color="white",
    corner_radius=16,
    border_width=0,
    font=ctk.CTkFont(size=13),
)
card_canvas.create_window(
    24, 128, anchor="nw", window=resultado,
    width=CARD_W - 48, height=CARD_H - 128 - 24,
)


# ---------- arraste manual da janela (sem barra de título nativa) ----------
def iniciar_arrasto(event):
	app._drag_start_x = event.x
	app._drag_start_y = event.y


def mover_janela(event):
	x = app.winfo_pointerx() - app._drag_start_x
	y = app.winfo_pointery() - app._drag_start_y
	app.geometry(f"+{x}+{y}")


# vincula o arraste ao canvas do card e ao título, evitando o textbox e o
# botão fechar (pra não atrapalhar seleção de texto e o clique de fechar)
card_canvas.bind("<Button-1>", iniciar_arrasto)
card_canvas.bind("<B1-Motion>", mover_janela)
titulo.bind("<Button-1>", iniciar_arrasto)
titulo.bind("<B1-Motion>", mover_janela)


def consultar_selecao():
	texto = copiar()
	if not texto:
		app.after(0, lambda: status.configure(text="Nenhum texto foi selecionado"))
		return

	app.after(0, lambda: status.configure(text="Consultando o Gemini..."))
	try:
		resposta = consulta(texto)
		app.after(0, lambda: resultado.insert("end", resposta + "\n\n"))
		app.after(0, lambda: status.configure(text="Resposta recebida"))
	except Exception as erro:
		app.after(0, status.configure(text="O serviço de IA atingiu temporariamente o limite de uso.\nTente novamente em alguns minutos."))


ky.add_hotkey("alt+a", consultar_selecao, suppress=True)
app.mainloop()