
.. image:: https://quickemailverification.com/images/logo_github.png
    :target: https://quickemailverification.com
    :width: 600
    :align: center
    :alt: Quick Email Verification Logo

Official Email Validation API library client for Python
=======================================================

.. image:: https://travis-ci.org/quickemailverification/quickemailverification-python.svg?branch=master
    :target: https://travis-ci.org/quickemailverification/quickemailverification-python

QuickEmailVerification provides the quickest way to avoid fake / invalid
emails.

-  Get actual users by scanning email address.
-  Remove invalid, dead and fake emails from your email list.
-  Save time and money by sending mail to actual users.

Let's Get Started
-----------------

To begin, signUp at
`quickemailverification.com <https://quickemailverification.com>`__ and
create a FREE account. After signup logged in, click on `API
Settings <https://quickemailverification.com/apisettings>`__ and then
click **Add API Key**. To use API you need 2 parameters.

email - (string) This is a email address you need to verify. It should
be url encoded.

apikey - (string) This is the key you generated from
"api settings" page.

NOTE: Keep API key with you. You'll need it to setup the client as explained below.

Installation
------------

Make sure you have `pip <https://pypi.python.org/pypi/pip>`__ installed.

.. code:: bash

    $ pip install quickemailverification

Versions
~~~~~~~~

Works with [ 2.6 / 2.7 / 3.2 / 3.3 / 3.4 ]

Usage
-----

.. code:: python

    import quickemailverification

    client = quickemailverification.Client('Your_API_Key_Here')
    quickemailverification = client.quickemailverification()
    
    # PRODUCTION MODE
    response = quickemailverification.verify('test@example.com')
    
    # SANDBOX MODE
    # response = quickemailverification.sandbox('valid@example.com')
    
    print(response.body) # The response is in the body attribute

Response information
~~~~~~~~~~~~~~~~~~~~

A successful API call responds with the following values:

-  **result** ``string`` - The verified results will be: ``valid``,
   ``invalid``, ``unknown``
-  **reason** ``string`` - Reason definitions are as below:
-  ``invalid_email`` - Specified email has invalid email address syntax
-  ``invalid_domain`` - Domain name does not exist
-  ``rejected_email`` - SMTP server rejected email. Email does not exist
-  ``accepted_email`` - SMTP server accepted email address
-  ``no_connect`` - SMTP server connection failure
-  ``timeout`` - Session time out occurred at SMTP server
-  ``unavailable_smtp`` - SMTP server is not available to process
   request
-  ``unexpected_error`` - An unexpected error has occurred
-  ``no_mx_record`` - Could not get MX records for domain
-  ``temporarily_blocked`` - Email is temporarily greylisted
-  ``exceeded_storage`` - SMTP server rejected email. Exceeded storage
   allocation

-  **disposable** ``true | false`` - *true* if the email address uses a
   *disposable* domain
-  **accept\_all** ``true | false`` - *true* if the domain appears to
   *accept all* emails delivered to that domain
-  **role** ``true | false`` - *true* if the email address is a *role*
   address (``manager@example.com``, ``ceo@example.com``, etc)
-  **free** ``true | false`` - *true* if the email address is from free
   email provider like Gmail, Yahoo!, Hotmail etc.
-  **email** ``string`` - Returns a normalized version.
   (``Niki@example.com`` -> ``niki@example.com``)
-  **user** ``string`` - The local part of an email address.
   (``niki@example.com`` -> ``niki``)
-  **domain** ``string`` - The domain of the provided email address.
   (``niki@example.com`` -> ``example.com``)
-  **mx_record** ``string`` - The preferred MX record of email domain. This 
   field contains empty string when MX record is not available.
-  **mx_domain** ``string`` - The domain name of the MX host. This field
   contains empty string when MX record is not available.
-  **safe\_to\_send** ``true | false`` - *true* if the email address is
   safe for deliverability
-  **did\_you\_mean** ``string`` - Returns email suggestions if specific
   typo errors found in email
-  **success** ``true | false`` - *true* if the API request was
   successful
-  **message** ``string`` - Describes API call failure reason

HTTP Response headers
~~~~~~~~~~~~~~~~~~~~~

Total remaining credits can be found by http response header. It
contains overall remaining credits, including Persistent & Per day
credits.

-  **X-QEV-Remaining-Credits** - Your remaining email verification
   credits (i.e. Per Day Credits + Persistent Credits).

HTTP status codes for QuickEmailVerification API calls
------------------------------------------------------

QuickEmailVerification API also returns following HTTP status codes to
indicate success or failure of request.

-  ``200`` - Request is completed successfully.
-  ``400`` - Server can not understand the request sent to it. This is
   kind of response can occur if parameters are passed wrongly.
-  ``401`` - Server can not verify your authentication to use api.
   Please check whether API key is proper or not.
-  ``402`` - You are running out of your credit limit.
-  ``404`` - Requested API can not be found on server.
-  ``429`` - Too many requests. Rate limit exceeded.

Sandbox Mode
------------------------------------------------------
QuickEmailVerification single email verification API sandbox mode helps developers to test their integration against simulated results. Requesting against sandbox endpoint is totally free and no credits will be deducted from actual credit quota.

Please refer our `knowledge base <http://docs.quickemailverification.com/email-verification-api/sandbox-mode>`__ to learn more about sandbox mode.

License
-------

MIT

Bug Reports
-----------

Report
`here <https://github.com/quickemailverification/quickemailverification-python/issues>`__.

Need Help? Feel free to contact us
----------------------------------

https://quickemailverification.com/contact-us
