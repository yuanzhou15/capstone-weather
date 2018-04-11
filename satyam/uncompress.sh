#!/bin/bash
#By Satyam Sharma-2018, Computer Engineering, CCNY
for tarfile in *.tar
do
	mkdir ${tarfile[@]:0:9}
	tar -xvf $tarfile -C ${tarfile[@]:0:9} && rm $tarfile
	cd ${tarfile[@]:0:9}
	for gzfile in *.gz
	do gunzip "$gzfile" done cd $OLDPWD
done
echo Its Done, $USER !!!