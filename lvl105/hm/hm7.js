function filterNames(names) {
 
  let newList = []

  for (let i = 0; i < names.length; i++) {
    if (names[i].length > 5 && names[i].length % 2 === 0) {
      newList.push(names[i])
    }
  }

  console.log("ლუწი სიგრძის (>5) სახელების სია:", newList)


  for (let i = 0; i < newList.length; i++) {
    if (newList[i][0].toLowerCase() === "ა") {
      newList.splice(i, 1)
      i--
    }
  }

  console.log("საბოლოო სია (წაშლილი 'ა'-ზე დაწყებულები):", newList)
  return newList
}

