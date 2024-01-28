class Elevador:
    _total_capacidade = 0
    _atual_capacidade = 0
    _total_andar = 0
    _atual_andar = 0

    def __init__(self, total_capacidade:int, atual_capacidade: int, total_andar: int, atual_andar: int) -> None:
        self._total_capacidade = total_capacidade
        self._atual_capacidade = atual_capacidade
        self._total_andar = total_andar
        self._atual_andar = atual_andar

    def __repr__(self) -> str:
        return f"Capacidade total: {self._total_capacidade}\
            \nTotal de andares: {self._total_andar}\
            \nAtual capacidade: {self._atual_capacidade}\
            \nAndar Atual: {self._atual_andar}"
    
    def get_capatidade_total(self) -> int:
        return self._total_capacidade
    
    def get_andar_atual(self) -> int:
        return self._atual_andar
    
    def entrar(self) -> None:
        if self._atual_capacidade < self._total_capacidade:
            print("Entrando uma pessoa")
            self._atual_capacidade +=1
        else:
            print("O ELEVADOR ESTÁ CHEIO")
            
    def sair(self) -> None:
        if self._atual_capacidade > 0:
            print("Saindo uma pessoa")
            self._atual_capacidade -= 1 
        else:
            print("NÂO TEM NINGUÉM")

    def subir(self) -> None:
        if self._atual_andar < self._total_andar:
            print("Subindo")
            self._atual_andar += 1
        else:
            print("VOCÊ ESTA NO ANDAR MAIS ALTO")

    def descer(self) -> None:
        if self._atual_andar > 0:
            print("Descendo")
            self._atual_andar -= 1
        else:
            print("VOCÊ JÁ ESTÁ NO TERREO")
    

   

