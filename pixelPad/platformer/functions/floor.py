def floor(x, y, num = 5, offset = 100):
    platforms = []

    for i in range(num):
        p = Platform()
        p.x = x + i * offset
        p.y = y
        platforms.append(p)

    return platforms
