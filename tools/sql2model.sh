sed -r 's/^ +`(.+)`(.+)/    \1 = Column(name="\1", \2)/g' | \
sed -r 's/, .+int\(.{1,3}\)/, type_=Integer,/g' | \
sed -r 's/varchar\(([0-9]+)\)/, type_=String(\1),/g' | \
sed -r 's/ text /type_=TEXT/g' | \
sed -r 's/COLLATE .+ci//g' | \
sed -r 's/unsigned//g' | \
sed -r 's/DEFAULT /,default=/g' | \
sed -r 's/,\)/\)/g' | \
sed -r 's/NOT NULL//g' | \
sed -r 's/, *,/,/g' | \
cat