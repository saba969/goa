function checkNumbers(start, end) {
  let i = start  
  while (i <= end) {  
    if (i % 2 === 0) {   
      console.log(i, "ლუწია")
    } else {             
      console.log(i, "კენტია")
    }
    i = i + 1   
  }
}


checkNumbers(1, 5)
