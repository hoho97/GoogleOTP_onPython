"# GoogleOTP_onPython" 


Please note that you take your own risk when using this program. This is wrote for learning purpose only and I cannot gaurantee the correctness of the output.

For safety please use Google Authenticator on iOS/Android.

Also please be reminded that your system should have correct time settings before using it.




This can be run on Python 3 only. Only a simple function to calculate OTP using python.

To use this tool, you need to decode the QR code of Authenticator first and have something like
otpauth://totp/Account?secret=XXXXXXXXXXXXXXXX&issuer=ISSUER

Use the secret XXXXXXXXXXXXXXXX from your QR code as your input

example usage: 

Simply Run main.py once downloaded.


or if you want to use this function somewhere else:

import OTP

OTP("XXXXXXXXXXXXXXXX")

And the program will return the OTP calculated.









