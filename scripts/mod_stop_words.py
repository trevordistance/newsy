###############################################################################
# stop_words
###############################################################################
import wordcloud
###############################################################################

def fcn_stop_words():
    stop_words = set(wordcloud.STOPWORDS)
    stop_words.add("")
    stop_words.add("article")
    stop_words.add("at")
    stop_words.add("amp")
    stop_words.add("as")
    stop_words.add("it")
    stop_words.add("back")
    stop_words.add("best")
    stop_words.add("buy")
    stop_words.add("case")
    stop_words.add("claim")
    stop_words.add("claims")
    stop_words.add("class")
    stop_words.add("day")
    stop_words.add("don")
    stop_words.add("eight")
    stop_words.add("femail")
    stop_words.add("find")
    stop_words.add("first")
    stop_words.add("five")
    stop_words.add("four")
    stop_words.add("go")
    stop_words.add("going")
    stop_words.add("home")
    stop_words.add("how")
    stop_words.add("href")
    stop_words.add("html")
    stop_words.add("I")
    stop_words.add("inline")
    stop_words.add("itemprop")
    stop_words.add("kicker")
    stop_words.add("list")
    stop_words.add("lives")
    stop_words.add("ll")
    stop_words.add("m")
    stop_words.add("make")
    stop_words.add("man")
    stop_words.add("may")
    stop_words.add("month")
    stop_words.add("must")
    stop_words.add("n")
    stop_words.add("n'")
    stop_words.add("need")
    stop_words.add("new")
    stop_words.add("news")
    stop_words.add("nine")
    stop_words.add("now")
    stop_words.add("nThe")
    stop_words.add("n3")
    stop_words.add("of")
    stop_words.add("one")
    stop_words.add("people")
    stop_words.add("put")
    stop_words.add("quot")
    stop_words.add("readers")
    stop_words.add("reveals")
    stop_words.add("return")
    stop_words.add("review")
    stop_words.add("right")
    stop_words.add("s")
    stop_words.add("say")
    stop_words.add("says")
    stop_words.add("sciencetech")
    stop_words.add("section_details")
    stop_words.add("separator")
    stop_words.add("set")
    stop_words.add("seven")
    stop_words.add("show")
    stop_words.add("six")
    stop_words.add("span")
    stop_words.add("sport")
    stop_words.add("star")
    stop_words.add("stars")
    stop_words.add("still")
    stop_words.add("t")
    stop_words.add("take")
    stop_words.add("ten")
    stop_words.add("three")
    stop_words.add("tight")
    stop_words.add("time")
    stop_words.add("times")
    stop_words.add("top")
    stop_words.add("two")
    stop_words.add("tv")
    stop_words.add("url")
    stop_words.add("us")
    stop_words.add("ve")
    stop_words.add("want")
    stop_words.add("week")
    stop_words.add("what")
    stop_words.add("will")
    stop_words.add("word")
    stop_words.add("without")
    stop_words.add("xa0")
    stop_words.add("year")

    return stop_words
