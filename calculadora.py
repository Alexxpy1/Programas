from tkinter import *
from tkinter import ttk
import math

def temaOscuro(*args):
    estilos.configure('mainframe.TFrame', background="#010924")

    estilosLabel1.configure('Label1.TLabel', background='#010924', foreground='white')
    estilosLabel2.configure('Label2.TLabel', background='#010924', foreground='white')

    estilosBotonesNumeros.configure('BotonesNumeros.TButton', background='#00044A', foreground='white')
    estilosBotonesNumeros.map("BotonesNumeros.TButton", background=[('active', '#020A90')])

    estilosBotonesBorrar.configure('BotonesBorrar.TButton', background='#010924', foreground='white')
    estilosBotonesBorrar.map('BotonesBorrar.TButton', background=[('active', '#000AB1')])
    
    estilosBotonesRestantes.configure('BotonesRestantes.TButton', background='#010924', foreground='white')
    estilosBotonesRestantes.map('BotonesRestantes.TButton', background=[('active', '#000AB1')])

def temaClaro(*args):
    estilos.configure('mainframe.TFrame', background='#DBDBDB', foreground='black')

    estilosLabel1.configure('Label1.TLabel', background='#DBDBDB', foreground='black')
    estilosLabel2.configure('Label2.TLabel', background='#DBDBDB', foreground='black')

    estilosBotonesNumeros.configure('BotonesNumeros.TButton', background='#FFFFFF', foreground='black')
    estilosBotonesNumeros.map('BotonesNumeros.TButton', background=[('active', '#B9B9B9')])

    estilosBotonesBorrar.configure('BotonesBorrar.TButton', background='#CECECE', foreground='black')
    estilosBotonesBorrar.map('BotonesBorrar.TButton', background=[('active', '#858585')])

    estilosBotonesRestantes.configure('BotonesRestantes.TButton', background='#CECECE', foreground='black')
    estilosBotonesRestantes.map('BotonesRestantes.TButton', background=[('active', '#858585')])

root = Tk()
root.title("Calculadora2")
root.geometry("+500+80")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

estilos = ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background='#DBDBDB')


mainframe = ttk.Frame(root, style="mainframe.TFrame")
mainframe.grid(column=0, row=0, sticky=(W, N, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.columnconfigure(1, weight=1)
mainframe.columnconfigure(2, weight=1)
mainframe.columnconfigure(3, weight=1)

mainframe.rowconfigure(0, weight=1)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)

# Estilos labels
estilosLabel1 = ttk.Style()
estilosLabel1.configure('Label1.TLabel', font="arial 15", anchor="E")

estilosLabel2 = ttk.Style()
estilosLabel2.configure('Label2.TLabel', font="arial 40", anchor="e")

entrada1 = StringVar()
label_entrada1 = ttk.Label(mainframe, textvariable=entrada1, style="Label1.TLabel")
label_entrada1.grid(column=0, row=0, columnspan=4, sticky=(W, N, E, S))

entrada2 = StringVar()
label_entrada2 = ttk.Label(mainframe, textvariable=entrada2, style='Label2.TLabel')
label_entrada2.grid(column=0, row=1, columnspan=4, sticky=(W, N, E, S))

#estilos para los botones
estilosBotonesNumeros = ttk.Style()
estilosBotonesNumeros.configure('BotonesNumeros.TButton', font="arial 22", width=5, background="#FFFFFF", relief="flat")
estilosBotonesNumeros.map('BotonesNumeros.TButton', background=[('active', '#B9B9B9')])

estilosBotonesBorrar = ttk.Style()
estilosBotonesBorrar.configure('BotonesBorrar.TButton', font="arial 22", width=5, relief="flat", background="#CECECE")
estilosBotonesBorrar.map('BotonesBorrar.TButton', foreground=[('active', '#FF0000')], background=[('active','#858585')])

estilosBotonesRestantes = ttk.Style()
estilosBotonesRestantes.configure('BotonesRestantes.TButton', font="arial 22", width=5, relief="flat", background="#CECECE")
estilosBotonesRestantes.map('BotoneRestantes.TButton', background=[('active', '#858585')])


button0 = ttk.Button(mainframe, text="0", style= 'BotonesNumeros.TButton')
button1 = ttk.Button(mainframe, text="1", style= 'BotonesNumeros.TButton')
button2 = ttk.Button(mainframe, text="2", style= 'BotonesNumeros.TButton')
button3 = ttk.Button(mainframe, text="3", style= 'BotonesNumeros.TButton')
button4 = ttk.Button(mainframe, text="4", style= 'BotonesNumeros.TButton')
button5 = ttk.Button(mainframe, text="5", style= 'BotonesNumeros.TButton')
button6 = ttk.Button(mainframe, text="6", style= 'BotonesNumeros.TButton')
button7 = ttk.Button(mainframe, text="7", style= 'BotonesNumeros.TButton')
button8 = ttk.Button(mainframe, text="8", style= 'BotonesNumeros.TButton')
button9 = ttk.Button(mainframe, text="9", style= 'BotonesNumeros.TButton')

buttonBorrar = ttk.Button(mainframe, text=chr(9003), style='BotonesBorrar.TButton')
buttonBorrarTodo = ttk.Button(mainframe, text="C", style='BotonesBorrar.TButton')
buttonParentesis1 = ttk.Button(mainframe, text="(", style='BotonesRestantes.TButton')
buttonParentesis2 = ttk.Button(mainframe, text=")", style='BotonesRestantes.TButton')
buttonPunto = ttk.Button(mainframe, text=".", style='BotonesRestantes.TButton')

buttonDivision = ttk.Button(mainframe, text=chr(247), style='BotonesRestantes.TButton')
buttonMultiplicacion = ttk.Button(mainframe, text="x", style='BotonesRestantes.TButton')
buttonResta = ttk.Button(mainframe, text="-", style='BotonesRestantes.TButton')
buttonSuma = ttk.Button(mainframe, text="+", style='BotonesRestantes.TButton')

buttonIgual = ttk.Button(mainframe, text="=", style='BotonesRestantes.TButton')
buttonRaizCuadrada = ttk.Button(mainframe, text="√", style='BotonesRestantes.TButton')

# Colocar botones en pantalla

buttonParentesis1.grid(column=0, row=2, sticky=(W, N, E, S))
buttonParentesis2.grid(column=1, row=2, sticky=(W, N, E, S))
buttonBorrarTodo.grid(column=2, row=2, sticky=(W, N, E, S))
buttonBorrar.grid(column=3, row=2, sticky=(W, N, E, S))

button7.grid(column=0, row=3, sticky=(W, N, E, S))
button8.grid(column=1, row=3, sticky=(W, N, E, S))
button9.grid(column=2, row=3, sticky=(W, N, E, S))
buttonDivision.grid(column=3, row=3, sticky=(W, N, E, S))

button4.grid(column=0, row=4, sticky=(W, N, E, S))
button5.grid(column=1, row=4, sticky=(W, N, E, S))
button6.grid(column=2, row=4, sticky=(W, N, E, S))
buttonMultiplicacion.grid(column=3, row=4, sticky=(W, N, E, S))

button1.grid(column=0,row=5, sticky=(W, N, E, S))
button2.grid(column=1,row=5, sticky=(W, N, E, S))
button3.grid(column=2,row=5, sticky=(W, N, E, S))
buttonSuma.grid(column=3,row=5, sticky=(W, N, E, S))

button0.grid(column=0, row=6, columnspan=2, sticky=(W, N, E, S))
buttonPunto.grid(column=2, row=6, sticky=(W, N, E, S))
buttonResta.grid(column=3, row=6, sticky=(W, N, E, S))

buttonIgual.grid(column=0, row=7, columnspan=3, sticky=(W, N, E, S))
buttonRaizCuadrada.grid(column=3, row=7, sticky=(W, N, E, S))


for child in mainframe.winfo_children():
    child.grid_configure(ipady=10, padx=1, pady=1)

root.bind('<KeyPress-o>', temaOscuro)
root.bind('<KeyPress-c>', temaClaro)

root.mainloop()