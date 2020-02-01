import pandas as pd
import json
import math
import random

class CSVParser():
    def __init__(self):
        amp_names = open("csv_amp_names.txt")
        water_names = open("csv_water_names.txt")
        
        self.amp_csvs = []
        self.water_csvs = []

        self.sus = 877
        self.eff = 692
        
        for line in amp_names:
            amp_draw = pd.DataFrame(pd.read_csv(line.split()[0]))
            self.amp_csvs.append(amp_draw)
            self.amp_length = 0
    
        for line in water_names:
            water_draw = pd.DataFrame(pd.read_csv(line.split()[0]))
            self.water_csvs.append(water_draw)

        self.power_over_time()
        self.water_over_time()
    
        self.aggregate_power()
        self.aggregate_water()
    
    def aggregate_power(self):
        self.total_amps = self.amp_csvs[0].groupby(by="room_id").sum()
        
        for room in self.amp_csvs:
            power_consumption = room.groupby(by="room_id")
            self.total_amps += power_consumption.sum()

        self.total_amps -= self.amp_csvs[0].groupby(by="room_id").sum()

            
    def power_over_time(self):
        for room in self.amp_csvs:
            power_consumption = room.groupby(by="room_id")

            ret_list = list([power_consumption.get_group(x) for x in power_consumption.groups][random.randrange(3)]["amp_draw"].to_json())

        with open('power_over_time.json', 'w') as f:
                json.dump(ret_list, f)


    def water_over_time(self):
        for room in self.water_csvs:
            water_consumption = room.groupby(by="room_id")

            ret_list = list([water_consumption.get_group(x) for x in water_consumption.groups][random.randrange(3)]["water_today"])

        with open('water_over_time.json', 'w') as f:
                json.dump(ret_list, f)

        
    def get_layout(self, layout_name):
    
        with open('water_over_time.json') as water_file:
            water_data = json.load(water_file)

        with open('power_over_time.json') as power_file:
            power_data = json.load(power_file)

        return {layout_name: {
            "sustainability": self.sus,
            "efficiency": self.eff,
            "variables": {
                "water": water_data,
                "power": power_data
            }
        },
        "Layout2": {
            "sustainability": random.randrange(600, 900),
            "efficiency": random.randrange(550, 800),
            "variables": {
                "water": water_data,
                "power": power_data
            }
        }}
            

    def aggregate_water(self):
        self.total_water = self.water_csvs[0].groupby(by="room_id").sum()
        
        for room in self.water_csvs:
            water_consumption = room.groupby(by="room_id")
            self.total_water += water_consumption.sum()
            
        self.total_water -= self.water_csvs[0].groupby(by="room_id").sum()
    
    def get_power_consumption(self):
        return self.total_amps.drop(["room_name", "equip_id"], axis=1).to_json()
    
    def get_water_consumption(self):
        return self.total_water
