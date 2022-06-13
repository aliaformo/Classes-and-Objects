class Student:
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = [tracks]
        self.score = float(score)

    def change_name(self, new_name):
        self.new_name = new_name
        print("\nNew_name: ", new_name)

    def change_age(self, new_age):
        # Should ensure age remains an integer
        if type(new_age) != int:
            print("***Invalid input for age. I am sorry, Age should be an integer number.***")
        else:
            self.age = new_age
            print("New_age: ", new_age)

    def add_track(self, new_track):
        self.tracks.append(new_track)
        print(f"Added new_track: {new_track}.  Total current tracks for student: {self.tracks}")

    def get_score(self):
        print("Score_gotten: ", self.score, "\n")
        return self.score


Bob = Student(name="Bob", age="26", tracks=["FE", "BE"], score=20.90)
# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
