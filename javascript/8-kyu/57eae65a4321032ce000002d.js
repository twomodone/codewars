function fakeBin(x){
  let newString = "";
  for (let i = 0; i < x.length; i++){
    if (x[i] < 5){
      newString += '0';
    } else {
      newString += '1';
    }
  }
  return newString;
}
