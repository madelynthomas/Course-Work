#!/usr/bin/env python

"""

An implementation of a combat system for a game.

"""

import random


class DiceRoller(object):
    """A utility class with a static method for dice rolling."""

    @staticmethod
    def roll(times, die):
        """Rolls times number of die-sided dice; returns the total."""
        total = 0
        for i in range(times):
            roll = random.randint(1, die)
            total += roll
        return total


r = DiceRoller()


class Attack(object):
    """Encapsulates the concept of an attack."""

    def __init__(self, name, number, damage_die, d_type, bonus=0):
        """Creates an attack with privates attributes.

        Adds _name, _number, damage_die, d_type, and an optional _bonus
        to self, with values provided by the arguments.

        """
        self._name = name
        self._damage_die = damage_die
        self._number = number
        self._d_type = d_type
        self._bonus = bonus

    def get_attack_type(self):
        """Returns the type of attack, as a string."""
        return self._d_type

    def get_damage(self):
        """Returns a damage value for this attack.

        Rolls _number number of _damage_die sided dice, using
        DiceRoller r, and adds _bonus to that value.

        """

        return r.roll(self._number, self._damage_die) + self._bonus


class Adventurer(object):
    """Encapsulates the concept of an adventurer."""

    def __init__(self, name, hit_points, armor, magic_resistance, initiative):
        """Creates an adventurer with privates attributes.

        Adds _name, _hit_points, _armor, magic_resistance, and _initiative to
        self, with values provided by the arguments.

        """
        self._name = name
        self._hit_points = hit_points
        self._armor = armor
        self.magic_resistance = magic_resistance
        self._initiative = initiative

    def is_alive(self):
        """Returns True if this object has more than 0 hit points."""
        if self._hit_points > 0:
            return True
        else:
            return False

    def get_initiative(self):
        """
        Returns a random integer between 0 and this object's
        _initiative value."""
        return random.randint(0, self._initiative)

    def damage(self, amount, d_type):
        """Applies damage to this object's attributes.

        If the damage type is "physical", reduce this object's hit points by
        what is left after reducing amount by the object's armor. If the damage
        type is "magic", reduce the object's hit points by what is left after
        reducing amount by the object's magic_resistance. Of course, make sure
        that the damage applied can never be less than 0.

        Also prints out information about the damage application process,
        as shown in the example run.

        """
        if d_type == "physical":
            damage = self._armor - amount
            self._hit_points += damage
            print(self._name, "suffers", amount, "damge after absorbing",
                  self._armor, "damage and has",
                  self._hit_points, "hit points left")
            print()
        if d_type == "magic":
            damage = self.magic_resistance - amount
            self._hit_points += damage
            print(self._name, "suffers", amount, "damge after resisting",
                  self.magic_resistance, "damage and has",
                  self._hit_points, "hit points left")
            print()


class Fighter(Adventurer):
    """Encapsulates a Fighter class, inheriting from Adventurer.

    Fighters are defined by 10-sided hit dice (__HD), armor of 10 (__ARMOR),
    and magic resistance (__MR) of 6, which are stored as class variables.

    Note: It is convention to capitalize the names of variables that are to
    remain constant, and note the use of double underscores to indicate
    that the variables are private.

    """
    __HD = 10
    __ARMOR = 10
    __MR = 4

    def __init__(self, name, hit_dice, initiative):
        """Creates a Fighter object.

        Calls the superclass __init__ method with name, a value for hit points
        that is calculated by rolling hit_dice number of __HD dice, __ARMOR,
        __MR, and initiative.

        Also adds a variable _attack that references an instance of the
        Attack class. For our simple game, this lets us create fixed
        attacks such as Attack("Slash", 1, 8, "physical", 2).

        """
        super(Fighter, self).__init__(name, r.roll(hit_dice, Fighter.__HD),
                                      Fighter.__ARMOR,
                                      Fighter.__MR, initiative)
        self._attack = Attack("Slash", 1, 8, "physical", 2)

    def attack(self):
        """Calculates and returns information about an attack from this object.

        Returns a tuple, consisting of a damage value and a damage type. The
        damage value is obtained by calling the get_damage() method on
        _attack, while the type is obtained by calling get_attack_type() on
        _attack.

        Also prints out information about the attack, as shown in the example
        run.

        """
        print(self._name, "attacks with", self._attack._name, "for",
              self._attack.get_damage(),
              self._attack.get_attack_type(), "damage")
        return (self._attack.get_damage(), self._attack.get_attack_type())

    def __str__(self):
        """Returns a string representation of this object.

        The format appears in the example run.

        """
        return str(self._name) + " with " + str(self._hit_points) + \
            " hit points and a " + str(self._attack._name) + " attack"


class Wizard(Adventurer):
    """Encapsulates a Wizard class, inheriting from Adventurer.

    Wizards have 4-sided hit dice, armor of 4, and magic resistance of 10, all
    stored as class variables using the same naming conventions as Fighter.

    """
    __HD = 4
    __ARMOR = 4
    __MR = 10

    def __init__(self, name, hit_dice, initiative):
        """Creates a Wizard object.

        Calls the superclass __init__ method with name, a value for hit points
        that is calculated by rolling hit_dice number of this class's
        __HD dice, __ARMOR, __MR, and initiative.

        Also adds a variable _spell that references an instance of the
        Attack class. For our simple game, this lets us create fixed
        attacks such as Attack("Fireball", 3, 6, "magic").

        """
        super(Wizard, self).__init__(name, r.roll(hit_dice, Wizard.__HD),
                                     Wizard.__ARMOR,
                                     Wizard.__MR, initiative)
        self._spell = Attack("Fireball", 1, 8, "magic", 2)

    def cast(self):
        """Calculates and returns information about a spell from this object.

        Returns a tuple, consisting of a damage value and a damage type. The
        values are obtained by calling get_damage() and get_attack_type() on
        _spell.

        Also prints out information about the attack, as shown in the example
        run.

        """
        print(self._name, "attacks with", self._spell._name, "for",
              self._spell.get_damage(),
              self._spell.get_attack_type(), "damage")
        return (self._spell.get_damage(), self._spell.get_attack_type())

    def __str__(self):
        """Returns a string representation of this object.

        The format appears in the example run.

        """
        return str(self._name) + " with " + str(self._hit_points) + \
            " hit points and a " + str(self._spell._name) + " attack"


if __name__ == "__main__":
    # Create a Fighter object by providing a name, number of hit dice, and
    # initiative value to the Fighter constructor, and print the object out
    a = Fighter("Aragorn", 5, 9)
    print("Created: ", a)

    # Create a Wizard object, using the Wizard constructor with similar
    # information as that provided for Fighter, and print the object out
    b = Wizard("Gandalf", 5, 7)
    print("Created: ", b)
    print()

    # Create a variable to keep track of the rounds of combat
    rounds = 1

    # As long as both combatants are alive, keep fighting rounds
    while a.is_alive() and b.is_alive():
        print("** ROUND", rounds)
        if a.get_initiative() > b.get_initiative():
            print(a._name, "wins initiative!")
            atk = a.attack()
            b.damage(atk[0], atk[1])

        else:
            print(b._name, "wins initiative!")
            atk = b.cast()
            a.damage(atk[0], atk[1])
        rounds += 1

    if a._hit_points > 0:
        print(a._name, "has won with", a._hit_points, "hit points left")
    if b._hit_points > 0:
        print(b._name, "has won with", b._hit_points, "hit points left")
