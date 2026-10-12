from BaseProduct import BaseProduct
class VirtualProduct(BaseProduct):
    def __init__(self, name, price, download_link):
        super().__init__(name, price)
        self.download_link = download_link

    def __str__(self):
        return f"{super().__str__()}, download_link={self.download_link}"