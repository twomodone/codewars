function flickSwitch(arr){
  let newArr = [];
  let boolVal = true;
  
  for (let i = 0; i < arr.length; i++){
    if (arr[i] === "flick"){
      boolVal = !boolVal;
    }
    newArr.push(boolVal);
  }
  return newArr;
}
