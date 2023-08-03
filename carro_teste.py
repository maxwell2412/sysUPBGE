from bge import logic as g, events
from bge import constraints as pc
import math
from bge.types import *


def main(cont):
    # type: (SCA_PythonController) -> None
    own = cont.owner  # type: KX_GameObject
    cenaAtual = g.getCurrentScene()
    print("pegou a cena e o own")
    rodas_carro = []
    grupo = own.groupObject
    objGrupo = grupo.groupMembers
    for obj in objGrupo:
        if "roda" in obj.getPropertyNames():
            rodas_carro.append(obj)
        if "volante" in obj.getPropertyNames():
            volante_carro = obj
        if "cam_car" in obj.getPropertyNames():
            cam_car = obj
        if "porta_dir" in obj.getPropertyNames():
            porta_dir = obj
        if "porta_esq" in obj.getPropertyNames():
            porta_esq = obj
        if "lugar_esq" in obj.getPropertyNames():
            lugar_esq = obj
        if "lugar_dir" in obj.getPropertyNames():
            lugar_dir = obj

    print(rodas_carro)
    sensor = cont.sensors[0]
    print("pegou o sensor ", sensor)
    # ao iniciar o jogo vamos transformar o objeto carro em uma instancia da classe
    if sensor.positive:
        print("sensor ativado!")
        own = Car(own, rodas_carro)
        print("objeto carro criado !")
        # instanciamos o obj a partir da classe Car que herda da KX_GameObject
        own.initCar(own)
        print("objeto carro iniciado !")

        #own.update()  # chamando a função que roda sempre 


class Car(KX_GameObject):

    def __init__(self, car, rodas_carro, volante_carro, cam_car, porta_dir, porta_esq, lugar_esq, lugar_dir comprimento_suspensao=0.5, raio_roda=0.72, raio_roda_2= 0.72, distancia_eixo=1.75,
                 roda_dianteira_pos=3.35, roda_traseira_pos=-3.35, influencia=0.25, rigidez=30.0, amortecimento=60.0,
                 compressao=1.5, atrito=3, altura_local=-0.7, estabilidade=0.1):
        #variaveis de obj do grupo 
        self.rodas = rodas_carro
        self.car = car
        self.volante = volante
        self.cam = cam_car
        self.porta_dir = porta_dir
        self.porta_esq = porta_esq
        self.lugar_dir = lugar_dir
        self.lugar_esq = lugar_esq
        #propriedades de constraints
        self.comprimento_suspensao = comprimento_suspensao
        self.raio_roda = raio_roda
        self.raio_roda_2 = raio_roda_2
        self.distancia_eixo = distancia_eixo
        self.roda_dianteira_pos = roda_dianteira_pos
        self.roda_traseira_pos = roda_traseira_pos
        self.influencia = influencia
        self.rigidez = rigidez
        self.amortecimento = amortecimento
        self.compressao = compressao
        self.atrito = atrito
        self.altura_local = altura_local
        self.estabilidade = estabilidade

    def initCar(self, car):
        print("iniciou o carro")
        wheelAttachDirLocal = [0, 0, -1]  # direção da roda Z
        wheelAxeleLocal = [-1, 0, 0]  # eixo da roda X
        print(car.getPhysicsId())
        vehicle = pc.createVehicle(car.getPhysicsId())
        car['cid'] = vehicle.getConstraintId()
        vehicle = pc.getVehicleConstraint(car['cid'])
        car['ds'] = 0.0
        for indice, roda in enumerate(self.rodas, start=0):
            #traseira fd=+,fe=- 1
            if "fd" in roda.getPropertyNames():
                wheelAttachPosLocal = [self.distancia_eixo, self.roda_dianteira_pos, self.altura_local]
                vehicle.addWheel(roda, wheelAttachPosLocal, wheelAttachDirLocal, wheelAxeleLocal,
                                 self.comprimento_suspensao, self.raio_roda, 1)
            elif "fe" in roda.getPropertyNames():
                wheelAttachPosLocal = [-self.distancia_eixo, self.roda_dianteira_pos, self.altura_local]
                vehicle.addWheel(roda, wheelAttachPosLocal, wheelAttachDirLocal, wheelAxeleLocal,
                                 self.comprimento_suspensao, self.raio_roda, 1)
            elif "td" in roda.getPropertyNames():
                wheelAttachPosLocal = [self.distancia_eixo, self.roda_traseira_pos, self.altura_local]
                vehicle.addWheel(roda, wheelAttachPosLocal, wheelAttachDirLocal, wheelAxeleLocal,
                                 self.comprimento_suspensao, self.raio_roda_2, 0)
            elif "te" in roda.getPropertyNames():
                wheelAttachPosLocal = [-self.distancia_eixo, self.roda_traseira_pos, self.altura_local]
                vehicle.addWheel(roda, wheelAttachPosLocal, wheelAttachDirLocal, wheelAxeleLocal,
                                 self.comprimento_suspensao, self.raio_roda_2, 0)
            

            print(roda, indice)
            vehicle.setRollInfluence(self.influencia, indice)
            vehicle.setSuspensionStiffness(self.rigidez, indice)
            vehicle.setSuspensionDamping(self.amortecimento, indice)
            vehicle.setTyreFriction(self.atrito, indice)
            vehicle.setSuspensionCompression(self.compressao, indice)
            print(f"o indice {indice} e a roda {roda}")
    def ligar_carro():
        pass
    def desligar_carro():
        pass
    def motorista_on():
        pass
    def carro_trancado():
        pass
    def lugares_carro():
        pass
    def update(self):
        pass
