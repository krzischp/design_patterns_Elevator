#### Singleton com os tipos de status
class TipoState:
    def __init__(self):
        self.paradoNoAndar = ParadoNoAndar()
        self.subindo = Subindo()
        self.descendo = Descendo()
        self.emperrado = Emperrado()
        self.emManutencao = EmManutencao()


#### O state basico
class ElevadorState(object):
    def sensorAndarAtivado(self) -> None:
        """
        Sensor que detecta quando o elevador chegou no andar do objetivo.
        Vale True quando atingiu o andar do objetivo.
        """
        raise NotImplementedError

    
    def sensorQuebradoAtivado(self) -> None:
        """
        Sensor que indica se o elevador é quebrado.
        Vale True quando quebrado.
        """
        raise NotImplementedError


    def pressionarBotaoExterno(self, andar: int) -> None:
        raise NotImplementedError


    def movimentar(self) -> None:
        raise NotImplementedError


    def tocarMusica(self) -> None:
        raise NotImplementedError


    def pararElevador(self) -> None:
        raise NotImplementedError


    def ligarEquipeManutencao(self) -> None:
        raise NotImplementedError


#### Os tipos de elevador
class Elevador(object):
    def __init__(self):
        """
        andar: 
            - o numero do andar onde o elevador esta parado
            - ou o numero do andar de onde o elevador vem, se o elevador estiver em movimento
        """
        raise NotImplementedError


    def sensorAndarAtivado(self):
        """
        Sensor que detecta quando o elevador chegou no andar do objetivo.
        Vale True quando atingiu o andar do objetivo.
        """
        raise NotImplementedError

    
    def sensorQuebradoAtivado(self):
        """
        Sensor que indica se o elevador é quebrado.
        Vale True quando quebrado.
        """
        raise NotImplementedError


    def pressionarBotaoExterno(self, andar: int):
        raise NotImplementedError


    def movimentar(self) -> None:
        raise NotImplementedError


    def tocarMusica(self):
        raise NotImplementedError


    def pararElevador(self):
        raise NotImplementedError


    def ligarEquipeManutencao(self):
        raise NotImplementedError


class ElevadorSocial(Elevador):
    def __init__(self, tipoState: TipoState, andar: int, currentState: ElevadorState, previousState: ElevadorState):
        """
        andar: 
            - o numero do andar onde o elevador esta parado
            - ou o numero do andar de onde o elevador vem, se o elevador estiver em movimento
        """
        self.tipoState = tipoState
        self.andar = andar
        self._currentState = currentState
        self._previousState = previousState


    def sensorAndarAtivado(self):
        """
        Sensor que detecta quando o elevador chegou no andar do objetivo.
        Vale True quando atingiu o andar do objetivo.
        """
        self._currentState.sensorAndarAtivado()

    
    def sensorQuebradoAtivado(self):
        """
        Sensor que indica se o elevador é quebrado.
        Vale True quando quebrado.
        """
        self._currentState.sensorQuebradoAtivado()


    def pressionarBotaoExterno(self, andar: int):
        self._currentState.pressionarBotaoExterno()


    def movimentar(self) -> None:
        self._currentState.movimentar()


    def tocarMusica(self):
        self._currentState.tocarMusica()


    def pararElevador(self):
        self._currentState.pararElevador()


    def ligarEquipeManutencao(self):
        self._currentState.ligarEquipeManutencao()



class ElevadorDeServico(Elevador):
    def __init__(self, tipoState: TipoState, andar: int, currentState: ElevadorState, previousState: ElevadorState):
        """
        andar: 
            - o numero do andar onde o elevador esta parado
            - ou o numero do andar de onde o elevador vem, se o elevador estiver em movimento
        """
        self.tipoState = tipoState
        self.andar = andar
        self._currentState = currentState
        self._previousState = previousState


    def sensorAndarAtivado(self):
        """
        Sensor que detecta quando o elevador chegou no andar do objetivo.
        Vale True quando atingiu o andar do objetivo.
        """
        self._currentState.sensorAndarAtivado()

    
    def sensorQuebradoAtivado(self):
        """
        Sensor que indica se o elevador é quebrado.
        Vale True quando quebrado.
        """
        self._currentState.sensorQuebradoAtivado()


    def pressionarBotaoExterno(self, andar: int):
        self._currentState.pressionarBotaoExterno()


    def movimentar(self) -> None:
        self._currentState.movimentar()


    def tocarMusica(self):
        self._currentState.tocarMusica()


    def pararElevador(self):
        self._currentState.pararElevador()


    def ligarEquipeManutencao(self):
        self._currentState.ligarEquipeManutencao()


#### Os states

class ParadoNoAndar(ElevadorState):
    def __init__(self) -> None:
        super().__init__()
    

    def sensorAndarAtivado(self, elevador: Elevador):
        """
        Sensor que detecta quando o elevador chegou no andar do objetivo.
        Vale True quando atingiu o andar do objetivo.
        """
        pass

    
    def sensorQuebradoAtivado(self, elevador: Elevador):
        """
        Sensor que indica se o elevador é quebrado.
        Vale True quando quebrado.
        """
        pass


    def pressionarBotaoExterno(self, andar: int, elevador: Elevador) -> None:
        """
        andar: o numero do andar onde o botao externo foi pressionado
        """
        if elevador.sensorQuebradoAtivado():
            elevador.setCurrentState(elevador.tipoState.emperrado)
            elevador.ligarEquipeManutencao()
        else:
            direcao = andar - elevador.getAndar()
            if direcao > 0:
                elevador.setCurrentState(elevador.tipoState.subindo)
            elif direcao < 0:
                elevador.setCurrentState(elevador.tipoState.descendo)
            else:
                elevador.setCurrentState(self)
            elevador.setPreviousState(self)
            elevador.setAndar(andar)
            elevador.movimentar()


    def movimentar(self):
        pass


    def tocarMusica(self):
        pass


    def pararElevador(self):
        pass


    def ligarEquipeManutencao(self):
        pass


class Subindo(ElevadorState):
    def __init__(self) -> None:
        super().__init__()
    

    def sensorAndarAtivado(self, elevador: Elevador):
        """
        Sensor que detecta quando o elevador chegou no andar do objetivo.
        Vale True quando atingiu o andar do objetivo.
        """
        pass

    
    def sensorQuebradoAtivado(self, elevador: Elevador):
        """
        Sensor que indica se o elevador é quebrado.
        Vale True quando quebrado.
        """
        pass


    def pressionarBotaoExterno(self, andar: int, elevador: Elevador):
        """
        Consideramos o caso mais simples sem fila de prioridade dos andares onde o botao externo foi pressionado.
        Ou seja, o elevador so toma a solicitaçao em consideraçao quando ele estiver parado e funcionando
        """
        pass


    def movimentar(self, elevador: Elevador):
        """
        a açao de se movimentar: descer quando o estado é Descendo e subir quando o estado é Subindo
        """
        parar = False
        while not parar:
            if elevador.sensorQuebradoAtivado():
                elevador.setCurrentState(elevador.tipoState.emperrado)
                parar = True
            elif elevador.sensorAndarAtivado():
                elevador.setCurrentState(elevador.tipoState.paradoNoAndar)
                parar = True
            else:
                elevador.setCurrentState(elevador.tipoState.subindo)
            elevador.setPreviousState(self)
            elevador.movimentar()


    def tocarMusica(self):
        pass


    def pararElevador(self):
        pass


    def ligarEquipeManutencao(self):
        pass


class Descendo(ElevadorState):
    def __init__(self) -> None:
        super().__init__()


    def sensorAndarAtivado(self, elevador: Elevador):
        """
        Sensor que detecta quando o elevador chegou no andar do objetivo.
        Vale True quando atingiu o andar do objetivo.
        """
        pass

    
    def sensorQuebradoAtivado(self, elevador: Elevador):
        """
        Sensor que indica se o elevador é quebrado.
        Vale True quando quebrado.
        """
        pass


    def pressionarBotaoExterno(self, andar: int, elevador: Elevador) -> None:
        """
        Consideramos o caso mais simples sem fila de prioridade dos andares onde o botao externo foi pressionado.
        Ou seja, o elevador so toma a solicitaçao em consideraçao quando ele estiver parado e funcionando
        """
        pass


    def movimentar(self, elevador: Elevador):
        """
        a açao de se movimentar: descer quando o estado é Descendo e subir quando o estado é Subindo
        """
        parar = False
        while not parar:
            if elevador.sensorQuebradoAtivado():
                elevador.setCurrentState(elevador.tipoState.emperrado)
                parar = True
            elif elevador.sensorAndarAtivado():
                elevador.setCurrentState(elevador.tipoState.paradoNoAndar)
                parar = True
            else:
                elevador.setCurrentState(elevador.tipoState.descendo)
            elevador.setPreviousState(self)
            elevador.movimentar()


    def tocarMusica(self):
        pass


    def pararElevador(self):
        pass


    def ligarEquipeManutencao(self):
        pass


class Emperrado(ElevadorState):
    def __init__(self) -> None:
        super().__init__()


    def sensorAndarAtivado(self, elevador: Elevador):
        """
        Sensor que detecta quando o elevador chegou no andar do objetivo.
        Vale True quando atingiu o andar do objetivo.
        """
        pass

    
    def sensorQuebradoAtivado(self, elevador: Elevador):
        """
        Sensor que indica se o elevador é quebrado.
        Vale True quando quebrado.
        """
        pass


    def pressionarBotaoExterno(self, andar: int, elevador: Elevador) -> None:
        pass


    def movimentar(self, elevador: Elevador):
        pass

    def tocarMusica(self):
        print("Tocando musica")


    def pararElevador(self):
        print("Parando o elevador")


    def ligarEquipeManutencao(self, elevador: Elevador):
        elevador.pararElevador()
        elevador.tocarMusica()
        elevador.setCurrentState(EmManutencao())
        # passar o estado anterior Descendo ou Subindo
        elevador.setPreviousState(self.getPreviousState())
        elevador.movimentar()


class EmManutencao(ElevadorState):
    def __init__(self) -> None:
        super().__init__()


    def sensorAndarAtivado(self, elevador: Elevador):
        """
        Sensor que detecta quando o elevador chegou no andar do objetivo.
        Vale True quando atingiu o andar do objetivo.
        """
        pass

    
    def sensorQuebradoAtivado(self, elevador: Elevador):
        """
        Sensor que indica se o elevador é quebrado.
        Vale True quando quebrado.
        """
        pass


    def pressionarBotaoExterno(self, andar: int, elevador: Elevador) -> None:
        pass


    def movimentar(self, elevador: Elevador):
        """
        a açao de se movimentar: descer quando o estado é Descendo e subir quando o estado é Subindo
        """
        parar = True
        while parar:
            if not elevador.sensorQuebradoAtivado():
                parar = False
                if elevador.getPreviousState().indexOf("Subindo"):
                    elevador.setCurrentState(elevador.tipoState.subindo)
                if elevador.getPreviousState().indexOf("Descendo"):
                    elevador.setCurrentState(elevador.tipoState.descendo)
                elevador.setPreviousState(self)
                elevador.movimentar()


    def tocarMusica(self):
        pass


    def pararElevador(self):
        pass


    def ligarEquipeManutencao(self, elevador: Elevador):
        pass


#### Factory
class ElevadorFactory(object):
    def createElevador(self) -> Elevador:
        raise NotImplementedError


class ElevadorSocialFactory(ElevadorFactory):
    def createElevador(self) -> Elevador:
        tipoState = TipoState()
        andar = 0,
        currentState = tipoState.paradoNoAndar
        previousState = tipoState.paradoNoAndar
        return ElevadorSocial(tipoState, andar, currentState, previousState)


class ElevadorDeServicoFactory(ElevadorFactory):
    def createElevador(self) -> Elevador:
        tipoState = TipoState()
        andar = 0,
        currentState = tipoState.paradoNoAndar
        previousState = tipoState.paradoNoAndar
        return ElevadorDeServico(tipoState, andar, currentState, previousState)



#### Observers

## Subject: sistema elevador, e observers
class SistemaElevador:
    def attach(self) -> None:
        raise NotImplementedError
    
    def detach(self) -> None:
        raise NotImplementedError

    def notify(self) -> None:
        raise NotImplementedError


class ElevadorObserver(object):
    def acionarElevador(self, sistemaElevador: SistemaElevador):
        raise NotImplementedError



from typing import List
class SistemaElevadorInteligente:
    def __init__(self, elevadores: List[Elevador], elevadorObservers: List[ElevadorObserver]):
        self.elevadores = elevadores
        self.elevadorObservers = elevadorObservers

    def attach(self, elevadorObserver: ElevadorObserver) -> None:
        self.elevadorObservers.append(elevadorObserver)
    
    def detach(self, elevadorObserver: ElevadorObserver) -> None:
        self.elevadorObservers.remove(elevadorObserver)

    def notify(self) -> None:
        for elevadorObserver in self.elevadorObservers:
            elevadorObserver.movimentarElevadores(self)
    
    def mandarProsAndares(self, listaTipoAndares):
        for tipo, andar in listaTipoAndares:
            if tipo == "social":
                for elevador in self.elevadores:
                    if isinstance(elevador, ElevadorSocial):
                        if elevador.getCurrentState().indexOf("ParadoNoAndar"):     
                            elevador.pressionarBotaoExterno(andar)
                        else:
                            elevador.updateListEspera(andar)
            if tipo == "servico":
                for elevador in self.elevadores:
                    if isinstance(elevador, ElevadorDeServico):
                        if elevador.getCurrentState().indexOf("ParadoNoAndar"):     
                            elevador.pressionarBotaoExterno(andar)
                        else:
                            elevador.updateListEspera(andar)


class ElevadorSocialObserver(ElevadorObserver):
    def movimentarElevadores(self, sistemaElevador: SistemaElevador):
        # checa a quantidade de elevadores sociais disponiveis
        if len(sistemaElevador.elevadores) >= 1:
            for elevador in sistemaElevador.elevadores:
                if isinstance(elevador, ElevadorSocial) and elevador.getCurrenState().indexOf("ParadoNoAndar") and elevador.listaEspera:
                    andar = elevador.listaEspera.pop()
                    elevador.pressionarBotaoExterno(andar)


class ElevadorDeServicoObserver(ElevadorObserver):
    def movimentarElevadores(self, sistemaElevador: SistemaElevador):
        # checa a quantidade de elevadores de servico disponiveis
        if len(sistemaElevador.elevadores) >= 1:
            for elevador in sistemaElevador.elevadores:
                if isinstance(elevador, ElevadorDeServico) and elevador.getCurrenState().indexOf("ParadoNoAndar") and elevador.listaEspera:
                    andar = elevador.listaEspera.pop()
                    elevador.pressionarBotaoExterno(andar)


#### Sistema elevador factory
class SistemaElevadorFactory:
    def createSistemaElevador(self) -> SistemaElevador:
        raise NotImplementedError


class SistemaElevadorInteligenteFactory(SistemaElevadorFactory):
    def createSistemaElevador(self) -> SistemaElevador:
        sistemaElevador = SistemaElevadorInteligente()
        sistemaElevador.setElevadores(
            [ElevadorSocialFactory().createElevador()] * 3 + [ElevadorDeServicoFactory().createElevador()] * 2
        )
        return sistemaElevador


if __name__ == "__main__":
    # Imaginamos o caso simples seguinte:
    # Um outro sistema consegue pegar os sinais de botoes pressionados, assim que o perfil do usuario que pressionou:
    # se ele for um morador do predio (precisa pegar o elevador social) ou um funcionario (precisa pegar o elevador de servico).
    # Via uma API, a gente recupera essa lista de tuples com os valores de andar e perfil de usuario.
    # A partir dessa lista, a gente consegue acionar o nosso sistema inteligente:
    # O sistema inteligente manda os elevadores adequados para os andares especificados na lista.
    # Podemos ser confrontados a um problema:
    # Caso nao tiver elevador disponivel (ou seja, no estado ParadoNoAndar) para um andar da lista, entao tem que armazenar esse andar em um lista de
    # espera do elevador solicitado.
    # Por isso, precisamos de Observer para monitorar os elevadores, para que assim que eles ficam disponiveis, eles começam a consumir a fila de espera respeitiva deles.
    # Pra isso, o nosso codigo cliente pode chamar a funcionalidade notify do nosso sistema De 5 em 5 minutos.
    # Quando chamar notify, ele olha pra fila de espera de cada elevador disponivel e, altera o estado do elevador para ele se movimentar pro primeiro andar da fila.
    elevadorSocialObserver = ElevadorSocialObserver()
    elevadorDeServicoObserver = ElevadorDeServicoObserver()

    sistemaElevadorInteligente = SistemaElevadorInteligenteFactory().createSistemaElevador()
    sistemaElevadorInteligente.attach(elevadorSocialObserver)
    sistemaElevadorInteligente.attach(elevadorDeServicoObserver)

    sistemaElevadorInteligente.mandarProsAndares([("social", 3), ("social", 5), ("servico", 6)])
    #### a partir de agora, o codigo cliente pode chamar notify de 5 em 5 minutos por ex, para atender quem nao teve um elevador disponivel quando apertou no botao
    # esperar 5 minutos
    sistemaElevadorInteligente.notify()
    # esperar 5 minutos
    sistemaElevadorInteligente.notify()
    # esperar 5 minutos
    sistemaElevadorInteligente.notify()
