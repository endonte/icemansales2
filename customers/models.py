from django.db import models
from django.utils import timezone
from sales.users.models import User
from datetime import datetime

class Customer(models.Model):
    contact = models.CharField(
        max_length=32,
        verbose_name='Contact Name',
#        help_text="Input the Attention To name here if the person is purchasing on behalf of a company or business",
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
#        help_text="Leave blank if no company details are provided",
    )
    business_reg_no = models.CharField(
        max_length=10,
        verbose_name='Business Registration Number',
        blank=True,
    )
    billing_address_1 = models.CharField(
        max_length=60,
        verbose_name='Billing Address Line 1',
        blank=True,
    )
    billing_address_2 = models.CharField(
        max_length=60,
        verbose_name='Billing Address Line 2',
        blank=True,
    )
    billing_postal = models.CharField(
        max_length=60,
        verbose_name='Billing Postal Code',
        blank=True,
    )
    is_lead = models.BooleanField(
        default=False,
    )
    lead_created_by = models.ForeignKey(
        User,
        verbose_name='Lead Created By',
        related_name='lead_creator',
        blank=True,
        null=True,
    )
    lead_created_by_date = models.DateTimeField(
        default=datetime.now,
        blank=True,
    )
    lead_owned_by = models.ForeignKey(
        User,
        verbose_name='Lead Owned By',
        related_name='lead_owner',
        blank=True,
        null=True,
    )
    lead_owned_by_date = models.DateTimeField(
        default=datetime.now,
        blank=True,
        null=True,
    )
    customer_created_by = models.ForeignKey(
        User,
        verbose_name='Customer Created By',
        related_name='customer_creator',
        blank=True,
        null=True,
    )
    customer_created_by_date = models.DateTimeField(
        default=datetime.now,
        blank=True,
        null=True,
    )
    customer_owned_by = models.ForeignKey(
        User,
        verbose_name='Customer Owned By',
        related_name='customer_owner',
        blank=True,
        null=True,
    )
    customer_owned_by_date = models.DateTimeField(
        default=datetime.now,
        blank=True,
        null=True,
    )

    def __str__(self):
        if self.business_name:
            return self.business_name
        return self.contact

    def create_lead(self):
        self.lead_created_by.add(*[request.User])
        self.lead_created_by_date = timezone.now()
        self.save()

    def claim_lead(self):
        #
        self.lead_owned_by.add(*[request.User])
        self.lead_owned_by_date = timezone.now()
        self.save()

    def create_customer(self):
        # This method will be called when a customer has been created directly
        # or when the customer has been converted from a lead.
        self.customer_created_by.add(*[request.User])
        self.customer_created_by_date = timezone.now()
        self.save()

    def delete(self):
        self
