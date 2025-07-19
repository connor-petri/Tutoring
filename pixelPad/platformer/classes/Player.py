#Player start
self.x = -400
self.y = 100

# Physics
self.vx = 0
self.vy = 0
self.grav = -1

self.x_speed = 2
self.jump_speed = 20

# Hitbox
self.hitbox = PlayerHitbox()
self.hitbox.parent = self
self.hitbox.scaleX = 1.5
self.hitbox.scaleY = 2
self.hitbox.offsetY = -20

# Spritesheets
idle_sheet = sprite("idle.png", 1, 11)
run_sheet = sprite("run.png", 1, 12)
jump_sheet = sprite("jump.png", 1, 1)
fall_sheet = sprite("fall.png", 1, 1)

# Animations
self.idle_animation = animation(idle_sheet, 24, 0, 10)
self.run_animation = animation(run_sheet, 24, 0, 11)
self.jump_animation = animation(jump_sheet, 12, 0, 0)
self.fall_animation = animation(fall_sheet, 12, 0, 0)

set_animation(self, self.idle_animation)


#Player loop

# x axis -------------------------------------------------------------------------------------
if key_is_pressed('d'):
    self.vx += self.x_speed
    self.skewY = 0

if key_is_pressed('a'):
    self.vx -= self.x_speed
    self.skewY = 180

# Gather Platform Collisions
platform_hitboxes = get_collision_list(self.hitbox, "PlatformHitbox")

for hitbox in platform_hitboxes:
    if hitbox.hitbox_type == "LEFT":
        self.vx = 0
        while get_collision(hitbox, "PlayerHitbox"):
            self.x -= 1
            self.hitbox.x -= 1

    elif hitbox.hitbox_type == "RIGHT":
        self.vx = 0
        while get_collision(hitbox, "PlayerHitbox"):
            self.x += 1
            self.hitbox.x += 1

self.vx *= .8
self.x += self.vx

# y axis -------------------------------------------------------------------------------------
self.vy += self.grav

# Refresh platform collisions
platform_hitboxes = get_collision_list(self.hitbox, "PlatformHitbox")

for hitbox in platform_hitboxes:
    if hitbox.hitbox_type == "TOP":
        self.vy = 0
        while get_collision(hitbox, "PlayerHitbox"):
            self.y += 1
            self.hitbox.y += 1
        self.y -= 1
        self.hitbox.y -= 1
    
    elif hitbox.hitbox_type == "BOTTOM":
        self.vy *= -0.75
        while get_collision(hitbox, "PlayerHitbox"):
            self.y -= 1
            self.hitbox.y -= 1


if key_was_pressed(" "):
    self.y += 5
    self.vy = self.jump_speed

self.vy *= 0.98
self.y += self.vy

# Animations -------------------------------------------------------------------------
if self.vy > 0:
    set_animation(self, self.jump_animation)
elif self.vy < 0:
    set_animation(self, self.fall_animation)
elif abs(self.vx) > 1:
    set_animation(self, self.run_animation)
else:
    set_animation(self, self.idle_animation)


