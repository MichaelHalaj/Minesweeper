"""File for color types"""
# colors = (, , (0, 0, 0))
colors = {
    'light green': (10, 230, 78),
    'dark green': (100, 200, 100),
    'black': (50, 50, 50),
    'red': (200, 30, 85)
}


def get_color(color):
    return colors[color]
