# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:21:24 2024

@author: José Alberto Rocha Munguía
"""

# Hogwarts OOP: Character, Student, Professor, plus a separate Wand object.
# Change the constructors at the bottom, then run:
#   python3 hogwarts_characters.py
#
# Prints student detail, a blank line, wand text, a blank line, professor detail.

class Character:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    def introduce_self(self):
        return f"Hello my name is {self.name} and my house is {self.house}"

class Wand:
    def __init__(self, material, length):
        self.material = material
        self.length = length
    def wand_description(self):
        return f"Wand made of {self.material}, and the length of my wand is {self.length} cm"

class Student(Character):
    def __init__(self, name, house, year):
        super().__init__(name, house)
        self.year = year
    def student_detail(self):
        return f"{self.introduce_self()} I am in my year {self.year} at Hogwarts"

class Professor(Character):
    def __init__(self, name, house, subject):
        super().__init__(name, house)
        self.subject = subject
    def professor_detail(self):
        return f"{self.name}: Teaches {self.subject}"

# try: "Hermione Granger", "Gryffindor", "4"
harry = Student("Harry Potter", "Gryffindor", "5")
harry_wand = Wand("Elder", "33")   # try: "Holly", "28"

mcgonagall = Professor("Minerva McGonagall", "Gryffindor", "Transfiguration")

print(harry.student_detail())
print()
print(harry_wand.wand_description())
print()
print(mcgonagall.professor_detail())
