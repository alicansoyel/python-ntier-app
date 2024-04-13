from typing import TypeVar, Generic,Iterable
from abc import ABC,abstractmethod

TModel = TypeVar('TModel')

class IBaseRepository(Generic[TModel],ABC):
    @abstractmethod
    def create(self, data: TModel) -> TModel:
        pass
    @abstractmethod
    def get_all(self) -> Iterable[TModel]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> TModel:
        pass

    @abstractmethod
    def exists_by_id(self, id: int) -> bool:
        pass

    @abstractmethod
    def update(self, instance: TModel, data: TModel) -> TModel:
        pass

    @abstractmethod
    def delete(self, instance: TModel) -> bool:
        pass

