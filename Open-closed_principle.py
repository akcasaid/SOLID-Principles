# Open/Closed Principle (OCP)

'''
 Open/Closed Principle, yazılım bileşenlerinin (sınıflar, modüller, fonksiyonlar vs.) genişlemeye açık ancak değişikliğe kapalı olması gerektiğini belirtir. 
 Bu ilke, mevcut kodun değiştirilmeden yeni davranışların eklenmesini teşvik eder. 
 Yani, bir sınıfın işlevselliği genişletilmek istendiğinde, sınıfın kendisinde değişiklik yapmak yerine bu işlevselliği genişletebilecek şekilde tasarlanmalıdır.
 
 Özetle: 
 Bir sınıf ya da fonksiyon halihazırda var olan özellikleri korumalı ve değişikliğe izin vermemelidir. 
 Yani davranışını değiştirmiyor olmalı ve yeni özellikler kazanabiliyor olmalıdır.
 
 '''

# İlk örnek OCP'ye uygun değildir.
'''
Aşağıdaki örnekte, farklı türdeki çalışanların maaşlarını hesaplayan bir sistem gösterilmektedir. 
Bu sistem, Open/Closed Principle'a uygun değildir çünkü yeni bir çalışan türü eklemek istediğimizde SalaryCalculator sınıfını değiştirmemiz gerekecektir.

'''
class Employee:
    def __init__(self, type_of_employee, base_salary):
        self.type_of_employee = type_of_employee
        self.base_salary = base_salary

class SalaryCalculator:
    def calculate_salary(self, employee):
        if employee.type_of_employee == "Permanent":
            return employee.base_salary + 500
        elif employee.type_of_employee == "Temporary":
            return employee.base_salary + 100
        # Yeni bir çalışan türü eklemek istenirse, bu metodun değiştirilmesi gerekir.




# Yukarıda verilen kodun OCP'ye uygun halde iyileştirilmiş hali aşağıdadır.
        
class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def calculate_salary(self):
        pass

class PermanentEmployee(Employee):
    def calculate_salary(self):
        return self.base_salary + 500

class TemporaryEmployee(Employee):
    def calculate_salary(self):
        return self.base_salary + 100

class SalaryCalculator:
    def calculate_salary(self, employee):
        return employee.calculate_salary()



'''
Bu tasarımda, Employee sınıfı soyut bir temel sınıftır ve calculate_salary metodunu her türlü çalışan için ayrı ayrı uygulayan türetilmiş sınıflar vardır.
 SalaryCalculator sınıfı, hangi tür çalışanın maaşını hesapladığını bilmeden, bu işlevselliği çalışan sınıfının kendisine bırakır. 
 Bu sayede, yeni bir çalışan türü eklemek istediğimizde, yalnızca yeni bir sınıf ekleyerek ve calculate_salary metodunu uygulayarak genişletme yapabiliriz;
   SalaryCalculator sınıfını veya diğer çalışan sınıflarını değiştirmemize gerek kalmaz.
Bu yaklaşım, sistemimizin genişlemeye açık ancak değişikliğe kapalı olmasını sağlar.

'''

# Çrnek çıktı almak için:


permanent_employee = PermanentEmployee(base_salary=3000)
temporary_employee = TemporaryEmployee(base_salary=1500)

# Maaş hesaplayıcı sınıfını kullanarak maaşları hesaplıyoruz.
salary_calculator = SalaryCalculator()

# Kalıcı ve geçici çalışanların maaşlarını hesaplayıp yazdırıyoruz.
print(f"Permanent Employee Salary: {salary_calculator.calculate_salary(permanent_employee)}")
print(f"Temporary Employee Salary: {salary_calculator.calculate_salary(temporary_employee)}")
