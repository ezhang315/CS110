import random

class MainCharacter:
    def __init__(self, name, x=0, y=0, sp=10):
        self.name = name
        self.x_coord = x
        self.y_coord = y
        self.skill_points = sp
        self.skills = {'Strength' : 0, 'Speed' : 0, 'Intelligence' : 0}
        self.rollSkills()

    def __str__(self):
        name = "Name:  " + self.name + '\n'
        point = "Resides at:  (%d, %d)\n" % (self.x_coord, self.y_coord)
        skills = "Skills: " + str([skill + ': ' + str(self.skills[skill]) for skill in self.skills])
        return name + point + skills

    def rollSkills(self):
        print("You have %d available Skill Points. Distribute them among your strength, intelligence, and speed." % self.skill_points)
        available_points = self.skill_points
        num_skills_remaining = len(self.skills)
        list_skills = list(self.skills)
        while num_skills_remaining > 0:
            points_to_add = int(input("How many skill points will you put into %s?  " % (list_skills[num_skills_remaining - 1])))
            if available_points - points_to_add >= 0:
                self.skills[list_skills[num_skills_remaining - 1]] += points_to_add
                available_points -= points_to_add
                num_skills_remaining -= 1
            else:
                print("You assigned an invalid number of Skill Points to that stat, please try again.")

    def move(self, direction):
        if direction == 'left':
            self.x_coord -= self.skills["Speed"]
        elif direction == 'right':
            self.x_coord += self.skills["Speed"]
        elif direction == 'up':
            self.y_coord += self.skills["Speed"]
        elif direction == 'down':
            self.y_coord -= self.skills["Speed"]

        print(self.name + " moved %d units %s" % (self.skills["Speed"], direction))

    def fight(self, opponent):
        roll = random.randrange(1,21)
        if roll >= 8:
            return True

        else:
            return False

def smallTest():
    kevin = MainCharacter('Kevin')
    kevin.move('left')
    kevin.move('up')
    for i in range(5):
        print(kevin.fight('Kobold'))
    print(kevin)
smallTest()
