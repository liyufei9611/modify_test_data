for f in *.txt; do
  head -n 20 $f > ./head/$f
done
