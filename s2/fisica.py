import math

def temps_caiguda_lliure(h):
    # y = h - 1/2gt^2
    return math.sqrt(h / (0.5 * 9.81))

def parabola(v, alpha):
    alpha = math.pi * alpha / 180
    vx = v * math.cos(alpha)
    vy = v * math.sin(alpha)

    t = 2 * vy / 9.81
    distancia = 2 * (vx*vy) / 9.81
    return t, distancia

def longitud_pendol(t):
    return 9.81 * (t / (2 * math.pi))**2
