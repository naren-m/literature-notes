# LOJAX

UEFI ROOTKIT

SEDNIT, a cyberattack group, used LoJax malware to launch attacks against governments in Europe.
Here is more information on SEDNIT:

https://attack.mitre.org/groups/G0007/

LoJax attacks are based on a legitimate product: Absolute Software LoJack product, originally called Computrace. LoJack allowed consumers to locate their computer to prevent theft. LoJax compromises the LoJack product.
Unbeknownst to consumers, Lojack was preinstalled on computers from a variety of vendors.

https://bit.ly/3ACevzG


Lojack is installed in the UEFI firmware of a computer or device. It relies on networking to “call home” and provide location information. There are several vulnerabilities
• UEFI is network enabled
• Lojack is persistent
• Since it is based on an actual product, most anti-virus programs and scanners do not detect a LoJax attack
• And much more


The security strategy of Absolute Software appeared to be –
“Security by obscurity”
Security by obscurity is rarely an adequate security defense. Worst of all, Absolute Software was made aware of potential problems in 2009. However, Absolute Software downplayed the problem for several years.


SEDNIT leveraged the network capability of LoJack.
• Dump system information to a file
• Redirected data from the device to
a server controlled by attackers
• Save the image of the system firmware
• Wrote a malicious module into the image and saved back to the SPI flash memory
Important: Secure Boot may not prevent this attack.
