from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

from cards.models import *  
import random


def menu(request): # request is an obj containing info about the sent HTTP request

    # shows a list of links corresponding to flashcard selection options
    return render(request, 'cards/menu-view.html')

# shows an expression (w/o the result) on a flashcard
def viewCard(request, operation):

    if operation == 'addition':
        card = getCard_add()
    elif operation == 'subtraction':
        card = getCard_subtract()
    elif operation == 'multiplication':
        card = getCard_multiply()
    elif operation == 'division':
        card = getCard_divide()
    elif operation == 'all':
        card = getCard_randomOp()
    else:
        return HttpResponseBadRequest("Invalid operation")
    
    # makes templates more dynamic
    context = {
        'operation': operation.capitalize(),
        'lhs': card.lhs,
        'operator': card.operator,
        'rhs': card.rhs,
        'result': card.result  
    }

    return render(request, 'cards/card-view.html', context)


def viewResult(request): 
    
    if request.method == 'POST':
        query = request.POST.get('query') 
        context = {
            'query': query,
        }
        return render(request, 'cards/result-view.html')
    
    else:
        return HttpResponse('ERROR: Form could not be submitted.')

def getCard_add():

     # totalRows = number of lhs values * number of rhs values
    totalRows = Add.objects.count()
    randomID = random.randint(1, totalRows)
    card = Add.objects.get(id=randomID)

    return card

def getCard_subtract():

     # totalRows = number of lhs values * number of rhs values
    totalRows = Subtract.objects.count()
    randomID = random.randint(1, totalRows)
    card = Subtract.objects.get(id=randomID)

    return card

def getCard_multiply():

     # totalRows = number of lhs values * number of rhs values
    totalRows = Multiply.objects.count()
    randomID = random.randint(1, totalRows)
    card = Multiply.objects.get(id=randomID)

    return card


def getCard_divide():

     # totalRows = number of lhs values * number of rhs values
    totalRows = Divide.objects.count()
    randomID = random.randint(1, totalRows)
    card = Divide.objects.get(id=randomID)

    return card

# user solves expressions whose operators were selected at random
def getCard_randomOp():

    # each operator has a 25% chance of being chosen
    # to place an expression on the card.
    randomOp = random.randint(1, 4)

    if randomOp == 1:
        card = getCard_add()
    elif randomOp == 2:
        card = getCard_subtract()
    elif randomOp == 3:
        card = getCard_multiply()
    else:
        card = getCard_divide()
 
    return card