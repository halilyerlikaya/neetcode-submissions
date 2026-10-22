class Solution {
    public boolean wordPattern(String pattern, String s) {
        // Cümleyi boşluklardan kelimelere ayır
        String[] words = s.split(" ");
        
        // Uzunluklar eşleşmiyorsa baştan elenir (örn: pattern="ab", s="dog cat balık")
        if (words.length != pattern.length()) {
            return false;
        }

        // Harften kelimeye, ve kelimeden harfe iki yönlü kontrol yapacağız
        HashMap<Character, String> charToWord = new HashMap<>();
        HashMap<String, Character> wordToChar = new HashMap<>();

        for (int i = 0; i < pattern.length(); i++) {
            char c = pattern.charAt(i);
            String word = words[i];

            // Daha önce bu harfi gördük mü?
            if (charToWord.containsKey(c)) {
                // Gördüysek, şu anki kelime ile eşleşiyor mu?
                if (!charToWord.get(c).equals(word)) {
                    return false;
                }
            } else {
                // Harfi ilk kez görüyoruz. Peki bu kelime daha önce BAŞKA bir harfe atandı mı?
                if (wordToChar.containsKey(word)) {
                    return false;
                }
                // İki yönlü olarak map'lere kaydet
                charToWord.put(c, word);
                wordToChar.put(word, c);
            }
        }
        
        return true;
    }
}