class Dog {
  String? name;
  int? age;
  String? span;

  Dog(this.name, this.age, this.span);

  void dogInfo() {
    print(
        "My dog name is $name and he is $age years old. the life span of dog is abou $name");
  }
}

void main() {
  Dog objDog = Dog("Malcom", 2, "18 years");
  objDog.dogInfo();

}
