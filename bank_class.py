#practice question 4
# 4. Class Variables and Class Methods

class Bank:
    bank_name = "UBL"
    def __init__(self):
        pass
    @classmethod
    def change_bank_name(cls, new_name):
         cls.bank_name = new_name
         print(f"Bank name changed to {cls.bank_name}")

branch1 = Bank() #UBL
branch2 = Bank() #UBL

print(branch1.bank_name)
print(branch2.bank_name)

Bank.change_bank_name("HBL")

# change for all instances
print(branch1.bank_name)
print(branch2.bank_name)
