from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseBadRequest

from cards.models import *  
import random


def index(request):

    HTML_STRING = render_to_string('home-view.html')
    return HttpResponse(HTML_STRING)


def viewCard(request, operation):

    if operation == 'addition':
        card = getCard_add(request)
    elif operation == 'subtraction':
        card = getCard_subtract(request)
    elif operation == 'multiplication':
        card = getCard_multiply(request)
    elif operation == 'division':
        card = getCard_divide(request)
    elif operation == 'everything':
        card = getCard_randomOp(request)
    else:
        return HttpResponseBadRequest("Invalid operation")
    
    # makes templates more dynamic
    context = {
        'operation': operation,
        'lhs': card.lhs,
        'operator': card.operator,
        'rhs': card.rhs,
        'result': card.result  
    }

    HTML_STRING = render_to_string('card-view.html', context=context)
    return HttpResponse(HTML_STRING)


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

# user solves expressions whose operators were selected at random
def getCard_randomOp(request):

    # each operator has a 25% chance of being chosen
    # to place an expression on the card.
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