// Runtime 3 ms Beats 52.63%
// Memory 2.7 MB Beats 33.33%

package leetcode_535

import (
	"encoding/base64"
)

type Codec struct {
}

func Constructor() Codec {
	return Codec{}
}

// Encodes a URL to a shortened URL.
func (this *Codec) encode(longUrl string) string {
	return base64.StdEncoding.EncodeToString([]byte(longUrl))
}

// Decodes a shortened URL to its original URL.
func (this *Codec) decode(shortUrl string) string {
	res, err := base64.StdEncoding.DecodeString(shortUrl)
	if err != nil {
		panic(err)
	}

	return string(res)
}

/**
 * Your Codec object will be instantiated and called as such:
 * obj := CConstructor();
 * url := obj.encode(longUrl);
 * ans := obj.decode(url);
 */
