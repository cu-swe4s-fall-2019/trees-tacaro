(for i in `seq 1 100`; do
    echo -e "$RANDOM" "$RANDOM";
done ) > rand.txt

(for i in `seq 1 100`; do
    echo -e $i $(($i+10));
done ) > sorted.txt
