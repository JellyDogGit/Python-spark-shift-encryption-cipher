So this was a little idea I had in mind when i was sitting in class bored
It works by taking the message you want to encrypt and putting each letter in a word by a specified shift amount
this makes it pretty hard to decode if you dont have the pattern which it was encrypted with

the way the patterns work is when you define a pattern it takes those numbers and turns them into shift
amounts that cycle through your pattern for example, if you had a pattern for the spark shift like: 12345 it would
line those letters up inside words Hxxxx xExxx xxLxx xxxLx xxxxO like that and to decrypt it does the same thing 
it just pulls out the words

I also implemented the same thing with the caesar cipher so you can mix and match all you want

A common pattern could look something like this: c123 s123 c123 s123. And when applied to a message like: hello world.
you get this:

jobs industrial whore visitor pursed jews say occurrence unwilling junior squinted acquaintance tapping / account enjoyed backwards skipped request to even / difficulty starved square mexico director ajar hull overlooking pickup / apply preliminary accuracy required jewel apparatus objective / bathing assault wide catch scowled / / rejection breasts able school / quote ot direct experiments swallow office failed / curses town snowy skies require hand sugar / navy import equipped box unsure agatha regardless / former up ashes noting partnership

there is a brute force pattern cracker function but it is very inefficent so for an encryption like the one I just showed, with my program would take years to guess

Anyway, if anyone is reading this I hope you enjoy it and i dont know if there are comments but tell me what you would
have done better!

- JellyDog