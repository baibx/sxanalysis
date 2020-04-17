import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import bs4 as bs



class Client(QWebEnginePage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self.on_page_load)
        self.load(QUrl(url))
        self.app.exec_()


    def on_page_load(self):
        self.app.quit()


url = input("Link?")
client_response = Client(url)
soup = bs.BeautifulSoup(client_response.html, 'html.parser')
js_test = soup.find('table', class_='activity-table table table-condensed table-striped ')
print(js_test.text)



