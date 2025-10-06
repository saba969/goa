function evenAndDivisibleByFive(numbers) {
 
  let newList = []

  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0 && numbers[i] % 5 === 0) {
      newList.push(numbers[i])
    }
  }

  console.log("ლუწი და 5-ის ჯერადი რიცხვების სია:", newList)


  let oddSum = 0

  for (let i = 0; i < newList.length; i++) {
    if (newList[i] % 2 !== 0) {
      oddSum += newList[i]
    }
  }

  console.log("ამ სიაში მყოფი კენტი რიცხვების ჯამი:", oddSum)
  return newList
}

