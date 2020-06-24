import dataset
from typing import List, NamedTuple, Iterable


class ProxyEntry(NamedTuple):
    host: str

class ProxiesProviderBase:

    db = dataset.connect('sqlite:///proxies.db')

    def update(self):
        for entry in self.fetch():
            if not self.db["Proxy"].find_one(host=entry.host):
                self.db["Proxy"].insert(entry._asdict())

    def fetch(self) -> Iterable[ProxyEntry]:
        NotImplemented

__all__ = ["ProxyEntry", "ProxiesProviderBase"]