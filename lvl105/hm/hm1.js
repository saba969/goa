function evenNumbersSum(numbers) {
  let evenList = []
  
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] % 2 === 0) { 

      evenList.push(numbers[i])
    }

  }

  let sum = 0
  for (let i = 0; i < evenList.length; i++) {
    sum += evenList[i];
  }


  console.log("ლუწი რიცხვებია:", evenList)
  console.log("ლუწი რიცხვების ჯამი არის:", sum)
}

