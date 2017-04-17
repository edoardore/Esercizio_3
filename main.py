from TestInsertion import TestInsShuffle
from TestInsertion import TestInsOrdered
from TestInsertion import TestInsBackwards
from TestMergeSort import TestMergeSortShuffle
from TestMergeSort import TestMergeSortOrdered

# test di insertion sort nel caso in cui i valori da ordinare sono casuali
TestInsShuffle()
# test di insertion sort nel caso in cui i valori da ordinare sono ordinati
TestInsOrdered()
# test di insertion sort nel caso in cui i valori da ordinare sono ordinati al contrario
TestInsBackwards()

# test di merge sort nel caso in cui i valori da ordinare sono casuali
TestMergeSortShuffle()
# test di merge sort nel caso in cui i valori da ordinare sono ordinati
TestMergeSortOrdered()
