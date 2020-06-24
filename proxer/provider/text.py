from typing import Iterable, Union
from .base import ProxiesProviderBase, ProxyEntry

class ProxiesTextFileProvider(ProxiesProviderBase):

    def __init__(self, fname: str):
        self.fname = fname

    def fetch(self) -> Iterable[ProxyEntry]:
        with open(self.fname) as fp:
            for line in fp:
                line = line.strip()
                if line == "": continue
                yield ProxyEntry(host=line)