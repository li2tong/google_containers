
from aligo import Aligo

if __name__ == '__main__':
    ali = Aligo()  
    
    user = ali.get_user()  
    print(user.user_name, user.nick_name, user.phone)  
    ali.upload_file('garbage_file')
  
