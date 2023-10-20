from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseBadRequest

from cards.models import *  
import random


def index(request):

   
    return viewCard(request)

def viewData(request):
    data = Subtract.objects.all()

    context = {
        'rows': data
    }

    HTML_STRING = render_to_string('card-view.html', context=context)
    return HttpResponse(HTML_STRING)
 


def viewCard(request, operator='random'):
    if operator == '+':
        card = getCard_add(request)
    elif operator == '-':
        card = getCard_subtract(request)
    elif operator == '*':
        card = getCard_multiply(request)
    elif operator == '/':
        card = getCard_divide(request)
    elif operator == 'random':
        card = getCard_randomOp(request)
    else:
        return HttpResponseBadRequest("Invalid operator")
    
    response = f"""
    {card.lhs} {card.operator} {card.rhs} = {card.result}
    """
    return HttpResponse(response)


def getCard_add(request):

     # totalRows = number of lhs values * number of rhs values
    totalRows = Add.objects.count()
    randomID = random.randint(1, totalRows)
    card = Add.objects.get(id=randomID)

    return card

def getCard_subtract(request):

     # totalRows = number of lhs values * number of rhs values
    totalRows = Subtract.objects.count()
    randomID = random.randint(1, totalRows)
    card = Subtract.objects.get(id=randomID)

    return card

def getCard_multiply(request):

     # totalRows = number of lhs values * number of rhs values
    totalRows = Multiply.objects.count()
    randomID = random.randint(1, totalRows)
    card = Multiply.objects.get(id=randomID)

    return card


def getCard_divide(request):

     # totalRows = number of lhs values * number of rhs values
    totalRows = Divide.objects.count()
    randomID = random.randint(1, totalRows)
    card = Divide.objects.get(id=randomID)

    return card

# returns a card from one of the 4 operations at random
def getCard_randomOp(request):

    randomOp = random.randint(1, 4)

    if randomOp == 1:
        card = getCard_add(request)
    elif randomOp == 2:
        card = getCard_subtract(request)
    elif randomOp == 3:
        card = getCard_multiply(request)
    else:
        card = getCard_divide(request)
 
    return card