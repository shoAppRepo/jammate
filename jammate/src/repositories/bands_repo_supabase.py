
class BandsRepoSupabase(BandsRepo):
  def create(self, event_id: str) -> Band:
      raise NotImplementedError()
      
  def getAll(self) -> list[Band]:
      raise NotImplementedError()
  
  def getById(self, band_id: str) -> Band:
      raise NotImplementedError()
      
  def getsByEventId(self, event_id: str) -> list[Band]:
      raise NotImplementedError()
