startsize=10000
endsize=1000000
step=10000
docker_image=aaronspirals/pythonDS

opt_list=('iteration-for' 'iteration-while' 'iteration-for-range' 'iteration-comp' 'insertion-beginning' 'insertion-middle' 'inertion-end' 'random-access' 'random-removal' 'clean' 'pop' 'extend');

opt_dict=('insertion' 'insertion-comp' 'iteration-key' 'iteration-kv' 'not-in' 'random-access');

opt_set=('insertion' 'insertion-comp' 'iteration' 'random-in' 'not-in');

types=('integer' 'float' 'str');

data_structures=('list' 'set' 'dict');


for ((size=$startsize; size <= $endsize; size += $step)); do
    for ds in "${data_structures[@]}"; do
	for t in "${types[@]}"; do
	    if [ "$ds" == "list" ]; then
		for opt in "${opt_list[@]}"; do
		    for i in {1..20}; do
			./tester.sh -n "$ds"_"$opt"_"$size" "$docker_image" --action "$opt" --size $size --data-structure "$ds" --type "$t"
			# echo python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t"
			# python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t"
		    done
		done
	    fi
	    if [ "$ds" == "dict" ]; then
		for opt in "${opt_dict[@]}"; do
		    for i in {1..20}; do
			./tester.sh -n "$ds"_"$opt"_"$size" "$docker_image" --action "$opt" --size $size --data-structure "$ds" --type "$t"
		    done
		done
	    fi
	    if [ "$ds" == "set" ]; then
		for opt in "${opt_set[@]}"; do
		    for i in {1..20}; do
			./tester.sh -n "$ds"_"$opt"_"$size" "$docker_image" --action "$opt" --size $size --data-structure "$ds" --type "$t"
		    done
		done
	    fi
	done
    done
done
