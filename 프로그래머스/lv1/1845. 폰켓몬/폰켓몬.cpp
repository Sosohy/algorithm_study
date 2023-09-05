#include <vector>
#include <set>
#include <stdio.h>
using namespace std;

int solution(vector<int> nums)
{
    int answer = 0;
    set<int> dup(nums.begin(), nums.end());
    
    // for(int i = 0; i<nums.size(); i++){
    //     dup.insert(nums[i]);
    // }
    
    if(dup.size() < nums.size()/2){
        answer = dup.size();
    }else{
        answer = nums.size()/2;
    }
    
    return answer;
}