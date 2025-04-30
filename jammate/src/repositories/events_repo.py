import abc
from domain.event import Event

class EventsRepo(metaclass=abc.ABCMeta):
    # TODO: イベント作成
    # @abc.abstractmethod
    # def updateProfile(self, profile: Profile) -> User:
    #     raise NotImplementedError()
    
    # TODO: イベント更新

    @abc.abstractmethod
    def getById(self, event_id: str) -> Event:
        raise NotImplementedError()
    
    # イベント一覧
    @abc.abstractmethod
    def getAll(self) -> list[Event]:
        raise NotImplementedError()
    
    # ユーザーが参加するイベント一覧
    @abc.abstractmethod
    def getsByUserId(self, user_id: str) -> list[Event]:
        raise NotImplementedError()
    
    # バンドが参加するイベント一覧
    @abc.abstractmethod
    def getsByBandId(self, band_id: str) -> list[Event]:
        raise NotImplementedError()