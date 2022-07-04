from datetime import datetime

from ckeditor.fields import RichTextField
from django.db import models


class Slider(models.Model):
    title = models.CharField(max_length=2000)
    short_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/slider", help_text="Upload picture of size 1920x850")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Slider"
        verbose_name_plural = "Sliders"


class CompanyInformation(models.Model):
    website_name = models.CharField(max_length=1000)
    tag_line = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to="images/company")
    favicon = models.ImageField(upload_to="images/company")
    copyright_text = models.TextField()

    def __str__(self):
        return self.website_name

    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"


class IntroSection(models.Model):
    icon = models.CharField(max_length=1000)
    heading = models.CharField(max_length=2000)
    description = models.TextField()

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "Intro Features"
        verbose_name_plural = "Intro Features"


class SupportingContent(models.Model):
    short_about_heading = models.CharField(max_length=1000, null=True, blank=True)
    about_heading = models.CharField(max_length=5000)
    about_description = RichTextField()

    service_section_heading = models.CharField(max_length=2500, null=True, blank=True)
    service_section_description = RichTextField(null=True, blank=True)

    feature_video_url = models.URLField(null=True, blank=True)
    feature_thumbnail = models.ImageField(upload_to="images/", null=True, blank=True)

    testimonial_section_heading = models.CharField(max_length=2500, null=True, blank=True)
    testimonial_section_description = RichTextField(null=True, blank=True)

    products_banner = models.ImageField(upload_to="images/", null=True, blank=True, help_text="Upload picture of size 1920x280")
    blog_banner = models.ImageField(upload_to="images/", null=True, blank=True, help_text="Upload picture of size 1920x280")
    case_study_banner = models.ImageField(upload_to="images/", null=True, blank=True, help_text="Upload picture of size 1920x280")

    def __str__(self):
        return self.about_heading

    class Meta:
        verbose_name = "Supporting Content"
        verbose_name_plural = "Supporting Content"


class Services(models.Model):
    service_picture = models.ImageField(upload_to="images/services")
    heading = models.CharField(max_length=5000)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "Solutions"
        verbose_name_plural = "Solutions"


class Statistics(models.Model):
    customers = models.IntegerField(null=True, blank=True)
    facilities_manages = models.IntegerField(null=True, blank=True)
    expert_team = models.IntegerField(null=True, blank=True)
    area_covered = models.IntegerField(null=True, blank=True)

    def __int__(self):
        return self.customers

    class Meta:
        verbose_name = "Statistics"
        verbose_name_plural = "Statistics"


class Features(models.Model):
    feature_icon = models.CharField(max_length=1000)
    feature_heading = models.CharField(max_length=2000)
    feature_description = models.TextField()

    def __str__(self):
        return self.feature_heading

    class Meta:
        verbose_name = "Features"
        verbose_name_plural = "Features"


class InsightsSection(models.Model):
    heading = models.CharField(max_length=5000)
    description = RichTextField(null=True, blank=True)
    picture = models.ImageField(upload_to="images/")
    pie_chart_1_heading = models.CharField(max_length=500)
    pie_chart_1_color = models.CharField(max_length=500)
    pie_chart_1_value = models.CharField(max_length=500)

    pie_chart_2_heading = models.CharField(max_length=500)
    pie_chart_2_color = models.CharField(max_length=500)
    pie_chart_2_value = models.CharField(max_length=500)

    def __int__(self):
        return self.heading

    class Meta:
        verbose_name = "Insights Section"
        verbose_name_plural = "Insights Section"


class WhyUs(models.Model):
    picture = models.ImageField(upload_to="images/team", help_text="Upload image of size 650x450")
    heading = models.CharField(max_length=5000)
    description = models.TextField(null=True, blank=True)

    def __int__(self):
        return self.heading

    class Meta:
        verbose_name = "Why Choose Us"
        verbose_name_plural = "Why Choose Us"


class Team(models.Model):
    name = models.CharField(max_length=500)
    designation = models.CharField(max_length=500, null=True, blank=True)
    picture = models.ImageField(upload_to="images/team", help_text="Upload image of size 260x260")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Team"


class Client(models.Model):
    client_name = models.CharField(max_length=500, null=True, blank=True)
    logo = models.ImageField(upload_to="images/clients", null=True, blank=True,help_text="Upload image of size 140x130")

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = "Clients"
        verbose_name_plural = "Clients"


class Testimonial(models.Model):
    name = models.CharField(max_length=1000)
    designation = models.CharField(max_length=1000, null=True, blank=True)
    picture = models.ImageField(upload_to="images/testimonial", null=True, blank=True)
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Testimonials"
        verbose_name_plural = "Testimonials"


class Blog(models.Model):
    post_title = models.TextField()
    slug = models.SlugField()
    cover_picture = models.ImageField(upload_to="images/blog", null=True, blank=True)
    post_content = RichTextField()
    tag = models.CharField(max_length=500, default="post", help_text="if case study, use 'case-study' in tag.")
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = "Blog And Case Studies"
        verbose_name_plural = "Blog And Case Studies"


class AboutUs(models.Model):
    banner = models.ImageField(upload_to="images/", help_text="Upload image of size 1920x280")
    heading = models.CharField(max_length=5000)
    description = RichTextField(null=True, blank=True)
    side_picture = models.ImageField(upload_to="images/about", null=True, blank=True,
                                     help_text="Upload image of size 460x455")
    mission = RichTextField(null=True, blank=True)
    experience = RichTextField(null=True, blank=True)
    vision = RichTextField(null=True, blank=True)

    heading_section_2 = models.CharField(max_length=5000)
    banner_section_2 = models.ImageField(upload_to="images/", help_text="Upload image of size 920x505")

    def __str__(self):
        return self.heading

    class Meta:
        verbose_name = "About Us"
        verbose_name_plural = "About Us"


class Products(models.Model):
    product_picture = models.ImageField(upload_to="images/")
    product_name = models.CharField(max_length=5000)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = "Products"
        verbose_name_plural = "Products"


class Applications(models.Model):
    application_title = models.CharField(max_length=5000)
    slug = models.SlugField()
    heading_section_1 = models.CharField(max_length=5000)
    description_section_1 = RichTextField(null=True, blank=True)
    picture_section_1 = models.ImageField(upload_to="images/")

    heading_section_2 = models.CharField(max_length=5000)
    description_section_2 = RichTextField(null=True, blank=True)
    picture_section_2 = models.ImageField(upload_to="images/")

    def __str__(self):
        return self.application_title

    class Meta:
        verbose_name = "Applications"
        verbose_name_plural = "Applications"


class ContactUs(models.Model):
    banner = models.ImageField(upload_to="images/", help_text="Upload image of size 1920x280")
    address = models.TextField(null=True, blank=True)
    email_address = models.TextField(null=True, blank=True)
    phone_number = models.TextField(null=True, blank=True)
    banner_section_2 = models.ImageField(upload_to="images/", help_text="Upload image of size 1920x785")

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
