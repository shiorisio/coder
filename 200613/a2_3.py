if(A < B) {
      	for(long i = 0;i<T;i++){
          A1 = A1 + V;
          B1 = B1 + W;
          if(A1 >= B1){ ans = 1; break;}
        }
        } else if (A > B) {
        for(long i = 0;i<T;i++){
          A1 = A1 - V;
          B1 = B1 - W;
          if(A1 <= B1){ ans = 1; break;}
        }
        } else {
          ans = 1;
        }
