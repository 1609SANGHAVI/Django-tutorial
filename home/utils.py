from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def send_customer_login_email(user, password, mobile):
    subject = "Your Login Credentials For GoVindu APP"
    from_email = settings.EMAIL_HOST_USER
    to_email = [user.email]

    context = {
        'user': user,
        'password': password,
        'mobile': mobile,
        'login_url': 'https://play.google.com/store/apps/details?id=com.govindu&pcampaignid=web_share'
    }

    html_content = render_to_string('email/login_details.html', context)
  # Make sure this template exists
    text_content = f"""
Dear {user.username},

Your account has been created.

Mobile Number: {mobile}
Password: {password}
Login URL: https://play.google.com/store/apps/details?id=com.govindu&pcampaignid=web_share

Please change your password after your first login.

Thank you,
Your Company Name
"""

    email = EmailMultiAlternatives(subject, text_content, from_email, to_email)
    email.attach_alternative(html_content, "text/html")
    email.send()  # <-- This is the line that likely fails