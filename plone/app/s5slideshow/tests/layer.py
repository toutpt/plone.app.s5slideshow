from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting, FunctionalTesting

class JSLayer(PloneSandboxLayer):
    default_bases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import plone.app.s5slideshow
        self.loadZCML(package=plone.app.s5slideshow)

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'plone.app.s5slideshow:default')


FIXTURE = JSLayer()

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                                 name="plone.app.s5slideshow:Integration")
FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                               name="plone.app.s5slideshow:Functional")
