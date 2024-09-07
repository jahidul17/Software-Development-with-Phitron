
const products=[
    {id:1 ,name:"Xiaomi",description:"This is xiaomi",price:500,color:"Black"},
    {id:2 ,name:"Iphon",description:"This is Iphon",price:600,color:"Gray"},
    {id:3 ,name:"Max",description:"This is Max",price:700,color:"Black"},
    {id:4 ,name:"Max",description:"This is Max",price:700,color:"Black"},
    {id:5 ,name:"Samsung",description:"This is Samsung",price:800,color:"Blue"},
    {id:6 ,name:"Samsung",description:"This is Samsung",price:800,color:"Blue"}
]

//Map
// const result =products.map(emement=>emement.id*2);
// console.log(result);

//Foreach
const result =products.forEach(element=>{
    console.log(element.id);
});



