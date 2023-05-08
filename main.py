# Librerías
from tkinter import *
from tkinter import Tk, Frame, Button, Label, ttk, PhotoImage, IntVar
# Crear figuras para incrustar en tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Librería para realizar gráficas
import matplotlib.pyplot as plt
# Librería para gráficas dinámicas
import matplotlib.animation as animation
# Se llama la clse del archivo
from interfaz import comunicacion
import numpy as np
# Librería para la recolección de datos
import collections
# Localización de GPS
import folium
import pandas as pd
import webbrowser
import csv, os
import tkinter.messagebox as ms

datos_señal_diez = []

class OtherWindow:
    # Constructor
    def __init__(self, master):
        self.master = master
        self.master.title("Lectura de Datos")
        # Se lee el archivo, para saber la cantidad de datos a muostrar
        with open("datos_IMU.txt", "r") as f:
            lineas = f.readlines()

        # Obtener la cantidad de filas en el archivo
        filas = len(lineas)

        

        # Cantidad de datos en el eje x que se van a mostrar
        self.muestra = filas
        # Datos que recibimos por 'default'
        self.datos = 0.0

        # Se crea la gráfica
        self.fig2, axs2 = plt.subplots(nrows=3, ncols=1,facecolor = '#FFFFFF', dpi = 100, figsize = (10,2))# Tamaño del plot
        ax21, ax22, ax23 = axs2
        # Personalización de la gráfica
        ax21.set_title("Gráfica de datos de Arduino", color = 'black', size = 12, family = "Arial")
        ax21.tick_params(direction = 'out', length = 5, width = 2, colors = 'black', 
                       grid_color = 'r')
        ax22.tick_params(direction = 'out', length = 5, width = 2, colors = 'black', 
                       grid_color = 'r')
        ax23.tick_params(direction = 'out', length = 5, width = 2, colors = 'black', 
                       grid_color = 'r')
        
        # Se crean las líneas personalizadas
        self.line, = ax21.plot([], [], color = 'm', linewidth = 0.5)

        self.line2, = ax21.plot([], [], color = 'g', linewidth = 0.5)
        
        self.line3, = ax21.plot([], [], color = 'r', linewidth = 0.5)

        self.line4, = ax22.plot([], [], color = 'y', linewidth = 0.5)

        self.line5, = ax22.plot([], [], color = 'c', linewidth = 0.5)
        
        self.line6, = ax22.plot([], [], color = 'r', linewidth = 0.5)

        self.line7, = ax23.plot([], [], color = 'purple', linewidth = 0.5)

        self.line8, = ax23.plot([], [], color = 'blue', linewidth = 0.5)
        
        self.line9, = ax23.plot([], [], color = 'gray', linewidth = 0.5)
        
        # Límites en el eje 'x' y en el eje 'y'
        ax21.set_xlim([0, self.muestra])
        ax21.set_ylim([-35,35])
        ax22.set_xlim([0, self.muestra])
        ax22.set_ylim([-80,80])
        ax23.set_xlim([0, self.muestra])
        ax23.set_ylim([-150,150])

        #Nombres del eje y
        ax21.set_ylabel("Giroscopio")
        ax22.set_ylabel("Acelerómetro")
        ax23.set_ylabel("Magnetómetro")

        # Abrir el archivo y leer todas las líneas en una lista
        data = np.loadtxt("datos_IMU.txt", delimiter=",")
        # Seleccionar la columna de interés, por ejemplo la primera columna
        s1 = data[:, 0]
        s2 = data[:, 1]
        s3 = data[:, 2]
        s4 = data[:, 3]
        s5 = data[:, 4]
        s6 = data[:, 5]
        s7 = data[:, 6]
        s8 = data[:, 7]
        s9 = data[:, 8]

        # Asignación de los datos. Creando lista vacía de la cantidad de datos definidas
        self.datos_señal_uno = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_dos = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_tres = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_cuatro = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_cinco = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_seis = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_siete = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_ocho = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_nueve = collections.deque([0]*self.muestra, maxlen= self.muestra)

        # Se almacenan los datos en el arreglo de n muestras
        self.datos_señal_uno = s1
        self.datos_señal_dos = s2
        self.datos_señal_tres = s3
        self.datos_señal_cuatro = s4
        self.datos_señal_cinco = s5
        self.datos_señal_seis = s6
        self.datos_señal_siete = s7
        self.datos_señal_ocho = s8
        self.datos_señal_nueve = s9
 
        # Se crea el widget
        self.widgets1()
        
    # Se crean los Frame, y wiggets que estarán en la ventana
    def widgets1(self):
        global select_giroscopio2, select_acelerometro2, select_magnetometro2
        global xg2, xa2, xm2, yg2, ya2, ym2, zg2, za2, zm2
        select_giroscopio2 = IntVar()
        select_acelerometro2 = IntVar()
        select_magnetometro2 = IntVar()
        xg2 = IntVar()
        yg2 = IntVar()
        zg2 = IntVar()
        xa2 = IntVar()
        ya2 = IntVar()
        za2 = IntVar()
        xm2 = IntVar()
        ym2 = IntVar()
        zm2 = IntVar()
        # Mostrar objetos en la ventana
        frame_21 = Frame(self.master, bg = 'white')
        frame_21.grid(column=0, columnspan=2, row=0,ipadx=35, ipady=270)
        frame_22 = Frame(self.master, bg = 'white')
        frame_22.grid(column=2, row=0, padx=3,ipadx=144, ipady=370)   

        # Se crea un objeto canvas, que crea la figura donde se va a mostrar la figura
        self.canvas = FigureCanvasTkAgg(self.fig2, master = frame_21)
        self.canvas.get_tk_widget().pack(padx=0, pady=0, expand=True, fill='both')
        # Se crea los botenes de acción para mostrar las señales leídas del archivo GIROSCOPIO
        def datos_giros():
            # Se muestran las señales cuando el checkbutton está activo
            if(select_giroscopio2.get()==1):
                if(xg2.get() == 1):
                    self.line.set_data(range(self.muestra), self.datos_señal_uno)
                    self.canvas.draw()
                if(yg2.get() == 1):
                    self.line2.set_data(range(self.muestra), self.datos_señal_dos)
                    self.canvas.draw()
                if(zg2.get() == 1):
                    self.line3.set_data(range(self.muestra), self.datos_señal_tres)
                    self.canvas.draw()

                if(xg2.get() == 0):
                    self.line.set_data(range(1), self.datos_señal_uno[0])
                    self.canvas.draw()
                if(yg2.get() == 0):
                    self.line2.set_data(range(1), self.datos_señal_dos[0])
                    self.canvas.draw()
                if(zg2.get() == 0):
                    self.line3.set_data(range(1), self.datos_señal_tres[0])
                    self.canvas.draw()

            # Quita las señales del plot
            if(select_giroscopio2.get() == 0):
                self.line.set_data(range(1), self.datos_señal_uno[0])
                self.line2.set_data(range(1), self.datos_señal_dos[0])
                self.line3.set_data(range(1), self.datos_señal_tres[0])
        # Se crea los botenes de acción para mostrar las señales leídas del archivo ACELERÓMETRO
        def datos_acel():
            # Se muestran las señales cuando el checkbutton está activo
            if(select_acelerometro2.get() == 1):
                if(xa2.get() == 1):
                    self.line4.set_data(range(self.muestra), self.datos_señal_cuatro)
                    self.canvas.draw()
                if(ya2.get() == 1):
                    self.line5.set_data(range(self.muestra), self.datos_señal_cinco)
                    self.canvas.draw()
                if(za2.get() == 1):
                    self.line6.set_data(range(self.muestra), self.datos_señal_seis)
                    self.canvas.draw()

                if(xa2.get() == 0):
                    self.line4.set_data(range(1), self.datos_señal_cuatro[0])
                    self.canvas.draw()
                if(ya2.get() == 0):
                    self.line5.set_data(range(1), self.datos_señal_cinco[0])
                    self.canvas.draw()
                if(za2.get() == 0):
                    self.line6.set_data(range(1), self.datos_señal_seis[0])
                    self.canvas.draw()
            # Quita las señales del plot
            if(select_acelerometro2.get() == 0):
                self.line4.set_data(range(1), self.datos_señal_cuatro[0])
                self.line5.set_data(range(1), self.datos_señal_cinco[0])
                self.line6.set_data(range(1), self.datos_señal_seis[0])
        # Se crea los botenes de acción para mostrar las señales leídas del archivo MAGNETÓMETRO
        def datos_mag():
            # Se muestran las señales cuando el checkbutton está activo
            if(select_magnetometro2.get() == 1):
                if(xm2.get() == 1):
                    self.line7.set_data(range(self.muestra), self.datos_señal_siete)
                    self.canvas.draw()
                if(ym2.get() == 1):
                    self.line8.set_data(range(self.muestra), self.datos_señal_ocho)
                    self.canvas.draw()
                if(zm2.get() == 1):
                    self.line9.set_data(range(self.muestra), self.datos_señal_nueve)
                    self.canvas.draw()

                if(xm2.get() == 0):
                    self.line7.set_data(range(1), self.datos_señal_siete[0])
                    self.canvas.draw()
                if(ym2.get() == 0):
                    self.line8.set_data(range(1), self.datos_señal_ocho[0])
                    self.canvas.draw()
                if(zm2.get() == 0):
                    self.line9.set_data(range(1), self.datos_señal_nueve[0])
                    self.canvas.draw()
            # Quita las señales del plot
            if(select_magnetometro2.get() == 0):
                self.line7.set_data(range(1), self.datos_señal_siete[0])
                self.line8.set_data(range(1), self.datos_señal_ocho[0])
                self.line9.set_data(range(1), self.datos_señal_nueve[0])




        # Controladores, son los botones que activan las señales GIROSCOPIO
        self.bt_giros = Button(frame_22, text='GIROSCOPIO', font=('Arial', 12, 'bold'),
                                  width=15, bg='orange', fg='black', command=datos_giros)
        self.bt_giros.place(x=75,y=95)

        self.bt_giroscopio2 = ttk.Checkbutton(frame_22,  text='Giroscopio', variable=select_giroscopio2, onvalue=1, offvalue=0)
        self.bt_giroscopio2.place(x=108,y=140)

        self.bt_xg2 = ttk.Checkbutton(frame_22,  text='X', variable=xg2, onvalue=1, offvalue=0)
        self.bt_xg2.place(x=132,y=170)

        self.bt_yg2 = ttk.Checkbutton(frame_22,  text='Y', variable=yg2, onvalue=1, offvalue=0)
        self.bt_yg2.place(x=132,y=200)

        self.bt_zg2 = ttk.Checkbutton(frame_22,  text='Z', variable=zg2, onvalue=1, offvalue=0)
        self.bt_zg2.place(x=132,y=230)
        # ----------------------------------------------------
        # Controladores, son los botones que activan las señales ACELERÓMETRO
        self.bt_acel = Button(frame_22, text='ACELERÓMETRO', font=('Arial', 12, 'bold'),
                                  width=15, bg='yellow', fg='black', command=datos_acel)
        self.bt_acel.place(x=75,y=290)

        self.bt_acelerometro2 = ttk.Checkbutton(frame_22, text='Acelerómetro', variable=select_acelerometro2, onvalue=1, offvalue=0)
        self.bt_acelerometro2.place(x=100,y=330)

        self.bt_xa2 = ttk.Checkbutton(frame_22,  text='X', variable=xa2, onvalue=1, offvalue=0)
        self.bt_xa2.place(x=132,y=360)

        self.bt_ya2 = ttk.Checkbutton(frame_22,  text='Y', variable=ya2, onvalue=1, offvalue=0)
        self.bt_ya2.place(x=132,y=390)

        self.bt_za2 = ttk.Checkbutton(frame_22,  text='Z', variable=za2, onvalue=1, offvalue=0)
        self.bt_za2.place(x=132,y=420)

        # ----------------------------------------------------
        # Controladores, son los botones que activan las señales MAGNETÓMETRO
        self.bt_mag = Button(frame_22, text='MAGNETÓMETRO', font=('Arial', 12, 'bold'),
                                  width=15, bg='yellow', fg='black', command=datos_mag)
        self.bt_mag.place(x=75,y=480)

        self.bt_magnetometro2 = ttk.Checkbutton(frame_22, text='Magnómetro', variable=select_magnetometro2, onvalue=1, offvalue=0)
        self.bt_magnetometro2.place(x=100,y=520)
        
        self.bt_xm2 = ttk.Checkbutton(frame_22,  text='X', variable=xm2, onvalue=1, offvalue=0)
        self.bt_xm2.place(x=132,y=550)

        self.bt_ym2 = ttk.Checkbutton(frame_22,  text='Y', variable=ym2, onvalue=1, offvalue=0)
        self.bt_ym2.place(x=132,y=580)

        self.bt_zm2 = ttk.Checkbutton(frame_22,  text='Z', variable=zm2, onvalue=1, offvalue=0)
        self.bt_zm2.place(x=132,y=610)




#############################################################################################################
#############################################################################################################
#############################################################################################################
#############################################################################################################

class grafica(Frame):
    # Constructor
    def __init__(self, master, *args):
        super().__init__(master, *args)
        global datos_señal_diez
        # Se crea un objeto datos_arduino de la clase 'comunicacion'
        self.datos_arduino = comunicacion()
        # Actualiza los puertos, solo al inicio
        self.actualizar_puertos()

        # Cantidad de datos en el eje x que se van a mostrar
        self.muestra = 8
        # Datos que recibimos por 'default'
        self.datos = 0.0

        # Se crea la gráfica
        self.fig, axs = plt.subplots(nrows=3, ncols=1,facecolor = '#FFFFFF', dpi = 100, figsize = (10,2))# Tamaño del plot
        ax1, ax2, ax3 = axs
        # Personalización de la gráfica
        ax1.set_title("Gráfica de datos de Arduino", color = 'black', size = 12, family = "Arial")
        ax1.tick_params(direction = 'out', length = 5, width = 2, colors = 'black', 
                       grid_color = 'r')
        ax2.tick_params(direction = 'out', length = 5, width = 2, colors = 'black', 
                       grid_color = 'r')
        ax3.tick_params(direction = 'out', length = 5, width = 2, colors = 'black', 
                       grid_color = 'r')
        
        # Se crean las líneas personalizadas
        self.line, = ax1.plot([], [], color = 'm', linewidth = 0.5)

        self.line2, = ax1.plot([], [], color = 'g', linewidth = 0.5)
        
        self.line3, = ax1.plot([], [], color = 'r', linewidth = 0.5)

        self.line4, = ax2.plot([], [], color = 'y', linewidth = 0.5)

        self.line5, = ax2.plot([], [], color = 'c', linewidth = 0.5)
        
        self.line6, = ax2.plot([], [], color = 'r', linewidth = 0.5)

        self.line7, = ax3.plot([], [], color = 'purple', linewidth = 0.5)

        self.line8, = ax3.plot([], [], color = 'blue', linewidth = 0.5)
        
        self.line9, = ax3.plot([], [], color = 'gray', linewidth = 0.5)
        
        # Límites en el eje 'x' y en el eje 'y'
        ax1.set_xlim([0, self.muestra])
        ax1.set_ylim([-35,35])
        ax2.set_xlim([0, self.muestra])
        ax2.set_ylim([-80,80])
        ax3.set_xlim([0, self.muestra])
        ax3.set_ylim([-150,150])

        #Nombres del eje y
        ax1.set_ylabel("Giroscopio")
        ax2.set_ylabel("Acelerómetro")
        ax3.set_ylabel("Magnetómetro")

        # Asignación de los datos. Creando lista vacía de la cantidad de datos definidas
        self.datos_señal_uno = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_dos = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_tres = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_cuatro = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_cinco = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_seis = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_siete = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_ocho = collections.deque([0]*self.muestra, maxlen= self.muestra)
        self.datos_señal_nueve = collections.deque([0]*self.muestra, maxlen= self.muestra)
        
        # Se crea el widget
        self.widgets()
        
        
    # Se crean los Frame, y wiggets que estarán en la ventana
    def window_2(self):
        ventana2 = Toplevel(ventana)
        ventana2.geometry("1080x950")
        ventana2.grab_set()
        ventana2.focus_set()

        OtherWindow(ventana2)
        ventana2.mainloop()

    # Función que se actualiza en la animación de las señales   
    def animate(self,i):
        # Se obtienen los datos
        self.datos = (self.datos_arduino.datos_recibidos.get())
        dato = self.datos.split(',')
        dato1 = float(dato[0])
        dato2 = float(dato[1])
        dato3 = float(dato[2])
        dato4 = float(dato[3])
        dato5 = float(dato[4])
        dato6 = float(dato[5])
        dato7 = float(dato[6])
        dato8 = float(dato[7])
        dato9 = float(dato[8])
        dato10 = float(dato[9])
        dato11 = float(dato[10])

        # Se crean el archivo .txt para la escritura de los datos IMU
        with open("datos_IMU.txt", "a") as f:
            f.write(f"{dato1},{dato2},{dato3},{dato4},{dato5},{dato6},{dato7},{dato8},{dato9}\n")
        # Se crean el archivo .txt para la escritura de los datos IMU
        with open("datos_GPS.txt", "a") as f:
            f.write(f"{dato10},{dato11}\n")

        # Se crean el archivo .txt para la escritura de los datos IMU
        filename = 'datos_gps.csv'
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([dato10,dato11])

        # Se almacenan los datos en el arreglo de 100 muestras
        self.datos_señal_uno.append(dato1)
        self.datos_señal_dos.append(dato2)
        self.datos_señal_tres.append(dato3)
        self.datos_señal_cuatro.append(dato4)
        self.datos_señal_cinco.append(dato5)
        self.datos_señal_seis.append(dato6)
        self.datos_señal_siete.append(dato7)
        self.datos_señal_ocho.append(dato8)
        self.datos_señal_nueve.append(dato9)
        # Asignación a las señales GIROSCOPIO, poracción del botón
        if(select_giroscopio.get() == 1):
            if(xg.get() == 1):
                self.line.set_data(range(self.muestra), self.datos_señal_uno)
            if(yg.get() == 1):
                self.line2.set_data(range(self.muestra), self.datos_señal_dos)
            if(zg.get() == 1):
                self.line3.set_data(range(self.muestra), self.datos_señal_tres)

            if(xg.get() == 0):
                self.line.set_data(range(1), self.datos_señal_uno[0])
            if(yg.get() == 0):
                self.line2.set_data(range(1), self.datos_señal_dos[0])
            if(zg.get() == 0):
                self.line3.set_data(range(1), self.datos_señal_tres[0])

        # Asignación a las señales ACELERÓMETRO, poracción del botón
        if(select_acelerometro.get() == 1):
            if(xa.get() == 1):
                self.line4.set_data(range(self.muestra), self.datos_señal_cuatro)
            if(ya.get() == 1):
                self.line5.set_data(range(self.muestra), self.datos_señal_cinco)
            if(za.get() == 1):
                self.line6.set_data(range(self.muestra), self.datos_señal_seis)

            if(xa.get() == 0):
                self.line4.set_data(range(1), self.datos_señal_cuatro[0])
            if(ya.get() == 0):
                self.line5.set_data(range(1), self.datos_señal_cinco[0])
            if(za.get() == 0):
                self.line6.set_data(range(1), self.datos_señal_seis[0])

        # Asignación a las señales ACELERÓMETRO, poracción del botón
        if(select_magnetometro.get() == 1):
            if(xm.get() == 1):
                self.line7.set_data(range(self.muestra), self.datos_señal_siete)
            if(ym.get() == 1):
                self.line8.set_data(range(self.muestra), self.datos_señal_ocho)
            if(zm.get() == 1):
                self.line9.set_data(range(self.muestra), self.datos_señal_nueve)

            if(xm.get() == 0):
                self.line7.set_data(range(1), self.datos_señal_siete[0])
            if(ym.get() == 0):
                self.line8.set_data(range(1), self.datos_señal_ocho[0])
            if(zm.get() == 0):
                self.line9.set_data(range(1), self.datos_señal_nueve[0])

        # Quita las señales del plot GIROSCOPIO
        if(select_giroscopio.get() == 0):
            self.line.set_data(range(1), self.datos_señal_uno[0])
            self.line2.set_data(range(1), self.datos_señal_dos[0])
            self.line3.set_data(range(1), self.datos_señal_tres[0])
        # Quita las señales del plot ACELERÓMETRO
        if(select_acelerometro.get() == 0):
            self.line4.set_data(range(1), self.datos_señal_cuatro[0])
            self.line5.set_data(range(1), self.datos_señal_cinco[0])
            self.line6.set_data(range(1), self.datos_señal_seis[0])
        # Quita las señales del plot MAGNETÓMETRO
        if(select_magnetometro.get() == 0):
            self.line7.set_data(range(1), self.datos_señal_siete[0])
            self.line8.set_data(range(1), self.datos_señal_ocho[0])
            self.line9.set_data(range(1), self.datos_señal_nueve[0])

    # Se ejecuta cuando se le da la opción de graficar
    def iniciar(self,):
        self.ani = animation.FuncAnimation(self.fig, self.animate, interval = 100, blit = False)
        # Configuración de botones
        self.bt_graficar.config(state = 'disabled')
        self.bt_pausar.config(state = 'normal')
        # Muestra las líneas de las gráficas
        self.canvas.draw()


    # Función que pausa la graficación
    def pausar(self):
        self.ani.event_source.stop()
        self.bt_reanudar.config(state = 'normal')

    # Función que reanuda el sistema
    def reanudar(self):
        self.ani.event_source.start()
        self.bt_reanudar.config(state = 'disabled')


    # Muestra el mapa
    def mostrar_mapa(self):
        # Carga los datos de GPS desde un archivo CSV
        df = pd.read_csv('datos_gps.csv', header=None, names=['latitud', 'longitud'])
        # Obtiene la lista de ubicaciones
        locations = df[['latitud', 'longitud']].values.tolist()

        if mapa_check.get():
            # Crea un objeto Map centrado en la primera ubicación
            first_location = locations[0]
            m = folium.Map(location=first_location, zoom_start=12)
            # Crea una capa de líneas en el mapa que muestra el recorrido GPS
            folium.PolyLine(locations=locations, color='red').add_to(m)
            # Guarda el archivo HTML y lo carga en la web
            m.save('mapa_gps.html')
            webbrowser.open('mapa_gps.html')

    # Se crean los Frame y los botones que estarán en la ventana
    def widgets(self):
        # Variables globales para el control de los botones
        global select_giroscopio, select_acelerometro, select_magnetometro, mapa_check
        global xg, xa, xm, yg, ya, ym, zg, za, zm
        select_giroscopio = IntVar()
        select_acelerometro = IntVar()
        select_magnetometro = IntVar()
        mapa_check = IntVar()
        xg = IntVar()
        yg = IntVar()
        zg = IntVar()
        xa = IntVar()
        ya = IntVar()
        za = IntVar()
        xm = IntVar()
        ym = IntVar()
        zm = IntVar()
        # Mostrar objetos en la ventana
        frame = Frame(self.master, bg = 'white', bd = 2)
        frame.grid(column=0, columnspan=2, row=0, sticky='nsew')
        frame1 = Frame(self.master, bg = 'white')
        frame1.grid(column=2, row=0, sticky='nsew')       
        frame4 = Frame(self.master, bg = 'white')
        frame4.grid(column=0, row=1, sticky='nsew')
        frame2 = Frame(self.master, bg = 'white')
        frame2.grid(column=1, row=1, sticky='nsew')
        frame3 = Frame(self.master, bg = 'white')
        frame3.grid(column=2, row=1, sticky='nsew')

        # Para mantener los datos en pantalla
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=1)
        self.master.columnconfigure(2, weight=1)
        self.master.rowconfigure(0, weight=5)
        self.master.rowconfigure(1, weight=1)


        # Se crea un objeto canvas, que crea la figura donde se va a mostrar la figura
        self.canvas = FigureCanvasTkAgg(self.fig, master = frame)
        self.canvas.get_tk_widget().pack(padx=0, pady=0, expand=True, fill='both')

        # Se crean los botones, de comunicación con el serial
        self.bt_graficar = Button(frame4, text='Graficar Datos', font=('Arial', 12, 'bold'),
                                  width=12, bg='purple4', fg='black', command=self.iniciar)
        self.bt_graficar.pack(pady = 5, expand = 1)

        self.bt_pausar = Button(frame4, state = 'disabled', text='Pausar', font=('Arial', 12, 'bold'),
                                  width=12, bg='salmon', fg='black', command=self.pausar)
        self.bt_pausar.pack(pady = 5, expand = 1)

        self.bt_reanudar = Button(frame4, state = 'disabled', text='Reanudar', font=('Arial', 12, 'bold'),
                                  width=12, bg='green', fg='black', command=self.reanudar)
        self.bt_reanudar.pack(pady = 5, expand = 1)

        # Valores
        Label(frame2, text = 'Señal de dispositivo a observar', font=('Arial',15, 'bold'), bg='white', fg='white').pack()
        Label(frame2, text = 'Señal de dispositivo a observar', font=('Arial',15, 'bold'), bg='white', fg='black').place(x=50)
        style = ttk.Style()
        # Estilo de color negro
        style.configure("Horizontal.TScale")
        # Controladores, son los botenes que dan la acción para mostrar la señal del GIROSCOPIO
        self.bt_giroscopio = ttk.Checkbutton(frame2,  text='Giroscopio', variable=select_giroscopio, onvalue=1, offvalue=0)
        self.bt_giroscopio.place(x=1,y=30)

        self.bt_xg = ttk.Checkbutton(frame2,  text='X', variable=xg, onvalue=1, offvalue=0)
        self.bt_xg.place(x=25,y=60)

        self.bt_yg = ttk.Checkbutton(frame2,  text='Y', variable=yg, onvalue=1, offvalue=0)
        self.bt_yg.place(x=25,y=90)

        self.bt_zg = ttk.Checkbutton(frame2,  text='Z', variable=zg, onvalue=1, offvalue=0)
        self.bt_zg.place(x=25,y=120)
        # ----------------------------------------------------
        # Controladores, son los botenes que dan la acción para mostrar la señal del ACELERÓMETRO
        self.bt_acelerometro = ttk.Checkbutton(frame2, text='Acelerómetro', variable=select_acelerometro, onvalue=1, offvalue=0)
        self.bt_acelerometro.place(x=150,y=30)

        self.bt_xa = ttk.Checkbutton(frame2,  text='X', variable=xa, onvalue=1, offvalue=0)
        self.bt_xa.place(x=175,y=60)

        self.bt_ya = ttk.Checkbutton(frame2,  text='Y', variable=ya, onvalue=1, offvalue=0)
        self.bt_ya.place(x=175,y=90)

        self.bt_za = ttk.Checkbutton(frame2,  text='Z', variable=za, onvalue=1, offvalue=0)
        self.bt_za.place(x=175,y=120)

        # ----------------------------------------------------
        # Controladores, son los botenes que dan la acción para mostrar la señal del MAGNETÓMETRO
        self.bt_magnetometro = ttk.Checkbutton(frame2, text='Magnómetro', variable=select_magnetometro, onvalue=1, offvalue=0)
        self.bt_magnetometro.place(x=310,y=30)
        
        self.bt_xm = ttk.Checkbutton(frame2,  text='X', variable=xm, onvalue=1, offvalue=0)
        self.bt_xm.place(x=335,y=60)

        self.bt_ym = ttk.Checkbutton(frame2,  text='Y', variable=ym, onvalue=1, offvalue=0)
        self.bt_ym.place(x=335,y=90)

        self.bt_zm = ttk.Checkbutton(frame2,  text='Z', variable=zm, onvalue=1, offvalue=0)
        self.bt_zm.place(x=335,y=120)


        # Puertos y velocidad de comunicación
        port = self.datos_arduino.puertos
        baud = self.datos_arduino.baudrates


        # Muestra el texto      
        Label(frame1, bg='white').pack(pady=30) # Espacio
        Label(frame1, text='Puertos COM', bg='white', fg='black', font=('Arial', 12, 'bold')).pack(pady=5)
        # Creación de objetos
        self.combobox_port = ttk.Combobox(frame1, values = port, justify='center', width=12, font='Arial')
        self.combobox_port.pack(pady=5)
        self.combobox_port.current(0)
        # Muestra el texto
        Label(frame1, bg='white').pack(pady=2) # Espacio
        Label(frame1, text='Baudrates', bg='white', fg='black', font=('Arial', 12, 'bold')).pack(pady=5)
        # Creación de objetos
        self.combobox_baud = ttk.Combobox(frame1, values = baud, justify='center', width=12, font='Arial')
        self.combobox_baud.pack(pady=5)
        self.combobox_baud.current(6)

        Label(frame1, bg='white').pack(pady=10) # Espacio
        # Se crean los botones control: Conectar, Actualizar, Desconectar
        self.bt_conectar = Button(frame1, text='Conectar', font=('Arial', 12, 'bold'), width=12, bg='green2',
                                  command=self.conectar_serial)
        self.bt_conectar.pack(pady=15)

        self.bt_actualizar = Button(frame1, text='Actualizar', font=('Arial', 12, 'bold'), width=12, bg='magenta',
                                  command=self.actualizar_puertos)
        self.bt_actualizar.pack(pady=15)

        self.bt_desconectar = Button(frame1, state='disabled', text='Desconectar', font=('Arial', 12, 'bold'), width=12, bg='red2',
                                  command=self.desconectar_serial)
        self.bt_desconectar.pack(pady=15)


        # Boton GPS
        mapa_checkbox = ttk.Checkbutton(frame3, text='Mostrar Mapa', variable=mapa_check)
        mapa_checkbox.pack(pady=10)

        self.bt_mapa = Button(frame3, text='Mostrar Ruta GPS', font=('Arial', 12, 'bold'),
                                  width=25, bg='green', fg='black', command= self.mostrar_mapa)
        self.bt_mapa.pack(pady=10)

        # Boton Lectura de archivos
        self.bt_datos_archivos = Button(frame3, text='Lectura de Archivos', font=('Arial', 12, 'bold'),
                                  width=25, bg='orange', fg='black', command= self.window_2) 
        self.bt_datos_archivos.pack(pady=10)


    # Actualiza los puertos. Solo se ejecuta al inicio
    def actualizar_puertos(self):
        self.datos_arduino.puertos_disponibles()

    # Se conecta al serial del Arduino
    def conectar_serial(self):
        self.bt_conectar.config(state='disabled')
        self.bt_desconectar.config(state='normal')
        self.bt_graficar.config(state='normal')
        self.bt_reanudar.config(state='disabled')
        # Se selecciona los puertos y la velocidad de comunicación
        self.datos_arduino.arduino.port = self.combobox_port.get()
        self.datos_arduino.arduino.baudrate = self.combobox_baud.get()
        # Realizamos conexión Serial
        self.datos_arduino.conexion_serial()


    # Desconecta el serial del Arduino
    def desconectar_serial(self):
        self.bt_conectar.config(state='normal')
        self.bt_desconectar.config(state='disabled')
        self.bt_pausar.config(state='disabled')

        # Excepción en caso de que no se esté ejecutando
        try:
            self.ani.event_source.stop()
        except AttributeError:
            pass
        self.datos_arduino.desconectar()

# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    ventana = Tk()
    ventana.geometry('1080x950')
    ventana.config(bg='gray30',bd=4)
    ventana.wm_title('Telemetría')
    ventana.minsize(width=10, height=2)
    ventana.call('wm', 'iconphoto', ventana._w, PhotoImage(file='logo.png'))
    app = grafica(ventana)
    app.mainloop()





