class CasNormal:
    def uneMethode(self):
        print ("normal")
class CasSpecial:
    def uneMethode(self):
        print("special")


def casQuiConvient(estNormal=True):
    return CasNormal() if estNormal else CasSpecial()

sk_test = casQuiConvient(1)
sk_test.uneMethode()
sk_test = casQuiConvient(0)
sk_test.uneMethode()
