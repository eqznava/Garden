class Planta:
    def __init__(self):
        self.__NombreComun = ''
        self.__NombreCientifico = ''
        self.__TipoPlanta = ''
        self.__Riego = ''
        self.__Clima = ''
        self.__Usos = ''
    def GetNombreComun(self):
        return self.__NombreComun
    def GetNombreCientifico(self):
        return self.__NombreCientifico
    def GetTipoPlanta(self):
        return self.__TipoPlanta
    def GetRiego(self):
        return self.__Riego
    def GetClima(self):
        return self.__Clima
    def GetUsos(self):
        return self.__Usos
    def SetNombreComun(self, nombrecomun):
        self.__NombreComun = nombrecomun
    def SetNombreCientifico(self, nombrecientifico):
        self.__NombreCientifico = nombrecientifico
    def SetTipoPlanta(self, tipoplanta):
        self.__TipoPlanta = tipoplanta
    def SetRiego(self, riego):
        self.__Riego = riego
    def SetClima(self, clima):
        self.__Clima = clima
    def SetUsos(self, usos):
        self.__Usos = usos
    def MostrarPlanta(self):
        print('\n♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ P L A N T A ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣\n')
        print('Nombre comun:',self.GetNombreComun())
        print('Nombre cientifico:',self.GetNombreCientifico())
        print('Tipo de Planta:',self.GetTipoPlanta())
        print('Riego:',self.GetRiego())
        print('Clima:',self.GetClima())
        print('Usos:',self.GetUsos())
        print('\n♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣\n')

class Jardin:
    def __init__(self, path):
        self.__ListaPlantas = []
        self.__Path = path
    def CargarPlantas(self):
        try:
            archivo = open(self.__Path, 'r')
        except:
            print('╔════════════════════════════════════════════════╗')
            print('║  ERROR: » El archivo que buscas no existe. «   ║')
            print('╚════════════════════════════════════════════════╝')
        else:
            plantas = archivo.readlines()
            archivo.close()
            if (len(plantas)>0):
                for planta in plantas:
                    datos = planta.split('|')
                    if(len(datos)==6):
                        plantanueva = Planta()
                        plantanueva.SetNombreComun(datos[0])
                        plantanueva.SetNombreCientifico(datos[1])
                        plantanueva.SetTipoPlanta(datos[2])
                        plantanueva.SetRiego(datos[3])
                        plantanueva.SetClima(datos[4])
                        plantanueva.SetUsos(datos[5])
                        self.__ListaPlantas = self.__ListaPlantas + [plantanueva]
                if len(self.__ListaPlantas)==1:
                    print('╔════════════════════════════════════════════════════════════════════════╗')
                    print('  INFO:  Se ha cargado un total de',len(self.__ListaPlantas),'planta. ♣')
                    print('╚════════════════════════════════════════════════════════════════════════╝')
                else:
                    print('╔════════════════════════════════════════════════════════════════════════╗')
                    print('  INFO:  Se han cargado un total de',len(self.__ListaPlantas),'plantas. ♣')
                    print('╚════════════════════════════════════════════════════════════════════════╝')
    def CrearNuevaPlanta(self, plantanueva):
        self.__ListaPlantas = self.__ListaPlantas + [plantanueva]
    def GuardarPlantas(self):
        try:
            archivo = open(self.__Path,'w')
        except:
            print('╔════════════════════════════════════════════════╗')
            print('║  ERROR: » El archivo que buscas no existe. «   ║')
            print('╚════════════════════════════════════════════════╝')
        else:
            for planta in self.__ListaPlantas:
                texto = planta.GetNombreComun()+'|'
                texto = texto + planta.GetNombreCientifico()+'|'
                texto = texto + planta.GetTipoPlanta()+'|'
                texto = texto + planta.GetRiego()+'|'
                texto = texto + planta.GetClima()+'|'
                texto = texto + planta.GetUsos()+'\n'
                archivo.write(texto)
            archivo.close()
            print('\n')
            print('╔════════════════════════════════════════════════╗')
            print('║    INFO: Datos almacenados exitosamente ♣      ║')
            print('╚════════════════════════════════════════════════╝\n')
    def MostrarJardin(self):
        print('\n♣ • ♠ • ♠ • ♠ • ♠ • ♠ • ♣ • ♣ J A R D I N ♣ • ♠ • ♠ • ♠ • ♠ • ♠ • ♣ • ♣\n')
        if len(self.__ListaPlantas)==0:
            print('╔════════════════════════════════════════════════╗')
            print('║    INFO: No hay plantas en el jardin ♣         ║')
            print('╚════════════════════════════════════════════════╝\n')
        elif len(self.__ListaPlantas)==1:
            print('╔════════════════════════════════════════════════════════════════════════════╗')
            print('     INFO: Hay',len(self.__ListaPlantas),'planta en el jardin ♣')
            print('╚════════════════════════════════════════════════════════════════════════════╝\n')
        elif len(self.__ListaPlantas)>1:
            print('╔════════════════════════════════════════════════════════════════════════════╗')
            print('     INFO: Hay',len(self.__ListaPlantas),'plantas en el jardin ♣')
            print('╚════════════════════════════════════════════════════════════════════════════╝\n')
        for planta in self.__ListaPlantas:
            planta.MostrarPlanta()
        print('\n♣ • ♠ • ♠ • ♠ • ♠ • ♠ • ♣ • ♣ • ♠ • ♠ • ♠ • ♠ • ♠ • ♣ • ♠ • ♠ • ♣ • ♣ • ♣\n')
    def BuscarPlantaPorNombreComun(self, nombrecomun):
        listaencontrados = []
        for planta in self.__ListaPlantas:
            if (planta.GetNombreComun() == nombrecomun):
                listaencontrados = listaencontrados + [planta]
        return listaencontrados
    def BuscarPlantaPorNombreCientifico(self, nombrecientifico):
        listaencontrados = []
        for planta in self.__ListaPlantas:
            if (planta.GetNombreCientifico() == nombrecientifico):
                listaencontrados = listaencontrados + [planta]
        return listaencontrados
    def BorrarPlantaPorNombreComun(self, nombrecomun):
        listafinal = []
        for planta in self.__ListaPlantas:
            if (planta.GetNombreComun() != nombrecomun):
                listafinal = listafinal + [planta]
                valorfinal = len(self.__ListaPlantas)-len(listafinal)
                if (valorfinal==1):
                    print('╔════════════════════════════════════════════════════════════════════════════╗')
                    print('      INFO:',valorfinal,'planta ha sido retirada del jardin.')
                    print('╚════════════════════════════════════════════════════════════════════════════╝\n')
                else:
                    print('╔════════════════════════════════════════════════════════════════════════════╗')
                    print('     INFO:',valorfinal,'plantas han sido retiradas del jardin.')
                    print('╚════════════════════════════════════════════════════════════════════════════╝\n')

        self.__ListaPlantas = listafinal
    def BorrarPlantaPorNombreCientifico(self, nombrecientifico):
        listafinal = []
        for planta in self.__ListaPlantas:
            if (planta.GetNombreCientifico() != nombrecientifico):
                listafinal = listafinal +[planta]
                valorfinal = len(self.__ListaPlantas)-len(listafinal)
                if (valorfinal==1):
                    print('╔════════════════════════════════════════════════════════════════════════════╗')
                    print('     INFO: ',valorfinal,'plantas ha sido retirada del jardin.')
                    print('╚════════════════════════════════════════════════════════════════════════════╝\n')
                else:
                    print('╔════════════════════════════════════════════════════════════════════════════╗')
                    print('     INFO: ',valorfinal,'plantas han sido retiradas del jardin.')
                    print('╚════════════════════════════════════════════════════════════════════════════╝\n')
        self.__ListaPlantas = listafinal
    def ModoficarAtributo(self,nombrecomun):#,nombrecientifico,tipoplanta,riego,clima,usos):
        #listamodificada = []
        for planta in self.__ListaPlantas:
            if (planta.GetNombreComun() == nombrecomun):
                print('Se encontro el nombre comun de la planata')
            else:
                print('No se encontro el nombre comun de la planta.')

#------>Funciones Generales

def ObtenerOpcion(texto):
    leido = False
    while not leido:
        try:
            numero = int(input(texto))
        except ValueError:
            print('╔═════════════════════════════════════════════════════╗')
            print('║   ERROR: » Solo se admiten numeros como opciones. « ║')
            print('╚═════════════════════════════════════════════════════╝\n')
        else:
            leido = True
    return numero

def MostrarMenu():
    print('''\tM E N U
    1) M O S T R A R   P L A N T A S
    2) B U S C A R   P L A N T A S
    3) A G R E G A R  P L A N T A
    4) B O R R A R  P L A N T A
    5) A C T U A L I Z A R  D A T O S
    6) G U A R D A R  P L A N T A
    7) S A L I R''')

def BuscarPlanta(jardin):
    print('''\tM E N U
    1) N O M B R E  C O M U N
    2) N O M B R E  C I E N T I F I C O
    3) V O L V E R  A L  M E N U  P R I N C I P A L''')

    finbuscar = False
    while not finbuscar:
        opcbuscar = ObtenerOpcion('\nELIJA UNA OPCION A BUSCAR:\n')
        if opcbuscar == 1:
            encontrados = jardin.BuscarPlantaPorNombreComun(input('\nIntrodece el nombre comun de la planta:\n'))
            if(len(encontrados) > 0):
                print('\n♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ║ P L A N T A  E N C O N T R A D A ║ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣\n')
                for item in encontrados:
                    item.MostrarPlanta()
                print('\n♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣\n')
            else:
                print('\n')
                print('╔═════════════════════════════════════════════════════╗')
                print('║           INFO: Planta no encontrada                ║')
                print('╚═════════════════════════════════════════════════════╝\n')
            finbuscar = True
        elif opcbuscar == 2:
            encontrados = jardin.BuscarPlantaPorNombreCientifico(input('\nIntroduce el nombre cientifico de la planta:\n'))
            if(len(encontrados) > 0):
                print('\n♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ P L A N T A  E N C O N T R A D A ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣\n')
                for item in encontrados:
                    item.MostrarPlanta()
                print('\n♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣\n')
            else:
                print('\n')
                print('╔═════════════════════════════════════════════════════╗')
                print('║           INFO: Planta no encontrada                ║')
                print('╚═════════════════════════════════════════════════════╝\n')
            finbuscar = True
        elif opcbuscar == 3:
            finbuscar = True

def ProcesoAgregarPlanta(jardin):
    plantanueva = Planta()
    plantanueva.SetNombreComun(input(('>Introduce el nombre comun de la planta:\n')))
    plantanueva.SetNombreCientifico(input(('>Introduce el nombre cientifico de la planta:\n')))
    plantanueva.SetTipoPlanta(input(('>Introduce el tipo de planta:\n')))
    plantanueva.SetRiego(input(('>Indica la frecuencia de riego de la planta:\n')))
    plantanueva.SetClima(input(('>Indica el clima adecuado para la planta:\n')))
    plantanueva.SetUsos(input(('>Indica los usos de la planta:\n')))
    jardin.CrearNuevaPlanta(plantanueva)

def BorrarPlanta(jardin):
    print('''\tBUSCAR PLANTA A BORRAR POR:
    1) N O M B R E  C O M U N
    2) N O M B R E  C I E N T I F I C O
    3) V O L V E R''')

    finbuscar = False
    while not finbuscar:
        opcbuscar = ObtenerOpcion('\nElige una opcion para borrar:\n')
        if opcbuscar == 1:
            jardin.BorrarPlantaPorNombreComun(input(('\nIntroduce el nombre comun de la planta a borrar:\n')))
            print('╔════════════════════════════════════════════════════════════════╗')
            print('║    INFO: La planta se a eliminado exitosamente del jardin •    ║')
            print('╚════════════════════════════════════════════════════════════════╝\n')
            finbuscar = True
        elif opcbuscar == 2:
            jardin.BorrarPlantaPorNombreCientifico(input(('\nIntroduce el nombre cientifico de la planta a borrar\n')))
            print('╔════════════════════════════════════════════════════════════════╗')
            print('║    INFO: La planta se a eliminado exitosamente del jardin •    ║')
            print('╚════════════════════════════════════════════════════════════════╝\n')
            finbuscar = True
        elif opcbuscar == 3:
            finbuscar = True

def ActualizarDatos(planta):
    print('''\tATRIBUTOS A MODIFICAR:
    1)N O M B R E  C O M U N
    2)N O M B R E  C I E N T I F I C O
    3)T I P O  D E  P L A N T A
    4)R I E G O
    5)C L I M A
    6)U S O S
    7)S A L I R''')

    finactualizar = False
    while not finactualizar:
        opcbuscar = ObtenerOpcion('Elige un atributo a modificar:\n')
        if opcbuscar == 1:
            planta.ModoficarAtributo()

def Main():
    jardin = Jardin('jardin.txt')
    jardin.CargarPlantas()
    fin = False
    while not fin:
        MostrarMenu()
        opc = ObtenerOpcion('\nELIJE UNA OPCION:\n')
        if (opc == 1):
            jardin.MostrarJardin()
        elif (opc == 2):
            BuscarPlanta(jardin)
        elif (opc == 3):
            ProcesoAgregarPlanta(jardin)
        elif (opc == 4):
            BorrarPlanta(jardin)
        elif (opc == 5):
            ActualizarDatos(jardin)
        elif (opc == 6):
            jardin.GuardarPlantas()
        elif (opc == 7):
            fin = True

Main()
