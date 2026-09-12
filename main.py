from pathlib import Path
import random

folder = Path(__file__).parent / "friends"
#print(folder)

files = sorted(folder.glob("*.txt"))

print(f" Files : {files}")
if not files:
    print("Plases put your friend.txt")
friend_file = random.choice(files)

#print(friend_file)
lines = friend_file.read_text(encoding="utf-8-sig").splitlines()

#print(lines)
clean_line = []
for line in lines:
    clean_line.append(line.strip())
answer = lines[0]
clues = lines[1:]
print("เพื่อนคนนี้คือใคร ???")
print("คำตอบเป็นชื่อเควิน ทายได้คำใบ้ละ 1 ครั้ง \n")

for number, clue in enumerate(clues, start=1):
    print(f"{number} คำใบ้ : {clue} ?")
    guess = input(" ทายชื่อ เพื่อนจากคำใบ้ ด้านบน ? ").strip()
    
    if guess.casefold() == answer.casefold():
        print(f" Correct !!!!")
        break
    print("ทายใหม่ อีกครั้ง ?")
print(f" เฉลย : เพื่อนคนนี้ คือ : {answer}")