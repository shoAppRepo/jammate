from repositories.events_repo import EventsRepo
from domain.event import Event

EVENT_MOCK_DATA_1 = Event(
    id="18bb1584-0136-436a-808e-ec5c758342c4",
    name="テストイベント",
    location="サンシャインビル14階",
    start_at="JPOP",
    memo="これはお試しのイベントです",
)

MOCK_EVENTS = [
    EVENT_MOCK_DATA_1,
]

class EventsRepoMock(EventsRepo):
    def getById(self, event_id: str) -> Event:
        return next(filter(lambda event: event.id == event_id, MOCK_EVENTS), None)
    
    # イベント一覧
    def getAll(self) -> list[Event]:
        return MOCK_EVENTS
    
    # ユーザーが参加するイベント一覧
    def getsByUserId(self, user_id: str) -> list[Event]:
        raise NotImplementedError()
    
    # バンドが参加するイベント
    def getByBandId(self, band_id: str) -> list[Event]:
        return next(
            (event for event in MOCK_EVENTS if any(band.id == band_id for band in event.performers)),
            None
        )    
