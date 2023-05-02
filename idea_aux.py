import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import graphviz
from tkinter import messagebox
import fitz  # esta biblioteca te permitirá visualizar el pdf en tiempo real

from vertice import Verice
from TDA.listanodos import ListaVertices

#globales
lista_vertices = ListaVertices()
imgGrafo = graphviz.Graph(name='mi_grafo', strict=False)

#Para interfaz desde cualquir funcion
opciones = []
root = tk.Tk()
left_frame = tk.Frame(root, width=600, height=400)
left_frame_2nodo = tk.Frame(root, width=600, height=400)
frame_finaliza = tk.Frame(root, width=600, height=400)
caja_texto = tk.Entry(left_frame_2nodo, width=18, font=("Arial", 15))
combo = ttk.Combobox(left_frame_2nodo,width=23,height=15, justify="center")
Cnodo_inicio = ttk.Combobox(frame_finaliza,width=23,height=15, justify="center")
Cnodo_final = ttk.Combobox(frame_finaliza,width=23,height=15, justify="center")


def segundo_nodo():
    #Limpiar Frame
    left_frame.pack_forget()
    
    name_nodo = texto_caja.get()

    #OBteniendo informacion 
    if len(name_nodo) == 0:
        messagebox.showwarning("Alerta", "No ingreso el nombre del Vertice")
        left_frame.pack(pady=0) #pendiente
    else: 
        objeto1 = Verice(name_nodo)
        imgGrafo.node(str(objeto1.ObtenerVertice()))
        lista_vertices.Insertar(name_nodo, objeto1)
        imgGrafo.view()

    nombre_nodo = tk.Label(left_frame_2nodo, text="", font=("Arial", 15))
    nombre_nodo.pack(pady=20)
    # Creamos la etiqueta "Ingrese un texto" y la caja de texto correspondiente, junto con el botón "Aceptar"
    nombre_nodo = tk.Label(left_frame_2nodo, text="Nombre del Nodo", font=("Arial", 15))
    nombre_nodo.pack(pady=0)

    #Creamos una caja de texto 
    # caja_texto = tk.Entry(left_frame_2nodo, width=18, font=("Arial", 15))
    caja_texto.pack(pady=10)

    #Creamos otra etiqueta
    opcion_combo = tk.Label(left_frame_2nodo, text="Seleccione Conexion", font=("Arial", 15))
    opcion_combo.pack(pady=0)
    
    #Creamos combobox
    opciones.append(objeto1.ObtenerVertice())
    combo['values'] = opciones
    # combo = ttk.Combobox(left_frame_2nodo, values=opciones,width=23,height=15, justify="center")
    combo.pack()

    # Crear botón verde
    boton_verde = tk.Button(left_frame_2nodo, text="Aceptar", font=("Arial", 15), bg="green", fg="white", command=nodos)
    boton_verde.pack(pady=30)

    finaliz = tk.Button(left_frame_2nodo, text="Finalizar Grafo", font=("Arial", 15), bg="Blue", fg="white", command=finaliza_grafo)
    finaliz.pack(pady=5)

    left_frame_2nodo.pack()

def nodos():
    #Valida si el nuevo nodo ya a sido ingresado anteriormente
    nuevo_nodo = caja_texto.get()
    
    if nuevo_nodo in opciones:
        #Obtiene seleccion combobox
        seleccion = combo.get()
        imgGrafo.edge(str(nuevo_nodo), str(seleccion))
        lista_vertices.Busqueda(nuevo_nodo,seleccion)
        caja_texto.delete(0, tk.END)
        imgGrafo.view()
    else:
        opciones.append(nuevo_nodo)
        combo['values'] = opciones

        caja_texto.delete(0, tk.END)

        #NuevoObjeto 
        seleccion = combo.get()
        nuevo_objeto = Verice(nuevo_nodo)
        imgGrafo.node(str(nuevo_nodo))
        lista_vertices.Insertar(nuevo_nodo, nuevo_objeto)
        lista_vertices.Busqueda(nuevo_nodo,seleccion)

        #se relaciona
        imgGrafo.edge(str(seleccion), str(nuevo_nodo))
    
        #Refresca la imagen 
        imgGrafo.view()

def finaliza_grafo():
    left_frame_2nodo.pack_forget()

    # Creamos la etiqueta "BIENVENIDO" y la colocamos en la sección izquierda
    titulo = tk.Label(frame_finaliza, text="Busqueda camino mas corto", font=("Arial", 25))
    titulo.pack(pady=20)

    # Creamos la etiqueta nodo inicial
    nombre_nodoI = tk.Label(frame_finaliza, text="Nodo Inicial", font=("Arial", 15))
    nombre_nodoI.pack(pady=0)

    #Para los comobos
    Cnodo_inicio['values'] = opciones
    Cnodo_inicio.pack()

    # Creamos la etiqueta nodo final
    nombre_nodoF = tk.Label(frame_finaliza, text="Nodo final", font=("Arial", 15))
    nombre_nodoF.pack(pady=0)

    #Para combo
    Cnodo_final['values'] = opciones
    Cnodo_final.pack()

    # Crear botón rojo
    boton_r = tk.Button(frame_finaliza, text="Ver camino optimo", font=("Arial", 15), bg="green", fg="white", command=camino_optimo)
    boton_r.pack(pady=15)

    # Crear botón amarillo
    boton_a = tk.Button(frame_finaliza, text="camino 1", font=("Arial", 15), bg="green", fg="white", command=camino_1)
    boton_a.pack(pady=15)

    # Crear botón cyan
    boton_v = tk.Button(frame_finaliza, text="camino 2", font=("Arial", 15), bg="green", fg="white", command=camino_2)
    boton_v.pack(pady=15)

    frame_finaliza.pack()

def camino_optimo():
    nodo_inicial = Cnodo_inicio.get()
    nodo_finaliza = Cnodo_final.get()

    #Devuelve el diccionario con los nodos y sus vecinos
    grafo = lista_vertices.crear_diccionario()
    #Duelve lista con caminos mas cortos  (xs)
    xs = lista_vertices.camino_corto(grafo, nodo_inicial, nodo_finaliza)
    cont = len(xs)
    print("esto devuelve camino1: "+str(xs))
    #itera la lista para llegar al camino optimo
    text = ''
    for i in xs:
        text += str(i)+"-->"
        imgGrafo.node(i, color='red')

    imgGrafo.view()
    messagebox.showwarning("Camino Optimo", "Notacion formal es: "+ text[:-3])
    for i in xs:
        imgGrafo.node(i, color='black')


def camino_1():
    nodo_inicial = Cnodo_inicio.get()
    nodo_finaliza = Cnodo_final.get()

    #Devuelve el diccionario con los nodos y sus vecinos
    grafo = lista_vertices.crear_diccionario()

    #Duelve lista con caminos que no sea optimo
    xs = lista_vertices.dfs_dos_caminos_no_cortos(grafo, nodo_inicial, nodo_finaliza)

    print("esto devuelve camino1: "+str(xs[0]))
    # itera la lista para llegar al camino optimo
    text = ''
    for i in xs[0]:
        text += str(i)+"-->"
        imgGrafo.node(i, color='blue')

    imgGrafo.view()
    messagebox.showwarning("Camino Optimo", "Notacion formal es: "+ text[:-3])

    for i in xs[0]:
        text += str(i)+"-->"
        imgGrafo.node(i, color='black')


def camino_2():
    nodo_inicial = Cnodo_inicio.get()
    nodo_finaliza = Cnodo_final.get()

    #Devuelve el diccionario con los nodos y sus vecinos
    grafo = lista_vertices.crear_diccionario()

    #Duelve lista con caminos que no sea optimo
    xs = lista_vertices.dfs_dos_caminos_no_cortos(grafo, nodo_inicial, nodo_finaliza)

    print("esto devuelve camino2: "+str(xs[1]))
    # itera la lista para llegar al camino optimo
    text = ''
    for i in xs[1]:
        text += str(i)+"-->"
        imgGrafo.node(i, color='cyan')

    imgGrafo.view()
    messagebox.showwarning("Camino Optimo", "Notacion formal es: "+ text[:-3])
    
    for i in xs[1]:
        text += str(i)+"-->"
        imgGrafo.node(i, color='black')

# Creamos la ventana principal de la interfaz gráfica
root.title("Mi aplicación")

# Definimos el tamaño de la ventana
root.geometry("600x400")

# Dividimos la ventana en dos secciones verticales



# Creamos la etiqueta "BIENVENIDO" y la colocamos en la sección izquierda
titulo = tk.Label(left_frame, text="BIENVENIDO", font=("Arial", 36))
titulo.pack(pady=40, padx=100)

# Creamos la etiqueta "Ingrese un texto" y la caja de texto correspondiente, junto con el botón "Aceptar"
texto_label = tk.Label(left_frame, text="Ingrese Nombre del Nodo Raiz", font=("Arial", 25))
texto_label.pack(pady=0)
#Caja de texto 
texto_caja = tk.Entry(left_frame, width=25, font=("Arial", 20))
texto_caja.pack(pady=0)


#boton 
boton_aceptar = tk.Button(left_frame, text="Aceptar", fg="white", bg="green", font=("Arial", 23), command=segundo_nodo)
boton_aceptar.pack(pady=30)

left_frame.pack()

# Iniciamos el bucle principal de la interfaz gráfica
root.mainloop()
