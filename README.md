# sift

## Summary
Sift is a email verifier and cleaner. It's just a prototype that build on my on interest to understand how can we build something like *Mailboxlayer*, *NeverBounce* or *DeBounce* with simple logics and this can be the solution for small use cases which do not need higher accuracy.

## How it functions? {#working-principle}
Entire Email filter system splitted into multiple steps, they are:
```
1. Address validation
2. Domain validation
3. TLD validation
4. Availability validation (working or not)
5. Free email validation
6. Disposible/Temp email validation
7. Role based email validation
```

So, in terms of coding they are multiple util functions where each will serve its own purpose.

## Installation
Most of the modules are built-in modules which comes on python installation, the third-party modules are inside `requirements.txt`, one can install all modules using the following command:

```
pip install -r requirements.txt
```

## It can be extend to
Additionally to the above steps [[2]](#working-principle), one can take this to further, by adding:

### 1. Catch-all mailbox
A catch-all mailbox, also known as a wildcard mailbox or default mailbox, is an email address setup that collects all incoming email messages sent to any email address within a specific domain, even if the recipient email address does not exist.

For example, let's say you have a domain "example.com" and you set up a catch-all mailbox for that domain. Any email sent to any address ending with "@example.com" (e.g., info@example.com, contact@example.com, randomname@example.com) will be delivered to the catch-all mailbox.

Detecting if an email address domain has a catch-all mailbox is not always straightforward, as it depends on the specific email service provider and their configuration. However, you can try the following approach to check if a domain has a catch-all mailbox:

1. *Send any random email within the domain*: You can send an email to a randomly generated or non-existent email address within the target domain, such as randomname@example.com.

2. Wait for the delivery response: Monitor the response you receive when sending the email. Typically, if the domain has a catch-all mailbox, you will receive a successful delivery response or a bounce message indicating that the email was accepted for delivery.

3. Analyze the response: Check the response message or bounce message you receive. If it indicates that the email was successfully delivered or accepted, it suggests the domain has a catch-all mailbox. However, if the response indicates a non-delivery or an error, it suggests that the domain does not have a catch-all mailbox or it is not configured to accept emails for non-existent addresses.

Here are some email providers which supports Catch-all mailboxes:
- Google Workspace (formerly G Suite), 
- Microsoft 365 (formerly Office 365),
- Zoho Mail, 
- cPanel, 
- DreamHost, 
- FastMail, 
- Rackspace Email
### 2. Spam filtering
    
Determining whether an email address is spam or not solely based on the email address itself is a challenging task. Email addresses alone do not provide sufficient information to accurately classify them as spam or legitimate.

Spam filtering typically involves analyzing the content, metadata, and various other factors associated with an email to make an informed decision. However, if you still want to perform a basic spam check based on the email address, you can consider the following approaches:

1. *Blacklist/Whitelist*: Maintain a list of known spam email addresses or domains (blacklist) and a list of trusted email addresses or domains (whitelist). Compare the email address against these lists and classify it accordingly. Keep in mind that this approach is limited and may not be effective against new or evolving spam sources.

2. *Domain reputation*: Evaluate the reputation of the domain associated with the email address. Several services and databases provide domain reputation scores that indicate the likelihood of the domain being associated with spam. You can integrate with such services or maintain your own reputation database.

3. *Disposable email address detection*: Identify disposable or temporary email addresses that are commonly used for spamming purposes. Maintain a list of known disposable email providers and check if the email address matches any of them.

4. *Pattern matching*: Look for patterns or characteristics commonly found in spam email addresses. For example, excessive use of random numbers, unusual combinations of letters, pruning words liks free, lottery, money, or inconsistent domain structures might indicate a higher likelihood of being spam.