void main() {
  String input = "Hello, World! 123";
  
  // Define a RegEx pattern that matches only alphanumeric characters
  RegExp regExp = RegExp(r'[^a-zA-Z0-9 ]');
  
  // Replace all non-alphanumeric characters with an empty string
  String result = input.replaceAll(regExp, '');
  
  print(result); // Output: HelloWorld123
}
