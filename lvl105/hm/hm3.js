function cutString(text, num) {
 
  if (text.length > 10) {
    
    let result = text.slice(0, num)
    console.log("შედეგი:", result)
  } else {
    console.log("სტრინგის სიგრძე უნდა იყოს 10-ზე მეტი!")
  }
}



