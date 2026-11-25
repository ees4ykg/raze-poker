# EDA

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pokerkit import HandHistory
from pathlib import Path

from datetime import datetime, date
import time

folder_names = [
    "ABS-2009-07-01_2009-07-23_50NLH_OBFU",
    "ABS-2009-07-01_2009-07-23_100NLH_OBFU",
    "ABS-2009-07-01_2009-07-23_200NLH_OBFU",
    "ABS-2009-07-01_2009-07-23_400NLH_OBFU",
    "ABS-2009-07-01_2009-07-23_600NLH_OBFU",
    "ABS-2009-07-01_2009-07-23_1000NLH_OBFU",
    "FTP-2009-07-01_2009-07-23_50NLH_OBFU",
    "FTP-2009-07-01_2009-07-23_600NLH_OBFU",
    "FTP-2009-07-01_2009-07-23_1000NLH_OBFU",
    "IPN-2009-07-01_2009-07-23_100NLH_OBFU",
    "IPN-2009-07-01_2009-07-23_200NLH_OBFU",
    "IPN-2009-07-01_2009-07-23_400NLH_OBFU",
    "IPN-2009-07-01_2009-07-23_600NLH_OBFU",
    "IPN-2009-07-01_2009-07-23_1000NLH_OBFU",
    "ONG-2009-07-01_2009-07-23_400NLH_OBFU",
    "ONG-2009-07-01_2009-07-23_600NLH_OBFU",
    "ONG-2009-07-01_2009-07-23_1000NLH_OBFU",
    "PS-2009-07-01_2009-07-23_25NLH_OBFU",
    "PS-2009-07-01_2009-07-23_50NLH_OBFU",
    "PS-2009-07-01_2009-07-23_200NLH_OBFU",
    "PS-2009-07-01_2009-07-23_400NLH_OBFU",
    "PS-2009-07-01_2009-07-23_600NLH_OBFU",
    "PS-2009-07-01_2009-07-23_1000NLH_OBFU",
    "PTY-2009-07-01_2009-07-23_25NLH_OBFU",
    "PTY-2009-07-01_2009-07-23_400NLH_OBFU",
    "PTY-2009-07-01_2009-07-23_600NLH_OBFU",
    "PTY-2009-07-01_2009-07-23_1000NLH_OBFU",
]

venues = {
    "ABS": "Absolute Poker",
    "FTP": "Full Tilt Poker",
    "IPN": "iPoker Network",
    "ONG": "Ongame Network",
    "PS": "PokerStars",
    "PTY": "PartyPoker",
}


def parse_folder(raw_folder_name, venue, folder_name=None):
    folder = Path(f"data/handhq/{raw_folder_name}")
    files = sorted(folder.rglob("*.phhs"))

    if folder_name == None:
        folder_name = raw_folder_name

    output_folder = Path(f"cleaned_data/{folder_name}/parsed_parquet_parts")
    output_folder.mkdir(parents=True, exist_ok=True)

    i = 0

    for path in files:

        rows = []

        with open(path, "rb") as file:
            hhs = list(HandHistory.load_all(file))
        for hh in hhs:
            rows.append({"file": path.name,
                         "time_stamp": datetime.combine(date(hh.year, hh.month, hh.day), hh.time),
                         "handId": hh.hand,
                         "tableId": hh.table,
                         "venue": venue,
                         "actions": list(hh.actions),
                         "n_seats": hh.seat_count,
                         "player_seats": hh.seats,
                         "blinds": [float(b) for b in hh.blinds_or_straddles],
                         "antes": [float(a) for a in hh.antes],
                         "players": hh.players,
                         "starting_stacks": [float(s) for s in hh.starting_stacks]})

        i += 1
        df = pd.DataFrame(rows)
        df.to_parquet(output_folder / f"{path.name[:-5]}_{i}.parquet")

        print(f"File processed: {path.name}")


if __name__ == "__main__":
    start_time = time.perf_counter()
    for folder in folder_names:
        venue = venues[folder.split('-')[0]]
        if venue == "iPoker Network":
            pass  # this venue had missing stacks so we will exclude this data
        else:
            parse_folder(folder_name=folder, venue=venue)
    end_time = time.perf_counter()
    print(f"Total runtime: {end_time - start_time:.1f} seconds")