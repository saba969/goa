function countGNames(students) {
  let count = 0

  for (let i = 0; i < students.length; i++) {
    if (students[i][0].toLowerCase() === "გ") {
      count++
    }
  }

  console.log("ასო 'გ'-ზე დაწყებული სახელების რაოდენობაა:", count)
  return count
}

