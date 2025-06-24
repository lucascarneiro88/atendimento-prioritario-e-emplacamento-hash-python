# Exigencia de código 1 de 7
# Implementar lista encadeada simples para pacientes

# Cartão / Paciente / Nodo
class Patient:
    def __init__(self, number, color):
        self.number = number
        self.color = color
        self.next = None  # Referência para o próximo paciente na lista

# Lista encadeada simples para pacientes
class PatientList:
    def __init__(self):
        self.head = None
        self.number_card_green = 1
        self.number_card_yellow = 201