class Duck(object):
    def __init__(self, input_name):
        self.__hidden_name = input_name
    def get_name(self):
        print("내부 겟터")
        return self.__hidden_name
    def set_name(self, input_name):
        print("내부 셋터")
        self.__hidden_name = input_name 
    name = property(get_name, set_name)
if __name__ == "__main__":
    duck  = Duck('John')
    print(duck.name)
    duck.name = 'Harry'
    print(duck.name)
    #duck.__hidden_name