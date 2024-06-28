# TODO здесь писать код
import random
class MyDict(dict):
    def get(self, key, default_value=0):
        if key in self:
            return self[key]
        else:
            return default_value


SW_dict = MyDict()
SW_dict['Qui-Gon Jinn'] = 1
SW_dict['Dart_Vader'] = 2
SW_dict['Yoda'] = 3
print(SW_dict)
rand = random.choice(['Qui-Gon Jinn','Dart_Vader','Yoda','Obi-Wan Kenobi'])
print(SW_dict.get(rand))



