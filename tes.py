import requests
import pprint

req = requests.get(f"https://api.banghasan.com/sholat/format/json/jadwal/kota/512/tanggal/2017-02-07").json()
pprint.pprint(req)