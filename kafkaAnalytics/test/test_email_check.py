import unittest

from email_check import fun, filter_mail

class EmailAddressCheckTestCase(unittest.TestCase):
    """

    Unit test case for check email address functionality (email_check.py)

    """

    def test_fun(self):
        """

        Test email address has @

        """
        test_email_address = "johnsmith@gmail.com"
        self.assertTrue(fun(test_email_address))

    def test_MultipleAT(self):
        """

        Test email address has more than one @

        """
        test_email_address = "johns@mith@gmail.com"
        self.assertFalse(fun(test_email_address))

    def test_NoDot(self):
        """

        Test email address does not have dot

        """
        test_email_address = "johns@mith@gmailcom"
        self.assertFalse(fun(test_email_address))

    def test_TwoDotsInWebsite(self):
        """

        Test email address does not have dot

        """
        test_email_address = "johns@mith@gmail..com"
        self.assertFalse(fun(test_email_address))

    def test_MissingAt(self):
        """

        Test email address does not have @

        """
        test_email_address = "johnsmithgmail.com"
        self.assertFalse(fun(test_email_address))

    def test_NoAtNoDot(self):
        """

        Test email address does not have @

        """
        test_email_address = "johnsmithgmailcom"
        self.assertFalse(fun(test_email_address))

    def test_NoUsername(self):
        """

        Test email address does not have @

        """
        test_email_address = "@hgmail.com"
        self.assertFalse(fun(test_email_address))

    def test_noWebsite(self):
        """

        Test email address does not have website part

        """
        test_email_address = "johnsmit@.com"
        self.assertFalse(fun(test_email_address))

    def test_noExtension(self):
        """

        Test email address does not have extension

        """
        test_email_address = "johnsmith@gmail."
        self.assertFalse(fun(test_email_address))

if __name__ == '__main__':
    unittest.main()


