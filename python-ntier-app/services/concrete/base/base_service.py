from typing import TypeVar, Generic,Iterable
from fastapi import HTTPException
from data_access.repositories.concrete.base.base_repository import BaseRepository
from services.abstract.base.base_service_interface import IBaseService

TSchemaInput = TypeVar('TSchemaInput')
TSchemaOutput = TypeVar('TSchemaOutput')
TModel = TypeVar('TModel')

class BaseService(Generic[TSchemaInput, TSchemaOutput],IBaseService[TSchemaInput, TSchemaOutput]):
    def __init__(self, repository: BaseRepository[TModel]):
        self.repository = repository

    def create(self, data: TSchemaInput) -> TSchemaOutput:
        try:
            return self.repository.create(data)
        except Exception as ex:
            raise ex

    def get_all(self) -> Iterable[TSchemaOutput]:
        try:
            return self.repository.get_all()
        except Exception as ex:
            raise ex

    def delete(self, id: int) -> bool:
        try:
            if not self.repository.exists_by_id(id):
                raise HTTPException(status_code=404, detail=f"{self.repository.model_class.__name__} not found")
            instance = self.repository.get_by_id(id)
            self.repository.delete(instance)
            return True
        except Exception as ex:
            raise ex

    def update(self, id: int, data: TSchemaInput) -> TSchemaOutput:
        try:
            if not self.repository.exists_by_id(id):
                raise HTTPException(status_code=404, detail=f"{self.repository.model_class.__name__} not found")
            instance = self.repository.get_by_id(id)
            return self.repository.update(instance, data)
        except Exception as ex:
            raise ex
    
    def get_by_id(self, id: int) -> TSchemaOutput:
        try:
            if not self.repository.exists_by_id(id):
                raise HTTPException(status_code=404, detail=f"{self.repository.model_class.__name__} not found")
            return self.repository.get_by_id(id)
        except Exception as ex:
            raise ex