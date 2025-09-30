function findMax(a, b, c) {
  if (a >= b && a >= c) {
    return a   
  } else if (b >= a && b >= c) {
    return b   
  } else {
    return c
  }
}


let result = findMax(7, 12, 5)
console.log("ყველაზე დიდი არის:", result)
