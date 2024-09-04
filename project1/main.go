package main

import (
	"fmt"
	"math/big"
	"math/bits"
	"time"
)

func splitAt(x *big.Int, m2 uint) (*big.Int, *big.Int) {
	// generates a bit map so that I can and numbers to get the top and bottom halves
	mask := big.NewInt(0).Lsh(big.NewInt(1), uint(m2))
	mask.Sub(mask, big.NewInt(1))

	// splits x down the middle
	lox := big.NewInt(0).And(x, mask)
	upx := big.NewInt(0).Rsh(x, uint(m2))

	return upx, lox
}

func karatsuba(x *big.Int, y *big.Int) *big.Int {
	// base case multiplies numbers together once they are small enough
	if x.Cmp(big.NewInt(2)) == -1 && y.Cmp(big.NewInt(2)) == -1 {
		return new(big.Int).Mul(x, y)
	}

	// gets the middle of the numbers by binary length
	m := max(x.BitLen(), y.BitLen())
	m2 := m - (m >> 1)
	bitLen := uint(bits.Len(uint(m2)))
	if m2 == (1 << (bitLen - 1)) {
		m2 = 1 << (bitLen - 1)
	} else {
		m2 = 1 << (bitLen)
	}
	upx, lox := splitAt(x, uint(m2))
	upy, loy := splitAt(y, uint(m2))

	// makes 3 recursive multiplcation calls to multiple each necessary part
	z0 := karatsuba(lox, loy)
	z1 := karatsuba(big.NewInt(0).Add(lox, upx), big.NewInt(0).Add(loy, upy))
	z2 := karatsuba(upx, upy)

	// combines the various numbers using bitshifting and subtracting
	// (z2 × 10 ^ (m2 × 2)) + ((z1 - z2 - z0) × 10 ^ m2) + z0
	unit1 := big.NewInt(0).Lsh(z2, uint(m2)*2)
	unit2 := big.NewInt(0).Sub(z1, z2)
	unit2.Sub(unit2, z0)
	unit2.Lsh(unit2, uint(m2))
	return unit1.Add(unit1, unit2).Add(unit1, z0)
}

func main() {
	j := "3141592653589793238462643383279502884197169399375105820974944592"
	k := "2718281828459045235360287471352662497757247093699959574966967627"
	x := new(big.Int)
	y := new(big.Int)
	x.SetString(j, 10)
	y.SetString(k, 10)
	start := time.Now()
	fmt.Printf("%d", karatsuba(x, y))
	fmt.Printf("\n %s", time.Since(start))
	start = time.Now()
	fmt.Printf("%d", big.NewInt(0).Mul(x, y))
	fmt.Printf("\n %s", time.Since(start))
}
