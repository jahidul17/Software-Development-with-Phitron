
var numbers = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10];
// unique value 
const getUnique=(array)=>(
    [...new Set(array)]
)
console.log(getUnique(numbers));
