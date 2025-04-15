import uuid

from domain.member import Member
from repositories.members_repo import MembersRepo
from value_objects.profile import Profile

from repositories.bands_repo_mock import MOCK_BANDS

MEMBER_MOCK_DATA_1 = Member(
    id="3b3ff274-4780-44ac-8321-a1813e1b9709",
    profile=Profile(
        name="テスト太郎",
        introduction="初めまして",
        icon_url="https://picsum.photos/50/50",
        favorite_genres="JPOP"
    ),
    joined_bands=[ MOCK_BANDS[0] ],
)

MEMBER_MOCK_DATA_2 = Member(
    id="f5edbd51-a202-4164-9fb7-6074ee10cc27",
    profile=Profile(
        name="テスト次郎",
        introduction="どうも",
        icon_url="https://picsum.photos/50/50",
        favorite_genres="プログレ"
    ),
    joined_bands=[ MOCK_BANDS[0] ],
)

MEMBER_MOCK_DATA_3 = Member(
    id="22d3652b-f2ec-4712-9647-7a155f4b6028",
    profile=Profile(
        name="テスト三郎",
        introduction="よろしくお願いします",
        icon_url="https://picsum.photos/50/50",
        favorite_genres="メタル"
    ),
    joined_bands=[ MOCK_BANDS[0] ],
)

MOCK_MEMBERS = [
    MEMBER_MOCK_DATA_1,
    MEMBER_MOCK_DATA_2,
    MEMBER_MOCK_DATA_3,
]

class MembersRepoMock(MembersRepo):
    # TODO: ユーザークラス実装
    # TODO: uuidを引数として指定できるようにする。uuidは値オブジェクトにする

    def create(self, user_id: str) -> Member:
        new_member = Member(
            id=user_id,
            profile=None,
            joined_bands=None,
        )
        MOCK_MEMBERS.append(new_member)
        return new_member

    def setProfile(self, profile: Profile) -> Member:
        raise NotImplementedError()
    
    def updateProfile(self, profile: Profile) -> Member:
        raise NotImplementedError()

    def getAll(self) -> list[Member]:
        return MOCK_MEMBERS
    
    def getById(self, user_id: str) -> Member:
      return next(filter(lambda user: user.id == user_id, MOCK_MEMBERS), None)
    
    def getsByInstrumentId(self, instrument_id: str) -> list[Member]:
        raise NotImplementedError()
    
    def getsByBandId(self, band_id: str) -> list[Member]:
        raise NotImplementedError()
    
    def getsByEventId(self, event_id: str) -> list[Member]:
        raise NotImplementedError()
    