void main() {
  String input = "Hello123";

  // RegEx to check if the string contains only alphanumeric characters
  RegExp regExp = RegExp(r'^[a-zA-Z0-9]+$');
  
  bool isAlphanumeric = regExp.hasMatch(input);
  
  print(isAlphanumeric); // Output: true
}
