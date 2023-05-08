# Permite reconocer los puertos disponibles
import serial, serial.tools.list_ports
# Crea subprocesos para estar recibiendo datos constantementes
from threading import Thread, Event
# Permite recibir datos de arduino en forma de String
from tkinter import StringVar

# Clase que permite leer datos de Arduino en forma de String
class comunicacion():
    # Método constructor
    def __init__(self, *args):
        super().__init__(*args)
        # Se crea la variable datos recibidos de Arduino
        self.datos_recibidos = StringVar()
        # Se crea objeto 'Arduino' para la comuicación Serial
        self.arduino = serial.Serial()
        # Retardo inicial de 0.5
        self.arduino.timeout = 0.5
        # Se crea lista de la velocidad en Baudios
        self.baudrates = ['1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200']
        self.puertos = []

        self.señal = Event()
        self.hilo = None


    # Función que detecta la cantidad de puertos disponibles
    def puertos_disponibles(self):
        # Ciclo for que lee todos los puertos disponibles
        self.puertos = [port.device for port in serial.tools.list_ports.comports()]


    def conexion_serial(self):
        # Se crea excepciones para evitar errores en la Tx
        try:
            # Abrimos Arduino
            self.arduino.open()
        except:
            pass
        if (self.arduino.is_open):
            # Inicia el hilo
            self.iniciar_hilo()
            print('Conectado')

    # Recibe un valor de datos
    def enviar_datos(self, data):
        if (self.arduino.is_open):
            # Se envía el dato con un salto
            self.datos = str(data)+"\n"
            # Escribimos en el Arduino
            self.arduino.write(self.datos.encode())
        else:
            print("ERROR")

    # Función de lectura de datos en hilo
    def leer_datos(self):
        # Se crea excepciones para evitar errores
        try:
            # Ciclo 'While' que está leyendo constantemente las señales
            while(self.señal.isSet() and self.arduino.is_open):
                # Se lee los datos de Arduino
                data = self.arduino.readline().decode("utf-8").strip()
                # COmprueba si tenemos un dato mayo a uno
                if(len(data) > 1):
                    # Se asigna el dato recibido a la variable
                    self.datos_recibidos.set(data)
        except TypeError:
            pass

    # Función que inicia el hilo
    def iniciar_hilo(self):
        # Recibe el método que se va ejecutar en 'target'
        self.hilo = Thread(target= self.leer_datos)
        self.hilo.setDaemon(1)
        self.señal.set()
        self.hilo.start()


    # Función que detiene el hilo
    def stop_hilo(self):
        if (self.hilo is not None):
            # Limpia la señal
            self.señal.clear()
            self.hilo.join()
            self.hilo = None


    # Función que desconecta
    def desconectar(self):
        # Cierra la conexión de Arduino
        self.arduino.close()
        # Detiene el hilo
        self.stop_hilo()