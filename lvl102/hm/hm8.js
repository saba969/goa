function countEvenOdd(n) {
  let i = 1
  let evenCount = 0 
  let oddCount = 0

  while (i <= n) {
    if (i % 2 === 0) {
      evenCount = evenCount + 1
    } else {
      oddCount = oddCount + 1
    }
    i = i + 1 
  }

  console.log("1-დან", n, "მდე:")
  console.log("ლუწი რიცხვების რაოდენობა:", evenCount)
  console.log("კენტი რიცხვების რაოდენობა:", oddCount)
}


countEvenOdd(5)
countEvenOdd(10)
countEvenOdd(15)
