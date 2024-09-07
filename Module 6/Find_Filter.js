const products=[
    {id:1 ,name:"Xiaomi",description:"This is xiaomi",price:500,color:"Black"},
    {id:2 ,name:"Iphon",description:"This is Iphon",price:600,color:"Gray"},
    {id:3 ,name:"Max",description:"This is Max",price:700,color:"Black"},
    {id:4 ,name:"Max",description:"This is Max",price:700,color:"Black"},
    {id:5 ,name:"Samsung",description:"This is Samsung",price:800,color:"Blue"},
    {id:6 ,name:"Samsung",description:"This is Samsung",price:800,color:"Blue"}
]

// for (let i=0;i<products.length;i++){
//     const element=products[i];

//     if(element.id==3){
//         console.log(element);
//     }
// }

// another way to find

// const result =products.find(emement=>emement.id==3);
// console.log(result);


//Filter
const result =products.filter(emement=>emement.color=="Black");
console.log(result);
