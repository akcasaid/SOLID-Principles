#  Interface Segregation Principle (ISP)

'''
Interface Segregation Principle (ISP), hiçbir istemcinin kullanmadığı metodlara bağımlı olmamalıdır; büyük arayüzlerin daha küçük ve özelleşmiş arayüzlere bölünmesi gerektiğini ifade eder.
Bu ilke, sınıfların gereksiz metodları uygulamak zorunda bırakılmamasını ve istemcilerin yalnızca ihtiyaç duydukları metodlara bağlı olmalarını savunur.

Özetle: Sorumlulukların hepsini tek bir arayüze toplamak yerine daha özelleştirilmiş birden fazla arayüz oluşturmalıyız.
'''


# Aşağıdaki kod örneği ISP'ne uygun olmayarak yazılmıştır.

'''
Bu örnekte, birden fazla farklı işlevi bir arada barındıran tek bir arayüz gösterilmektedir. 
Bu tasarım, ISP'ye aykırıdır çünkü tüm uygulayıcılar bu arayüzdeki tüm metodları uygulamak zorundadır, bu da gereksiz metod bağımlılıklarına yol açar.

Bu örnekte, Robot sınıfı eat metodunu uygulamak zorundadır, ancak bu metod Robot için anlamsızdır.
'''


class IWork:
    def work(self):
        pass

    def eat(self):
        pass

class Human(IWork):
    def work(self):
        print("İnsan çalışıyor.")

    def eat(self):
        print("İnsan yemek yiyor.")
        
class Robot(IWork):
    def work(self):
        print("Robot çalışıyor.")

    def eat(self):
        # Robotlar yemek yemez, bu metodun burada olması mantıksız.
        pass

# Yukarıda yazılan kod örneği IPS'ye uygun halde düzeltilmiş hali aşağıya yazılmıştır.
    
''''''


class IWork:
    def work(self):
        pass

class IEat:
    def eat(self):
        pass

class Human(IWork, IEat):
    def work(self):
        print("İnsan çalışıyor.")

    def eat(self):
        print("İnsan yemek yiyor.")

class Robot(IWork):
    def work(self):
        print("Robot çalışıyor.")

'''
ISP'ye uygun bir tasarım, işlevsellikleri daha özelleşmiş arayüzlere ayırır, böylece sınıflar yalnızca ilgili oldukları metodları uygular.
Bu düzenlemeyle, work ve eat işlevleri ayrı arayüzlerde tanımlanmıştır (IWork ve IEat). 
Human sınıfı hem IWork hem de IEat arayüzlerini uygular, çünkü insanlar hem çalışır hem de yer.
 Robot sınıfı ise yalnızca IWork arayüzünü uygular, çünkü robotlar sadece çalışır ve yemez. 
 Bu yapı, sınıfların yalnızca ilgili oldukları işlevsellikleri uygulamasını sağlar ve gereksiz bağımlılıkları ortadan kaldırır, bu da kodun daha temiz ve sürdürülebilir olmasını sağlar.

'''


# Çıktı örneğini görmek için 


# İnsan ve robot nesnelerini oluşturuyoruz.
human = Human()
robot = Robot()

# İnsan için çalışma ve yeme işlevlerini çağırıyoruz.
print("İnsan:")
human.work()
human.eat()

# Robot için çalışma işlevini çağırıyoruz.
print("\nRobot:")
robot.work()

# Robot için 'eat' işlevini çağırmıyoruz çünkü robot bu işlevi uygulamaz.





























