"""
write a class MobilePhone which has an init function with attributes for display size,
RAM and operating system.

This class should work seamlessly with the code below to print an automated review
"""

class MobilePhone:
    def __init__(self,display_size,ram,os):
        self.display_size = display_size
        self.ram = ram
        self.os = os

pearPhone = MobilePhone(5.5, "3GB", "yOS 11.2")
simsun = MobilePhone(5.4, "4GB", "Cyborg 8.1")

print(f"The new Pear Phone has a {pearPhone.display_size}"
      f"inch display. {pearPhone.ram} of RAM and runs on"
      f"the latest version of {pearPhone.os}. Its biggest competitor is"
      f"the Simsun phone which supports a similar Amoled {simsun.display_size}"
      f"inch display, {simsun.ram} of RAM and runs {simsun.os}.")