let count = 3;
function shadow() {
  let count = 7;
  {
    let count = 9;
    console.log(count);
  }
  console.log(count);
}
shadow();
console.log(count);
