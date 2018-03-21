import base64
import time
import hashlib
import hmac
#shared secret from QR code link
def OTP(secret):
    qr_secret = secret
    secret = base64.b32decode(qr_secret)
    timer = str(hex(int(time.time() / 30)))
    timer = timer.replace("0x",'')
    #Make the timer in to Bytearray of 8 bytes with padding 0s.
    #Example:00000000AABBCCDD
    if (len(timer) % 2 == 1):
        timer = "0" + timer
    while (len(timer) < 16):
        timer = "00" + timer
    byte_timer = bytes.fromhex(timer)
    HMAC = hmac.new(secret, byte_timer, hashlib.sha1).digest()

    #To determine the starting point of continuous 4 bytes
    offset = HMAC[19] & 0x0F

    FourBytes = HMAC[offset : offset + 4]
    #print(FourBytes[0],FourBytes[1],FourBytes[2],FourBytes[3])

    #Make the leftmost bit to 0
    LeftByte = str(hex(FourBytes[0] & 0x7F))
    RestByte = str(hex(FourBytes[1]))+str(hex(FourBytes[2]))+str(hex(FourBytes[3]))
    Key = int((LeftByte + RestByte).replace("0x",''),16)
    Key = int(Key % 1e6)
    #padding 0 if only 5 digits
    return str(Key).zfill(6)