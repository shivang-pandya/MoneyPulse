
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
import requests  
from website.models import Members
from gnews import GNews  # Google News API wrapper


@csrf_exempt
def convert_index(request):
    if not request.session.get('user_email'):
        return redirect('login')  # Only allow access if user is logged in

    user_email = request.session.get('user_email')
    user_name = request.session.get('user_name')

    context = {
        'user_email': user_email,
        'user_name': user_name,
        'conversion_result': None,
        'error_message': None
    }

    if request.method == 'POST':
        try:
            amount = float(request.POST.get('amount'))
            from_currency = request.POST.get('from_currency').upper()
            to_currency = request.POST.get('to_currency').upper()

            response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{from_currency}")
            data = response.json()

            if 'rates' in data and to_currency in data['rates']:
                converted = round(amount * data['rates'][to_currency], 2)
                context['conversion_result'] = f"{amount} {from_currency} = {converted} {to_currency}"
            else:
                context['error_message'] = "Invalid currency code."
        except Exception as e:
            context['error_message'] = f"Error: {str(e)}"

    return render(request, 'converter_index.html', context)

@csrf_exempt
def live_updates(request):
    if not request.session.get('user_email'):
        return redirect('login')

    user_email = request.session.get('user_email')
    user_name = request.session.get('user_name')
    base_currency = request.GET.get('currency', 'USD')  # default: USD

    rates = {}
    error = None

    try:
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base_currency}")
        data = response.json()

        if 'rates' in data:
            rates = data['rates']
        else:
            error = "Unable to fetch rates."
    except Exception as e:
        error = f"Error: {str(e)}"

    return render(request, 'live_update.html', {
        'user_email': user_email,
        'user_name': user_name,
        'base_currency': base_currency,
        'rates': rates,
        'error': error
    })

@csrf_exempt
def update_profile(request):
    if not request.session.get('user_email'):
        return redirect('login')

    user_email = request.session.get('user_email')
    user = Members.objects.get(email=user_email)

    if request.method == 'POST':
        new_name = request.POST.get('uname')
        new_email = request.POST.get('email')
        new_password = request.POST.get('passwd')

        user.uname = new_name
        user.email = new_email

        if new_password:
            user.passwd = new_password

        user.save()

        request.session['user_name'] = new_name
        request.session['user_email'] = new_email

        messages.success(request, "Profile updated successfully!")
        return redirect('update_profile')

    return render(request, 'update_profile.html', {'user': user})

@csrf_exempt
def news_view(request):
    gnews = GNews(language='en', country='us', max_results=10)
    articles = []
    error = None

    try:
        results = gnews.get_news('exchange rate OR forex OR currency')
        for art in results:
            articles.append({
                'title': art.get('title'),
                'description': art.get('description'),
                'url': art.get('url') ,
                'published': art.get('published date'),
                'publisher': art.get('publisher')
            })
    except Exception as e:
        error = f"Could not fetch news ({e})"

    return render(request, 'news.html', {
        'articles': articles,
        'error_message': error
    })