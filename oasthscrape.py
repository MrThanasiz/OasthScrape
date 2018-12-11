import sys


def getData(stopid):
    from PyQt4.QtGui import QApplication
    from PyQt4.QtCore import QUrl
    from PyQt4.QtWebKit import QWebPage
    import bs4 as bs
    import urllib.request
    class Client(QWebPage):
        def __init__(self,url):
            self.app=QApplication(sys.argv)
            QWebPage.__init__(self)
            self.loadFinished.connect(self.on_page_load)
            self.mainFrame().load(QUrl(url))
            self.app.exec_()
             
        def on_page_load(self):
            self.app.quit()
        

    url= 'http://oasth.gr/#el/stopinfo/screen/'+stopid+'/'
    #print('url='+ url)
    client_response = Client(url)
    source=client_response.mainFrame().toHtml()
    soup = bs.BeautifulSoup(source,'lxml')


    p_tag = soup.find("h2", text="Άφιξη Λεωφορείων στη στάση")
    print("Σταση: ",stopid)
    #if p_tag is None:    << den uparxei h stash check
    if len(p_tag.find_next_siblings("ul")) == 0:
        print("Δεν υπάρχουν διερχομενα λεωφορεία")
    else:
        for li in p_tag.find_next_siblings("ul")[0].find_all("li"):
            print("Ερχονται τα παρακατω: ", li.text)

