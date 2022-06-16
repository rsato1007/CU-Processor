from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MemberSerializer
from .models import Member

# This class handles the creation and deletion of new users of the API (i.e., employees of the credit union).
# class User(APIView):
    # Post requests will handle the creation of new users to the website. Only users with admin abilities can create a new user.
    # def post(self, request, format=None):
        # This post will automatically assign the username to be the user's initials, if the user's intials are already being used by
        # someone else, then we can add a number to the end for the username. For example if Robert Sato worked there
        # then his username would be RS. However, if Ralph Sun joins the credit union, his username would be RS1.
        # Let's also assign the password to something temporary. Maybe we can implement reset password to email or something like that.

# This class handles all member based requests including getting an individual member, creating an individual member, etc.
class Member(APIView):
    serializer_class = MemberSerializer
    def get(self, request, format=None):
        print("You've submitted a get request")
        return Response("Hello World")

    def post(self, request, format=None):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)
        print("You've successfully created a new member")
        return Response("Thanks for creating a new member bud.")

# This class will handle creating new memberships, editing memberships, and viewing memberships.
# class Membership(APIView):
    # This specific request will handle the creation of new memberships
    # def post(self, request, format=None):

# This class will handle transaction based requests
# class Transactions(APIView):
    # This handles transactions done an account including transfers, withdrawals, etc.
    # def post(self, request, format=None):


# Create your views here.
# Some things to code in views.py:
# (1) only display middle initial instead of middle name
# (2) Implement rules for what member numbers are allowed:
# --Must be at least 6 digits and 9 digits max
# --Can't have numbers like 111222, 333444 (We'll figure out how to program this)
# --Maybe program something where it starts with 6 digits and increases as the number gets bigger.
# in fact my initial idea is to have the program start at the halfway point and go from there. Halves 1000 times or soemthign like that.
# There's a name for this algorithm, I know it.

# # Helper functions for testMemberNumber
# # first one checks for number of unique digits in member number
# def uniqueDigits(str):
#     counter = 0
#     compareStr = ""
#     for digit in str:
#         if compareStr.find(digit) < 0:
#             counter += 1
#             compareStr += digit
#         if counter == 3:
#             return False
#     return True

# # Checks if the member number is comprised of sequential digits with
# # the following format: 1234, 2345, 6789, etc. So a number like 123466 would fail this test since the first four 
# # meet the criteria we're trying to avoid.
# # Let's revamp this one, it's overkill.
# def countUpCheck(num):
#     # For this one, I am thinking of a window based pattern.
#     increase_count = 0
#     decrease_count = 0
#     winEnd = 1
#     while winEnd < len(num):
#         # Checks for possible sequential increasing order (12345..etc)
#         if int(num[winEnd - 1]) + 1 == int(num[winEnd]):
#             increase_count += 1
#         else:
#             increase_count = 0
#         # Checks for possible sequential decreasing order (654321...etc)
#         if int(num[winEnd - 1]) - 1 == int(num[winEnd]):
#             decrease_count += 1
#         else:
#             decrease_count = 0
#         if increase_count == len(num) - 1 or decrease_count == len(num) - 1:
#             return True
#         winEnd += 1
#     return False

# # A function designed to be a unit test for the member numebr function to ensure 
# # it's not selecting unsecure numbers for membership (i.e., 123456, 222222, etc.).
# # The function calls two other functions for better organization.
# def testMemberNumber(num):
#     # Ensures number isn't less than 5 digits or more than 9 digits.
#     if num <= 100000 or num >= 1000000000:
#         return False
#     # converts number to string for other tests.
#     num = str(num)
#     if uniqueDigits(num):
#         return False
#     if countUpCheck(num):
#         return False
#     return True

# # This function provides a secure member number based on criteria
# # mentioned above.
# def createNum(num = None):
#     # Maybe this can be a while function that only breaks out once it run through the function tests
#     # and has a number that meets those requirements.
#     if num:
#         # Instead of going through each number one at time, I am going to implement
#         # the ability 
#         valid = testMemberNumber(num)
#         while not valid:
#             num += 1
#             valid = testMemberNumber(num)
#             print(num)
#         return num
#     else:
#         num = 100011
#         num = createNum(num)
#         return num

# print("This is the num I got: ", createNum())
# print(testMemberNumber(53647)) # Fail
# print(testMemberNumber(111222)) # Fail
# print(testMemberNumber(88888444)) # Fail
# print(testMemberNumber(123456)) # Fail
# print(testMemberNumber(654321)) # Fail
# print(testMemberNumber(654322)) # Pass
# print(testMemberNumber(19234567)) # Pass
# print(testMemberNumber(375536)) # Pass
# print(testMemberNumber(12345678912)) #Fail