sleeptime=120
startsize=1000000000
endsize=1000000000000
nbtests=20
step=10000
for ((size = $startsize; size <= $endsize; size += $step)); do
    for datastructure in L S D A T N; do
	if [ "$datastructure" == "A" ];
	then
	    for t in i s f; do
	        for b in l c r w; do
		    for i in {1..20}; do
			sleep $sleeptime
			./tester.sh -n "$datastructure$t$b$size" aaronspirals/dstest "-$datastructure$t$b" $size
		    done
		done
	    done
	else
	    for t in o i f s; do
		if [ "$datastructure" == "D" ] || [ "$datastructure" == "S" ];
		then
		    for b in c r ; do
			for i in {1..20}; do
			    sleep $sleeptime
			    ./tester.sh -n "$datastructure$t$b$size" aaronspirals/dstest "-$datastructure$t$b" $size
			done
		    done
		else
		    for b in l c r w; do
			for i in {1..20}; do
			    sleep $sleeptime
			    ./tester.sh -n "$datastructure$t$b$size" aaronspirals/dstest "-$datastructure$t$b" $size
			done
		    done
		fi
	    done
	fi
    done
done
