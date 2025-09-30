
function pushElement(arr, element) {
  arr.push(element)
  return arr
}

function addStudent(arr, student) {
  arr.push(student)
  console.log("სტუდენტი დამატებულია!")
}


function popElement(arr) {
  return arr.pop()  
}

function sellProduct(arr) {
  let product = arr.pop()
  console.log("გაყიდული პროდუქტი იყო:", product)
}


function unshiftElement(arr, element) {
  arr.unshift(element)   
  return arr
}

function addCity(arr, city) {
  arr.unshift(city)
  return arr
}


function shiftElement(arr) {
  return arr.shift()   
}


function getLength(arr) {
  return "სიაში არის " + arr.length + " ელემენტი"
}


function concatArrays(arr1, arr2) {
  return arr1.concat(arr2)
}


function pushPopTest(arr) {
  arr.push("test")
  arr.pop();
  return arr
}


function unshiftShiftTest(arr) {
  arr.unshift("hello")
  arr.shift()
  return arr
}


function concatLength(arr1, arr2) {
  let newArr = arr1.concat(arr2)
  console.log("გაერთიანებული სიის სიგრძეა:", newArr.length)
}


function allTogether(arr) {
  arr.unshift("A")
  arr.push("Z")
  arr.shift()
  arr.pop()
  let newArr = ["X", "Y"]
  let finalArr = arr.concat(newArr)
  console.log("საბოლოო სიის სიგრძე არის:", finalArr.length, "და საბოლოო სიაა:", finalArr)
}




let arr = [1, 2, 3]

console.log(pushElement([arr], 4))
addStudent([arr], "გიორგი")

console.log(popElement([arr]))
sellProduct([arr])

console.log(unshiftElement([arr], 0))
console.log(addCity([arr], "თბილისი"))

console.log(shiftElement([arr]))

console.log(getLength([arr]))

console.log(concatArrays([1,2],[3,4]))

console.log(pushPopTest([arr]))
console.log(unshiftShiftTest([arr]))

concatLength([1,2,3],[4,5,6])

allTogether([arr])
