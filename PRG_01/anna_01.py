class User:
  def __init__(self, id, name, age):
    self.id = id
    self.name = name
    self.age = age
  def show_info(self):
    print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}")

user1 = User(1, "若松杏南", 18)
user1.show_info()
user2 = User(2, "若松英寿", 61)
user2.show_info()
user3 = User(3, "若松ひさよ", 60)
user3.show_info()