#Platform start

self.sprite = sprite("tile.png")

self.top_box = platform_hitbox(self, "TOP", 0, 35)
self.top_box.scaleX = 3

self.bottom_box = platform_hitbox(self, "BOTTOM", 0, -38)
self.bottom_box.scaleX = 3

self.left_box = platform_hitbox(self, "LEFT", -38, 0)
self.left_box.scaleY = 2

self.right_box = platform_hitbox(self, "RIGHT", 38, 0)
self.right_box.scaleY = 2
