import click

@click.group()
def main():
    pass

@main.command("import", help="Import proxies to text file")
@click.option("-f", "--from", "fname", help="Proxy list file name", type=click.STRING)
def loadtxt(fname):
    from provider import ProxiesTextFileProvider
    if not fname: exit()
    ProxiesTextFileProvider(fname).fetch()

@main.command("export", help="Export proxies to text file")
@click.option("-o", "--to", "fname", default="export.txt", help="Proxy list file name", type=click.STRING)
def writetxt(fname):
    from export import export
    export(fname=fname)

@main.command("test", help="Test proxies")
@click.option("-np", "--npool", default=25, help="Test proxies", type=click.INT)
def testproxies(npool):
    from tester import Tester
    Tester(npool=npool).test()


if __name__ == "__main__":
    main()