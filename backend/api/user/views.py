from rest_framework import viewsets
from rest_framework.permissions import AllowAny 
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model, login, logout
from django.views.decorators.csrf import csrf_exempt

import random
import re 

from .serializers import UserSerializer
from .models import CustomUser

# Create your views here.

def generate_session_token(length=20):
    #Return 20 char array of randomized numbers and letters. 
    #Yield cannot be used in this context ie not a generator function. Tokens cached in memory.    
    return ''.join(random.SystemRandom().choice([chr(i) for i in range(97, 123)] + [str(i) for i in range(20)]) for _ in range(length))

@csrf_exempt
def signin(request):
    if not request.method == 'POST':
        return JsonResponse({'error': 'Post request requires valid parameter'})

    username = request.POST['email']
    password = request.POST['password']
    print(username, password) #For debugging in development environment.

    #Validate with regex (re) 
    if not re.match("^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", username): #email/username
        return JsonResponse({'error': 'Enter a valid email/username.'})
    if len(password) < 8: #Check passwd length 
        return JsonResponse({'error': 'Password needs to be at least 8 characters'})

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)
        if user.check_password(password): #Validate passwd
            usr_dict = UserModel.objects.filter(email=username).values().first()
            usr_dict.pop('password') 
            if user.session_token != "0": #Are they already signed in?
                user.session_token = "0"
                user.save() 
                return JsonRespon({'error': 'Already logged-in. Previous session connection is still alive'})
            #Did they provide a valid passwd? 
            token = generate_session_token() 
            user.session_token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': usr_dict}) #Correct passwd

        else: #If password invalid 
            return JsonResponse({'error': 'Invalid password'}) 

    except UserModel.DoesNotExist: #Wrong email provided 
        return JsonResponse({'error': 'Invalid Email'}) 

def signout(request, id):
    logout(request)
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=id) #django included shorthand 
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({'error': 'Invalid user ID'}) 
    return JsonResponse({'status': 'Logout success'}) 


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]} 
    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer
    
    def get_permission(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]] 
        except KeyError:
            return [permission() for permision in self.permission_classes] 

                    
                                            

