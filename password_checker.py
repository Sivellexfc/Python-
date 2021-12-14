def passwordChecker(psw):
    import re
    if len(psw) < 8:
        raise Exception("Parola en az 8 karakter olmalıdır.")
    elif not re.search("[a-z]",psw):
        raise Exception("Parola küçük harf içermelidir.")
    elif not re.search("[A-Z]",psw):
        raise Exception("Parola büyük harf içermelidir.")
    elif not re.search("[0-9]",psw):
        raise Exception("Parola rakam içermelidir.")
    elif not re.search("[_@$]",psw):
        raise Exception("Parola numeric alfabe içermelidir.")
    elif re.search("\s",psw):
        raise Exception("Parola boşluk içermemelidir.")
    else:
        print("Geçerli parola")



def passwordMaker():
    try:
        password = str(input("Parola Belirleyiniz ="))
        passwordChecker(password)
    except Exception as e:
        print(e)
        passwordMaker()
    else:
        print("geçerli parola else")
    finally:
        print("validation is completed")

passwordMaker()
