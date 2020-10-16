'''
        DR1 Spheres and Materials

Creado por:

    Juan Fernando De Leon Quezada   Carne 17822

Raytracer Engine 

'''
from gl import *
from texture import Texture
from obj import ObjReader
from envmap import Envmap
from sphere import *

if __name__ == '__main__':
    '''Main Program'''

    brick = Material(diffuse = color(0.8, 0.25, 0.25 ), spec = 16)
    stone = Material(diffuse = color(0.4, 0.4, 0.4 ), spec = 32)
    mirror = Material(spec = 64, matType = REFLECTIVE)
    glass = Material(spec = 64, ior = 1.5, matType= TRANSPARENT) 

    boxMat = Material(texture = Texture('./TexturesAndMaterials/wood2.bmp'))

    earthMat = Material(texture = Texture('./TexturesAndMaterials/earthDay.bmp'))
    jupiterMat = Material(texture = Texture('./TexturesAndMaterials/2k_jupiter.bmp'))
    moonMat = Material(texture = Texture('./TexturesAndMaterials/2k_moon.bmp'))
    sunMat = Material(texture = Texture('./TexturesAndMaterials/2k_sun.bmp'))

    bookMat = Material(texture = Texture('./TexturesAndMaterials/book1-1.bmp'))
    concretewallMat = Material(texture = Texture('./TexturesAndMaterials/concretewall.bmp'))
    bookMat_2 = Material(texture = Texture('./TexturesAndMaterials/book2-1.bmp'))
    bookMat_3 = Material(texture = Texture('./TexturesAndMaterials/book3.bmp'))
    bookMat_4 = Material(texture = Texture('./TexturesAndMaterials/book4.bmp'))


    width = 500
    height = 500
    r = Raytracer(width,height)
    r.glClearColor(0.2, 0.6, 0.8)
    r.glClear()

    r.envmap = Envmap('./TexturesAndMaterials/intothewoods.bmp')

    # Lights
    r.pointLights.append( PointLight(position = V3( -3.3,-2.5,-10), intensity = 0.7))
    r.pointLights.append( PointLight(position = V3( -3.2,-2.5,-9.75), intensity = 0.7))
    r.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.5)
    r.ambientLight = AmbientLight(strength = 0.1)

    # Desk
    r.scene.append( AABB(V3(0, -3, -10), V3(10, 0.1, 5) , boxMat, 'box' ) )
    r.scene.append( AABB(V3(-5, -5.45, -10), V3(0.1, 5, 5) , boxMat, 'box' ) )
    r.scene.append( AABB(V3(5, -5.45, -10), V3(0.1, 5, 5) , boxMat, 'box' ) )

    # # Box of balls
    r.scene.append( AABB(V3(-3, -2.75, -10), V3(1.5, 1, 1) , glass, 'basket' ) )
    
    # # Balls
    r.scene.append( Sphere(V3( -3, -2.75, -10), 0.1, earthMat))
    r.scene.append( Sphere(V3( -3.25, -2.75, -9.80), 0.1, jupiterMat))
    r.scene.append( Sphere(V3( -2.75, -2.75, -9.80), 0.1, moonMat))
    r.scene.append( Sphere(V3( -3.25, -2.65, -9.90), 0.1, sunMat))

    # # Books
    r.scene.append( AABB(V3(3, -2, -10), V3(0.45, 1.75, 1.5) , bookMat, 'box' ) )
    r.scene.append( AABB(V3(3.5, -2, -10), V3(0.45, 1.75, 1.5) , bookMat_2, 'box' ) )
    r.scene.append( AABB(V3(4, -2, -10), V3(0.45, 1.75, 1.5) , bookMat_3, 'box' ) )
    r.scene.append( AABB(V3(4.5, -2, -10), V3(0.45, 1.75, 1.5) , bookMat_4, 'box' ) )

    r.scene.append( AABB(V3(0,0,-12.5), V3(15,10,10), concretewallMat, 'room') )

    r.rtRender()

    r.glFinish('output.bmp')