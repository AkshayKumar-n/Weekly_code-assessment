import re

def validation(name,bgroup,pincode,mobno,email,last_donated_date):

    val1 = re.match("([a-z]+)([a-z]+)([a-z]+)$",name)
    val2 = re.match("/^(A|B|AB|O)[+-]$/",bgroup)
    val3 = re.match("^[1-9][0-9]{5}$",pincode)
    val4 = re.match("^[6-9]\d{9}$",mobno)
    val5 = re.match("^\w+[\._]?\w+[@]\w+[.]\w{2,3}$",email)
    val6 = re.match("^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$",last_donated_date)

    if val1 and val2 and val3 and val4 and val5 and val6:

        return True
    else:

        return False