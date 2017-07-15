from django.db import models

class Customer(models.Model):
    contact = models.CharField(
        max_length=32,
        verbose_name='Customer Name',
        help_text="Input the Attention To name here if the person is purchasing on behalf of a company or business",
    )
    contact_email = models.CharField(
        max_length=200,
        verbose_name='E-mail',
    )
    contact_num = models.CharField(
        max_length=40,
        verbose_name='Phone Number',
    )
    business_name = models.CharField(
        max_length=60,
        verbose_name='Business Registered Name',
        blank=True,
        unique=True,
        help_text="Leave blank if no company details are provided",
    )
    business_reg_no = models.CharField(
        max_length=10,
        verbose_name='Business Registration Number',
        blank=True,
    )
    billing_address_1 = models.CharField(
        max_length=60,
        verbose_name='Billing Address Line 1',
    )
    billing_address_2 = models.CharField(
        max_length=60,
        blank=True,
        verbose_name='Billing Address Line 2',
    )
    billing_postal = models.CharField(
        max_length=60,
        verbose_name='Billing Postal Code',
    )
    INDUSTRY_CHOICES = (
        ('NON', 'Home, Office'),
        ('FNB', 'Food and Beverage, Hotel, Restaurant'),
        ('EVT', 'Event, Pasar Malam'),
        ('BAR', 'Bars, Pubs, Clubs'),
        ('IND', 'Industrial, Concrete, Manufacturing'),
        ('MAR', 'Minimart, Supermarket'),
        ('WTM', 'Wetmarket'),
        ('OTR', 'Other'),
    )
    industry = models.CharField(
        max_length=3,
        choices=INDUSTRY_CHOICES,
        default='NON',
    )


    def __str__(self):
        if self.business_name:
            return self.business_name
        return self.name
