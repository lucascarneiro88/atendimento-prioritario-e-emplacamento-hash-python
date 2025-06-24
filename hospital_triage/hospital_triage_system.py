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


# Exigência de código 2 de 7
# Implementar função para add pacientes sem prioridade à lista
# inserir no final da lista

    def insertWithoutPriority(self, patient):
        if not self.head:
            self.head = patient
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = patient

# Exigência de código 3 de 7
# Implementar função para add pacientes com prioridade a lista
# inserir após todos os nodos(pacientes) com prioridade( cartão amarelo - A ) mas sempre antes dos pacientes sem prioridade (cartão verde - V)

def insertWithPriority(self, patient):
    if not self.head or self.head.color == 'V':
        patient.next = self.head
        self.head = patient
    else:
        current = self.head
        while current.next and current.next.color == 'A':
            current = current.next
        patient.next = current.next
        current.next = patient

    

   