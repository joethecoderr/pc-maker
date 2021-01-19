#Instance Of article
import argparse
import logging
logging.basicConfig(level=logging.INFO)
import pandas as  pd
import numpy as np
import scrap_from_pcbenchmark
import scrap_from_steam
from requirements import LowReqSteam
from base import Base, engine, Session
from scrapers.can_you_run_it import scrape

low_Game_Name_arr = []
low_Descr_arr = []
low_OS_arr = []
low_processor_arr = []
low_ram_arr = []
low_Graphics_arr = []
low_DirectX_arr = []
low_size_arr = []
low_notes_arr = []


rec_Game_Name_arr = []
rec_Descr_arr = []
rec_OS_arr = []
rec_processor_arr = []
rec_ram_arr = []
rec_Graphics_arr = []
rec_DirectX_arr = []
rec_size_arr = []
rec_notes_arr = []

logger = logging.getLogger(__name__)
dummy_df = pd.DataFrame(columns=["Game_Name","Descr", "OS" , "Processor", "Ram", "Graphics", "DirectX",  "size",  "Notes"])
steam_low_req_df = pd.DataFrame(columns=["Game_Name","Descr", "OS" , "Processor", "Ram", "Graphics", "DirectX",  "size",  "Notes"])
steam_rec_req_df = pd.DataFrame(columns=["Game_Name","Descr", "OS" , "Processor", "Ram", "Graphics", "DirectX",  "size",  "Notes"])

pcbenchmark_low_req_df = pd.DataFrame(columns=["Game_Name","Descr", "OS" , "Processor", "Ram", "Graphics", "DirectX",  "size",  "Notes"])
pcbenchmark_rec_req_df = pd.DataFrame(columns=["Game_Name","Descr", "OS" , "Processor", "Ram", "Graphics", "DirectX",  "size",  "Notes"])

def save_data(df):
    Base.metadata.create_all(engine)
    session = Session()
    
    for row in range(len(df.index)):
        
       
        logger.info(f'Loading game info: {df["Game_Name"][row]}')
   
        low_req_steam = LowReqSteam(
            df['Game_Name'][row],
            df['Descr'][row],
            df['OS'][row],
            df['Processor'][row],
            df['Ram'][row],
            df['Graphics'][row],
            df['DirectX'][row],
            df['size'][row],
            df['Notes'][row],
            
                                      )
        session.add(low_req_steam)
    session.commit()
    session.close()
    

    
def fill_arrays(game_name, scraper):


    data_desc, merged_arr_min, merged_arr_rec  = scraper.scrap_page(game_name)
    print(f"DATA DESCR: {data_desc[1]}")
    print('/'*20)
    print(f"MIN REQ: {merged_arr_min}")
    print('/'*20)
    print(f"RECOMMENDED: {merged_arr_rec}")
    print('/'*20)
    

    
    low_Game_Name_arr.append(game_name)
    low_Descr_arr.append(data_desc[1])
    #Note: What if there is no element?
    low_OS_arr.append(merged_arr_min[int(np.where(merged_arr_min[:,0] == "OS:")[0])][1])
    low_processor_arr.append(merged_arr_min[int(np.where(merged_arr_min[:,0] == "Processor:")[0])][1])
    low_ram_arr.append(merged_arr_min[int(np.where(merged_arr_min[:,0] == "Memory:")[0])][1])
    low_Graphics_arr.append(merged_arr_min[int(np.where(merged_arr_min[:,0] == "Graphics:")[0])][1])
    low_DirectX_arr.append(merged_arr_min[int(np.where(merged_arr_min[:,0] == "DirectX:")[0])][1])
    low_size_arr.append(merged_arr_min[int(np.where(merged_arr_min[:,0] == "Storage:")[0])][1])
    low_notes_arr.append(merged_arr_min[int(np.where(merged_arr_min[:,0] == "Additional Notes:")[0])][1])
  
    rec_Game_Name_arr.append(game_name)
    rec_Descr_arr.append(data_desc[1])
    rec_OS_arr.append(merged_arr_rec[int(np.where(merged_arr_rec[:,0] == "OS:")[0])][1])
    rec_processor_arr.append(merged_arr_rec[int(np.where(merged_arr_rec[:,0] == "Processor:")[0])][1])
    rec_ram_arr.append(merged_arr_rec[int(np.where(merged_arr_rec[:,0] == "Memory:")[0])][1])
    rec_Graphics_arr.append(merged_arr_rec[int(np.where(merged_arr_rec[:,0] == "Graphics:")[0])][1])
    rec_DirectX_arr.append(merged_arr_rec[int(np.where(merged_arr_rec[:,0] == "DirectX:")[0])][1])
    rec_size_arr.append(merged_arr_rec[int(np.where(merged_arr_rec[:,0] == "Storage:")[0])][1])
    rec_notes_arr.append(merged_arr_rec[int(np.where(merged_arr_rec[:,0] == "Additional Notes:")[0])][1])

      
def fill_df(low_df, rec_df):
    low_df.Game_Name = low_Game_Name_arr
    low_df.Descr =low_Descr_arr
    low_df.OS = low_OS_arr
    low_df.Processor = low_processor_arr
    low_df.Ram = low_ram_arr
    low_df.Graphics =low_Graphics_arr
    low_df.DirectX  =low_DirectX_arr
    low_df.size =  low_size_arr
    low_df.Notes =  low_notes_arr
    
    rec_df.Game_Name = rec_Game_Name_arr
    rec_df.Descr =rec_Descr_arr
    rec_df.OS = rec_OS_arr
    rec_df.Processor = rec_processor_arr
    rec_df.Ram = rec_ram_arr
    rec_df.Graphics =rec_Graphics_arr
    rec_df.DirectX  =rec_DirectX_arr
    rec_df.size =  rec_size_arr
    rec_df.Notes =  rec_notes_arr
    
    
    
if __name__ == '__main__':
    low_Game_Name_arr.clear()
    low_Descr_arr.clear()
    low_OS_arr.clear()
    low_processor_arr.clear()
    low_ram_arr.clear()
    low_Graphics_arr.clear()
    low_DirectX_arr.clear()
    low_size_arr.clear()
    low_notes_arr.clear()

    rec_Game_Name_arr.clear()
    rec_Descr_arr.clear()
    rec_OS_arr.clear()
    rec_processor_arr.clear()
    rec_ram_arr.clear()
    rec_Graphics_arr.clear()
    rec_DirectX_arr.clear()
    rec_size_arr.clear()
    rec_notes_arr.clear()

    for game in ["Monster Hunter World", "Cyberpunk 2077"]:
        fill_arrays(game, scrap_from_steam)
       
    
    fill_df(steam_low_req_df, steam_rec_req_df)
    
    save_data(steam_low_req_df)
    save_data(steam_rec_req_df)
