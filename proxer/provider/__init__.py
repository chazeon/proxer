from .base import ProxiesProviderBase
from .text import ProxiesTextFileProvider

if __name__ == "__main__":
    import sys
    ProxiesTextFileProvider(sys.argv[1]).update()