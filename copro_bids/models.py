from django.db import models


class Project(models.Model):

    client = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    bid_deadline = models.DateField()

    def __str__(self):
        return f'{self.client}: {self.code}- {self.name}'


class Bid(models.Model):
    PROJECTS = (
        ('191101', 'Holiday Digital (191101)'),
        ('190930', 'Non-Profit Video (190930)'),
        ('190711', 'Website & Digital Marketing (190711)'),
    )
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='bids', choices=PROJECTS)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=100)
    phases_and_pricing = models.TextField(max_length=700)
    total_price = models.CharField(max_length=100)
    website_urls = models.TextField(max_length=500)
    work_sample_urls = models.TextField(max_length=500)
    statement = models.TextField(max_length=600)
    conditions = models.CharField(max_length=255)
    submitted_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.project}'


class Teammate(models.Model):

    bid = models.ForeignKey(
        Bid, on_delete=models.CASCADE, related_name='teammates'
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    img_url = models.URLField()
    role = models.CharField(max_length=100)
    years_experience = models.DecimalField(max_digits=2, decimal_places=0)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    public_profile_urls = models.TextField(max_length=500)
