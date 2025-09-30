function checkResult(p1, p2, p3) {
 
  let sum = p1 + p2 + p3;

  
  let average = sum / 3;

  
  if (average >= 51) {
    console.log("დადებითი შედეგი")
  } else {
    console.log("უარყოფითი შედეგი")
  }
}


checkResult(60, 70, 55); 
checkResult(30, 40, 50);  
