class Band():
    
    instances=[] # same name of test file

    def __init__(self, name, members):
        # the name is string same name of test file
        self.name = name 
        # the members is array(list) same name of test file
        self.members = members
        # to get all musicans
        Band.instances.append(self)
    
    def play_solos(self):
        solo_musican = []
        
        for x in self.members:
            solo_musican.append(x.play_solos())
        return solo_musican
    
    #class method
    
    @classmethod
    def to_list(cls):
        return cls.instances
    
class Musician():
    """
    this class is a base class!
    """

    def __init__(self, name):
        self.name = name
    
    def play_solos(self):
        pass 
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def get_instrument(self):
        pass 

    def play_solo(self):
        return self.play_solos()


class Guitarist(Musician):
    """
    Guitar Class
    """
    def __init__(self, name):
        self.name = name
    
    # def __str__(self):
    #     return f'Hello, Im {self.name} & i play with guitar'
    
    # def __repr__(self):
    #     return f'it is the guitarist instance.and the name is {self.name}'
    
    def get_instrument(self): # from test file 
        return "guitar"

    def play_solos(self): # from test file 
        return "face melting guitar solo"

class Bassist(Musician):
    """
    Bass Class
    """
    def __init__(self,name):
        self.name=name
    
    # def __str__(self):
    #     return f'Hello, Im {self.name} & i play with bass'
    
    # def __repr__(self):
    #     return f'it is the bassistit instance.and the name is {self.name}'
    
    def get_instrument(self): # from test file 
        return "bass"

    def play_solos(self): # from test file 
        return "bom bom buh bom"

class Drummer(Musician):
    """
    Drum Class
    """
    def __init__(self,name):
        self.name=name
    
    # def __str__(self):
    #     return f'Hello, Im {self.name} & i play with drum'
    
    # def __repr__(self):
    #     return f'it is the drummer instance.and the name is {self.name}'
    
    def get_instrument(self): # from test file 
        return "drums"
    
    def play_solos(self): # from test file
        return "rattle boom crash"