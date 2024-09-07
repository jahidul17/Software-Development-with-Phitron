
var friends=["hero",4,56,'test',{name:"jhon"},["rahim","korim"]]

// for(var i=0; i<friends.length;i++){
//     // console.log(friends[i]);
//     console.log(i);
// }

for(var i=0;i<friends.length;i++){
    var element=friends[i];

    if(element=="test"){
        console.log("It found");
    }
    else{
        console.log("Not found");
    }
}

