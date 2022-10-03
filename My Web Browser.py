from sys import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

def is_protocol(url):
    protocols = ["https://", "https:/", 
                 "http://", "http:/"]

    for i in protocols:
        if i in url:
            return True
    
    return False

def is_domain(url):
    domains = [".com", ".com/", ".in", ".in/", 
               ".org", ".org/", ".net", ".net/", 
               ".edu", ".edu/", ".gov", ".gov/"]

    for i in domains:
        if i in url:
            return True
    
    return False

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # Navigation Bar
        nav_bar = QToolBar()
        self.addToolBar(nav_bar)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        nav_bar.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        nav_bar.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        nav_bar.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        nav_bar.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        nav_bar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        
        if is_domain(url) and is_protocol(url) == False:
            new_url = "https://" + url

        elif is_domain(url) == False:
            new_url = "https://google.com/search?q="+url

        else:
            new_url = url

        self.browser.setUrl(QUrl(new_url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


if __name__ == "__main__":
    app = QApplication(argv)
    QApplication.setApplicationName("My Browser")
    window = MainWindow()
    app.exec()
