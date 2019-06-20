opt_list=('iteration-for' 'iteration-while' 'iteration-for-range' 'insertion-comp' 'insertion-beginning' 'insertion-middle' 'insertion-end' 'random-access' 'random-removal' 'clean' 'pop' 'extend' 'create-beginning' 'create-end' 'modify-map-lambda' 'modify-comp' 'modify-map-fct' 'modify-loop' 'insertion-beginning-concat' 'insertion-end-concat' 'access-in-list' 'access-in-set');

opt_dict=('insertion' 'insertion-comp' 'iteration-key' 'iteration-kv' 'not-in' 'random-access' 'random-removal' 'not-in-fct' 'in-fct' 'in-error');

opt_set=('insertion' 'insertion-comp' 'iteration' 'random-in' 'not-in' 'random-removal');

types=( 'integer' );

data_structures=('list' 'set' 'dict');

size=10

for ds in "${data_structures[@]}"; do
    for t in "${types[@]}"; do
	if [ "$ds" == "list" ]; then
	    for opt in "${opt_list[@]}"; do
		echo python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t" --extra 1
		python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t" --extra 1
	    done
	fi
	if [ "$ds" == "set" ]; then
	    for opt in "${opt_set[@]}"; do
		echo python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t" --extra 1
		python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t" --extra 1
	    done
	fi
	if [ "$ds" == "dict" ]; then
	    for opt in "${opt_dict[@]}"; do
		echo python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t" --extra 1
		python main.py --action "$opt" --size $size --data-structure "$ds" --type "$t" --extra 1
	    done
	fi
    done
done
		
		
