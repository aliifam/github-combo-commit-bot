a=0
for i in `seq 5`; #just change the 5 numbers as you want how many bot want commit to github
do
    python bot.py 
    let "a+=1"
    echo commit: $a ✔️
done
echo $a success commits to github by bot 🤖
time auto.sh