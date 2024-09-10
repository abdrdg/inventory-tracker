class Item:

    def __init__(self, id, name, quantity, description, tags, image):
        self.id = id
        self.name = name
        self.quantity = quantity
        self.description = description
        self.tags = tags
        self.image = image

    def qrCode(self):
        pass

    def sync(self):
        pass

    def upload(self):
        pass