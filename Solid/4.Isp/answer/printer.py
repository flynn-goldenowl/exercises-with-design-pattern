from abc import abstractmethod, ABC


class Machine(ABC):
    @abstractmethod
    def print(self, document: str) -> None:
        raise NotImplementedError


class OldFashionedPrinter(Machine):
    def print(self, document: str) -> None:
        print(f"Printing document: {document}")
        
class NewFashionedPrinter(Machine):
    def print(self, document: str) -> None:
        print(f"Printing document: {document}")

    def scan(self, document: str) -> None:
        print(f"Scanning document: {document}")

    def fax(self, document: str) -> None:
        print(f"Faxing document: {document}")
        
