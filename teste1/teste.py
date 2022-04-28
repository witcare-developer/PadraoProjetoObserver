'''
Uma demonstração de como o Padrão Observer poderia ser codificado em um modo "pythonico",
com __setattr__ no subject override para atualizar o observer.
'''
from abc import ABC, abstractmethod

class Subject(object):
    """
    Mantém uma lista de observers e notifica as mudanças de estado.
    """
    def __init__(self):
        """
        Inicializa uma lista de observers.
        """
        self.__dict__['state'] = 0
        self.__dict__['observers'] = set()

    def __setattr__(self, name, value):
        """
        Sobreescreve notificação
        """
        self.__dict__[name] = value
        if name == 'state':
            self.notify_observers()

    def register(self, observer):
        """
        Add an observer to the list of observers
        to be notified of state changes.
        """
        self.observers.add(observer)

    def deregister(self, observer):
        """
        Remove an observer.
        """
        self.observers.remove(observer)

    def notify_observers(self):
        """
        Iterate through observers an call the update() method on each one.
        """
        for observer in self.observers:
            observer.update()

    # Create an abstract base class for and concrete classes for observer.

class Observer(object):
    """
    Abstract class to response to changes in the subject.
    """
    @abstractmethod
    def update(self):
        """
        Update observer state.
        """
        raise NotImplementedError("update() is not implemented.")

class BinaryObserver(Observer):
    """
    Observer tht prints subject state in binary.
    """
    def __init__(self, subject):
        """
        Keep a reference to the subject.
        """
        self.subject = subject
        self.subject.register(self)

    def update(self):
        print("\t em binário: " + bin(self.subject.state))

class HexadecimalObserver(Observer):
    """
    Observer tht prints subject state in Hexa.
    """
    def __init__(self, subject):
        """
        Keep a reference to the subject.
        """
        self.subject = subject
        self.subject.register(self)

    def update(self):
        print("\t em hexadecimal: " + hex(self.subject.state))

def main():
    """
    Test the observer pattern implementation
    """
    subject = Subject()
    BinaryObserver(subject)
    HexadecimalObserver(subject)

    print("\nPrimeira mudança de estado:")
    subject.state = 1024

    print("\nSegunda mudança de estado:")
    subject.state = 255

if __name__ == '__main__':
    main()