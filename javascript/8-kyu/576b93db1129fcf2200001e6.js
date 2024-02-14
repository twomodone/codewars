function sumArray(array) {
  if (!array || array.length <= 2){
    return 0;
  } 
  
  array.sort(function (a, b){return a - b;});
  let sum = 0;
  for (let i = 1; i < array.length - 1; i++){
    sum += array[i];
  }
  return sum;
}
