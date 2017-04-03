#! /usr/bin/python
# -*- coding: utf-8 -*-

print 'あなたの名前を教えてください。'

# 3系は「input」を使用、2系「raw_input」を使用
your_name = raw_input(">> ")

print "こんにちは！{}さん" . format(your_name)

