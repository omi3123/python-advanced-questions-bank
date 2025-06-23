"""
ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. If the function is passed a valid PIN string, return true, else return false
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false
"""
def validatePin(pin):
    if len(pin) in [4, 6]:
        if pin.isdigit():
            return True
    return False
print(validatePin("12345"))