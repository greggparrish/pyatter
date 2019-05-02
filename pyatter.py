import sys

from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage, QWebEngineSettings
from PyQt5.QtWidgets import QMainWindow, QAction, QApplication, QToolBar
from PyQt5.QtCore import QUrl


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("pyatter")
        self.show()
        self.browser = self.init_browser()
        self.profile = self.init_profile(self.browser)
        self.webpage = QWebEnginePage(self.profile, self.browser)
        self.browser.setPage(self.webpage)
        self.setCentralWidget(self.browser)
        self.init_navbar()

        url = "https://www.google.com"
        self.webpage.load(QUrl(url))

    def init_browser(self):
        browser = QWebEngineView()
        browser.settings().setAttribute(QWebEngineSettings.AllowRunningInsecureContent, True)
        browser.settings().setAttribute(QWebEngineSettings.AllowWindowActivationFromJavaScript, True)
        return browser

    def init_profile(self, browser):
        profile = QWebEngineProfile(browser)
        profile.setHttpUserAgent('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36')
        return profile

    def init_navbar(self):
        navigation_bar = QToolBar('Navigation')
        self.addToolBar(navigation_bar)

        wa_button = QAction('whatsapp', self)
        wa_url = 'https://web.whatsapp.com'
        wa_button.triggered.connect(lambda: self.open_service(wa_url))
        navigation_bar.addAction(wa_button)

        slack_button = QAction('slack', self)
        sl_url = 'https://www.slack.com'
        slack_button.triggered.connect(lambda: self.open_service(sl_url))
        navigation_bar.addAction(slack_button)

        skype_button = QAction('skype', self)
        sk_url = 'https://www.skype.com'
        skype_button.triggered.connect(lambda: self.open_service(sk_url))
        navigation_bar.addAction(skype_button)

        quit_button = QAction('quit', self)
        quit_button.triggered.connect(self.close_app)
        navigation_bar.addAction(quit_button)

    def open_service(self, surl):
        self.webpage.load(QUrl(surl))

    def close_app(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
