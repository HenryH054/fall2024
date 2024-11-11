# Milestone 3

## Introduction

In the pursuit of making modern life easier, we have developed something known as session management. Session management is the answer to how we, as modern individuals, can avoid signing into our bank accounts every time we open a browser and how we can start automatically scrolling as soon as we open TikTok. But in practice, what is actually happening?

Session management can be implemented through a variety of means, but one of the more common methods is cookies. Cookies are unique identifiers that a client sends to a server, which the server then recognizes, granting the client access to otherwise password-protected information—all in the effort of never needing the user to sign in. This creates a problem known as session hijacking. Session hijacking is an attack that allows someone to gain access to that unique identifier and then pretend to be you, all without ever having gained access to your password.

This attack vector can be mitigated through proper coding techniques, but it is never fully guaranteed to be protected against. That being said, in the modern era, it is critical that we harden our systems as much as possible because so much of an average person's life is now online.

As such, this report will investigate session hijacking. The report will begin by outlining the fundamentals of session management, such as how keys are secured and alternatives to cookies. It will then discuss session hijacking and the methodology used to attack systems. The report will also highlight real-world instances where this attack vector has caused damage to individuals and businesses. Finally, possible solutions to session hijacking will be discussed, followed by a guide on what to do if your session is hijacked.

## Background

Session management is a key aspect of modern web applications, enabling seamless user experiences while ensuring security. It revolves around maintaining a user's state as they interact with a website or application, ensuring that the system recognizes the user without requiring them to repeatedly log in. Sessions are crucial for applications that require personalized experiences or sensitive data access, such as online banking or social media platforms. These sessions are typically tracked using session identifiers (session IDs) that are stored either server-side or client-side (often via cookies).

Sessions are created when a user logs in or initiates interaction with a web application. Upon successful authentication, the server generates a unique session ID, which is sent to the user's browser and stored as a cookie. This session ID acts as a key that identifies the user to the server on subsequent requests. As the user navigates through the site, each request includes the session ID, allowing the server to retrieve and maintain the user's state, such as login status, preferences, or activity history. The session is typically maintained until it expires, the user logs out, or the session is explicitly terminated by the server.

Secure session management is essential to protect sensitive user data and prevent unauthorized access. If session management is improperly handled, it can expose users to attacks like session hijacking, where an attacker gains control of a user's session and can impersonate them without needing the user's password. To mitigate these risks, secure practices are critical. This includes using secure cookie flags (HTTPOnly, Secure), encrypting session data, implementing session expiration policies, and employing mechanisms like multi-factor authentication (MFA) to further strengthen session security. By adopting robust session management practices, organizations can protect user data and maintain trust, which is crucial in an increasingly digital world.
