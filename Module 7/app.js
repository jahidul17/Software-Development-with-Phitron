
// const target=document.getElementsByClassName("box");

// // target.style.color="red";

// const allBox=document.getElementsByClassName("box");

// for(let i=0;i<allBox.length;i++){
//     const element=allBox[i];
//     element.style.backgroundColor="green";

//     if(element.innerText=="Box -5"){
//         element.style.backgroundColor="red"
//     }
// }




// 7.4-Add event listener-------------------

// document.getElementById("handleAdd").addEventListener("click",(Event)=>{
// console.log("Hello box");
// })

// const handleSearch=(Event)=>{
//     console.log("Hello Box");
// }


// const handleSearch=(Event)=>{
//     const inputValue=document.getElementById("search-Box").value;
//     console.log(inputValue);
// }


// 7.5-DOM-Manupulation---------------------

// document.getElementById("handleAdd").addEventListener("click",(Event)=>{
// const inputValue=document.getElementById("search-Box").value;

// const container=document.getElementById("comment-container");

// const p=document.createElement("p");

// p.innerText=inputValue;
// // console.log(p)

// container.appendChild(p)

// // empty then click
// document.getElementById("search-Box").value="";


// })


// 7.6-Dom-Manupulation-------------------------------

document.getElementById("handleAdd").addEventListener("click",(Event)=>{
    const inputValue=document.getElementById("search-Box").value;
    
    const container=document.getElementById("comment-container");
    
    const p=document.createElement("p");
    
    p.classList.add("Child");

    p.innerText=inputValue;
    // console.log(p)
    
    container.appendChild(p)
    
    // empty then click
    document.getElementById("search-Box").value="";

    const allcomments=document.getElementsByClassName("Child");

    // for(let i=0;i<allcomments.length;i++){
    //     const element=[i];
    // }
    // same as

    // console.log(allcomments);
    // for(const element of allcomments){
    //     console.log();
    // }
    

    for(const element of allcomments){
        element.addEventListener("click",(e)=>{
            e.target.parentNode.removeChild(element);
        });
    }
    
    
    });


    // 7.8-API-jsonplace holder------------------------

    fetch('https://jsonplaceholder.typicode.com/todos/1')
    .then(response=> response.json())
    .then(data=>{
        console.log(data);
    }
       
    )
    .catch((err)=>{
        console.log(err);
    });


    // 7.9-Api-jsonplaceholder------------------------
    const displayData=(userData)=>{
        const container=document.getElementById
        ("userData-container");

        userData.forEach((user)=>{
            const div=document.createElement("div");

            div.innerHTML=
            `
            <h4>Title</h4>
            <p>Description</p>
            <button>Details</button>
            `
            ;         

            
            container.appendChild(div);

        });

    };








