class Russia:
    def capital(self):
        print("Moscow is the capital of Russia")
    def language(self):
        print("Russian is the primary language of Russia")
    def type(self):
        print("Russia is a developed country")

class India:
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is most widely used in India")
    def type(self):
        print("India is a developing country")

obj_rus = Russia()
obj_ind = India()

for country in(obj_rus,obj_ind):
    country.capital()
    country.language()
    country.type()