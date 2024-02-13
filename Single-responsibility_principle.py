'''
Single Responsibility Principle (SRP): Bir sınıfın yalnızca bir sebepten dolayı değişmesi gerektiğini belirtir.
'''

# Aşağıdaki kod örneği SRP'ye uymamaktadır.

# Bu tasarım, SRP'ye aykırıdır çünkü UserManager sınıfı hem kullanıcı bilgilerini yönetmek (e-posta değişikliği gibi) hem de bu bilgileri veritabanına kaydetmekle sorumludur.

class UserManager:
    def __init__(self, user_name: str, email: str):
        self.user_name = user_name
        self.email = email

    def change_email(self, new_email):
        if self.validate_email(new_email):
            self.email = new_email
            self.save_to_database()

    def validate_email(self, email):
        return "@" in email  # Basit e-posta doğrulama

    def save_to_database(self):
        print(f"Saving {self.user_name} to database...")
        # Veritabanına kaydetme işlemi burada gerçekleşir




# Yukarıdaki kod SRP'ye uygun biçimde düzenlenerek aşağıya eklenmiştir. Bu iyileştirmede, kullanıcı yönetimi ve veritabanı işlemleri ayrı sınıflara taşınır.
        
class User:
    def __init__(self, user_name: str, email: str):
        self.user_name = user_name
        self.email = email

class EmailManager:
    @staticmethod
    def validate_email(email):
        return "@" in email  # Basit e-posta doğrulama

    @staticmethod
    def change_email(user, new_email):
        if EmailManager.validate_email(new_email):
            user.email = new_email

class DatabaseManager:
    @staticmethod
    def save_to_database(user):
        print(f"Saving {user.user_name} to database...")
        # Veritabanına kaydetme işlemi burada gerçekleşir


'''
Bu düzenlemede, User sınıfı yalnızca kullanıcı bilgilerini saklar. 
EmailManager kullanıcı e-postasını yönetirken, DatabaseManager kullanıcı bilgilerini veritabanına kaydetme işlemini üstlenir. 
Bu şekilde, her bir sınıfın yalnızca bir sorumluluğu olur, bu da kodun daha temiz, sürdürülebilir ve genişletilebilir olmasını sağlar.'''