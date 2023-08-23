# Bloom Filter

A bloom filter is a hash driven algorithm. It is an algorithm that confirms a probable membership. Conversely, the algorithm confirms that a value is not a member.

Bloom filters are an example of non-secure cryptography but a high- performance methodology for identifying members of list, even if not sorted.

You can use non-secure algorithms with bloom filters, such as MD5 and SHA1. Bloom filters typically rely on 2 or more hash algorithms.

With bloom filters, arbitrarily set the size of the filter. Larger filters more accurately assert membership but performance is slower.

You typically choose two or more hash algorithms to create distribution of bits within the filter. The more algorithms the more accurate the bloom filter. Two or three different algorithms is reasonably accurate for a modest list.