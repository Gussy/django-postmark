from django.conf.urls import patterns, url

urlpatterns = patterns("",
    url(r"^bounce/$", "postmark.views.bounce", name="postmark_bounce_hook"),
)
