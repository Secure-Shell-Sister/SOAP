__author__ = 'DickyIrwanto'
import urllib2, bs4, sys
import time
if __name__ == '__main__':
    url = 'localhost'
    if len(sys.argv) > 1:
        url = sys.argv[1]
    time_start = time.time()
    Resp = urllib2.urlopen("http://"+url+":8888/Security")
    try:
        soup = bs4.BeautifulSoup(Resp,"lxml")
        soup = soup.findAll('datas')
        for x in soup:
            print x
    except:
        print Resp.read()
        print time.time() - time_start, 'seconds'
