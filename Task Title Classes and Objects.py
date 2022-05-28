class Student:
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name, age, tracks, score):
        self.name = str(name)
        self.age = int(age)
        self.tracks = [tracks]
        self.score = float(score)

    def change_name(self, new_name):
        self.new_name = new_name
        print("New_name: ", new_name)

    def change_age(self, new_age):
        self.new_age = new_age
        print("New_age: ", new_age)

    def add_track(self, new_tracks):
        self.new_tracks = self.tracks.append(new_tracks)
        print("Added_tracks:", self.tracks)

    def get_score(self):
        print("Score_gotten: ", self.score)


Bob = Student(name="Bob", age=26, tracks=["FE", "BE"], score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
