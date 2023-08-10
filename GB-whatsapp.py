class DownloadManager:
    def __init__(self):
        self.downloads = []

    def add_download(self, url):
        self.downloads.append(url)

    def start_downloads(self):
        for url in self.downloads:
            download = self._create_download_instance(url)
            download.start()

    def _create_download_instance(self, url):
        if "gbwhatsapp" in url:
            return GBWhatsAppDownload(url)
        else:
            return DefaultDownload(url)

class Download:
    def __init__(self, url):
        self.url = url

    def start(self):
        print(f"Downloading: {self.url}")

class GBWhatsAppDownload(Download):
    def start(self):
        print(f"Downloading GB WhatsApp from {self.url}")

class DefaultDownload(Download):
    pass

# Usage
manager = DownloadManager()
manager.add_download("http://example.com/gbwhatsapp")
manager.add_download("http://example.com/file1")
manager.add_download("http://example.com/gbwhatsapp")
manager.start_downloads()
gb whatsapp download from here :-  https://moktymokapoprt.blogspot.com/2023/08/gb-whatsapp-download-gb-whatsapp.html

from abc import ABC, abstractmethod

class Download(ABC):
    @abstractmethod
    def start(self):
        pass

class GBWhatsAppDownload(Download):
    def __init__(self, url):
        self.url = url

    def start(self):
        print(f"Downloading GB WhatsApp from {self.url}")

class DefaultDownload(Download):
    def __init__(self, url):
        self.url = url

    def start(self):
        print(f"Downloading: {self.url}")

class DownloadManager:
    def __init__(self):
        self.downloads = []

    def add_download(self, download):
        self.downloads.append(download)

    def start_downloads(self):
        for download in self.downloads:
            download.start()

# Usage
manager = DownloadManager()
manager.add_download(GBWhatsAppDownload("http://example.com/gbwhatsapp"))
manager.add_download(DefaultDownload("http://example.com/file1"))
manager.add_download(GBWhatsAppDownload("http://example.com/gbwhatsapp"))
manager.start_downloads()
