import click
import requests
import sys
import untangle

@click.command()
@click.option('--dic', default='ita.dic')
@click.option('--minlen', default=10)
@click.option('--maxlen', default=16)
@click.option('--wordcount', default=1)
def ploodood(**kwargs):
    """Generates words that "sound like real words"."""
    req = requests.post("http://www.ploodood.net/genWords.php", data=kwargs)

    reload(sys)
    sys.setdefaultencoding('iso-8859-1')
    res = untangle.parse(req.text)

    for w in res.words.word:
        click.echo(w.cdata)
