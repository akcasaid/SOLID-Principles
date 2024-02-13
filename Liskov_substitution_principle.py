#Liskov Substitution Principle (LSP)

'''
Liskov Substitution Principle (LSP), türetilmiş sınıfların, temel sınıflarının yerine geçebilir olması gerektiğini belirtir.
 Bu ilke, bir alt sınıfın, üst sınıfın davranışlarını değiştirmemesi ve üst sınıfın beklediği özellikleri koruması gerektiğini ifade eder. 
 Bu şekilde, alt sınıf nesneleri, üst sınıf nesnelerinin yerine kullanılabilmelidir.
 
 Özetle: Kodlarımızda herhangi bir değişiklik yapmaya gerek duymadan alt sınıfları, türedikleri(üst) sınıfların yerine kullanabilmeliyiz. '''

# Aşağıdaki kod örneğinde Liskov Substitution Principle (LSP)' ye uygun olmayan bir örnek verilmiştir.

class Bird:
    def fly(self):
        return "Bu kuş uçabilir"

class Eagle(Bird):
    def fly(self):
        return "Kartal yükseklerde uçar"

class Penguin(Bird):
    def fly(self):
        raise NotImplementedError("Penguenler uçamaz")

'''
Bu örnekte, bir üst sınıf ve bu sınıftan türetilmiş iki alt sınıf gösterilmektedir. 
Ancak, alt sınıflardan biri üst sınıfın beklediği davranışı bozmaktadır.
Penguin sınıfı Bird sınıfından türemesine rağmen, fly metodunu uygulayamaz çünkü penguenler uçamaz. 
Bu durum, LSP'ye aykırıdır çünkü Bird türündeki bir nesnenin yerine Penguin türündeki bir nesne kullanıldığında, beklenen davranış bozulmaktadır.
'''



# Yukarıda verilen kod LSP'ye uygun hale getirilerek düzeltilmiş hali aşağıdadır.



class Bird:
    pass

class FlyingBird(Bird):
    def fly(self):
        return "Bu kuş uçabilir"

class Eagle(FlyingBird):
    def fly(self):
        return "Kartal yükseklerde uçar"

class Penguin(Bird):
    pass


'''
LSP'ye uygun bir tasarım, uçabilen kuşlar ile uçamayan kuşları farklı hiyerarşilere ayırmayı içerir.
Bu düzenlemeyle, Bird sınıfı artık tüm kuşların genel bir temelidir. 
Uçma yeteneğine sahip kuşlar için ayrı bir FlyingBird sınıfı tanımlanmıştır. 
Bu sayede, Eagle gibi uçabilen kuşlar FlyingBird sınıfından türetilirken, Penguin gibi uçamayan kuşlar doğrudan Bird sınıfından türetilir. 
Bu yapı, tüm alt sınıfların üst sınıfın yerine geçebileceği bir durum sağlar ve LSP'ye uyar.

Bu düzenleme, sistemdeki sınıfların doğru şekilde kullanılmasını sağlar ve tür hiyerarşisinin mantıklı bir şekilde organize edilmesine yardımcı olur.
Bu, kodun okunabilirliğini ve sürdürülebilirliğini artırır.

'''