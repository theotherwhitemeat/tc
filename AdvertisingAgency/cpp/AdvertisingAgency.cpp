/*
http://community.topcoder.com/stat?c=problem_statement&pm=7558
Problem Statement for AdvertisingAgency


Problem Statement
        
You are working in an advertising agency. There are 100 billboards owned by your agency,
numbered from 1 to 100.

You clients send you requests, one after another. Each request is the number of the
billboard on which the client would like to place his advertisement.

Initially all billboards are empty. Each time you receive a request, you act as follows.
If the corresponding billboard is empty, you satisfy the request and occupy the
billboard with the client's advertisement. If the corresponding billboard is occupied,
you reject the request.

You are given a int[] requests containing the requests in the order you receive them.
Return the number of rejected requests.

 
Definition
        
Class:    AdvertisingAgency
Method:    numberOfRejections
Parameters:    int[]
Returns:    int
Method signature:    int numberOfRejections(int[] requests)
(be sure your method is public)
    
 
Constraints
-    requests will contain between 1 and 50 elements, inclusive.
-    Each element of requests will be between 1 and 100, inclusive.
 
Examples
0)    
        
{1,2,3}
Returns: 0
All requests will be satisfied.
1)    
        
{1,1,1}
Returns: 2
Only the first request will be satisfied.
2)    
        
{1,2,1,2}
Returns: 2
3)    
        
{100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
 100, 100, 100, 100, 100, 100, 100, 100, 100, 100
}
Returns: 49
*/
// Status: Complete

#include <iostream>
#include <set>
#include <vector>
using namespace std;


class AdvertisingAgency {
public:
	int numberOfRejections(std::vector<int> requests);
};

int AdvertisingAgency::numberOfRejections(std::vector<int> requests) {
	std::set<int> slots_used;
	int fails = 0;
	for (int i = 0; i < requests.size(); i++)
	{
		if (!(slots_used.insert(requests[i]).second)){
			// .insert() returns a pair, the second being
			// a success boolean
			fails++;
		}
	}
	return fails;
}

int main() {
	// setup test cases
	vector<vector<int>> requests = 
		{{1,2,3},
		 {1,1,1},
		 {1,2,1,2},
		 {100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
		 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
		 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
		 100, 100, 100, 100, 100, 100, 100, 100, 100, 100,
		 100, 100, 100, 100, 100, 100, 100, 100, 100, 100}
		 };

	AdvertisingAgency agency;
	for (int i = 0; i < requests.size(); i++){
		int rejections = agency.numberOfRejections(requests[i]);
		cout << "Rejections: " << rejections << endl;
	}
}