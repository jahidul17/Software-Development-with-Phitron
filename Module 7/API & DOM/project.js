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
        // console.log(product);

        const div=document.createElement("div");

        div.innerHTML=`
            <img src="" alt="">
            <h5></h5>
            <p></p>
            <button>Details</button>
            <button>Add to Cart</button>
        `;
        productsContaine.appendChild(div);
    });
}

loadAllProduct();

// asink award or asynchronous javascript