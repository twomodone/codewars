function howMuchILoveYou(nbPetals) {
  let messages = {
    0: "not at all",
    1: "I love you",
    2: "a little",
    3: "a lot",
    4: "passionately",
    5: "madly"
  } 
  return messages[nbPetals % 6];
}
