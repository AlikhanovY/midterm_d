from django.utils import path

from . import views

urlpatterns =[
    path('/posts', veiws.list_posts, name="list_posts")
]

