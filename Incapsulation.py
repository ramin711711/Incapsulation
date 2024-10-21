class InctoSm:
    def __init__(self, inc):
        self.__sm = inc*2.54 #'_' makes private, '__' makes extra private 

    def get_answer_sm(self):
        return self.__sm
    
    def set_answer_m(self, formula):
        self.__sm = self.__calculate_formula(formula)

    def __calculate_formula(self, formula):
        return self.__sm / formula

answer = InctoSm(10)
answer.set_answer_m(100)
# answer.__sm = 0  
print(f'{answer.get_answer_sm()} m')