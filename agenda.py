


class Agenda:
    def __init__(self,nome,carro,dias_da_semana,horario):
        self.nome = nome
        self.carro= carro
        self.semana = ["segunda","terca","quarta","quinta","sexta","sabado"]
        if dias_da_semana in self.semana:
            self.dias_da_semana = dias_da_semana
        else:
            print("Não é possivél agendar neste dia")
        
        self.horas = ["7:30","8:30","9:30","10:30","11:30","13:00","14:00","15:00","16:00","17:00"]
        if horario in self.horas:
            self.horario = horario
        else:
            print("não há disponibilidade para este horário")
            
    def mudar_horario(self,novo_horario):
        if novo_horario in self.horas:
            self.horario = novo_horario
        else:
            print(f"{novo_horario} inválido")
    

        
        
            
            
cliente1 = Agenda("nicolas","gol","segunda","8:30")
print(cliente1.nome,cliente1.carro,cliente1.dias_da_semana,cliente1.horario)
cliente1.mudar_horario(input("digite o novo horário:"))
print(cliente1.nome,cliente1.carro,cliente1.dias_da_semana,cliente1.horario)
