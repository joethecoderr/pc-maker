import argparse
import logging
import pandas as  pd
import numpy as np
from scrapers import scrap_from_pcbenchmark
from scrapers import scrap_from_steam
import get_games
from requirements import LowReqSteam, RecReqSteam, LowReqPCGBM, RecReqPCGBM
from requirements import LowReqCanYouRunIt, RecReqCanYouRunIt
import re
from base import Base, engine, Session
from scrapers.can_you_run_it import scrape


def save_data_req_steam(game,descr, data, low_or_rec):
    Base.metadata.create_all(engine)
    session = Session()
    descr = ''.join(descr)

    descr = re.sub('[^0-9a-zA-Z]+', ' ', descr)
    os = [row[1]  for row in data if row[0] == "OS:"] 
    if len(os) == 0: os = [""]
    cpu = [cpu[1] for cpu in data if cpu[0] == "Processor:" ] 
    if len(cpu) == 0: cpu = [""]
    ram = [ram[1]  for ram in data if ram[0] == "Memory:"]
    if len(ram) == 0: ram = [""]
    gpu = [graphics[1] for graphics in data if graphics[0] == "Graphics:"]
    if len(gpu) == 0: gpu = [""]
    DX = [direct[1]  for direct in data if direct[0] == "DirectX:"]
    if len(DX) == 0: DX = [""]
    
    
    size = [size[1] for size in data if size[0] == "Storage:"]
    if len(size) == 0: size = [""]
    
    
    note = [note[1] for note in data if note[0] == "Additional Notes:" ] 
    if len(note) == 0: note = [""]
    #note = re.sub('\uFF1A', ' ', note[0])
    note[0] = re.sub('[^0-9a-zA-Z]+', ' ', note[0])
    
    
    if low_or_rec == "low":
        low_req_steam = LowReqSteam(
            game,
            descr,
            os[0],
            cpu[0] ,
            ram[0] ,
            gpu[0],
            DX[0] ,
            size[0],
            note[0],
                    )
        session.add(low_req_steam)
        session.commit()
        session.close()
    else:
        rec_req_steam = RecReqSteam(
            game,
            descr,
             os[0],
             cpu[0] ,
            ram[0] ,
            gpu[0],
            DX[0] ,
            size[0],
            note[0],
                    )
        session.add(rec_req_steam)
        session.commit()
        session.close()    

def save_data_req_pcbm(game,descr, data, low_or_rec):
    print(f"PCBM: {data}")
    Base.metadata.create_all(engine)
    session = Session()
    descr = ''.join(descr)

    os = [row[1]  for row in data if row[0] == "OS:"] 
    if len(os) == 0: os = [""]
   
    cpu = [cpu[1] for cpu in data if "CPU:" in cpu[0]] 
    if len(cpu) == 0: cpu = [""]
    
    
    ram = [ram[1]  for ram in data if ram[0] == "Memory:"]
    if len(ram) == 0: ram = [""]
    gpu = [graphics[1] for graphics in data if graphics[0] == "Graphics Card:"]
    if len(gpu) == 0: gpu = [""]
    DX = [direct[1]  for direct in data if direct[0] == "DirectX:"]
    if len(DX) == 0: DX = [""]
    size = [size[1] for size in data if "File Size:" in size[0]]
    if len(size) == 0: size = [""]
    note = [note[1] for note in data if note[0] == "Additional Notes:" ]
    if len(note) == 0: note = [""]
    #note = re.sub('\uFF1A', ' ', note[0])
    
    if low_or_rec == "low":
        low_req_pcgbm = LowReqPCGBM(
            game,
            descr,
            os[0],
            cpu[0] ,
            ram[0] ,
            gpu[0],
            DX[0] ,
            size[0],
            note[0],
                    )
        session.add(low_req_pcgbm)
        session.commit()
        session.close()
    else:
        rec_req_pcgbm = RecReqPCGBM(
            game,
            descr,
             os[0],
             cpu[0] ,
            ram[0] ,
            gpu[0],
            DX[0] ,
            size[0],
            note[0],
                    )
        session.add(rec_req_pcgbm)
        session.commit()
        session.close()    

def save_data_canyourunit_reqs(reqs, low_or_rec, game_name):
    Base.metadata.create_all(engine)
    session = Session()
    os = [os[1] for os in reqs if os[0] == "OS" ]
    if len(os) == 0 : os = [' ']
    cpu = [cpu[1] for cpu in reqs if cpu[0] == "CPU"]
    if len(cpu) == 0 : os = ['']
    ram = [ram[1] for ram in reqs if ram[0] == "RAM"]
    if len(ram) == 0 : ram = ['']
    graphics = [graphics[1]  for graphics in reqs if graphics[0] == "VIDEO CARD"]
    if len(graphics) == 0 : graphics = ['']
    size = [size[1] for size in reqs if size[0] == "FREE DISK SPACE"]
    if len(size) == 0 : size = ['']
    if low_or_rec == "low":
        low_req_canyourunit = LowReqCanYouRunIt(
            game_name,
            "TEST",
            os[0],
            cpu[0],
            ram[0],
            graphics[0],
            "Test",
            size[0],
            "TEST")
        session.add(low_req_canyourunit)
        session.commit()
        session.close()
    elif low_or_rec == "rec":
        rec_req_canyourunit = RecReqCanYouRunIt(
            game_name,
            "TEST",
            os[0],
            cpu[0],
            ram[0],
            graphics[0],
            "Test",
            size[0],
            "TEST")
        session.add(rec_req_canyourunit)
        session.commit()
        session.close()

def scrape_from_canyourunit(games):
    
    for game in games:
        print('GAME!!!!: ',game)
        if game == 'PLAYERUNKNOWN’S BATTLEGROUNDS' : game = 'PUBG'
        amazon, minimun, rec = scrape(game)
        if len(minimun) > 0:
            save_data_canyourunit_reqs(minimun, "low", game)
        if len(rec) > 0:
            save_data_canyourunit_reqs(rec, "rec", game)

# def scrape_from_steam(games):
#     for game in games:
#         data_desc, merged_arr_min, merged_arr_rec  = scrap_from_steam.scrap_page(game)
#         save_data_req_steam(game, data_desc,merged_arr_min, "low")
#         save_data_req_steam(game, data_desc, merged_arr_rec, "rec")
#         data_desc_pcbm, merged_arr_min_pcbm, merged_arr_rec_pcbm  = scrap_from_pcbenchmark.scrap_page(game)

if __name__ == '__main__':
    games = get_games.Get_names('https://www.pcgamebenchmark.com/best-pc-games?tags=&sort=0')

    
    print(games)
    for game in games[221:]: #Sabotaj idx
        if game != "Genshin Impact" and  game != "Hogwarts Legacy" and game != "Cooking Simulator" and game != "FINAL FANTASY XV" and game != "コイカツ！ / Koikatsu Party" and game != "Sabotaj" and game != "Google Stadia" :

            data_desc, merged_arr_min, merged_arr_rec, link_path  = scrap_from_steam.scrap_page(game)
            if game.replace(" ", "_") in link_path:
               save_data_req_steam(game, data_desc,merged_arr_min, "low")
               save_data_req_steam(game, data_desc, merged_arr_rec, "rec")    
                   
        if game != "Attack on Titan 2 - A.O.T.2 - 進撃の巨人２" and game != "コイカツ！ / Koikatsu Party"  and game != "Sabotaj"  and game != "Google Stadia":
            
            data_desc_pcbm, merged_arr_min_pcbm, merged_arr_rec_pcbm  = scrap_from_pcbenchmark.scrap_page(game)
            save_data_req_pcbm(game,data_desc_pcbm, merged_arr_min_pcbm, "low")
            save_data_req_pcbm(game,data_desc_pcbm, merged_arr_rec_pcbm, "rec")


