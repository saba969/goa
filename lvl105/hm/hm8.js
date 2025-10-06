function compareSums(list1, list2) {
  
  let sum1 = 0
  for (let i = 0; i < list1.length; i++) {
    sum1 += list1[i]
  }

  let sum2 = 0
  for (let i = 0; i < list2.length; i++) {
    sum2 += list2[i]
  }

 
  let totalSum = sum1 + sum2

  
  if (totalSum > 50 && totalSum % 2 === 0) {
    console.log("ორი რიცხვის ჯამი არის მაღალი და ეს რიცხვია", totalSum)
  } else {
    console.log("ორი რიცხვის ჯამი არის ძალიან დაბალი და ეს რიცხვია", totalSum)
  }

  return totalSum
}

