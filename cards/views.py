""" cards/views.py """
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

from cards.models import *  
import random


def menu(request): # request is an obj containing info about the sent HTTP request

    # will be used to track user's progress while working through flashcard set
    request.session['cardNum'] = 0
    request.session['numCorrect'] = 0

    # shows a list of links corresponding to flashcard selection options
    return render(request, 'cards/menu-view.html')

# shows an expression (w/o the result) on a flashcard
def viewCard(request, operation):

    if operation == 'Addition':
        card = getCard_add()
    elif operation == 'Subtraction':
        card = getCard_subtract()
    elif operation == 'Multiplication':
        card = getCard_multiply()
    elif operation == 'Division':
        card = getCard_divide()
    elif operation == 'All':
        card = getCard_randomOp()
    else:
        return HttpResponseBadRequest("Invalid operation")

    cardNum = request.session['cardNum']
    cardNum += 1
    request.session['cardNum'] = cardNum

    # makes templates more dynamic
    context = {
        'cardNum': cardNum,
        'operation': operation,
        'lhs': card.lhs,
        'operator': card.operator,
        'rhs': card.rhs,
        'result': card.result  
    }

    return render(request, 'cards/card-view.html', context)


def viewResult(request): 
    
    if request.method == 'POST':
        data = request.POST 

        cardNum = request.session['cardNum']
        numCorrect = request.session['numCorrect']

        if data['userAnswer'] == data['result']:
            numCorrect = request.session['numCorrect']
            numCorrect += 1
            request.session['numCorrect'] = numCorrect

        context = {
            'cardNum': cardNum,
            'numCorrect': numCorrect,
            'operation': data['operation'],
            'lhs': data['lhs'],
            'operator': data['operator'],
            'rhs': data['rhs'],
            'result': data['result'],
            'userAnswer': data['userAnswer']
        }
        return render(request, 'cards/result-view.html', context)
    
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