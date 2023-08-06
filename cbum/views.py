from django.shortcuts import render
from django.http import HttpResponse

from random import choice


# Create your views here.


def home(request):
    return HttpResponse("qale")


medium_password_generator = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                             'i', 'j', 'k', 'l',
                             'm', 'n', 'o', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'p', 'q', 'r', 's', 't',
                             'u', 'v', 'w', 'x',
                             'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                             'Q', 'R', 'S', 'T',
                             'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

hard_password_generator = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8',
                           '9', 'a', 'b', 'c',
                           'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', '0', '1', '2', '3', '4', '5',
                           '6', '7', '8', '9',
                           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                           'H', 'I', 'J', 'K',
                           'L', 'M', '!', '#', '$', '%', '&', '(', ')', '*', '+', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                           'U', 'V', 'W', 'X',
                           'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

for_easy = ""


def easy(request):
    global for_easy
    for i in range(1, 11):
        for_easy += choice(letters)
    return HttpResponse(for_easy)


for_medium = ""


def medium(request):
    global for_medium
    for i in range(1, 16):
        for_medium += choice(medium_password_generator)
    return HttpResponse(for_medium)


for_hard = ""


def hard(request):
    global for_hard
    for i in range(1, 21):
        for_hard += choice(hard_password_generator)
    return HttpResponse(for_hard)
