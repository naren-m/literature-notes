---
layout: "default"
title: "Cold Boot"
word_count: 238
created: "2024-11-28T18:24:53.149997"
modified: "2024-11-28T18:24:53.149997"
backlinks:
  - title: "Cryptography"
    url: "cse/cryptography/cryptography/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-01t08_11_36626zdesktop/"
  - title: "Cryptography"
    url: "logseq/bak/cse/cryptography/cryptography/2024-11-29t01_57_40576zdesktop/"
breadcrumbs:
  - title: "Home"
    url: "/"
  - title: "Cse"
    url: "/topics/cse//"
  - title: "Cryptography"
    url: "/topics/cse/cryptography//"
---
# Cold Boot



- Imaginative attacks are appearing every day. This is yet another excellent reason to implement defense in depth.
- The cold boot attack is a perfect example of creative from the evil empire

- Cold boot attack is another example of a [side channel attack](docs/cse/cryptography/side-channel-attack/index/).
There are actually two forms of cold-boot attacks. For one of the attacks, the term “cold-boot” is figurative.
For the other, the term “cold book” is a literal description. Brrrr...
Both categories of cold boot attacks requires physical access to the device.


When a computer is shutdown, data in the memory chips may persists for a few seconds, even minutes after the abrupt shutdown. Memory in the DRAM and SRAM are especially vulnerable to this sort of attack.
Most often the system is rebooted from a operating system on a secondary device, such as a usb stick. The hacker can then employ various techniques for dumping the sensitive information.


As an extension to the cold boot attack, you can actually freeze memory chips using liquid nitrogen, freeze sprays, and other techniques. When cooled, the memory will take longer to erode. This provides the hacker more time to remove sensitive data from the impacted memory.


Typically this attack is done Disgruntled employees. Mostly an inside job

In one of the Episodes of Burn Notice, lead charecters mom does this, uses liquid nitrogen
to freeze the chip and read the data off of it.