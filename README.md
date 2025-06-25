# Sistemas de Triagem Hospitalar em Python


## Visão Geral

Este repositório contém um projeto em Python desenvolvido para uma tarefa da faculdade com foco em estruturas de dados:

1. **Sistema de Triagem Hospitalar**  
   Implementação de uma fila de prioridade usando lista encadeada simples para gerenciar a triagem de pacientes com base na cor e número do cartão.
---

### Exigência de código 1 de 7
- Implementar lista encadeada simples.
- O Nodo representa um cartão numerado contendo: número, cor e um ponteiro para o próximo paciente.
- A lista é não circular ( o último elemento aponta para None).

### Cartão / Paciente / Nodo

```python
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
  ```


- Aqui temos a definição do *Nodo* com três atributos obrigatórios e o inicio da *ListaEncadeada* com o ponteiro para a cabeça(head).

- **Nodo(nó):** Representa um elemento (Paciente) da lista, em estrutura de dados um *nodo* é uma célula de uma estrutura encadeada que guarda um valor e também uma referência para outro(próximo)nodo.



### Exigência de código 2 de 7
- Implementar função para adicionar pacientes sem prioridade à lista.
- O paciente deve ser inserido no **final da lista**.

### Função `insertWithoutPriority`

```python
def insertWithoutPriority(self, patient):
    if not self.head:
        self.head = patient
    else:
        current = self.head
        while current.next:
            current = current.next
        current.next = patient
```


### Exigência de código 3 de 7
- Implementar função para adicionar pacientes com prioridade à lista.
- O paciente com prioridade (cartão amarelo - "A") deve ser inserido **após todos os pacientes com prioridade já existentes**, mas sempre **antes dos pacientes sem prioridade** (cartão verde - "V").

### Função `insertWithPriority`

```python
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
```