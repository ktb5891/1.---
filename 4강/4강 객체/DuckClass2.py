class Duck(object):
    def __init__(self, input_name):
        self.__hidden_name = input_name
    
    @property
    def name(self):
        print("내부 겟터")
        return self.__hidden_name
    @name.setter
    def name(self, input_name):
        print("내부 셋터")
        self.__hidden_name = input_name 


if __name__ == "__main__":
    duck = Duck('Harry')
    duck.name
    print(duck.name)
    duck.name = 'David'   
    print(duck.name)
