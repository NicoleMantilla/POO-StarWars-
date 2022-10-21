#Vamos a crear una aplicación de tipo cátalogo de personajes de Star Wars, algo similar a la wookipedia 
from enum import Enum


class Affiliation(Enum):
    REBEL_ALLIANCE = 0
    GALACTIC_EMPIRE = 1
    UNKNOWN = 2 

class StarWarsCharacter:
    def __init__(self, name, alias, affiliation):
        self.name = name 
        self.alias = alias
        self.affiliation = affiliation


        
    def __repr__(self):
        """
        Muestra una representación textual del objeto
        """
        return f'<{self.__class__}: {self.name} {self.alias}>'
"""__REPR__ Representación textual de un objeto. Muy bueno cuando estás depurando. Lo usa el programador. __STR__ lo usa el usuario"""

class ForceSensitive(StarWarsCharacter): #desciende de StarWars Characters, representa personajes sensibles a la fuerza. 
    def __init__(self, name, alias, affiliation, midichlorians):
        super().__init__( name, alias, affiliation)
        self.midichlorians = midichlorians
    def __repr__(self):
        return f'<{self.alias}: {self.name} {self.midichlorians}>'

    def unsheathe(self): #Este método solo sirve para que mis subclases lo entienda y no tenga que repetirlo 
        raise NotImplementedError()

chewie = StarWarsCharacter('Chewbacca', 'chewie', Affiliation.REBEL_ALLIANCE)
jabba = StarWarsCharacter('Jabba Dessilic Tiure', 'Jabba The Hutt', Affiliation.UNKNOWN)



#SUBCLASES DE ForceSensitive  HIJO

class Jedi(ForceSensitive):

    def master(cls, name, alias):
        #crea un maestro çjedi (con 100k modicholorianos ) cls es clase 
        return cls(name, alias, 100000)
    def __init__(self, name, alias, midichlorians):
       super().__init__(name, alias, Affiliation.REBEL_ALLIANCE, midichlorians)#Llama a la clase padre y le asigna el init, para distinguirse del otro init y los midichlorians.
    def unsheathe(self):
        return ' ▐▍░▐░░▣░▒░▒░▒▕|' + "█" * 40
    def __repr__(self):
        pass  
yoda = Jedi(alias = 'Master Yoda', name = 'Minch Yoda', midichlorians = 10000000000)

#Hacer repr en Jedi. 
"""Se le podría añadir a ForceSensitive este método:
def __repr__(self):
    return super().__repr__() + f' {self.midichlorians}'"""

class Sith(ForceSensitive):

    @classmethod
    def darklord(cls, name, alias):
        return cls(name, alias, 1200000)

    def __init__(self, name, alias, midichlorians):
       super().__init__(name, alias, Affiliation.GALACTIC_EMPIRE, midichlorians)#Llama a la clase padre y le asigna el init, para distinguirse del otro init y los midichlorians.
    
    def unsheathe(self):
        return '▔▔▔▔▔▔▔▔▔▝▔▔▔ ' + "█" * 40

luke = Jedi('Luke Skywalker', 'Luke', 10000)

palpatine = Sith('Palpatine', 'Darth Sidious', 100000)

print(luke.unsheathe())


