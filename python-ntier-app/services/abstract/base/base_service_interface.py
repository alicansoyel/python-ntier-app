from typing import TypeVar, Generic,Iterable
from abc import ABC,abstractmethod

TSchemaInput = TypeVar('TSchemaInput')
TSchemaOutput = TypeVar('TSchemaOutput')

class IBaseService(ABC,Generic[TSchemaInput, TSchemaOutput]):
    @abstractmethod
    def create(self, data: TSchemaInput) -> TSchemaOutput:
        pass
    @abstractmethod
    def get_all(self) -> Iterable[TSchemaOutput]:
        pass
    @abstractmethod
    def delete(self, id: int) -> bool:
        pass
    @abstractmethod
    def update(self, id: int, data: TSchemaInput) -> TSchemaOutput:
        pass
    @abstractmethod
    def get_by_id(self, id: int) -> TSchemaOutput:
        pass