from rest_framework import routers
#from core import views as myapp_views
#from snippets import views
from .views import *


router = routers.DefaultRouter()
router.register(r'projects', ProjectViewset)
router.register(r'actions', ActionViewset)
router.register(r'users', UserViewSet)
