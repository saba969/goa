
let start = prompt("შეიყვანეთ საწყისი რიცხვი:")
let end = prompt("შეიყვანეთ საბოლოო რიცხვი:")


start = Number(start)
end = Number(end)

let evenCount = 0 
let oddCount = 0  

for (let i = start; i <= end; i++) {
    if (i % 2 === 0) {
        evenCount++ 
    } else {
        oddCount++ 
    }
}


console.log("ლუწების რაოდენობა: " + evenCount + ", კენტების რაოდენობა: " + oddCount)



