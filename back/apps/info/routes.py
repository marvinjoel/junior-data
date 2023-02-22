from rest_framework import routers
from apps.info.genercviews import ListUsers

router = routers.SimpleRouter()
router.register(r'user', ListUsers)

urlpatterns = router.urls
