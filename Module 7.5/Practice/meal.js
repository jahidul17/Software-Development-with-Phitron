const allmeal=()=>{
    fetch('https://fakestoreapi.com/products')
    .then(res=>res.json())
    .then((data)=>{
        // console.log(data);
        displayMeal(data);
    });
}


const displayMeal=(products)=>{
    const productContain=document.getElementById("product-container");

    products.forEach(product => {
        console.log(product);

        const div=document.createElement("div");
        div.classList.add("card");

    
        div.innerHTML=`
           <img class="card-image" src=${product.image} alt="">
            <h5>${product.title}</h5>
            <h3>Price: ${product.price}</h3>
            <p>${product.description.slice(0,50)}</p>
            <button onClick="singleProduct('${product.id}')">Details</button>
            <button onclick="handleAddToCart('${product.title?.slice(0,12)}',${product.price})">Add to Cart</button>
        `;
        productsContaine.appendChild(div);
    });
}


allmeal()