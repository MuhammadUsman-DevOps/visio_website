from django.contrib import admin

from Visio_Website.models import CompanyInformation, SupportingContent, Statistics, InsightsSection, AboutUs, ContactUs, \
    Slider, IntroSection, Services, Applications, Products, Blog, Testimonial, Client, Team, WhyUs, Features

admin.site.index_title = "Visio Administration"
admin.site.site_title = "Visio Administration"
admin.site.site_header = "Visio Administration"


class SliderAdminModel(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'image']


class CompanyInformationAdminModel(admin.ModelAdmin):
    list_display = ['website_name', 'tag_line', 'logo', 'favicon', 'copyright_text']

    def has_add_permission(self, request):
        return not CompanyInformation.objects.exists()


class IntroSectionAdminModel(admin.ModelAdmin):
    list_display = ['heading', 'description', 'icon']


class SupportingContentAdminModel(admin.ModelAdmin):
    list_display = ['short_about_heading', 'about_heading', 'about_description', 'service_section_heading',
                    'service_section_description']

    def has_add_permission(self, request):
        return not SupportingContent.objects.exists()


class ServiceAdminModel(admin.ModelAdmin):
    list_display = ['heading', 'description', 'service_picture']


class StatisticsAdminModel(admin.ModelAdmin):
    list_display = ['customers', 'facilities_manages', 'expert_team', 'area_covered']

    def has_add_permission(self, request):
        return not Statistics.objects.exists()


class FeaturesAdminModel(admin.ModelAdmin):
    list_display = ['feature_icon', 'feature_heading', 'feature_description']


class InsightsSectionAdminModel(admin.ModelAdmin):
    list_display = ['heading']

    def has_add_permission(self, request):
        return not InsightsSection.objects.exists()


class WhyUsAdminModel(admin.ModelAdmin):
    list_display = ['heading', 'description', 'picture']


class TeamAdminModel(admin.ModelAdmin):
    list_display = ['name', 'designation', 'picture']


class ClientAdminModel(admin.ModelAdmin):
    list_display = ['client_name', 'logo']


class TestimonialAdminModel(admin.ModelAdmin):
    list_display = ['name', 'designation', 'picture', 'comment']


class AboutUsAdminModel(admin.ModelAdmin):
    list_display = ['heading']

    def has_add_permission(self, request):
        return not AboutUs.objects.exists()


class BlogAdminModel(admin.ModelAdmin):
    list_display = ['post_title', 'slug', 'cover_picture', 'tag', 'date']
    prepopulated_fields = {"slug": ("post_title",)}


class ProductsAdminModel(admin.ModelAdmin):
    list_display = ['product_name', 'description', 'product_picture']


class ApplicationsAdminModel(admin.ModelAdmin):
    list_display = ['application_title', 'slug']
    prepopulated_fields = {"slug": ("application_title",)}


class ContactUsAdminModel(admin.ModelAdmin):
    list_display = ['email_address', 'phone_number', 'banner', 'address']

    def has_add_permission(self, request):
        return not ContactUs.objects.exists()


admin.site.register(Slider, SliderAdminModel)
admin.site.register(CompanyInformation, CompanyInformationAdminModel)
admin.site.register(IntroSection, IntroSectionAdminModel)
admin.site.register(SupportingContent, SupportingContentAdminModel)
admin.site.register(Services, ServiceAdminModel)
admin.site.register(Statistics, StatisticsAdminModel)
admin.site.register(Features, FeaturesAdminModel)
admin.site.register(InsightsSection, InsightsSectionAdminModel)
admin.site.register(WhyUs, WhyUsAdminModel)
admin.site.register(Team, TeamAdminModel)
admin.site.register(Client, ClientAdminModel)
admin.site.register(Testimonial, TestimonialAdminModel)
admin.site.register(Blog, BlogAdminModel)
admin.site.register(AboutUs, AboutUsAdminModel)
admin.site.register(Products, ProductsAdminModel)
admin.site.register(Applications, ApplicationsAdminModel)
admin.site.register(ContactUs, ContactUsAdminModel)
