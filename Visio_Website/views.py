from django.shortcuts import render

from Visio_Website.models import Slider, CompanyInformation, IntroSection, SupportingContent, Services, Statistics, \
    Features, InsightsSection, WhyUs, Team, Client, Testimonial, Blog, AboutUs, Products, Applications, ContactUs


def base(request):
    return render(request, template_name="base/base_all.html")


def home(request):
    slider = Slider.objects.all()
    company_info = CompanyInformation.objects.first()
    intro_section = IntroSection.objects.all()
    supporting_content = SupportingContent.objects.first()
    services = Services.objects.all()
    statistics = Statistics.objects.first()
    features = Features.objects.all()
    why_us = WhyUs.objects.all()
    insight_section = InsightsSection.objects.first()
    teams = Team.objects.all()
    clients = Client.objects.all()
    testimonial = Testimonial.objects.all()
    blogs = Blog.objects.all()
    three_blogs = Blog.objects.all()[:3]
    all_products = Products.objects.all()
    all_applications = Applications.objects.all()
    about_us_info = AboutUs.objects.first()
    contact_us_info = ContactUs.objects.first()

    context = {
        "sliders": slider,
        "company_info": company_info,
        "intro_section": intro_section,
        "supporting_content": supporting_content,
        "services": services,
        "statistics": statistics,
        "features": features,
        "why_us": why_us,
        "insight_section": insight_section,
        "teams": teams,
        "clients": clients,
        "testimonials": testimonial,
        "blogs": blogs,
        "all_products": all_products,
        "all_applications": all_applications,
        "about_us_info": about_us_info,
        "contact_us_info": contact_us_info,
        "three_blogs": three_blogs,

    }
    return render(request, template_name="wsite/home.html", context=context)


def about_us(request):
    slider = Slider.objects.all()
    company_info = CompanyInformation.objects.first()
    intro_section = IntroSection.objects.all()
    supporting_content = SupportingContent.objects.first()
    services = Services.objects.all()
    statistics = Statistics.objects.first()
    features = Features.objects.all()
    why_us = WhyUs.objects.all()
    insight_section = InsightsSection.objects.first()
    teams = Team.objects.all()
    clients = Client.objects.all()
    testimonial = Testimonial.objects.all()
    blogs = Blog.objects.all()
    three_blogs = Blog.objects.all()[:3]
    all_products = Products.objects.all()
    all_applications = Applications.objects.all()
    about_us_info = AboutUs.objects.first()
    contact_us_info = ContactUs.objects.first()

    context = {
        "sliders": slider,
        "company_info": company_info,
        "intro_section": intro_section,
        "supporting_content": supporting_content,
        "services": services,
        "statistics": statistics,
        "features": features,
        "why_us": why_us,
        "insight_section": insight_section,
        "teams": teams,
        "clients": clients,
        "testimonials": testimonial,
        "blogs": blogs,
        "all_products": all_products,
        "all_applications": all_applications,
        "about_us_info": about_us_info,
        "contact_us_info": contact_us_info,
        "three_blogs": three_blogs,

    }
    return render(request, template_name="wsite/about_us.html", context=context)


def contact_us(request):
    slider = Slider.objects.all()
    company_info = CompanyInformation.objects.first()
    intro_section = IntroSection.objects.all()
    supporting_content = SupportingContent.objects.first()
    services = Services.objects.all()
    statistics = Statistics.objects.first()
    features = Features.objects.all()
    why_us = WhyUs.objects.all()
    insight_section = InsightsSection.objects.first()
    teams = Team.objects.all()
    clients = Client.objects.all()
    testimonial = Testimonial.objects.all()
    blogs = Blog.objects.all()
    three_blogs = Blog.objects.all()[:3]
    all_products = Products.objects.all()
    all_applications = Applications.objects.all()
    about_us_info = AboutUs.objects.first()
    contact_us_info = ContactUs.objects.first()

    context = {
        "sliders": slider,
        "company_info": company_info,
        "intro_section": intro_section,
        "supporting_content": supporting_content,
        "services": services,
        "statistics": statistics,
        "features": features,
        "why_us": why_us,
        "insight_section": insight_section,
        "teams": teams,
        "clients": clients,
        "testimonials": testimonial,
        "blogs": blogs,
        "all_products": all_products,
        "all_applications": all_applications,
        "about_us_info": about_us_info,
        "contact_us_info": contact_us_info,
        "three_blogs": three_blogs,

    }
    return render(request, template_name="wsite/contact_us.html", context=context)


def applications(request, slug):
    app = Applications.objects.get(slug=slug)
    slider = Slider.objects.all()
    company_info = CompanyInformation.objects.first()
    intro_section = IntroSection.objects.all()
    supporting_content = SupportingContent.objects.first()
    services = Services.objects.all()
    statistics = Statistics.objects.first()
    features = Features.objects.all()
    why_us = WhyUs.objects.all()
    insight_section = InsightsSection.objects.first()
    teams = Team.objects.all()
    clients = Client.objects.all()
    testimonial = Testimonial.objects.all()
    blogs = Blog.objects.all()
    three_blogs = Blog.objects.all()[:3]
    all_products = Products.objects.all()
    all_applications = Applications.objects.all()
    about_us_info = AboutUs.objects.first()
    contact_us_info = ContactUs.objects.first()

    context = {
        "sliders": slider,
        "company_info": company_info,
        "intro_section": intro_section,
        "supporting_content": supporting_content,
        "services": services,
        "statistics": statistics,
        "features": features,
        "why_us": why_us,
        "insight_section": insight_section,
        "teams": teams,
        "clients": clients,
        "testimonials": testimonial,
        "blogs": blogs,
        "all_products": all_products,
        "all_applications": all_applications,
        "about_us_info": about_us_info,
        "contact_us_info": contact_us_info,
        "three_blogs": three_blogs,
        "app": app,

    }
    return render(request, template_name="wsite/applications.html", context=context)


def products(request):
    slider = Slider.objects.all()
    company_info = CompanyInformation.objects.first()
    intro_section = IntroSection.objects.all()
    supporting_content = SupportingContent.objects.first()
    services = Services.objects.all()
    statistics = Statistics.objects.first()
    features = Features.objects.all()
    why_us = WhyUs.objects.all()
    insight_section = InsightsSection.objects.first()
    teams = Team.objects.all()
    clients = Client.objects.all()
    testimonial = Testimonial.objects.all()
    blogs = Blog.objects.all()
    three_blogs = Blog.objects.all()[:3]
    all_products = Products.objects.all()
    all_applications = Applications.objects.all()
    about_us_info = AboutUs.objects.first()
    contact_us_info = ContactUs.objects.first()

    context = {
        "sliders": slider,
        "company_info": company_info,
        "intro_section": intro_section,
        "supporting_content": supporting_content,
        "services": services,
        "statistics": statistics,
        "features": features,
        "why_us": why_us,
        "insight_section": insight_section,
        "teams": teams,
        "clients": clients,
        "testimonials": testimonial,
        "blogs": blogs,
        "all_products": all_products,
        "all_applications": all_applications,
        "about_us_info": about_us_info,
        "contact_us_info": contact_us_info,
        "three_blogs": three_blogs,

    }
    return render(request, template_name="wsite/products.html", context=context)


def blog(request):
    slider = Slider.objects.all()
    company_info = CompanyInformation.objects.first()
    intro_section = IntroSection.objects.all()
    supporting_content = SupportingContent.objects.first()
    services = Services.objects.all()
    statistics = Statistics.objects.first()
    features = Features.objects.all()
    why_us = WhyUs.objects.all()
    insight_section = InsightsSection.objects.first()
    teams = Team.objects.all()
    clients = Client.objects.all()
    testimonial = Testimonial.objects.all()
    blogs = Blog.objects.all()
    three_blogs = Blog.objects.all()[:3]
    all_products = Products.objects.all()
    all_applications = Applications.objects.all()
    about_us_info = AboutUs.objects.first()
    contact_us_info = ContactUs.objects.first()

    context = {
        "sliders": slider,
        "company_info": company_info,
        "intro_section": intro_section,
        "supporting_content": supporting_content,
        "services": services,
        "statistics": statistics,
        "features": features,
        "why_us": why_us,
        "insight_section": insight_section,
        "teams": teams,
        "clients": clients,
        "testimonials": testimonial,
        "blogs": blogs,
        "all_products": all_products,
        "all_applications": all_applications,
        "about_us_info": about_us_info,
        "contact_us_info": contact_us_info,
        "three_blogs": three_blogs,
        "title": "Blog"

    }
    return render(request, template_name="wsite/blog.html", context=context)


def case_studies(request):
    slider = Slider.objects.all()
    company_info = CompanyInformation.objects.first()
    intro_section = IntroSection.objects.all()
    supporting_content = SupportingContent.objects.first()
    services = Services.objects.all()
    statistics = Statistics.objects.first()
    features = Features.objects.all()
    why_us = WhyUs.objects.all()
    insight_section = InsightsSection.objects.first()
    teams = Team.objects.all()
    clients = Client.objects.all()
    testimonial = Testimonial.objects.all()
    blogs = Blog.objects.filter(tag="case-study")
    three_blogs = Blog.objects.all()[:3]
    all_products = Products.objects.all()
    all_applications = Applications.objects.all()
    about_us_info = AboutUs.objects.first()
    contact_us_info = ContactUs.objects.first()

    context = {
        "sliders": slider,
        "company_info": company_info,
        "intro_section": intro_section,
        "supporting_content": supporting_content,
        "services": services,
        "statistics": statistics,
        "features": features,
        "why_us": why_us,
        "insight_section": insight_section,
        "teams": teams,
        "clients": clients,
        "testimonials": testimonial,
        "blogs": blogs,
        "all_products": all_products,
        "all_applications": all_applications,
        "about_us_info": about_us_info,
        "contact_us_info": contact_us_info,
        "three_blogs": three_blogs,
        "title": "Case Studies"

    }
    return render(request, template_name="wsite/blog.html", context=context)


def post(request, slug):
    slider = Slider.objects.all()
    company_info = CompanyInformation.objects.first()
    intro_section = IntroSection.objects.all()
    supporting_content = SupportingContent.objects.first()
    services = Services.objects.all()
    statistics = Statistics.objects.first()
    features = Features.objects.all()
    why_us = WhyUs.objects.all()
    insight_section = InsightsSection.objects.first()
    teams = Team.objects.all()
    clients = Client.objects.all()
    testimonial = Testimonial.objects.all()
    blog_post = Blog.objects.get(slug=slug)
    three_blogs = Blog.objects.all()[:3]
    all_products = Products.objects.all()
    all_applications = Applications.objects.all()
    about_us_info = AboutUs.objects.first()
    contact_us_info = ContactUs.objects.first()

    context = {
        "sliders": slider,
        "company_info": company_info,
        "intro_section": intro_section,
        "supporting_content": supporting_content,
        "services": services,
        "statistics": statistics,
        "features": features,
        "why_us": why_us,
        "insight_section": insight_section,
        "teams": teams,
        "clients": clients,
        "testimonials": testimonial,
        "blog_post": blog_post,
        "all_products": all_products,
        "all_applications": all_applications,
        "about_us_info": about_us_info,
        "contact_us_info": contact_us_info,
        "three_blogs": three_blogs,
        "title": "Case Studies"

    }
    return render(request, template_name="wsite/post.html", context=context)
