### 🕹 Guide

After installing the module and setting up your `Flask` app:

Main classes and packages are
```Mail```  ```Message``` ```utils.DefaultChecker``` ```utils.WhoIsXmlApi```

### Available config options
class has following attributes

-  **MAIL_USERNAME**  : Username for email, some email hosts separates username from the default sender(AWS).
    - If you service does not provide username use sender address for connection.
-  **MAIL_PASSWORD** : Password for authentication
-  **MAIL_SERVER**  : SMTP Mail server.
-  **MAIL_USE_TLS** : For TLS connection
-  **MAIL_USE_SSL** : For TLS connection
-  **MAIL_DEBUG** : Debug mode for while sending mails, defaults 0.
-  **MAIL_FROM** : Sender address
- **MAIL_DEFAULT_SENDER** : Sender address
-  __MAIL_FROM_NAME__ : Title for Mail
-  __TEMPLATE_FOLDER__: If you are using jinja2, specify template folder name
-  **SUPPRESS_SEND**:  To mock sending out mail, defaults 0.
-  **USE_CREDENTIALS**: Defaults to `True`. However it enables users to choose whether or not to login to their SMTP server.
-  __VALIDATE_CERTS__: Defaults to `True`. It enables to choose whether to verify the mail server's certificate

### ```Mail``` class
class has following attributes and methods

- `send_message` : The methods has two atributes, message: Message, template_name=None
    - message : where you define message sturcture for email
    - template_name : if you are using jinja2 consider template_name as well for passing HTML.

- `send_mail` : sending emails with message string and recipients very similar to Django.
    - subject : A String containing the subject of the message.
    - message : A string containing the message body.
    - recipients : A list of strings, each an email address. Each member of recipients will see the other recipients in the “To:” field of the email message.
    - msgkwargs : the kwargs based parameters for `Message` class.

- `send_mass_mail` : To handle mass mailing.
    - datatuple : is a tuple in which each element is in this format:
        ```bash
        (subject, message, recipients)
        ```


### ```Message``` class
class has following attributes


-  recipients  : List of recipients.
-  attachments : attachments within mail.
-  subject  : subject content of the mail.
-  body : body of the message.
-  template_body: parameters for the jinja template.
-  template_params: parameters for the jinja template.
-  cc : cc recipients of the mail.
-  bcc : bcc recipients of the mail.
-  reply_to : Reply-To recipients in the mail.
-  charset : charset defaults to utf-8.
-  subtype : subtype of the mail defaults to plain.
- add_recipient : a method to add additional recipients.
- attach : a method to add additional attachments.

   
### ```utils.DefaultChecker``` class
Default class for checking email from collected public resource.
The class makes it possible to use redis to save data.

-  source  : `optional` source for collected email data.
-  db_provider  : switch to redis
  



### ```utils.WhoIsXmlApi``` class
WhoIsXmlApi class provide working with api  [WhoIsXmlApi](https://www.whoisxmlapi.com)
This service gives free 1000 request to checking email address per month.

-  token  : token you can get from this [WhoIsXmlApi](https://www.whoisxmlapi.com) link
-  email  : email for checking