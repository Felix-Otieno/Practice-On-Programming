class Dog {
  String? name;
  int? age;
  String? breed;

  Dog(this.name, this.age, this.breed);

  void bark() {
    print("woo! woo! woo!");
  }
}

void main() {
  Dog dogObj = Dog("Bosco", 2, "German Shepherd");

  print(dogObj.name);
  print(dogObj.age);
  print(dogObj.breed);

  dogObj.bark();
}
