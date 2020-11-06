import sys, os
from random import randint

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

# Items del jugador.
class Inventario(object):
    balas = 1
    cuchillo = True

# Escena de muerte.
class Death(Inventario):

    def enter(self):
        input("")
        print('Moriste...')
        input(" ..")
        sys.exit(1)

### Escena inicial.
class Escena_Inicial(Inventario):

    def enter(self):
        escena_actual = 'escena_inicial'

        print ("")
        print ("Estás en escena inicial.")
        print ("")
        print('opciones: inventario, hablar, pegar, apuñalar, disparar\n')

        action = input("> ")
        action.lower()

        if action == "inventario":

            print ("")
            print ("Inventario:")
            print(Inventario.balas)
            print(Inventario.cuchillo)

            return escena_actual

        elif action == "hablar":

            print ("")
            print ("Texto")

            return 'death'

        if action == "pegar":

            print ("")
            print ("Texto")

            return 'death'

        elif action == "apuñalar":

            print ("")
            print ("Texto")
            Inventario.cuchillo = False

            return 'camino_1'

        elif action == "disparar":

            print ("")
            print ("Texto")
            Inventario.balas = 0

            return 'camino_2'

        else:
            print ("")
            print ("> Acción inválida.")
            return escena_actual


### Camino 1
class Camino_1(Inventario):

    def enter(self):
        escena_actual = 'camino_1'

        print ("")
        print ("Estás en camino 1")
        print ("")
        print('opciones: inventario, hablar, pegar, apuñalar, disparar\n')

        action = input("> ")
        action.lower()

        if action == "inventario":

            print ("")
            print ("Inventario:")
            print(Inventario.balas)
            print(Inventario.cuchillo)

            return escena_actual

        if action == "pegar":

            print ("")
            print ("Texto")

            return 'death'

        elif action == "apuñalar":

            if Inventario.cuchillo is True:
                print ("")
                print ("Texto")
                returnAux = 'death'
            elif Inventario.cuchillo is False:
                print ("")
                print ("Texto")
                returnAux = 'final_1'

            return returnAux

        elif action == "disparar":

            if Inventario.balas == 1:
                print ("")
                print ("Texto")

                returnAux = 'death'

            elif Inventario.balas == 0:
                print ("")
                print ("No tenés balas")
                returnAux = 'final_1'

            return returnAux

        elif action == "hablar":
            print ("")
            print ("Mulo del transa: Si no vas a comprar tomatelá porque te lleno de tiro' bigote.")

            return escena_actual

        elif action == "comprar":
            print ("")
            print ("Vos: Quiero 3.")
            print ("")
            print ("Sacás 90 pesos y se los pasás al mulo. Este agarra 2 papeles y te los pasa.")
            print ("Mulo del transa: Uno es pa' nosotro. Ahora tomateláaaaa daleee rápidoo eeeh.")
            print ("El mulo te empieza a disparar a los pies. Vos te vas corriendo.")

            return 'final_1'

        else:
            print ("")
            print ("> Acción inválida.")
            return escena_actual

### Escena final 1
class Final_1(Inventario):

    def enter(self):
        print ("")
        print ("Saliste de la Betha papá!!")
        print ("")
        input("..")
        return 'finished'

### Camino 2
class Camino_2(Inventario):

    def enter(self):
        escena_actual = 'camino_2'

        print ("")
        print ("Estás en camino 2.")
        print ("")
        print('opciones: inventario, hablar, pegar, apuñalar, disparar\n')

        action = input("> ")
        action.lower()

        if action == "inventario":

            print ("")
            print ("Inventario:")
            print(Inventario.balas)
            print(Inventario.cuchillo)

            return escena_actual

        if action == "pegar":
            print ("")
            print ("Te acercás al pibe y le metés una patada, haciendo que se caiga.")
            print ("Éste empieza a gritar, un vecino se acerca corriendo y te pega un cascotazo en la sien.")

            return 'death'

        elif action == "apuñalar":

            if Inventario.cuchillo is True:
                print ("")
                print ("Apuñalás al pibe. Agarrás la bicicleta y te vas andando a las chapas.")
                returnAux = 'final_2'
            elif Inventario.cuchillo is False:
                print ("")
                print ("No tenés un cuchillo.")
                returnAux = escena_actual

            return returnAux

        elif action == "disparar":

            if Inventario.balas == 1:
                print ("")
                print ("Sacás rápidamente tu revólver y le metés un tiro en la cabeza al pibe.")
                print ("Tomás la bicicleta y empezás a pedalear, sin embargo llamaste mucho la atención.")
                print ("Unos hombres salen a la vereda y comienzan a dispararte.")
                returnAux = 'death'

            elif Inventario.balas == 0:
                print ("")
                print ("No tenés balas")
                returnAux = 'final_2'

            return returnAux

        elif action == "hablar":
            print ("")
            print ("Vos: ¿No me prestás la bici amigo?.")
            print ("El pibe se te rie en la cara y se aleja pedaleando tranquilamente.")

            return 'final_2'

        elif action == "robar":
            print ("")
            print ("Te acercás rápidamente al pibe, lo agarrás y lo empujás lejos.")
            print ("Te subís a la bicicleta y en un parpadeo empezás a acelerar.")
            print ("Algunas personas te ven, pero ya estás muy lejos y no te pueden alcanzar.")

            return 'death'

        else:
            print ("> Acción inválida.")
            return escena_actual



### Escena final 2
class Final_2(Inventario):

    def enter(self):

        print ("")
        print ("Saliste de la Betha papá!!")
        print ("")
        input("..")
        return 'finished'

### Última escena
class Finished():

    def enter(self):

        print ("")
        print ("FIN.")
        print ("")
        input("..")
        return 'finished'

# ### Escena final 3
# class Final_3(Inventario):

#     def enter(self):
#         print ("")
#         print ("Saliste de la Betha papá!!")
#         print ("")
#         input("..")
#         return 'final_3'

class Map(object):

    scenes = {
        'escena_inicial': Escena_Inicial(),

        'camino_1': Camino_1(),
        'final_1': Final_1(),

        'camino_2': Camino_2(),
        'final_2': Final_2(),

        'death': Death(),
        'finished': Finished(),

        # 'camino_3': Camino_3(),
        # 'final_3': Final_3(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('escena_inicial')
a_game = Engine(a_map)
a_game.play()
