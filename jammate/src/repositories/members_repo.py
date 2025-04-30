import abc
from domain.member import Member
from value_objects.profile import Profile

class MembersRepo(metaclass=abc.ABCMeta):
    # TODO: ユーザークラス実装
    # TODO: uuidを引数として指定できるようにする。uuidは値オブジェクトにする

    @abc.abstractmethod
    def create(self, user_id: str) -> Member:
        raise NotImplementedError()

    @abc.abstractmethod
    def setProfile(self, profile: Profile) -> Member:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def updateProfile(self, profile: Profile) -> Member:
        raise NotImplementedError()

    @abc.abstractmethod
    def getAll(self) -> list[Member]:
        raise NotImplementedError()
    
    @abc.abstractmethod
    def getById(self, user_id: str) -> Member:
        raise NotImplementedError()
    
    # 楽器からユーザー検索
    # 楽器IDから取得
    @abc.abstractmethod
    def getsByInstrumentId(self, instrument_id: str) -> list[Member]:
        raise NotImplementedError()
    
    # バンドメンバー取得
    # バンドIDから取得
    @abc.abstractmethod
    def getsByBandId(self, band_id: str) -> list[Member]:
        raise NotImplementedError()
    
    # イベント参加メンバー取得
    # イベントIDから取得
    @abc.abstractmethod
    def getsByEventId(self, event_id: str) -> list[Member]:
        raise NotImplementedError()
    
    # TODO: ユーザー削除