function calculateArea(shape) {
    function squareArea(side) {
        return side * side;
    }

    function circleArea(radius) {
        return Math.PI * radius * radius;
    }

    if (shape.type === "square") {
        return squareArea(shape.side);
    } else if (shape.type === "circle") {
        return circleArea(shape.radius);
    }
    return null; // For unsupported shapes
}

// Usage
const square = { type: "square", side: 4 };
const circle = { type: "circle", radius: 3 };

console.log(calculateArea(square)); // 16
console.log(calculateArea(circle)); // 28.27
