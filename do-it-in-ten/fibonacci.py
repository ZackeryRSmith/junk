F = lambda n: (pow(2<<n,n+1,(4<<2*n)-(2<<n)-1)%(2<<n)) if n >= 0 else None
