startsize=10000
endsize=1000000
step=10000
docker_image=aaronspirals/pythonds

opt_list=('iteration-for' 'iteration-while' 'iteration-for-range' 'insertion-comp' 'insertion-beginning' 'insertion-middle' 'insertion-end' 'random-access' 'random-removal' 'clean' 'pop' 'extend');

opt_dict=('insertion' 'insertion-comp' 'iteration-key' 'iteration-kv' 'not-in' 'random-access');

opt_set=('insertion' 'insertion-comp' 'iteration' 'random-in' 'not-in');

types=('integer' 'float' 'str');

data_structures=('list' 'set' 'dict');

for ((size=$startsize; size <= $endsize; size += $step)); do
    for ds in "${data_structures[@]}"; do
	for t in "${types[@]}"; do
	    if [ "$ds" == "list" ]; then
		for opt in "${opt_list[@]}"; do
		    # cas d'insertion dans la liste
		    if [[ "$opt" =~ "insertion" ]] || [[ "$opt" == "extend" ]] || [[ "$opt" == "pop" ]] || [[ "$opt" =~ "random" ]] || [[ "$opt" == "" ]] ; then
			for d in {1..3}; do
			    # Pour ajouter tous les éléments, la moitié puis
			    # le tiers
			    for i in {1..20}; do
				# nombre d'éléments à insérer
				ins=$(( $size / $d ))
				sync;  echo 3 > /proc/sys/vm/drop_caches
				swapoff -a && swapon -a
				./tester.sh -n "$ds$t"_"$opt"_"1-$d"_"$size" "$docker_image" --action "$opt" --size $size --data-structure "$ds" --type "$t" --extra $ins
				#  python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t"
				# python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t"
			    done
			done
		    else	# sinon
			for i in {1..20}; do
			    sync;  echo 3 > /proc/sys/vm/drop_caches
			    swapoff -a && swapon -a
			    ./tester.sh -n "$ds$t"_"$opt"_"$size" "$docker_image" --action "$opt" --size $size --data-structure "$ds" --type "$t"
			done
		    fi
		done
	    fi
	    if [ "$ds" == "dict" ]; then
		for opt in "${opt_dict[@]}"; do
		    if [[ "$opt" =~ "insertion" ]] || [[ "$opt" =~ "random" ]] || [[ "$opt" == "not-in" ]] ; then
			for d in {1..3}; do
			    # Pour ajouter tous les éléments, la moitié puis
			    # le tiers
			    for i in {1..20}; do
				# nombre d'éléments à insérer
				ins=$(( $size / $d ))
				sync;  echo 3 > /proc/sys/vm/drop_caches
				swapoff -a && swapon -a
				./tester.sh -n "$ds$t"_"$opt"_"1-$d"_"$size" "$docker_image" --action "$opt" --size $size --data-structure "$ds" --type "$t" --extra $ins
				#  python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t"
				# python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t"
			    done
			done
		    else	# sinon
			for i in {1..20}; do
			    sync;  echo 3 > /proc/sys/vm/drop_caches
			    swapoff -a && swapon -a
			    ./tester.sh -n "$ds$t"_"$opt"_"$size" "$docker_image" --action "$opt" --size $size --data-structure "$ds" --type "$t"
			done
		    fi
		done
	    fi
	    if [ "$ds" == "set" ]; then
		for opt in "${opt_set[@]}"; do
		    if [[ "$opt" =~ "insertion" ]] || [[ "$opt" =~ "random" ]] || [[ "$opt" == "not-in" ]] ; then
			for d in {1..3}; do
			    # Pour ajouter tous les éléments, la moitié puis
			    # le tiers
			    for i in {1..20}; do
				# nombre d'éléments à insérer
				ins=$(( $size / $d ))
				sync;  echo 3 > /proc/sys/vm/drop_caches
				swapoff -a && swapon -a
				./tester.sh -n "$ds"_"$opt"_"1-$d"_"$size" "$docker_image" --action "$opt" --size $size --data-structure "$ds" --type "$t" --extra $ins
				#  python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t"
				# python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t"
			    done
			done
		    else	# sinon
			for i in {1..20}; do
			    sync;  echo 3 > /proc/sys/vm/drop_caches
			    swapoff -a && swapon -a
			    ./tester.sh -n "$ds$t"_"$opt"_"$size" "$docker_image" --action "$opt" --size $size --data-structure "$ds" --type "$t"
			done
		    fi
		done
	    fi
	done
    done
done
