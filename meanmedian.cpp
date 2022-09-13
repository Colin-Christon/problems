#include <iostream>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--){
	    int x,y;
	    cin>>x>>y;
	    int a,b,c;
	    b=y;
	    if(x==y){
	        cout<<x<<" "<<x<<" "<<x<<endl;
	    }
	   else{
	      int ex=(3*x)-b;
	      for(int i=-1000;i<=b;i++){
	          a=i;
	          c=ex-a;
	          if(c<1000){
	          cout<<a<<" "<<b<<" "<<c<<endl;
	           break;
	          }
	      }
	   }
	    
	}
	return 0;
}
