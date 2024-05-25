from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Pkb(models.Model):
    patterns = models.TextField(max_length=500, verbose_name="Patterns", blank=True, null=True)
    strategies = models.TextField(max_length=100, verbose_name="Strategia", blank=True, null=True)
    description = models.TextField(max_length=500, verbose_name="Descrizione", blank=True, null=True)
    context = models.TextField(max_length=500, verbose_name="Contesto", blank=True, null=True)
    mvc = models.TextField(max_length=100, verbose_name="Collocazione MVC", blank=True, null=True)

class Iso(models.Model):
    pkb = models.ForeignKey(Pkb, on_delete=models.CASCADE)
    iso = models.TextField(max_length=100, verbose_name="Iso", blank=True, null=True)

class ArticleGdpr(models.Model):
    class Article(models.TextChoices):
        article5 = "A5", "Article 5"
        article6 = "A6", "Article 6"
        article12 = "A12", "Article 12"
        article13 = "A13", "Article 13"
        article25 = "A25", "Article 25"
        article28 = "A28", "Article 28"
        article32 = "A32", "Article 32"
        article35 = "A35", "Article 35"
    pkb = models.ForeignKey(Pkb, on_delete=models.CASCADE, null=True, blank=True )
    article = models.CharField(choices=Article.choices, null=True, blank=True, max_length=3)


class Owasp(models.Model):
    class TopTen(models.TextChoices):
        a01 = "A01", "Broken Access Control"
        a02 = "A02", "Cryptographic Failures"
        a03 = "A03", "Injection"
        a04 = "A04", "Insecure Design"
        a05 = "A05", "Security Misconfiguration"
        a06 = "A06", "Vulnerable and Outdated Components"
        a07 = "A07", "Identification and Authentication Failures"
        a08 = "A08", "Software and Data Integrity Failures"
        a09 = "A09", "Security Logging and Monitoring Failures"
        a10 = "A10", "Server-Side Request Forgery (SSRF)"

    top_ten = models.CharField(choices=TopTen.choices, blank=True, null=True, max_length=3)
    pkb = models.ForeignKey(Pkb, on_delete=models.CASCADE, blank=True, null=True)


class Exemple(models.Model):
    exemple = models.TextField(max_length=500, verbose_name="Exemple", blank=True, null=True)
    pkb = models.ForeignKey(Pkb, on_delete=models.CASCADE, blank=True, null=True)

class PrivacyByDesign(models.Model):
    class Design(models.TextChoices):
        ps = "PS","Privacy as the default setting"
        pd = "PD", "Privacy Embedded into Design"
        vs = "VS", "Visibility and Transparency"
        pr = "PR", "Proactive not Reactive"
        rp = "RP", "Respect for User Privacy"

    design = models.CharField(choices=Design.choices, null=True, blank=True, max_length=3)
    pkb = models.ForeignKey(Pkb, on_delete=models.CASCADE)

class Notification(models.Model):
    pkb = models.ForeignKey(Pkb, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)