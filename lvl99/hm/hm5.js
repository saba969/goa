let value = prompt("შეიყვანე რაიმე მნიშვნელობა:")


if (isNaN(value)) {
  console.log("you entered string number,so you are wrong")
} else {
  
  let number = Number(value)

  for (let i = 1; i <= number; i++) {
    if (i % 2 !== 0) { 
      console.log(i)
    }
  }
}
