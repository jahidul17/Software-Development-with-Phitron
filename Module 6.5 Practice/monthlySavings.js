

const monthlySavings=(array,number)=>{   

    if(Array.isArray(array) && Number.isInteger(number)){
        sum=0;

        for(let i=0;i<array.length;i++){
            let element=array[i];
    
            if(element>=3000){
                let tax=(element/100)*20;
                element=element-tax;
            }
            sum=sum+element;
        }
        
        let saving=sum-number;
        if(saving<0){
            return "\"earn more\"";
        }
        else{
            return saving;
        }  
    }
    else{
        return "invalid input";
    }
   
}

all_payment=[1000,2000,2500];
living_cost=5000;

console.log(monthlySavings(all_payment,living_cost));
