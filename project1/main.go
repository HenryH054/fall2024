package main

import (
	"errors"
	"fmt"
	"math"
	"math/big"
)

func parseNum(num *big.Int, bits int) (int32, *big.Int) {
	// returns the top bits (must have bit size set to < 32) and the rest of the big int
	var sigValues int32
	var remainder big.Int
	length := num.BitLen()
	if num.BitLen() <= bits {
		return int32(num.Int64()), nil
	}
	lowerBitFence := length - bits
	lowerBits := big.NewInt(1).Lsh(big.NewInt(1), uint(lowerBitFence))
	lowerBits = lowerBits.Sub(lowerBits, big.NewInt(1))

	remainder = *remainder.And(num, lowerBits)
	sigValues = int32(big.NewInt(1).Rsh(num, uint(lowerBitFence)).Int64())
	return sigValues, &remainder
}

func karatsuba(x *big.Int, y *big.Int) (*big.Int, error) {
	base := 2.0
	m := 31.0
	z := math.Pow(base, m)
	a, b := parseNum(x, int(m))
	c, d := parseNum(y, int(m))
	if b == nil && d == nil {
		return big.NewInt(int64(a) * int64(c)), nil
	}
	if b == nil || d == nil {
		return big.NewInt(0), errors.New("Values of unequal length")
	}
	xy := big.NewInt(1)
	return xy, nil
}

func main() {
	j := "123456789"
	k := "987654321"
	x := new(big.Int)
	y := new(big.Int)
	x.SetString(j, 10)
	y.SetString(k, 10)
	_, err := karatsuba(x, y)
	if err != nil {
		panic(fmt.Sprintf("Something went wrong: %s", err))
	}
}
