#include <vector>
#include <set>
#include <stdio.h>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    set<int> dup(nums.begin(), nums.end());
    
    answer = min(dup.size(), nums.size()/2);
    
    return answer;
}