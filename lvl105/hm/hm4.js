function separateStrings(list) {
  let evenList = []

  for (let i = 0; i < list.length; i++) {
    if (list[i].length % 2 === 0) {
     
      evenList.push(list[i])
    } else {
      
      list[i] = false
    }
  }

  console.log("განახლებული საწყისი სია:", list)
  console.log("ლუწი სიგრძის სტრინგების ახალი სია:", evenList)
}

