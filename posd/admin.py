from django.contrib import admin
from posd.models import Pkb, Iso, ArticleGdpr, Owasp, Example, Notification

# Register your models here.
admin.site.register(Pkb)
admin.site.register(Iso)
admin.site.register(ArticleGdpr)
admin.site.register(Owasp)
admin.site.register(Example)
admin.site.register(Notification)
