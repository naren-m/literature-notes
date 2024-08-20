# Side Channel Attack

Side channel attacks are often the most creative sort of exploitation.
A side channel attack exploits the unintended information exhaust of an application or device. For example, the electrical emissions of a computer monitor or integrated chip (IC).

Side channel attacks can be avoided by [[Encryption]]

[[Rowhammer]] attacks are an example of a side channel attack.


When securing applications, the focus is on inputs and outputs, the conventional attack points. This is the traditional approach even for hardware and UEFI.
However, hardware exists at a physical level. Computers can sometimes be attacked based on physical side effects, such as power, time, and sound. Hackers use Side Channel attacks to interpret these side effects. They can then obtain sensitive data and even secrets.

The most common Side Channel attacks are:
- Timing attack. An attack that measures the amount of time to complete a calculation or algorithm.
- Power analysis attack. An attack that measures power consumption for various calculations, algorithms, or activities.
- Electromagnetic attack. An attack that measures leaked electromagnetic radiation.
- Acoustic attack. An attack that measures amount or deviation of sound related to a calculation, algorithm, or activity.
- And many more


Tel Aviv University has done significant research on side channel attacks. 
For example: https://bit.ly/3xOfuLt

What offers effective protection against a side channel attack? Cryptography!