# Raspberry
125 points

Raspberries are so tasty. I have to have more than just one!

Download the file below.

prompt.txt

## Flag 
```shell
flag{there_are_a_few_extra_berries_in_this_one}
```

## Solution
This one also comes with a text file:
```
n = 7735208939848985079680614633581782274371148157293352904905313315409418467322726702848189532721490121708517697848255948254656192793679424796954743649810878292688507385952920229483776389922650388739975072587660866986603080986980359219525111589659191172937047869008331982383695605801970189336227832715706317
e = 65537
c = 5300731709583714451062905238531972160518525080858095184581839366680022995297863013911612079520115435945472004626222058696229239285358638047675780769773922795279074074633888720787195549544835291528116093909456225670152733191556650639553906195856979794273349598903501654956482056938935258794217285615471681
```

That's 304 digits in n this time. Well, guess what, sympy can still deal with it. Don't even need to do any fancy footwork with square roots of big int or anything. However - we get 32 primes back, not just the usual 2. This is called RSA multi-prime (RSA-MP). Lots of articles written about it, but stackexchange (https://crypto.stackexchange.com/questions/67043/what-is-multi-prime-rsa-rsa-mp) once again describes it beautifully:

- more efficient key-generation and decryption/signing operation
- easier to factor
- neither recommended or recommended against, it's simply an possible option without any endorsement.


As with the previous problem, use the getModInverse function and pop out a flag (albeit takes a bit longer this time).
