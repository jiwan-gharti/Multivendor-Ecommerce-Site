
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from accounts.models import User

@receiver(user_signed_up,sender = User)
def populate_profile(sociallogin, user, **kwargs): 
    print("------------Signal---------------")
    if sociallogin.account.provider == 'google':
        user_data = user.socialaccount_set.filter(provider='google')[0].extra_data        
        print(user_data)
        # picture_url = user_data['picture-urls']['picture-url']
        # email = user_data['email-address']
        # first_name = user_data['first-name']

    
    user.is_customer = True
    user.save()
    