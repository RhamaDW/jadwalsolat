import requests
import datetime
from fuzzywuzzy import process

idkota = requests.get(
    "https://api.banghasan.com/sholat/format/json/kota").json()

now = datetime.datetime.now()
month = str(now.day).zfill(2)
day = str(now.day).zfill(2)


def request(namakota):
    kota_names = [kota["nama"] for kota in idkota["kota"]]
    best_match = process.extractOne(namakota, kota_names)
    limitation = 80
    if best_match[1] >= limitation:
        kota_id = next((kota["id"] for kota in idkota["kota"]
                       if kota["nama"] == best_match[0]), None)
        if kota_id:
            print("ID dari", best_match[0], "adalah:", kota_id)
            jadwalkota = requests.get(
                f"https://api.banghasan.com/sholat/format/json/jadwal/kota/{kota_id}/tanggal/{now.year}-{month}-{day}").json()
            print(f"Tanggal : {jadwalkota['jadwal']['data']['tanggal']}")
            print(f"Shubuh: {jadwalkota['jadwal']['data']['subuh']}")
            print(f"Dhuha: {jadwalkota['jadwal']['data']['dhuha']}")
            print(f"Dzuhur: {jadwalkota['jadwal']['data']['dzuhur']}")
            print(f"Ashar: {jadwalkota['jadwal']['data']['ashar']}")
            print(f"Maghrib: {jadwalkota['jadwal']['data']['maghrib']}")
            print(f"Isya: {jadwalkota['jadwal']['data']['isya']}")
            
        else:
            print("Kota tidak ditemukan.")
    else:
        print("Kota tidak ditemukan.")


request("surabaya")  
