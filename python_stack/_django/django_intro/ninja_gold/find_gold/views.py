from django.shortcuts import render, HttpResponse, redirect
import random
import datetime


# Create your views here.
def index(request):
    # check for gold in session:
    if 'gold' in request.session:
        return render(request, 'find_gold/index.html')
    # if none, set to 0 and create empty logs
    else:
        request.session['move_count'] = 0
        request.session['gold'] = 0
        request.session['logs'] = []
        return render(request, 'find_gold/index.html')


def take_bet(request):
    if 'guess' in request.session:
        return redirect("/")
    else:
        request.session['guess'] = int(request.POST['guess'])
        return redirect("/")


def process(request):
    # make sure the user submitted a bet
    if 'guess' not in request.session:
        request.session['message'] = ("You must place a bet!")
        return redirect("/")

    # get place value from POST and adjust 'gold' accordingly:
    if request.POST['mine'] == 'casino':
        earned_gold = random.randint(-50, 50)

    elif request.POST['mine'] == 'farm':
        earned_gold = random.randint(10, 20)

    elif request.POST['mine'] == 'cave':
        earned_gold = random.randint(5, 10)

    elif request.POST['mine'] == 'house':
        earned_gold = random.randint(2, 5)

    # adjust gold 
    request.session['gold'] += earned_gold
    # log the activity: 
    timestamp = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S +0000")
    if earned_gold > 0:
        log = (f"Earned {earned_gold} gold from the {request.POST['mine']}! {timestamp}")
        request.session['logs'].append(log)
    else:
        log = (f"\nEntered a casino and lost! {earned_gold} gold. Ouch! {timestamp}")
        request.session['logs'].append(log)       
    
    # increment the move count:
    request.session['move_count'] += 1
    # check to see if user won:
    if request.session['move_count'] < request.session['guess']:
        moves_left = (request.session['guess'] - request.session['move_count'])
        request.session['message'] = (f'{moves_left} moves remaining!')

    if request.session['gold'] < 200:
        if request.session['move_count'] == request.session['guess']:
            request.session['message'] = ("You lost! Try again.")

    if request.session['gold'] >= 200:
        if request.session['move_count'] == request.session['guess']:
            request.session['message'] = ("You won!")
        else:
            request.session['message'] = ("Too early! Please try again.")      

    return redirect("/")


def reset(request):
    request.session.flush()
    return redirect("/")