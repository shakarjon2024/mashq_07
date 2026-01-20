class Gallery:
    def __init__(self):
        self.images = []

    def add_image(self, name, size_mb):
        self.images.append((name, size_mb))

    def total_size(self):
        return sum(size for _, size in self.images)

gallery = Gallery()
gallery.add_image("photo1.jpg", 2.5)
gallery.add_image("photo2.png", 3.1)

print("Jami hajm (MB):", gallery.total_size())
