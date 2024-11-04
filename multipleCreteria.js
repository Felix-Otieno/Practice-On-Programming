const items = [
    { name: 'Apple', price: 100, quantity: 5 },
    { name: 'Banana', price: 50, quantity: 3 },
    { name: 'Banana', price: 60, quantity: 2 },
    { name: 'Apple', price: 80, quantity: 4 }
  ];
  
  // Sort by name first, then by price, and finally by quantity
  items.sort((a, b) => {
    if (a.name < b.name) return -1;
    if (a.name > b.name) return 1;
    // If names are equal, sort by price
    if (a.price < b.price) return -1;
    if (a.price > b.price) return 1;
    // If prices are also equal, sort by quantity
    return a.quantity - b.quantity; // Ascending order for quantity
  });
  
  console.log(items);
  