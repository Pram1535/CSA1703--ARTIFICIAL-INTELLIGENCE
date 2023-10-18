takes(ajit,his201).
takes(ajit,cse232).
takes(ramu,his201).
takes(ramu,ece321).
classmates(X,Y):-takes(X,Z),takes(Y,Z).
