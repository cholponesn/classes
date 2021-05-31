class Human:

    def __init__(self,name,age,weight,height,gender):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.gender = gender
        self.soul = True
        self.viruses =[]

    def __str__(self):
        return self.name + str(self.age)

    def add_viruse(self,viruse):
        if viruse not in self.viruses:
            self.viruses.append(viruse)


human1 = Human(name='john',age=48,weight=90,height=185,gender='m')
human.add_viruse('covid19')
human1.add_viruse('covid19')