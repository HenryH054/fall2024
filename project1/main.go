package main

import (
	"fmt"
	"math/big"
)

func karatsuba(x *big.Int, y *big.Int) *big.Int {
	// base case multiplies numbers together once they are small enough
	if x.Cmp(big.NewInt(2)) == -1 || y.Cmp(big.NewInt(2)) == -1 {
		return new(big.Int).Mul(x, y)
	}

	// gets the middle of the numbers by binary length
	m := max(x.BitLen(), y.BitLen())
	m2 := m / 2

	// generates a bit map so that I can and numbers to get the top and bottom halves
	mask := new(big.Int).Lsh(big.NewInt(1), uint(m2))
	mask.Sub(mask, big.NewInt(1))

	// splits x down the middle
	lox := new(big.Int).And(x, mask)
	upx := new(big.Int).Rsh(x, uint(m2))

	// splits y down the middle
	loy := new(big.Int).And(y, mask)
	upy := new(big.Int).Rsh(y, uint(m2))

	// makes 3 recursive multiplcation calls to multiple each necessary part
	z0 := karatsuba(lox, loy)
	z1 := karatsuba(new(big.Int).Add(lox, upx), new(big.Int).Add(loy, upy))
	z2 := karatsuba(upx, upy)

	// combines the various numbers using bitshifting and subtracting
	unit1 := new(big.Int).Lsh(z2, uint(m2)*2)
	unit2 := new(big.Int).Sub(z1, z2)
	unit2 = new(big.Int).Sub(unit2, z0)
	unit2 = unit2.Lsh(unit2, uint(m2))
	return unit1.Add(unit1, unit2).Add(unit1, z0)
}

func main() {
	j := "31415926535897932384626433832795028841971693993751058209749445929999999999999"
	k := "2718281828459045235360287471352662497757247093699959574966967627"
	x := new(big.Int)
	y := new(big.Int)
	x.SetString(j, 10)
	y.SetString(k, 10)
	fmt.Printf("%d", karatsuba(x, y))
}
