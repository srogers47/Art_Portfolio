from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt #Requests will be made to backend from react 

import braintree #Payment gateway sandbox. 

#If you intend to use braintree services, hide this configuration in an .env/.dockerignore file.
#In order to connect to braintree sandox servers, you must sign up for a free account.  
gateway = braintree.BraintreeGateway(
        braintree.Configuration(
            braintree.Environment.Sandbox,
            merchant_id = "xy9645bhjvjv3s4n",
            public_key = "72gr49pzwf4tf2wy",
            private_key = "460d144d94d96cfcc64b54f8e2cd7183",
            )
        )
def validate_user_session(id, token):
    UserModel = get_user_model()
    try:
        UserModel.objects.get(pk=id)
        if user.session_token == token:
            return True
        return False

    except UserMode.DoesNotExist:
        return False 

@csrf_exempt
def generate_token(request, id, tokenn): 
    if not validate_user_session(id, token):
        return JsonResponse({'error':'Try logging in again'}) 
    return JsonResponse({'clientToken': gateway.client_token.generate(), 'success': True}) #Pass to frontend 

@csrf_exempt
def process_payment(request, id, token):
    if not validate_user_session(id, token):
        return JsonResponse({'error':'Try logging in again'}) 

    nonce_from_the_client = request.POST["paymentMethodNonce"]
    amount_from_the_client = request.POST["amount"]
    #This is minimal braintree boilerplate required to make transaction.
    result = gatewat.transaction.sale({  #Use these variable names 
        "amount": amount_from_the_client,
        "payment_method_nonce": nonce_from_the_client,
        "options": {
            "submit_for_settlement": True
            }
        }) 

    if result.is_success:
        return JsonResponse({
            'success': result.is_success, 'transaction': {
                'id': result.transaction.id, 
                'amount': result.transaction.amount
                }
            })
    else:
        return JsonResponse({'error': True, 'success': False}) 
