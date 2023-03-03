# Módulo que contiene todas las clases de micoorganismos a almacenar

# Clase padre para cualquier microorganismo
class Microorganism():
    # Atributos
    def __init__(self):
        self.__serial: int
        self.__position: tuple
        self.__medium: str
        self.__dangerous: bool
    
    # Setters
    def set_serial(self, serial):
        self.__serial = serial

    def set_position(self, row, column):
        self.__position = (row, column)

    def set_medium(self, growth_medium):
        self.__medium = growth_medium

    def set_medium(self, danger):
        self.__dangerous = danger

    # Getters
    def get_serial(self):
        return self.__serial 

    def get_position(self):
        return self.__position 

    def get_medium(self):
        return self.__medium 

    def get_medium(self):
        return self.__dangerous 

    # Deleters
    def del_serial(self):
        del self.__serial 

    def del_position(self):
        del self.__position 

    def del_medium(self):
        del self.__medium 

    def del_medium(self):
        del self.__dangerous 


# Clase para bacterias
class Bacterium(Microorganism):
    def __init__(self):
        super().__init__()
        self.__gram: str
        self.__form: str
    
    # Setters
    def set_gram(self, gram):
        self.__gram = gram
    
    def set_form(self, form):
        self.__form = form

    # Getters
    def get_gram(self):
        return self.__gram
    
    def get_form(self):
        return self.__form
    
    # Deleters
    def del_gram(self):
        del self.__gram
    
    def del_form(self):
        del self.__form


# Clase para virus
class Virus(Microorganism):
    def __init__(self):
        super().__init__()
        self.__infection_capacity: bool
        self.__preferred_host: str
    
    # Setters
    def set_infection_capacity(self, infection_capacity):
        self.__infection_capacity = infection_capacity
    
    def set_host(self, host):
        self.__preferred_host = host
    
    # Getters
    def get_infection_capacity(self):
        return self.__infection_capacity 
    
    def get_host(self):
        return self.__preferred_host 

    # Deleters
    def del_infection_capacity(self):
        del self.__infection_capacity 
    
    def del_host(self):
        del self.__preferred_host 


# Clase para priones 
class Prion(Microorganism):
    def __init__(self):
        super().__init__()
        self.__origin: str
        self.__danger_level: int

    # Setters
    def set_origin(self, origin_species):
        self.__origin = origin_species
    
    def set_danger_level(self, danger_level):
        self.__danger_level = danger_level
    
    # Getters
    def get_origin(self):
        return self.__origin 
    
    def get_danger_level(self):
        return self.__danger_level 

    # Deleters
    def set_origin(self):
        del self.__origin 
    
    def set_danger_level(self):
        del self.__danger_level 


# Clase para otros microorganismos
class Other(Microorganism):
    def __init__(self):
        super().__init__()
        self.__name: str
        self.__nature: str
        self.__description: str

    # Setters
    def set_name(self, name):
        self.__name = name
    
    def set_nature(self, nature):
        self.__nature = nature

    def set_description(self, description):
        self.__description = description
    
    # Getters
    def set_name(self):
        return self.__name 
    
    def set_nature(self):
        return self.__nature 

    def set_description(self):
        return self.__description 
    
    # Deleters
    def set_name(self):
        del self.__name 
    
    def set_nature(self):
        del self.__nature 

    def set_description(self):
        del self.__description 
