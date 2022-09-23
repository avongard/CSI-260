"""

The following module is a class implemented to take the values of a countries name, population, and area to calculate and
return data to the user. Through a series of methods the class can accomplish this goal and reference these values to
achieve its goal.

Author: Michael Portegello
Class: CSI-260-02
Assignment: Week 3 Lab
Due Date: September 20, 2021 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""


class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area

    def __str__(self):
        return f'{self.name} population: {self.population} area: {self.area}'

    def __repr__(self):
        return f'<<{self.name}>>'

    def is_larger(self, other: "Country"):
        if self.area > other.area:
            return True
        else:
            return False

    def population_density(self):
        return self.population / self.area

    def summary(self, name, population, area, population_density):
        return f'{self.name} has a population of {self.population} people and is {self.area} square km. It therefore'
        f'has a population density of {population_density:.4f} people per square km.'


canada = Country('Canada', 34482779, 9984670)
usa = Country('United States of America', 313914040, 98826675)
