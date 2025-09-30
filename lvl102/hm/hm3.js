function checkPassword(correctPassword) {
  let input = prompt("შეიყვანე პაროლი:")

  while (input !== correctPassword) {
    input = prompt("არასწორია, სცადე თავიდან:")
  }

  console.log("წარმატებით!")
}


checkPassword("12345")
