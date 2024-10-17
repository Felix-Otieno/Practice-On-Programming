void main() {
  Person obj = Person("Alice", 38);
  obj.show();
  print(obj.age);
  print(obj.name);
}

class Person {
  String? name;
  int? age;

  Person(this.name, this.age);

  void show() {
    print("$name \n $age");
  }
}
