# Generated by Django 3.2.13 on 2022-07-03 18:19

import ckeditor.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(help_text='Upload image of size 1920x280', upload_to='images/')),
                ('heading', models.CharField(max_length=5000)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('side_picture', models.ImageField(blank=True, help_text='Upload image of size 460x455', null=True, upload_to='images/about')),
                ('mission', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('experience', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('vision', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('heading_section_2', models.CharField(max_length=5000)),
                ('banner_section_2', models.ImageField(help_text='Upload image of size 920x505', upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_section_1', models.CharField(max_length=5000)),
                ('description_section_1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('picture_section_1', models.ImageField(upload_to='images/')),
                ('heading_section_2', models.CharField(max_length=5000)),
                ('description_section_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('picture_section_2', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.TextField()),
                ('slug', models.SlugField()),
                ('cover_picture', models.ImageField(blank=True, null=True, upload_to='images/blog')),
                ('post_content', ckeditor.fields.RichTextField()),
                ('tag', models.CharField(default='post', help_text="if case study, use 'case-study' in tag.", max_length=500)),
                ('date', models.DateField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': 'Blog And Case Studies',
                'verbose_name_plural': 'Blog And Case Studies',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(blank=True, max_length=500, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='images/clients')),
            ],
            options={
                'verbose_name': 'Clients',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='CompanyInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_name', models.CharField(max_length=1000)),
                ('tag_line', models.TextField(blank=True, null=True)),
                ('logo', models.ImageField(upload_to='images/company')),
                ('favicon', models.ImageField(upload_to='images/company')),
                ('copyright_text', models.TextField()),
            ],
            options={
                'verbose_name': 'Company Information',
                'verbose_name_plural': 'Company Information',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner', models.ImageField(help_text='Upload image of size 1920x280', upload_to='images/')),
                ('address', models.TextField(blank=True, null=True)),
                ('email_address', models.TextField(blank=True, null=True)),
                ('phone_number', models.TextField(blank=True, null=True)),
                ('banner_section_2', models.ImageField(help_text='Upload image of size 1920x785', upload_to='images/')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_icon', models.CharField(max_length=1000)),
                ('feature_heading', models.CharField(max_length=2000)),
                ('feature_description', models.TextField()),
            ],
            options={
                'verbose_name': 'Features',
                'verbose_name_plural': 'Features',
            },
        ),
        migrations.CreateModel(
            name='InsightsSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=5000)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('picture', models.ImageField(upload_to='images/')),
                ('pie_chart_1_heading', models.CharField(max_length=500)),
                ('pie_chart_1_color', models.CharField(max_length=500)),
                ('pie_chart_1_value', models.CharField(max_length=500)),
                ('pie_chart_2_heading', models.CharField(max_length=500)),
                ('pie_chart_2_color', models.CharField(max_length=500)),
                ('pie_chart_2_value', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Insights Section',
                'verbose_name_plural': 'Insights Section',
            },
        ),
        migrations.CreateModel(
            name='IntroSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=1000)),
                ('heading', models.CharField(max_length=2000)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Intro Features',
                'verbose_name_plural': 'Intro Features',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_picture', models.ImageField(upload_to='images/')),
                ('product_name', models.CharField(max_length=5000)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Products',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_picture', models.ImageField(upload_to='images/services')),
                ('heading', models.CharField(max_length=5000)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Services',
                'verbose_name_plural': 'Services',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('short_description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='images/slider')),
            ],
            options={
                'verbose_name': 'Slider',
                'verbose_name_plural': 'Sliders',
            },
        ),
        migrations.CreateModel(
            name='Statistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customers', models.IntegerField(blank=True, null=True)),
                ('facilities_manages', models.IntegerField(blank=True, null=True)),
                ('expert_team', models.IntegerField(blank=True, null=True)),
                ('area_covered', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Statistics',
                'verbose_name_plural': 'Statistics',
            },
        ),
        migrations.CreateModel(
            name='SupportingContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_about_heading', models.CharField(blank=True, max_length=1000, null=True)),
                ('about_heading', models.CharField(max_length=5000)),
                ('about_description', ckeditor.fields.RichTextField()),
                ('service_section_heading', models.CharField(blank=True, max_length=2500, null=True)),
                ('service_section_description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('feature_video_url', models.URLField(blank=True, null=True)),
                ('feature_thumbnail', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('testimonial_section_heading', models.CharField(blank=True, max_length=2500, null=True)),
                ('testimonial_section_description', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Supporting Content',
                'verbose_name_plural': 'Supporting Content',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('designation', models.CharField(blank=True, max_length=500, null=True)),
                ('picture', models.ImageField(help_text='Upload image of size 260x260', upload_to='images/team')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team',
            },
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('designation', models.CharField(blank=True, max_length=1000, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='images/testimonial')),
                ('comment', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Testimonials',
                'verbose_name_plural': 'Testimonials',
            },
        ),
        migrations.CreateModel(
            name='WhyUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=5000)),
                ('heading', models.CharField(max_length=5000)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Why Choose Us',
                'verbose_name_plural': 'Why Choose Us',
            },
        ),
    ]