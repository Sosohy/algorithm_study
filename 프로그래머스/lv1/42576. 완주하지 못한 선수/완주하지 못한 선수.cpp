#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    map<string, int> m;
    for(int i = 0; i < participant.size(); i++) {
        if(m.find(participant[i]) == m.end()) {
            m.insert(make_pair(participant[i],1));
        }
        else {
            m[participant[i]]++;
        }
    }
    
    for(int i = 0; i < completion.size(); i++) {
            m[completion[i]]--; 
    }
    
    for(int i = 0; i < participant.size(); i++) {
        if(m[participant[i]] > 0) {
            answer = participant[i];
        }
    }
    
    return answer;
}
/*
string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    
    for(int i=0; i<participant.size(); i++){
        auto idx = find(completion.begin(), completion.end(), participant[i]);
        if(idx != completion.end()){
            completion.erase(idx);
        }else{
            return participant[i];
        }
    }
    
    return answer;
}
*/