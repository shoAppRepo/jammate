import abc
from domain.band import Band

class BandsRepo(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, event_id: str) -> Band:
        raise NotImplementedError()
    
    # TODO: バンド情報更新
    # @abc.abstractmethod
    # def updateProfile(self, profile: Profile) -> User:
    #     raise NotImplementedError()
    
    @abc.abstractmethod
    def getAll(self) -> list[Band]:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def getById(self, band_id: str) -> Band:
        raise NotImplementedError()
        
    @abc.abstractmethod
    def getsByEventId(self, event_id: str) -> list[Band]:
        raise NotImplementedError()
    
    # バンド削除