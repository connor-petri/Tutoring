#PlayerHitbox start
self.hitbox_types = ["NONE", "TOP", "BOTTOM", "LEFT", "RIGHT"]
self.hitbox_type = "NONE"
self.prev_type = "NONE"

self.sprite = sprite("hitbox.png")
self.parent = None

self.offsetX = 0
self.offsetY = 0


#PlayerHitbox loop

self.alpha = 1 if Game.debug else 0

if self.parent:
    self.x = self.parent.x + self.offsetX
    self.y = self.parent.y + self.offsetY

if self.hitbox_type not in self.hitbox_types:
    print("Invalid PlayerHitbox type assigned. Reverting...")
    self.hitbox_type = self.prev_type
else:
    self.prev_type = self.hitbox_type
