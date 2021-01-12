#Class example
#For this class we will use sqlalchemy
from sqlalchemy import Column, String, Integer, Text
from base import Base

class Article(Base):
    __tablename__ = 'low_req_steam'
    id = Column(String(200), primary_key=True)
    Game_Name = Column(String(255))
    Descr = Column(String(255))
    OS = Column(String(255))
    Processor = Column(String(255))
    Ram = Column(String(255))
    Graphics = Column(String(255))
    DirectX = Column(String(255))
    size = Column(String(255))
    Notes = Column(String(255))
    

    def __init__(self, uid, Game_Name, Descr, OS, Processor, Ram, Graphics, DirectX,size,Notes):
        self.id = uid
        self.Game_Name = Game_Name
        self.Descr = Descr
        self.OS = OS
        self.Processor = Processor
        self.Ram = Ram
        self.Graphics = Graphics
        self.DirectX = DirectX
        self.size = size
        self.Notes = Notes