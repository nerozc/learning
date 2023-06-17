
class Employer:
    def __init__(self, name, salary,on_vacation,is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee
    def get_info(self):
        return self.name,self.salary,self.on_vacation
print('Введите количество работников')
employers_list = []
for i in range(0,5):
        worker = Employer((input('name'),int(input('salary')),input('on_vacation')),is_good_employee = input('is_good_employee')=='True')
        if not worker.is_good_employee:
             employers_list.append('Уволен')
        else :
             employers_list.append(worker.name)
for i in employers_list:
    print(i.get_info())