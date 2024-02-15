from arango import ArangoClient
import time

#TODO
    # Merge with 'tab_w_drop_down.py'
'
class TT_Data:
    def __init__(self, **kwargs):
        self.j_date = j_date
        self.subtotal = subtotal
        self.list_o_entries = list_o_entries
        self.total_hours = total_hours


    def get_th(self):
        self.total_hours = self.subtotal * 0.25

    def __repr__(self):
        nl = "\n"
        return(f"Today is: {self.j_date}{nl}Total Hours = {self.total_hours}")

    def add_new_entry(self, **kwargs):
            temp_entry = {ts_now: {
            "time_slot": time_slot, 
            "category":category, 
            "time_val":time_val, 
            "notes":notes
            }}
            self.list_o_entries.append(temp_entry)

    def gen_subtotal(self):
        temp_subtotal = 0
        loe = self.list_o_entries
        for entry in loe:
            for k, v in entry.items():
                temp_tv = v["time_val"]
                temp_subtotal = temp_subtotal + temp_tv
        return temp_subtotal
            


##################
# j_date = ""
j_date = "2024.1"
ts_now = str(round(time.time()*1000))
time_slot = 0000
category = "sleep"
time_val = 99
notes = "nap"
subtotal = 0
list_o_entries = []
total_hours = 0.0
# list_o_j_dates = []

def upload_to_adb(tt_day, dts_coll):
    j_date = tt_day.j_date
    temp_day = {'_key': j_date, j_date:(tt_day.__dict__)}
    dts_coll.insert(temp_day)
    backup

tt_day = TT_Data(j_date = j_date, subtotal = 0, list_o_entries = [], TH = 0.0)
tt_day.add_new_entry(time_slot = time_slot, category = category, time_val = time_val, notes = notes)

st = tt_day.gen_subtotal()
tt_day.subtotal = st
th = tt_day.get_th()

# client = ArangoClient(hosts='https://adb.dekaminas.com')
# timesheet_db = client.db('tt', username='root', password='passwd')

client = ArangoClient(hosts='https://adb.dekaminas.com')
timesheet_db = client.db('tt', username='gary', password='gary')

dts_coll = timesheet_db.collection('daily_ts')

# TT_data = [{'id': 0, 't_slot': '0015', 'cat': 'Work', 'length': 'length', 'notes': 'test a'}, {'id': 1, 't_slot': '0030', 'cat': 'Work', 'length': 'length', 'notes': 'test b'}, {'id': 2, 't_slot': '0045', 'cat': 'Play', 'length': 'length', 'notes': 'test c'}]

print(77, (tt_day.__dict__))

upload_to_adb(tt_day, dts_coll)
