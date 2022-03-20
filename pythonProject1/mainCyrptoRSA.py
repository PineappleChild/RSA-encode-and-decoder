import random


def gcd(aVal, bVal):
    if bVal == 0:
        return aVal;
    return gcd(bVal, aVal%bVal);

def isPrime(value):
    if value <= 3:
        if value > 1:
            return True
    if value%2 == 0 or value%3 == 0:
        return False;
    pValue = 5
    while pValue ** 2 <= value:
        if value % pValue == 0 or value % (pValue + 2) == 0:
            return False
        pValue += 6
    return True

class keyGenerator:
    def keyGemeratpr(self):
        self.p = 0;
        self.q = 0;
        self.n = 0;
        self.k = 0;
        self.d = 0;

    def setP(self, pValue):
        if isPrime(pValue):
            self.p = pValue;
        return None;

    def setQ(self, qValue):
        if isPrime(qValue):
            self.q = qValue;
        return None;

    def getD(self):
        return self.d;

    def getN(self):
        return self.n;

    def generateN(self):
        self.n = self.p * self.q
        return self.n

    def generateK(self):
        self.k = (self.p - 1) * (self.q - 1)
        return self.k

    def generateE(self):
        possibleE = []
        kValue = self.generateK()
        for a in range(2, kValue):
            if gcd(a, kValue) == 1:
                possibleE.append(a)
        self.e = possibleE[random.randint(0, possibleE.__len__())]
        # return possibleE

    def generateD(self):
        possibleVal = [];
        for a in range(1,(self.n + self.k)):
            if a * self.e % self.k == 1:
                if a >= self.n and a >= self.k:
                    possibleVal.append(a);
        self.d = possibleVal[0];
        return possibleVal

    def getPublicKey(self):
        return "(" + str(self.n) + ", " + str(self.e) + ")";

    def getPrivateKey(self):
        return "(" + str(self.n) + ", " + str(self.d) + ")";

    def encryptMessage(self, msg):
        msgArr = [];
        encrypted = [];

        for a in msg:
            msgArr.append(ord(a));
        for b in msgArr:
            encrypted.append(self.powerMod(b, self.e, self.n))
        print(msgArr)

        return encrypted

    def encToEng(self, enc):
        msgTxt = "";
        for c in enc:
            msgTxt += chr(c);
        print(msgTxt + "\n" + str(enc));

    def decryptMessage(self, msg, d, n):
        encrypted = [];
        msgArr = [];
        msgTxt = "";
        for a in msg:
            encrypted.append(self.powerMod(a, d, n))
        for b in encrypted:
            msgArr.append(chr(b));
            msgTxt += chr(b);
        return msgTxt

    def powerMod(self, base, exponent, modulus):
        if modulus == 1:
            return 0;
        result = 1;
        base = base % modulus;
        while (exponent > 0):
            if (exponent % 2 == 1):
                result = (result * base) % modulus;
            exponent = exponent >> 1;
            base = (base * base) % modulus;
        return result;

class test:
    #must be prime numbers
    pValue = 617;
    qValue = 967;

    message = "deez nuts"

    keyGen = keyGenerator();

    keyGen.setP(pValue);
    keyGen.setQ(qValue);

    keyGen.generateN();
    keyGen.generateK();
    keyGen.generateE();
    keyGen.generateD();

    print(keyGen.getPublicKey());
    print(keyGen.getPrivateKey());
    # print(message)
    print("Encrypted: ");
    message = keyGen.encryptMessage(message);
    print(keyGen.encToEng(message));
    print("Decrypted: ");
    print(keyGen.decryptMessage(message, keyGen.getD(), keyGen.getN()));

test();
exit();