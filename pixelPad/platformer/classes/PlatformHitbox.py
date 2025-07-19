#PlatformHitbox start

# Properties
self.enabled = True

self.sprite = sprite("hitbox.png")

self.parent = None
self.offsetX = 0
self.offsetY = 0


#PlatformHitbox loop

self.alpha = 1 if Game.debug else 0

# Follow Parent
if self.parent:
    self.x = self.parent.x + self.offsetX
    self.y = self.parent.y + self.offsetY

