'Goal:  Concurrently, visit websites and report statistics on the page'

from urllib.request import urlopen

sites = [
    'http://www.perl.org/',
    'http://www.python.org/',
    'http://golang.org/',
    'http://cisco.com/',
    'http://www.wikipedia.org/',
    'http://cnn.com/',
    'http://cnbc.com/',
    'http://abcnews.com/',
    'http://nbcnews.com/',
    'http://cbsnews.com/',
]

stopwords = set('''
    and but  nor the for by with of from over 
    are were have has had any about this that been being
    meta header footer abbr  return var begin end tags there above below open close
    head body these those this that fonts elements text
    media you him his her she your yours mine our ours pre else
    items was into are articletitlesection out icon come get
    function typeof video slot currentslot item autoplay
    playsinline
'''.split())

