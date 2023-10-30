import requests
import datetime
import pprint  

idkota = requests.get("https://api.banghasan.com/sholat/format/json/kota").json()

now = datetime.datetime.now()
find_id = input("Nama Kota : ").upper()


for kota in idkota["kota"]:
    if kota["nama"] == find_id:
        print("ID dari", find_id, "adalah:", kota["id"])
        id = kota["id"]
        jadwalkota = requests.get(f"https://api.banghasan.com/sholat/format/json/jadwal/kota/{id}/tanggal/{now.year}-{now.month}-{now.day}").json()
        print(f"Tanggal : {jadwalkota['jadwal']['data']['tanggal']}")
        print(f"Shubuh: {jadwalkota['jadwal']['data']['subuh']}")
        print(f"Dhuha: {jadwalkota['jadwal']['data']['dhuha']}")
        print(f"Dzuhur: {jadwalkota['jadwal']['data']['dzuhur']}")
        print(f"ashar: {jadwalkota['jadwal']['data']['ashar']}")
        print(f"Maghrib: {jadwalkota['jadwal']['data']['maghrib']}")
        print(f"Isya: {jadwalkota['jadwal']['data']['isya']}")

        break
    
    else:
        print("Tidak Ada Dalam Data")
