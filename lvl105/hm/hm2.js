function replaceNamesWithG(students) {
  for (let i = 0; i < students.length; i++) {
    if (students[i][0].toLowerCase() === "გ") { 
      students[i] = false
    }
  }
  console.log("განახლებული სია:", students)
}

let studentList = ["გიორგი", "ნიკა", "თეო", "გუგა", "მარიამ"]
replaceNamesWithG(studentList)
