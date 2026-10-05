# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:21:21 2024

@author: José Alberto Rocha Munguía
"""

# OOP demo: class, inheritance, polymorphism (Hogwarts).
# Change the names / house / year / subject below, then run:
#   python3 hogwarts_oop_demo.py
#
# Prints 4 lines (intro, student detail, then each character.action()).

# --- 1) Class ---
class Character:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    def introduce_self(self):
        return f"Hello, my name is {self.name} and I am from {self.house}"

# try: "Hermione Granger", "Gryffindor"
Ron = Character("Ron Weasley", "Gryffindor")
print(Ron.introduce_self())

# --- 2) Inheritance (Student extends Character) ---
class Student(Character):
    def __init__(self, name, house, year):
        super().__init__(name, house)
        self.year = year

    def student_detail(self):
        return f"{self.introduce_self()}, I am in my year {self.year} at Hogwarts"

# try year "1" or "7"
Ron = Student("Ron Weasley", "Gryffindor", "5")
print(Ron.student_detail())


# --- 3) Polymorphism (same method name, different classes) ---
class Character:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    def action(self):
        return "participates in Hogwarts activities"

class Student(Character):
    def __init__(self, name, house, year):
        super().__init__(name, house)
        self.year = year

    def action(self):
        return f"Attends class and studies for exams in year {self.year}"

class Professor(Character):
    def __init__(self, name, house, subject):
        super().__init__(name, house)
        self.subject = subject

    def action(self):
        return f"teaches {self.subject}"

Ron = Student("Ron Weasley", "Gryffindor", "5")
Mcgonagall = Professor("Minerva McGonagall", "Gryffindor", "Transfiguration")  # try: "Potions"

characters = [Ron, Mcgonagall]

for character in characters:
    print(f"{character.name}: {character.action()}")
