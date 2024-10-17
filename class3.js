let number = [0, 1, 2, 3, 4, 5, 78, 89, 100];

let max = number[0];

for(let i = 1; i < number.length; i++) {

    let value = number[i];

    if(value > max) {
        max = value;
        
    }
    

}
 console.log(max)