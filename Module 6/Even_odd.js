const oddEven=(array)=>{
    let evenNumber=[];
    let oddNumber=[];

    for (let i=0;i<array.length;i++){
        const element=array[i];

        if(element%2==0){
            evenNumber.push(element)
        }
        else{
            oddNumber.push(element)
        }
    }

    return oddNumber;
}

const number=[1,2,4,5,6,7,7,8,8,9];

const result = oddEven(number);
console.log(result);