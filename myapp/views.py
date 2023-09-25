from django.shortcuts import render,redirect
from django.utils.html import mark_safe
from django.http import JsonResponse
from django.http import request
import openai
import os
from .models import Diet

from dotenv import load_dotenv

load_dotenv()

# ... other settings ...

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


openai.api_key  = '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'

def report(request):
        age=request.POST['age']
        gender=request.POST['gender']
        height=request.POST['height']
        weight=request.POST['weight']
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(age,gender,height,weight),
            temperature=0,
            max_tokens=1000  # Adjust this value as needed
        )
        result=response.choices[0].text
        
        return render(request,"report.html",{'result': mark_safe(result)})

def profile(request):
    return render(request,"detail.html")
        
   



def generate_prompt(age,gender,height,weight):
    profile= f"""
    Age: {age}
    Gender: {gender}
    Weight: {weight}
    Height: {height}
    Activity Level: Active
    Health Goals: Weight Gain
    Dietary Preferences: Vegetarian
    Allergies or Dietary Restrictions: None
    
    Number of Meals per Day: 4

    Nutrient Requirements:
        Protein: 100 g/day
        Fiber: 25 g/day
        
    Daily Schedule:
        Wake-up Time: 7:00 AM
        Bedtime: 11:00 PM
        Preferred Meal Times: Breakfast (8:00 AM), Lunch (1:00 PM), Snack (4:00 PM), Dinner (8:00 PM)
    Additional Information:
        No Medical Conditions
        No Dietary Supplements or Medications

    "Give response in well formatted html report"
"""
    prompt="Generate a personalized diet plan for the following profile:" + profile
    return prompt
    



# Create your views here.
from django.http import HttpResponse



def bodyfat(request):
    return render(request,'bodyfatCalculator.html')

def calorie(request):
    return render(request,'calorieCalculator.html')

def bmi(request):
    return render(request,'bmical.html')



import requests 
from django.core.cache import cache
import datetime

def api_data_view(request):
    # Check if the data is already in the cache
    cached_data = cache.get('api_data')

    if cached_data is None:
        # Data is not in the cache, fetch it from the API
        api_url = 'https://content.guardianapis.com/search?q=12%20years%20a%20slave&page-size=6&format=json&tag=food/food&from-date=2010-01-01&show-tags=contributor&show-fields=starRating,headline,thumbnail,short-url&order-by=relevance&api-key=e4f451bc-3a4f-445f-809f-2d28fbb0bb91'

        try:
            response = requests.get(api_url)
            response.raise_for_status()
            response_data = response.json()
            articles = response_data.get('response', {}).get('results', [])
            cache.set('api_data', articles, 3600)  # Cache the data for 1 hour (adjust as needed)
            error_message = None
        except requests.exceptions.RequestException as e:
            error_message = str(e)
            articles = []
    else:
        # Data is in the cache, retrieve it
        articles = cached_data
        error_message = None

    # Fetch diets from your model
    diets = Diet.objects.all()

    return render(request, 'index.html', {'articles': articles, 'diets': diets, 'error_message': error_message})




