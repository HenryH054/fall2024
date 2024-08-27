package main

import (
	"fmt"
	"math/big"
)

func karatsuba(x *big.Int, y *big.Int) *big.Int {
	// base case multiplies numbers together once they are small enough
	if x.Cmp(big.NewInt(2)) == -1 {
		return x.Mul(x, y)
	}

	// gets the middle of the numbers by binary length
	m := max(x.BitLen(), y.BitLen())
	m2 := m / 2

	mask := new(big.Int).Lsh(big.NewInt(1), uint(m2))
	mask.Sub(mask, big.NewInt(1))

	lox := new(big.Int).And(x, mask)
	upx := new(big.Int).Rsh(x, uint(m2))

	loy := new(big.Int).And(y, mask)
	upy := new(big.Int).Rsh(y, uint(m2))

	z0 := karatsuba(lox, loy)
	z1 := karatsuba(new(big.Int).Add(lox, upx), new(big.Int).Add(loy, upy))
	z2 := karatsuba(upx, upy)

	unit1 := new(big.Int).Lsh(z2, uint(m2)*2)
	unit2 := new(big.Int).Sub(z1, z2)
	unit2 = new(big.Int).Sub(unit2, z0)
	unit2 = unit2.Lsh(unit2, uint(m2))
	return unit1.Add(unit1, unit2).Add(unit1, z0)
}

func main() {
	j := "3141592653589793238462643383279502884197169399375105820974944592"
	k := "2718281828459045235360287471352662497757247093699959574966967627"
	x := new(big.Int)
	y := new(big.Int)
	x.SetString(j, 10)
	y.SetString(k, 10)
	fmt.Printf("%d", karatsuba(x, y))
}
