#!/usr/bin/env python2
import click
import requests
import untangle

@click.command()
@click.option('--dic', default='ita.dic')
@click.option('--minlen', default=10)
@click.option('--maxlen', default=16)
@click.option('--wordcount', default=1)
def ploodood(**kwargs):
    """Generates words that "sound like real words"."""
    req = requests.post("http://www.ploodood.net/genWords.php", data=kwargs)
    res = untangle.parse(req.text)

    for w in res.words.word:
        click.echo(w.cdata)

if __name__ == '__main__':
    ploodood()
