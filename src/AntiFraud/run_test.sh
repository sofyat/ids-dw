#!/bin/bash

# run_test.sh https://github.com/InsightDataScience/digital-wallet"""
# helper script for running all the tests
# author Sofya Irwin
# email sofyat@gmail.com
# date Thu Nov 10 13:40:07 PST 2016

TESTS="unit_test antifraud antifraud_trie"

if [ $# -ne 0 ]; then
    TESTS="$*"
fi

unit_test()
{
    python2 -m unittest discover
}

_antifraud_helper()
{
    script=$1
    rm -rf ./test-outputs ./test-inputs
    mkdir -p ./test-outputs ./test-inputs
    batchf=./test-inputs/batch
    streamf=./test-inputs/stream
    out1=./test-outputs/out1
    out2=./test-outputs/out2
    out3=./test-outputs/out3
    echo "time, id1x, id2x, amount, message" > $batchf
    echo "2016-11-02 09:38:53, 11, 12, 3.19, l1" >> $batchf
    echo "2016-11-02 09:38:53, 12, 13, 3.19, l2" >> $batchf
    echo "2016-11-02 09:38:53, 13, 14, 3.19, l3" >> $batchf
    echo "time, id1x, id2x, amount, message" > $streamf
    echo "2016-11-02 09:49:29, 11, 12, 20.42, s1" >> $streamf
    echo "2016-11-02 09:49:29, 11, 14, 20.42, s2" >> $streamf
    cmd="$script $batchf $streamf $out1 $out2 $out3"
    echo "cmd: $cmd"
    eval $cmd || return 1
    cat $out1 | paste -d ' ' - $out2 $out3 > ./test-outputs/out
    echo "result: ./test-outputs/out"
    echo "trusted trusted trusted" > ./test-outputs/expected
    echo "unverified unverified trusted" >> ./test-outputs/expected
    diff ./test-outputs/out ./test-outputs/expected || return 1
    rm -rf ./test-outputs
    rm -rf ./test-inputs
}

antifraud()
{
    _antifraud_helper ./antifraud.py
}

antifraud_trie()
{
    _antifraud_helper ./antifraud_trie.py
}


error_count=0
for test in $TESTS; 
do
    echo $test
    eval $test
    if [ $? -eq 0 ]; then
        echo "TEST RESULT: $test succeeded"
    else
        echo "TEST RESULT: $test failed"
        let error_count+=1
    fi
done
exit $error_count

