from plone.app.s5slideshow.tests import base

class TestIntegration(base.TestCase):

    def test_browserresource(self):
        pass

def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    return base.build_test_suite((TestIntegration,))
