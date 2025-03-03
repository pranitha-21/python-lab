class Password_manager:
    def __init__(self):
        self.old_passwords=[]
    def get_password(self):
        return self.old_passwords[-1] if self.old_passwords else None
    def set_password(self,new_password):
        if len(self.old_passwords)==0:
            self.old_passwords.append(new_password)
            print("password updated")
            return
        for i in self.old_passwords:
            if i==new_password:
                print("password already used")
                return  
            else:
                self.old_passwords.append(new_password)
                print("password updated")
    def is_correct(self,password):
        return password==(self.old_passwords[-1] if self.old_passwords else None)

pm=Password_manager()
while True:
    a=int(input("Enter number:\n 1.set password\n 2.getpassword \n 3.check password\n 4.exit\n"))
    if a==1 :
        pm.set_password(input("password:"))
    elif a==2:
        print(pm.get_password())
    elif a==3:
        print(pm.is_correct(input("Enter password to check:")))
    elif a==4:
        break
    else: print("not valid")
