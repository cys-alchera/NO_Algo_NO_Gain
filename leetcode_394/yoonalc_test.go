package main

import (
	"github.com/stretchr/testify/assert"
	"testing"
)

func Test_sortColors(t *testing.T) {
	tcs := []struct {
		input  string
		aspect string
	}{
		{"3[a]2[bc]", "aaabcbc"},
		{"10[a]", "aaaaaaaaaa"},
	}

	for _, tc := range tcs {
		t.Run("성공", func(t *testing.T) {
			result := decodeString(tc.input)
			assert.Equal(t, tc.aspect, result)
		})
	}
}
