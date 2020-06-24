import dataset

db = dataset.connect('sqlite:///proxies.db')

def export(fname: str):
    with open(fname, "w") as fp:
        for entry in db["Proxy"].find(state="working"):
            host = entry["host"]
            fp.write(f"{host}\n")

if __name__ == "__main__":
    export()