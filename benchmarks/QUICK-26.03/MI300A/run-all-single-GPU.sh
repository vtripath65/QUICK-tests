exe=quick.hip
host=$(hostname -s)
echo ">>> Running on host $host <<<"

for bench in `ls *.in`
do
    echo
    echo "Benchmark $bench"
    tstart=$(date '+%s')
    $exe $bench
    tstop=$(date '+%s')
    echo "$tstart $tstop" | awk '{elapsed=$2-$1; printf " >> Elapsed time = %d seconds = %8.1f minutes\n", elapsed, elapsed/60}'
    prefix=`echo $bench|sed 's/.in//'`
    mv $prefix.out ${prefix}-single-GPU.out
done
