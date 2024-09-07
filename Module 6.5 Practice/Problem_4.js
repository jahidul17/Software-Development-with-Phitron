const year=prompt("Enter year: ");

if((year%4==0 && year%100!=0) ||(year%400==0)){
    console.log("This is a Leap Year.")
}
else{
    console.log("This is not a Leap Year.")
}


