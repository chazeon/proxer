import dataset
from typing import List, NamedTuple, Iterable
import requests
import datetime
import multiprocessing.pool

db = dataset.connect('sqlite:///proxies.db')

class Tester:

    def __init__(self, npool=24):
        self.pool = multiprocessing.pool.Pool(npool)
 
    def test(self):
        entries = self.pool.map(Tester.update, db["Proxy"].find())
        for entry in entries:
            db["Proxy"].update(entry, ["id"])
    
    @staticmethod
    def update(entry):
        host = entry["host"]
        try:
            r = requests.get(
                "https://www.gstatic.com/generate_204",
                proxies={
                    "http": f"http://{host}",
                    "https": f"https://{host}"
                },
                timeout=3)
        except:
            entry["state"] = "failed"
            print(host, "failed")
            return entry

        if r.status_code == 204:
            entry["last_ping"] = datetime.datetime.now()
            entry["last_delay"] = r.elapsed.microseconds / 1000
            entry["state"] = "working"
            print(host, r.elapsed.microseconds / 1000)
        else:
            entry["state"] = "failed"
            print(host, "failed")

        return entry

if __name__ == "__main__":
    Tester().test()

