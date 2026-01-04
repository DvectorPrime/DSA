class CaesarCiper:
    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26

        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord('A'))
            decoder[i] = chr((i - shift) % 26 + ord('A'))

        self._forward = "".join(encoder)
        self._backward = "".join(decoder)

    def encrypt(self, message):
        return self._translate(message, self._forward)
    
    def decrypt(self, secret):
        return self._translate(secret, self._backward)
    
    def _translate(self, original, code):
        msg = list(original)

        for i in range(len(msg)):
            j = ord(msg[i].upper()) - ord('A')
            if j == -33:
                msg[i] = " "
            else:
                msg[i] = code[j]

        return "".join(msg)
    
ciper_5 = CaesarCiper(5)

message = "i wNAT TO SEE"
hidden_message = ciper_5.encrypt(message)
print(hidden_message)
print(ciper_5.decrypt(hidden_message))