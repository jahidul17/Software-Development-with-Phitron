
const loadAllProduct=()=>{
    fetch('https://fakestoreapi.com/products')
            .then(res=>res.json())
            .then((data)=>{
                // console.log(data);
                displayProduct(data);
            });
};



const displayProduct=(products)=>{
    const productsContaine=document.getElementById("product-container");

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
};


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
    <h3 class="price">${price}</h3>

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


const singleProduct=(id)=>{

    // console.log(id);
    fetch(`https://fakestoreapi.com/products/${id}`)
            .then(res=>res.json())
            .then(json=>console.log(json))
}

loadAllProduct();

// asink award or asynchronous javascript