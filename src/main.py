#Instance Of article
import argparse
import logging
logging.basicConfig(level=logging.INFO)
import pandas as  pd
import numpy as np
import scrap_from_pcbenchmark

from requirements import LowReqSteam
from base import Base, engine, Session
from scrapers.can_you_run_it import scrape


logger = logging.getLogger(__name__)
dummy_df = pd.DataFrame(columns=["Game_Name","Descr", "OS" , "Processor", "Ram", "Graphics", "DirectX",  "size",  "Notes"])
dummies_Game_Name = []
dummies_Descr = []
dummies_OS= []
dummies_processor = []
dummies_ram = []
dummies_Graphics = []
dummies_DirectX = []
dummies_size = []
dummies_notes = []

def create_dummies_datapoints(number_dummies):
    
    for i in range(number_dummies):
        dummies_Game_Name.append( f"Game_Name_{i}")
        dummies_Descr.append(f"Descr_{i}")
        dummies_OS.append(f"OS_{i}")
        dummies_processor.append(f"Processor_{i}")
        dummies_ram.append(f"Ram_{i}")
        dummies_Graphics.append(f"Graphics_{i}")
        dummies_DirectX.append(f"DirectX_{i}")
        dummies_size.append(f"size_{i}")
        dummies_notes.append(f"Notes_{i}")
        
    dummy_df.Game_Name = dummies_Game_Name
    dummy_df.Descr = dummies_Descr
    dummy_df.OS = dummies_OS
    dummy_df.Processor = dummies_processor
    dummy_df.Ram = dummies_ram
    dummy_df.Graphics = dummies_Graphics
    dummy_df.DirectX  = dummies_DirectX
    dummy_df.size = dummies_size
    dummy_df.Notes = dummies_notes
        

def main():
    Base.metadata.create_all(engine)
    session = Session()
    print(dummy_df.index)
    print(scrape())
    for row in range(len(dummy_df.index)):
        
       
        logger.info(f'Loading dummy game: {dummy_df["Game_Name"][row]}')
   
        low_req_steam = LowReqSteam(
                          dummy_df['Game_Name'][row],
                          dummy_df['Descr'][row],
                          dummy_df['OS'][row],
                          dummy_df['Processor'][row],
                          dummy_df['Ram'][row],
                          dummy_df['Graphics'][row],
                          dummy_df['DirectX'][row],
                          dummy_df['size'][row],
                          dummy_df['Notes'][row]
                          )
    
        session.add(low_req_steam)
       
    session.commit()
    session.close()
def fill_arrays(game_name):
    data_desc, merged_arr_min, merged_arr_rec  = scrap_from_pcbenchmark.scrap_from_pcgbm(game_name)
    dummies_Game_Name.append(game_name)
    dummies_Descr.append(data_desc)
    dummies_OS.append(merged_arr_min[9][1])
    dummies_processor.append(merged_arr_min[7][1])
    dummies_ram.append(merged_arr_min[5][1])
    dummies_Graphics.append(merged_arr_min[6][1])
    dummies_DirectX.append('')
    dummies_size.append('')
    dummies_notes.append('')
        
    print(f"DATA DESCR: {data_desc}")
    print()
    print(f"MIN REQ: {merged_arr_min[0][1]}")
    print()
    print(f"RECOMMENDED: {merged_arr_rec}")
    print()
    print(f'dummies{dummies_Descr}')
    
    dummy_df.Game_Name = dummies_Game_Name
    dummy_df.Descr = dummies_Descr
    dummy_df.OS = dummies_OS
    dummy_df.Processor = dummies_processor
    dummy_df.Ram = dummies_ram
    dummy_df.Graphics = dummies_Graphics
    dummy_df.DirectX  = dummies_DirectX
    dummy_df.size = dummies_size
    dummy_df.Notes = dummies_notes
    
if __name__ == '__main__':
    fill_arrays("Cyberpunk 2077")
    main()
   # create_dummies_datapoints(5)
    #print(dummy_df)
    
    #parser=argparse.ArgumentParser()
   #parser.add_argument('filename',
    #                    help='The file to load to the db',
     #                   type=str)
    #args = parser.parse_args()
    #main()