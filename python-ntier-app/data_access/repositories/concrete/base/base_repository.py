from typing import Iterable, Type, TypeVar, Generic
from sqlalchemy.orm import Session
from data_access.repositories.abstract.base.base_repository_interface import IBaseRepository

TModel = TypeVar('TModel')

class BaseRepository(Generic[TModel],IBaseRepository[TModel]):
    def __init__(self, session: Session, model_class: Type[TModel])->None:
        self.session = session
        self.model_class = model_class

    def create(self, data: TModel) -> TModel:
        instance = self.model_class(**data.model_dump(exclude_none=True))
        self.session.add(instance)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def get_all(self) -> Iterable[TModel]:
        return self.session.query(self.model_class).all()
        
    def get_by_id(self, id: int) -> TModel:
        return self.session.query(self.model_class).filter_by(id=id).first()

    def exists_by_id(self, id: int) -> bool:
        instance = self.session.query(self.model_class).filter_by(id=id).first()
        return bool(instance)

    def update(self, instance: TModel, data: TModel) -> TModel:
        for key, value in data.model_dump(exclude_none=True).items():
            setattr(instance, key, value)
        self.session.commit()
        self.session.refresh(instance)
        return instance

    def delete(self, instance: TModel) -> bool:
        self.session.delete(instance)
        self.session.commit()
        return True
