# First argument must be the FULL path to the theme folder!

for file in $1/*; do
  cd /Applications/
  sips -i $1/*
done
