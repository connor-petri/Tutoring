def platform_hitbox(parent, box_type, offsetX = 0, offsetY = 0):
    p = PlatformHitbox()

    p.hitbox_type = box_type
    p.parent = parent
    p.offsetX = offsetX
    p.offsetY = offsetY

    return p
