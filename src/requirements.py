#Class example
#For this class we will use sqlalchemy
from sqlalchemy import Column, String, Integer, Text
from base import Base

<<<<<<< HEAD
class LowReqSteam(Base):
    def __init__(self ,Game_Name, Descr, OS, Processor, Ram, Graphics, DirectX,size,Notes):
      
        self.Game_Name = Game_Name
        self.Descr = Descr
        self.OS = OS
        self.Processor = Processor
        self.Ram = Ram
        self.Graphics = Graphics
        self.DirectX = DirectX
        self.size = size
        self.Notes = Notes
        
        
    __tablename__ = 'low_req_steam'
  

    id = Column(Integer(), primary_key=True, autoincrement = True)
    Game_Name = Column(String(255))
    Descr = Column(String(255))
    OS = Column(String(255))
    Processor = Column(String(255))
    Ram = Column(String(255))
    Graphics = Column(String(255))
    DirectX = Column(String(255))
    size = Column(String(255))
    Notes = Column(String(255))
=======
# class LowReqSteam(Base):
#     __tablename__ = 'low_req_steam'
#     id = Column(Integer(), primary_key=True, autoincrement = True)
#     Game_Name = Column(String(255))
#     Descr = Column(String(255))
#     OS = Column(String(255))
#     Processor = Column(String(255))
#     Ram = Column(String(255))
#     Graphics = Column(String(255))
#     DirectX = Column(String(255))
#     size = Column(String(255))
#     Notes = Column(String(255))

#     def __init__(self ,Game_Name, Descr, OS, Processor, Ram, Graphics, DirectX,size,Notes,table_name):
#         self.Game_Name = Game_Name
#         self.Descr = Descr
#         self.OS = OS
#         self.Processor = Processor
#         self.Ram = Ram
#         self.Graphics = Graphics
#         self.DirectX = DirectX
#         self.size = size
#         self.Notes = Notes
        
        

>>>>>>> ac22dd9d99aeb61390b397efddf5a89ff7516a86
    

# class RecReqSteam(Base):
#     def __init__(self ,Game_Name, Descr, OS, Processor, Ram, Graphics, DirectX,size,Notes):
       
#         self.Game_Name = Game_Name
#         self.Descr = Descr
#         self.OS = OS
#         self.Processor = Processor
#         self.Ram = Ram
#         self.Graphics = Graphics
#         self.DirectX = DirectX
#         self.size = size
#         self.Notes = Notes
        
        
#     __tablename__ = 'rec_req_steam'
#     id = Column(Integer(), primary_key=True, autoincrement = True)
#     Game_Name = Column(String(255))
#     Descr = Column(String(255))
#     OS = Column(String(255))
#     Processor = Column(String(255))
#     Ram = Column(String(255))
#     Graphics = Column(String(255))
#     DirectX = Column(String(255))
#     size = Column(String(255))
#     Notes = Column(String(255))
    
# class LowReqPCGBM(Base):
#     def __init__(self ,Game_Name, Descr, OS, Processor, Ram, Graphics, DirectX,size,Notes):
       
#         self.Game_Name = Game_Name
#         self.Descr = Descr
#         self.OS = OS
#         self.Processor = Processor
#         self.Ram = Ram
#         self.Graphics = Graphics
#         self.DirectX = DirectX
#         self.size = size
#         self.Notes = Notes
        
        
#     __tablename__ = 'low_req_pcbenchmark'
#     id = Column(Integer(), primary_key=True, autoincrement = True)
#     Game_Name = Column(String(255))
#     Descr = Column(String(255))
#     OS = Column(String(255))
#     Processor = Column(String(255))
#     Ram = Column(String(255))
#     Graphics = Column(String(255))
#     DirectX = Column(String(255))
#     size = Column(String(255))
#     Notes = Column(String(255))


class LowReqCanYouRunIt(Base):
    __tablename__ = 'low_req_canyourunit'
    id = Column(Integer(), primary_key=True, autoincrement = True)
    Game_Name = Column(String(255))
    Descr = Column(String(255))
    OS = Column(String(255))
    Processor = Column(String(255))
    Ram = Column(String(255))
    Graphics = Column(String(255))
    DirectX = Column(String(255))
    size = Column(String(255))
    Notes = Column(String(255))
    
    def __init__(self ,Game_Name, Descr, OS, Processor, Ram, Graphics, DirectX,size,Notes):
        self.Game_Name = Game_Name
        self.Descr = Descr
        self.OS = OS
        self.Processor = Processor
        self.Ram = Ram
        self.Graphics = Graphics
        self.DirectX = DirectX
        self.size = size
        self.Notes = Notes