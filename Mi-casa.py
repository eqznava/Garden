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
        print('Tipo de Planta',self.GetTipoPlanta())
        print('Riego',self.GetRiego())
        print('Clima:',self.GetClima())
        print('Usos:',self.GetUsos())
        print('\n♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣\n')

class Jardin:
    def __init__(self, path):
        self.__Path = path
        self.__ListaPlantas = []
    def CargarPlantas(self):
        try:
            archivo = open(self.__Path, 'r')
        except:
            print('ERROR: » El archivo que buscas no existe. «')
        else:
            plantas = archivo.readlines()
            archivo.close()
            if (len(plantas)>0):
                for planta in plantas:
                    datos = planta.split('■')
                    if(len(datos)==6):
                        plantanueva = Planta()
                        plantanueva = SetNombreComun([0])
                        plantanueva = SetNombreCientifico([1])
                        plantanueva = SetTipoPlanta([2])
                        plantanueva = SetRiego([3])
                        plantanueva = SetClima([4])
                        plantanueva = SetUsos([5])
                        self.__ListaPlantas = self.__ListaPlantas + [plantanueva]
                print('INFO:Se han cargado un total de',len(self.__ListaPlantas),'plantas.')
    def AgregarPlantaNueva(self, plantanueva):
        self.__ListaPlantas = self.__ListaPlantas + [plantanueva]
    def GuardarPlantas(self):
        try:
            archivo = open(self.__Path,'w')
        except:
            print('ERROR: » El Archivo que buscas no existe. «')
        else:
            for planta in self.__ListaPlantas:
                texto = planta.GetNombreComun() + '■'
                texto = texto + planta.GetNombreCientifico() + '■'
                texto = texto + planta.GetTipoPlanta() + '■'
                texto = texto + planta.GetRiego() + '■'
                texto = texto + planta.GetClima() + '■'
                texto = texto + planta.GetUsos() + '■'
                archivo.write(texto)
            archivo.close()
            print('INFO: Planta almacenada exitosamente ♣')
    def MostrarJardin(self):
        print('\n♣ • ♠ • ♠ • ♠ • ♠ • ♠ • ♣ • ♣ J A R D I N ♣ • ♠ • ♠ • ♠ • ♠ • ♠ • ♣ • ♣\n')
        print('Numero de Plantas en el jardin:',len(self.__ListaPlantas,'plantas'))
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
                print('INFO:',len(self.__ListaPlantas) - len(listafinal),'plantas han sido retiradas del jardin.')
        self.__ListaPlantas = listafinal
    def BorrarPlantaPorNombreCientifico(self, nombrecientifico):
        listafinal = []
        for planta in self.__ListaPlantas:
            if (planta.GetNombreCientifico() != nombrecientifico):
                listafinal = listafinal +[planta]
                print('INFO:',len(self.__ListaPlantas) - len(listafinal),'plantas han sido retiradas del jardin')
        self.__ListaPlantas = listafinal
        
#------>Funciones Generales

def ObtenerOpcion(texto):
    leido = False
    while not leido:
        try:
            numero = int(input(texto))
        except ValueError:
            print('ERROR: » Solo se admiten numero como opciones. «')
        else:
            leido = True
    return numero

def MostrarMenu():
    print('''M E N U
    1) M O S T R A R   P L A N T A S
    2) B U S C A R   P L A N T A S
    3) A G R E G A R  P L A N T A
    4) B O R R A R  P L A N T A
    5) G U A R D A R  P L A N T A
    6) S A L I R''')

def BuscarPlanta(jardin):
    print('''M E N U
    1) N O M B R E  C O M U N
    2) N O M B R E  C I E N T I F I C O
    3) V O L V E R  A L  M E N U  P R I N C I P A L''')

    finbuscar = False
    while not finbuscar:
        opcbuscar = ObtenerOpcion('\nElija una opcion para buscar:\n')
        if opcbuscar == 1:
            encontrados = jardin.BuscarPlantaPorNombreComun(input('\nIntrodece el nombre comun de la planta:\n'))
            if(len(encontrados) > 0):
                print('\n♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ P L A N T A  E N C O N T R A D A ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣\n')
                for item in encontrados:
                    item.MostrarPlanta()
                print('\n♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣\n')
            else:
                print('INFO: Planta no encontrada')
            finbuscar = True
        elif opcbuscar == 2:
            encontrados = jardin.BuscarPlantaPorNombreCientifico(input('\nIntroduce el nombre cientifico de la planta:\n'))
            if(len(encontrados) > 0):
                print('\n♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ P L A N T A  E N C O N T R A D A ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣\n')
                for item in encontrados:
                    item.MostrarPlanta()
                print('\n♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣ ♣\n')
            else:
                print('INFO: Planta no encontrada')
            finbuscar = True
        elif opcbuscar == 3:
            finbuscar = True

def PorcesoAgregarPlanta(jardin):
    plantanueva = Planta()
    plantanueva.SetNombreComun('Introduce el nombre comun de la planta:\n')
    plantanueva.SetNombreCientifico('Introduce el nombre cientifico de la planta:\n')
    plantanueva.SetTipoPlanta('Introduce el tipo de planta:\n')
    plantanueva.SetRiego('Indica la frecuencia de riego de la planta:\n')
    plantanueva.SetClima('Indica el clima adecuado para la planta:\n')
    plantanueva.SetUsos('Indica los usos de la planta:\n')
    jardin.AgregarPlantaNueva(plantanueva)

def BorrarPlanta(jardin):
    print('''Buscar planta a borrar por:
    1) N O M B R E  C O M U N
    2) N O M B R E  C I E N T I F I C O
    3) V O L V E R''')

        finbuscar = False
        while not finbuscar:
            opcbuscar = ObtenerOpcion('\nElige una opcion para borrar:\n')
            if opcbuscar == 1:
                jardin.BorrarPlantaPorNombreComun('\nIntroduce el nombre comun de la planta a borrar:\n')
                finbuscar = True
            elif opcbuscar == 2:
                jardin.BorrarPlantaPorNombreCientifico()
