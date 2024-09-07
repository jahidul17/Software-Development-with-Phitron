

// console.clear();
// // console.log(window);
// fetch('https://jsonplaceholder.typicode.com/posts')
//     .then((res)=>{
//         if(!res.ok){
//             const message=`Not found : ${res.status}`;
//             throw new Error(message);
//         }
//         return res.json();
//     })
//     .then((data)=>console.log(data))
//     .catch((err)=>console.log(err));






const allproduct=()=>{
    fetch('https://jsonplaceholder.typicode.com/posts')
    .then((res)=>{
        if(!res.ok){
            const message=`Not found : ${res.status}`;
            throw new Error(message);
        }
        return res.json();
    })
    .then((data)=>{
        displayProduct(data);
    })
    .catch((err)=>console.log(err));
}



const displayProduct=(products)=>{
    const productContainer=document.getElementById("product-container");


    products.forEach(element => {
        // console.log(element);

        const div=document.createElement("div");
        div.classList.add("card");


        div.innerHTML=`
        <img src="" alt="">
        <h4>${element.title}</h4>
        <p>${element.body.slice(0,50)}</p>
        <button>Details</button>
        <button>Add to cart</button>
        `
        productContainer.appendChild(div);

    });
}


function search() {
    let filter = document.getElementById("find").value.toUpperCase();
    let item = document.querySelectorAll(".card");
    let l = document.getElementsByTagName("h4");
    for (var i = 0; i <= l.length; i++) {
      let a = item[i].getElementsByTagName("h4")[0];
      let value = a.innerHTML || a.innerText || a.textContent;
      if (value.toUpperCase().indexOf(filter) > -1) {
        item[i].style.display = "";
      } else {
        item[i].style.display = "none";
      }
    }
  }






allproduct()

