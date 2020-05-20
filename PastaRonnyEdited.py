import numpy

class Pasta:
    def __init__(self, name, time):
        self.name = name
        self.time = time
 
pasta_list = [
    Pasta("penne", 8),
    Pasta("fusilli", 10),
    Pasta("farfalle", 12),
    Pasta("rigatoni", 7),
    Pasta("spaghetti", 7)]
pasta_number = numpy.random.randint(0, len(pasta_list))
pasta_object = pasta_list[pasta_number]
pasta_name = pasta_object.name
pasta_time = pasta_object.time

#print(pasta_tuple)
print("pasta number =", pasta_number)
print("pasta name =", pasta_name)
print("pasta time =", pasta_time)
print("Take", pasta_name, "out of the package, and put it in a large boiling pot of water. Boil for", pasta_time, "minutes.")