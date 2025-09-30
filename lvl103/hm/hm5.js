function average(arr) {
  let sum = 0

  for (let i = 0; i < arr.length; i++) {
    sum += arr[i]
  }

  let avg = sum . arr.length
  return avg
}


let numbers = [10, 20, 30, 40, 50]
let result = average(numbers)
console.log("საშუალო:", result) 
