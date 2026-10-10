class User:
  def __init__(self, id, name, age):
    self.id = id
    self.name = name
    self.age = age
  def show_info(self):
    print(f"ID: {self.id}, Name: {self.name}, Age: {self.age}")

user = User(1, "若松杏南", 18)
user.show_info()
