function sumRange(start, end) {
  let sum = 0

  
  for (let i = start; i <= end; i++) {
    sum = sum + i
  }

 
  if (sum > 100) {
    console.log("დიდი ჯამი")
  } else {
    console.log("პატარა ჯამი")
  }
}


sumRange(1, 10)   
sumRange(20, 30)