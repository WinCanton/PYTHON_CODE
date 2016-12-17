def toJadenCase(quote_words):
    quote_words = quote_words.split(' ')
    quote_new = ""
    for quote_word in quote_words:
        quote_new = quote_new + quote_word[0].upper() + quote_word[1:] + " "
    return quote_new[:-1]

quote = "How can mirrors be real if our eyes aren't real"
#test.assert_equals(toJadenCase(quote), "How Can Mirrors Be Real If Our Eyes Aren't Real")
print toJadenCase(quote)