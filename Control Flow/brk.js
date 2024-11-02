const grade = 'B';

switch (grade) {
    case 'A':
        console.log("Excellent!");
        break;
    case 'B':
    case 'C': // Fall-through
        console.log("Well done!");
        break;
    case 'D':
        console.log("You passed.");
        break;
    default:
        console.log("Invalid grade.");
}
