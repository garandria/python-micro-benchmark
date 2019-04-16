for ((size = 1000000000; size <= 1000000000000; size += 10000)); do
    for datastructure in L S D A T; do
	if [ "$datastructure" == "S" ];
	then
	    for t in i s f; do
	        for l in l c r w; do
		    sleep 120
		    ./tester.sh -n "$datastructure$t$l$size" aaronspirals/dstest "-$datastructure$t$l" $size
		done
	    done
	else
	    for t in o i f s; do
		if [ "$datastructure" == "D" ] || [ "$datastructure" == "S" ];
		then
		    for l in c r ; do
			sleep 120
			./tester.sh -n "$datastructure$t$l$size" aaronspirals/dstest "-$datastructure$t$l" $size
		    done
		else
		    for l in l c r w; do
			sleep 120
		        ./tester.sh -n "$datastructure$t$l$size" aaronspirals/dstest "-$datastructure$t$l" $size
		    done
		fi
	    done
	fi
    done
done
