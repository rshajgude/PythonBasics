from tkinter.font import names


class Player:
    def __init__(self, name, birth_year, runs, matches):
        self.name = name
        self.birth_year = birth_year
        self.runs = runs
        self.matches = matches

    def get_avg(self):
        return self.runs/self.matches

    def player_info(self):
        print(f"{self.name} played {self.matches} matches and he scored {self.runs} runs in his career with avg of {self.get_avg()}.")

    def __str__(self):
        return f"{self.name}:{self.birth_year}:{self.runs}:{self.matches}"

p1=Player("Sachin", 1973, 18020, 438)
p1.player_info()
print(p1)