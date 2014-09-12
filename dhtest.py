#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#                   -------------------------------------
#    Diffie-Hellman key exchange example
#    Copyright (C) 2014  Andrey Arapov
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#                   -------------------------------------
#
#
# Notes:
#   - Based on the https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
#   - The parameters used here are artificially small
#   - I've tried to apply KISS principle here
#
#

import random
from fractions import gcd

class bcolors:
        RED = '\033[91m'
        DRED = '\033[31m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        ENDC = '\033[0m'


# Primality test
# https://en.wikipedia.org/wiki/Primality_test#Python_implementation

def is_prime(num):
    if num <= 3:
        if num <= 1:
            return False
        return True
    if not num % 2 or not num % 3:
        return False
    for i in range(5, int(num ** 0.5) + 1, 6):
        if not num % i or not num % (i + 2):
            return False
    return True

print ":: Diffie-Hellman key exchange"
print

# Alice and Bob agree to use a prime number p and base random g.

print "1. Alice and Bob agree to use a prime number"+bcolors.BLUE+" p"+bcolors.ENDC+\
	 " and base random "+bcolors.YELLOW+"g."+bcolors.ENDC
i = 0
while i < 1:
        rand = random.randint(100000, 999999)
        if is_prime(rand):
                p=rand
                i += 1


g = random.randint(1000000, 9999999)

print bcolors.BLUE+"p"+bcolors.ENDC+" =", bcolors.BLUE, p, bcolors.ENDC, "\tprime?", is_prime(p)
print bcolors.YELLOW+"g"+bcolors.ENDC+" =", bcolors.YELLOW, g, bcolors.ENDC
print


print "2. Alice chooses a secret integer "+bcolors.DRED+"a"+bcolors.ENDC+\
	 ", then sends Bob "+bcolors.CYAN+"A"+bcolors.ENDC+" = "+bcolors.YELLOW+"g"+bcolors.ENDC+\
	" ^ "+bcolors.DRED+"a"+bcolors.ENDC+" mod "+bcolors.BLUE+"p"+bcolors.ENDC
a = random.randint(10000, 99999)
print bcolors.DRED+"a"+bcolors.ENDC+" =", bcolors.DRED, a, bcolors.ENDC
A = (g ** a) % p
print bcolors.CYAN+"A"+bcolors.ENDC+" =", bcolors.YELLOW, g, bcolors.ENDC, "^", \
	bcolors.DRED, a, bcolors.ENDC, "mod", bcolors.BLUE, p, bcolors.ENDC, "=",\
	bcolors.CYAN, A, bcolors.ENDC
print


print "3. Bob chooses a secret integer "+bcolors.DRED+"b"+bcolors.ENDC+\
	", then sends Alice "+bcolors.CYAN+"B"+bcolors.ENDC+" = "+bcolors.YELLOW+"g"+bcolors.ENDC+\
        " ^ "+bcolors.DRED+"b"+bcolors.ENDC+" mod "+bcolors.BLUE+"p"+bcolors.ENDC
b = random.randint(10000, 99999)
print bcolors.DRED+"b"+bcolors.ENDC+" =", bcolors.DRED, b, bcolors.ENDC
B = (g ** b) % p
#print bcolors.CYAN+"B"+bcolors.ENDC+" =", bcolors.CYAN, B, bcolors.ENDC
print bcolors.CYAN+"B"+bcolors.ENDC+" =", bcolors.YELLOW, g, bcolors.ENDC, "^", \
	bcolors.DRED, b, bcolors.ENDC, "mod", bcolors.BLUE, p, bcolors.ENDC, "=",\
	bcolors.CYAN, B, bcolors.ENDC
print


print "4. Alice computes her "+bcolors.RED+"s"+bcolors.ENDC+" = "+bcolors.CYAN+"B"+bcolors.ENDC+\
	" ^ "+bcolors.DRED+"a"+bcolors.ENDC+" mod "+bcolors.BLUE+"p"+bcolors.ENDC
s1 = (B ** a) % p
print bcolors.RED+"s"+bcolors.ENDC+" =", bcolors.CYAN, B, bcolors.ENDC, "^", \
	bcolors.DRED, a, bcolors.ENDC, "mod", bcolors.BLUE, p, bcolors.ENDC, "=", bcolors.RED, s1, bcolors.ENDC
print


print "5. Bob computes his "+bcolors.RED+"s"+bcolors.ENDC+" = "+bcolors.CYAN+"A"+bcolors.ENDC+\
	" ^ "+bcolors.DRED+"b"+bcolors.ENDC+" mod "+bcolors.BLUE+"p"+bcolors.ENDC
s2 = (A ** b) % p
#print bcolors.RED+"s"+bcolors.ENDC+" =", bcolors.RED, s2, bcolors.ENDC
print bcolors.RED+"s"+bcolors.ENDC+" =", bcolors.CYAN, A, bcolors.ENDC, "^", \
	bcolors.DRED, b, bcolors.ENDC, "mod", bcolors.BLUE, p, bcolors.ENDC, "=", bcolors.RED, s2, bcolors.ENDC
print


print "6. Alice and Bob now share a secret ( the number"+bcolors.RED, s1, bcolors.ENDC+") which had never passed over the channel"
print

print "    The only "+bcolors.BLUE+"p",p,bcolors.ENDC+", "+bcolors.YELLOW+"g", g, bcolors.ENDC+", "+\
	bcolors.CYAN+"A",A,bcolors.ENDC+" and "+bcolors.CYAN+"B",B,bcolors.ENDC+" have passed over the channel"
print

print "  ", bcolors.DRED, "a", a, bcolors.ENDC, "," , bcolors.DRED, "b", b, bcolors.ENDC, \
	"and", bcolors.RED, "s", s1, bcolors.ENDC, "have never passed over the channel"
print

