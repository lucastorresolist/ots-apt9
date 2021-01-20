from .base_model import BaseModel
from sqlalchemy import Column, String


class Marketplace(BaseModel):
    __tablename__ = 'marketplaces'

    name = Column( String(length=(50)))
    description = Column ( String(length=(150)))

    def __init__(self, name:str, description:str, id:int = None)-> None:
        self.__id = id
        self.__name = name
        self.__description = description
