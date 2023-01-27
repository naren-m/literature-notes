# Zero-Trust

Philosophy: “never trust, always verify”

## Definition

### My definition

- Approach to security by eliminating implicit trust(based on Firewals, i-tables etc.,).
- Core principle is “never trust, always verify”.
- Uses strong authentication to verify the workloads.

### From Articles

A zero-trust networking is based on a security model that establishes trust through continuous authentication and monitoring of each network access attempt. It's different from the traditional model of assuming everything in a corporate network can be trusted.

### What are the benefits of a zero-trust network?

The benefits of a zero-trust network include:

- Greater security. Attacks usually originate far from the intended target, such as a corporate network. Attackers also frequently piggyback on approved users' access before moving laterally within a network to gain access to targeted assets.
- Ability to manage dispersed infrastructure. Network infrastructure has become more complex and dispersed, with data, applications, and assets spread across many cloud and hybrid environments. Users are working from many locations as well, making it more difficult to define a defensible perimeter. In fact, simply securing a perimeter is an outdated approach to a complex challenge that varies widely from company to company.
- Simpler approach to security. Historically, organizations have layered security solutions to block attackers. Over time, this can create security gaps for attackers to compromise. With zero-trust networking, security is seamless and more well integrated throughout networks.

### How does a zero-trust network operate?

- The zero-trust philosophy is "never trust, always verify." Traditionally, network perimeters were secured by verifying user identity only the first time a user or device entered an environment. With zero trust, networks are built around "microperimeters," each with its own authentication requirements.
- Microperimeters surround specific assets, such as data, applications, and services. Through segmentation gateways, authentication is defined not just by user identity but also by parameters such as device, location, time stamp, recent activity, and description of the request. These complex authentications are more secure and can occur passively in the background.
- Narrowly defined authentication rules protect networks from unauthorized users. They also grant approved users only the specific privileges for which they have an immediate need. This workflow helps ensure that even if attackers gain entry, they can't move freely in the network environment.

## Reference

<https://www.cisco.com/c/en/us/solutions/automation/what-is-zero-trust-networking.html>
<https://www.paloaltonetworks.com/cyberpedia/what-is-a-zero-trust-architecture>
