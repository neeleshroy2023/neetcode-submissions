class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const hash = {}
        for (let word of strs) {
            const freq = Array(26).fill(0)
            for(let i=0; i < word.length; i++) {
                const idx = word.charCodeAt(i) - 'a'.charCodeAt(0)
                freq[idx] += 1
            }

            const key = freq.join('#')
            if (hash[key]) {
                hash[key].push(word)
            } else {
                hash[key] = [word]
            }
        }

        return Object.values(hash)
    }
}
