function sumOdd(start, end) {
  let sum = 0

  
  for (let i = start; i <= end; i++) {
    if (i % 2 !== 0) {   
      sum = sum + i
    }
  }

  
  if (sum > 50) {
    console.log("დიდი ჯამი")
  } else {
    console.log("პატარა ჯამი")
  }
}


sumOdd(1, 10)  
sumOdd(10, 20)  
