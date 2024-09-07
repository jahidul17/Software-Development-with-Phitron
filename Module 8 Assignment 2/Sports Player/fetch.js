

const allmeals=()=>{
  fetch('https://www.themealdb.com/api/json/v1/1/search.php?f=b')
    .then((res)=>{
        if(!res.ok){
            const message=`Not found : ${res.status}`;
            throw new Error(message);
        }
        return res.json();
    })
    .then((data)=>{
      displaymeal(data.meals);
        // console.log(data.meals)
    })
    .catch((err)=>console.log(err));
}


const displaymeal=(meal)=>{
    const mealContainer=document.getElementById("product-container");
    

    meal.forEach(element => {
        console.log(element);

        const div=document.createElement("div");
        div.classList.add("card");

        div.innerHTML=`
        <img class="card-img" src="${element.strMealThumb}" alt="">        
        <h4>${element.strMeal.slice(0,10)} <b> (${element.strArea}) </b></h4>        
         <p>${element.strInstructions.slice(0,100)}</p>         
         <a href="${element.strYoutube}"><img style="width: 30px; height: 30px; border-radius: 10px;" src="youtube.png" alt=""></a>
         <br>
        <button data-toggle="modal" data-target="#exampleModal" onclick="popUpFun('${element.strMeal}',${element.strInstructions})">Details</button>
        <br>
        <button onclick="handleAddToCart('${element.strMeal?.slice(0,12)}',${element.idMeal})">Add to cart</button>
        
        `
        mealContainer.appendChild(div);
        

    });
}

const popUpFun=(title,discription)=>{

  const popUp=document.getElementById("modal-body");
  const div=document.createElement("div");
  div.classList.add("modal-info");

  div.innerHTML=`  
  <h3>${title}</h3>
  <p>${discription}</p>
  `
  popUp.appendChild(div);

  // console.log(title);
  // console.log(discription);
}

const handleAddToCart=(name,price)=>{
    //cart count
    const cartCount=document.getElementById("cart-count").innerText;
    let convertedCount=parseInt(cartCount);
    convertedCount+=1;
    document.getElementById("cart-count").innerText=convertedCount;

    // console.log(info);

    const container=document.getElementById("cart-main-container");

    const div=document.createElement("div");
    div.classList.add("cart-info");

    div.innerHTML=`
    <p>${name.slice(0,10)}</p>
    <p class="price">${price}</p>

    `
    container.appendChild(div);
    UpdateTotal();
}


const UpdateTotal=()=>{
    const allPrice=document.getElementsByClassName("price");
    let count=0;
    for(const element of allPrice){
        count=count+parseFloat(element.innerText);
    }

    document.getElementById("total").innerText=count.toFixed(2);
    
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



allmeals();




