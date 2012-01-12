from plone.app.s5slideshow.tests import base

class TestIntegration(base.TestCase):

    def test_body(self):
        pass

    def test_enabled(self):
        pass

    def test_content(self):
        pass

    def test_creator(self):
        pass
    
    def test_author(self):
        pass
    
    def test_authorname(self):
        pass
    
    def test_viewlet(self):
        pass

def test_suite():
    """This sets up a test suite that actually runs the tests in the class
    above
    """
    return base.build_test_suite((TestIntegration,))
