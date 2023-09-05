#include <string>
#include <vector>

using namespace std;

int* swap(int a, int b){
    
    int* array = new int[2];
    int tmp = a;
    array[0] = b;
    array[1] = tmp;
    
    return array;
}

long long solution(int a, int b) {
    long long answer = 0;
    
    if(a == b){
        return a;
    }else{
        if(a > b){
            int* t = swap(a, b);
            a = t[0];
            b = t[1];
        }
        for(int i=a; i<=b; i++){
            answer += i;
        }
    }
    return answer;
}