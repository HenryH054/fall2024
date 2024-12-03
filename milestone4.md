# Milestone 4

Session hijacking is not just a theoretical concern—it has been demonstrated in numerous real-world incidents, each underscoring the critical need for secure session management. Three notable examples, Firesheep, the Gmail CSRF attack, and the MySpace Samy Worm, illustrate the diverse methods used by attackers and the significant impacts these breaches have had on users and organizations alike.

## Hack #1

Firesheep highlighted the vulnerabilities of public Wi-Fi networks by intercepting unencrypted cookies exchanged between users and websites like Facebook and Twitter. This browser extension allowed attackers to impersonate users by simply capturing their session cookies, enabling unauthorized access to personal accounts. Firesheep did not directly result in monetary loss or data breaches on a massive scale, but its significance lay in demonstrating the risks of unencrypted session transmissions. The incident spurred a widespread push toward implementing HTTPS, drastically improving the standard for secure web communication and inspiring changes in how platforms protect their users.

## Hack #2

The Gmail Cross-Site Request Forgery (CSRF) attack revealed how an absence of robust CSRF protections could compromise even a widely trusted service. This attack tricked users into clicking malicious links that exploited Gmail's session vulnerabilities. By hijacking user sessions, attackers could send emails, access sensitive data, and impersonate victims without needing direct access to their credentials. While the number of users affected is unclear, the attack exposed significant weaknesses in session handling and forced Gmail to strengthen its security practices. This case emphasized the importance of token-based CSRF prevention and vigilance in web application design.

## Hack #3

The MySpace Samy Worm represents a classic example of session hijacking through client-side exploitation. The worm exploited weak input validation in MySpace's system, using JavaScript to steal session cookies and propagate itself across the platform. Within 24 hours, it had infected over one million profiles, showcasing the scale and speed of such attacks when platforms lack sufficient safeguards. Although the attack was not monetarily driven, it disrupted MySpace operations and significantly impacted user trust. The incident highlighted the dangers of inadequate input sanitization and the need for strong server-side defenses to prevent similar exploits.

## Comparison

These three cases demonstrate the diverse techniques attackers use and their wide-ranging impacts. Firesheep showcased the importance of encrypting session data to protect users in vulnerable network environments. Gmail's CSRF attack highlighted the necessity of server-side defenses like anti-CSRF tokens to guard against user manipulation. Meanwhile, the MySpace Samy Worm underscored the catastrophic potential of failing to sanitize inputs, which can lead to widespread disruption and loss of user confidence.

Despite differences in execution and consequences, these incidents converge on a single point: insecure session management presents a severe threat to both users and organizations. Each case illustrates how attackers exploit technical weaknesses, underscoring the need for vigilant and evolving security practices in the development and maintenance of digital platforms.
