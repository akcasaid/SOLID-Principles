#Dependency Inversion Principle (DIP)

'''

Dependency Inversion Principle (DIP)
Açıklama:

Dependency Inversion Principle (DIP), yüksek seviyeli modüllerin düşük seviyeli modüllere doğrudan bağımlı olmamaları gerektiğini belirtir.
 Bunun yerine, her iki tür modül de soyutlamalara (arayüzlere veya soyut sınıflara) bağımlı olmalıdır. 
 Bu prensip, bağımlılıkların yönetimini kolaylaştırır ve kodun daha esnek olmasını sağlar.

Özetle: Sınıflar arası bağımlılıklar olabildiğince az olmalıdır özellikle üst seviye sınıflar alt seviye sınıflara bağımlı olmamalıdır.
'''

# Dependency Inversion Principle (DIP) uygun olmayan kod aşağıda yazılmıştır.

'''
Bu örnekte, NotificationManager sınıfı, e-posta göndermek için doğrudan EmailService sınıfına bağımlıdır.
Bu bağımlılık, mesajlaşma yöntemlerini genişletmek veya değiştirmek istediğimizde esnekliği azaltır.

'''


class EmailService:
    def send_email(self, message, receiver):
        print(f"Email '{message}' to {receiver} sent via EmailService")

class NotificationManager:
    def __init__(self):
        self.email_service = EmailService()

    def notify(self, message, receiver):
        self.email_service.send_email(message, receiver)


'''
Bu örnekte, NotificationManager sınıfı, e-posta göndermek için doğrudan EmailService sınıfına bağımlıdır. 
Bu bağımlılık, mesajlaşma yöntemlerini genişletmek veya değiştirmek istediğimizde esnekliği azaltır.
'''

# Yukarıda yazılan kodu DIP'ye göre uygun hale getiirlmiş hali aşağıda yazılmıştı.

'''
DIP'ye uygun bir tasarım, NotificationManager'ın bir mesajlaşma servisine genel bir arayüz üzerinden bağımlı olmasını sağlar. 
Bu şekilde, e-posta, SMS, veya başka herhangi bir mesajlaşma servisi kolaylıkla entegre edilebilir.
'''


from abc import ABC, abstractmethod

class MessageService(ABC):
    @abstractmethod
    def send_message(self, message, receiver):
        pass

class EmailService(MessageService):
    def send_message(self, message, receiver):
        print(f"Email '{message}' to {receiver} sent via EmailService")

class SMSService(MessageService):
    def send_message(self, message, receiver):
        print(f"SMS '{message}' to {receiver} sent via SMSService")

class NotificationManager:
    def __init__(self, message_service: MessageService):
        self.message_service = message_service

    def notify(self, message, receiver):
        self.message_service.send_message(message, receiver)

'''
Bu düzenleme ile NotificationManager, MessageService soyut sınıfına (veya arayüzüne) bağımlı hale gelir ve bu sınıfı uygulayan herhangi bir mesajlaşma servisi (EmailService, SMSService vb.) ile çalışabilir. 
Bu, yeni mesajlaşma servisleri eklendiğinde NotificationManager sınıfının değişikliğe uğramadan kullanılabilmesini sağlar, böylece sistem esnekliği ve genişletilebilirliği artar.
'''