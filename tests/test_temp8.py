# -*- coding: utf-8 -*-
# --------------------------------------------------
# temp-mail.org wrapper test file
# Quentin 'MCXIV' Dufournet, 2023
# --------------------------------------------------
# Built-in
import sys
import os

# 3rd party
import temp8 as script

# --------------------------------------------------


def test_init():
    """ Scenario:
    * Init the class
    * Check if the mailbox.json file exists
    * Check the class attributes (i.e. file loaded properly)
    """

    mail = script.TempMail()

    assert os.path.exists('mailbox.json') == True
    assert mail.mailbox is not None
    assert mail.token is not None
    assert mail.timestamp is not None


def test_generate_mailbox():
    """ Scenario:
    * Init the class
    * Remove the mailbox.json file
    * Check if the file has been removed
    * Generate a new mailbox
    * Check if the file has been created
    * Check if the file is not empty
    """

    mail = script.TempMail()
    os.remove('mailbox.json')
    assert os.path.exists('mailbox.json') == False

    mail = mail.generate_mailbox()
    assert os.path.exists('mailbox.json') == True
    assert os.path.getsize('mailbox.json') > 0


def test_get_messages():
    """ Scenario:
    * Init the class
    * Get the messages
    * Check if the messages are not None (i.e. the request was successful, messages can be empty)
    """

    mail = script.TempMail()
    messages = mail.get_messages()
    assert messages is not None


def test_refresh_mailbox():
    """ Scenario:
    * Init the class
    * Save the class attributes
    * Refresh the mailbox
    * Check if the mailbox.json file exists
    * Check that the class attributes changed
    """

    mail = script.TempMail()
    mailboxAttributes = {
        'mailbox': mail.mailbox,
        'token': mail.token,
        'timestamp': mail.timestamp
    }

    mail.refresh_mailbox()

    assert os.path.exists('mailbox.json') == True
    assert mail.mailbox is not mailboxAttributes['mailbox']
    assert mail.token is not mailboxAttributes['token']
    assert mail.timestamp is not mailboxAttributes['timestamp']


def test_anti_cloudfare_anti_bots():
    """ Scenario:
    * Init the class
    * Get the messages 1000 times
    * Check if the request failed less than 10%
    """

    mail = script.TempMail()
    result = [mail.get_messages() for _ in range(1000)]

    assert result.count(-1) < 100
