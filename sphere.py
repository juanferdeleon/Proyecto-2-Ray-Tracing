from gl import color
from arithmetics import *

WHITE = color(1,1,1)

class AmbientLight(object):
    def __init__(self, strength = 0, _color = WHITE):
        self.strength = strength
        self.color = _color

class PointLight(object):
    def __init__(self, position = V3(0,0,0), _color = WHITE, intensity = 1):
        self.position = position
        self.intensity = intensity
        self.color = _color

class Material(object):
    # Un material es un conjunto de propiedades que determina como interactua la
    # iluminacion con una superficie
    # En raytracing, el color de un pixel es determinado por el material de la superficie
    # que un rayo intercepta
    def __init__(self, diffuse = WHITE, spec = 0):
        # Diffuse es el color basico de un objeto. Cuando recibe luz, se esparce por igual en todas las direcciones.
        self.diffuse = diffuse
        self.spec = spec

class Intersect(object):
    def __init__(self, distance, point, normal, sceneObject):
        self.distance = distance
        self.point = point
        self.normal = normal
        self.sceneObject = sceneObject

class Sphere(object):
    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def ray_intersect(self, orig, dir):
        # Regresa falso o verdadero si hace interseccion con una esfera

        # Formula para un punto en un rayo
        # t es igual a la distancia en el rayo
        # P = O + tD
        # P0 = O + t0 * D
        # P1 = O + t1 * D
        #d va a ser la magnitud de un vector que es
        #perpendicular entre el rayo y el centro de la esfera
        # d > radio, el rayo no intersecta
        #tca es el vector que va del orign al punto perpendicular al centro
        L = sub(self.center, orig)
        tca = dot(L, dir)
        l = magnitud(L) # magnitud de L
        d = (l**2 - tca**2) ** 0.5
        if d > self.radius:
            return None

        # thc es la distancia de P1 al punto perpendicular al centro
        thc = (self.radius ** 2 - d**2) ** 0.5
        t0 = tca - thc
        t1 = tca + thc
        if t0 < 0:
            t0 = t1

        if t0 < 0: # t0 tiene el valor de t1
            return None
        
        hit = sum(orig, mul(dir, t0))
        norm = sub(hit, self.center)
        norm = div(norm, magnitud(norm))

        return Intersect(distance = t0, point = hit, normal = norm, sceneObject = self)
