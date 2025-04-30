import uuid
from bands_repo import BandsRepo
from domain.band import Band

from events_repo_mock import EVENT_MOCK_DATA_1

BAND_MOCK_DATA_1 = Band(
    band_id="0754fcd4-0631-4539-bb26-864e6646cc77",
    event_id=EVENT_MOCK_DATA_1.id,
    name="お試しバンド",
    description="これはお試しバンドです",
    genre="ロック",
    image_url="https://picsum.photos/200/300",
)

BAND_MOCK_DATA_2 = Band(
    band_id="902a5b82-fdf3-4daa-8c2a-574c9994eb71",
    event_id=EVENT_MOCK_DATA_1.id,
    name="アイウエオ",
    description="これはお試しバンドです",
    genre="JPOP",
    image_url="https://picsum.photos/200/300",
)

BAND_MOCK_DATA_3 = Band(
    band_id="ccf8d8a6-907f-4e2d-9bd9-cf54af574ef8",
    event_id=EVENT_MOCK_DATA_1.id,
    name="aiueo",
    description="これはお試しバンドです",
    genre="JAZZ",
    image_url="https://picsum.photos/200/300",
)

MOCK_BANDS = [
    BAND_MOCK_DATA_1,
    BAND_MOCK_DATA_2,
    BAND_MOCK_DATA_3,
]

class BandsRepoMock(BandsRepo):
  def create(self, event_id: str) -> Band:
      new_band = Band(
          band_id=str(uuid.uuid4()),
          event_id=event_id,
          name="newバンド",
          description="",
          genre="",
          image_url="",
      )   
      MOCK_BANDS.append(new_band)
      return new_band
      
  def getAll(self) -> list[Band]:
      return MOCK_BANDS
  
  def getById(self, band_id: str) -> Band:
      return next(filter(lambda band: band.id == band_id, MOCK_BANDS), None)
      
  def getsByEventId(self, event_id: str) -> list[Band]:
      return next(filter(lambda band: band.event_id == event_id, MOCK_BANDS), None)
