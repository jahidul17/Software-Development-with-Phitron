
var result=70

if (result<0){
    console.log("Failed")
}
else if(result>=0 && result<=39){
    console.log("You get C grade.")
}
else if (result>=40 && result<60){
    console.log("You get B grade.")
}
else if(result>=60 && result<70){
    console.log("You get A- grade")
}
else if(result>=70 && result<80){
    console.log("You get A grade")
}
else if(result>=80 && result<100){
    console.log("You get A+ grade")
}
else{
    console.log("Invalid Input")
}