# Conky Crypto Alert (single coin) (by CoinLore)
 
A conky (with a script written in Python) which sets 2 targets, one higher and one lower than the current price of a given crypto. When one of the two targets is reached, the conky emits a sound. Using [CoinLore API](https://www.coinlore.com/cryptocurrency-data-api#ticker) website.<br>

<br>
<br>

## **WIKI**<br>

Download the .zip file, extract the file, copy the file `.conkyrc_crypto` and the folder `.conky` inside your Linux `home`.<br>
If your `home` is named *pippo*, copy inside *pippo* so you get: `/home/pippo/.conky` and `/home/pippo/.conkyrc_crypto`.<br>
Go to `/home/YOURHOMENAME/.conky/crypto/` and open with a text editor the file `crypto_alert.py`, go to rows block 50-60 and decide what you want to use for the two targets values: the script variables or the statement that read the file `usertargets.txt`. Then go to row 62 and edit the ID coin, based on the coin you choosed.<br>
If you don't know how to do all that, follow this video instructions: [APPID guide](https://www.youtube.com/watch?v=aDSMSjkxLsE)<br>
<br>
In the `font` folder, you can find some fonts you need.<br>
The python script saves data in file so you can build your conky weather as you wish.<br>
Edit `.conkyrc_crypto` to build your conky.<br>
The `.conkyrc_crypto` file i attach, works.<br>
Run the file `.conkyrc_crypto` from terminal (the first time you run this conky), so you can get possible errors. 




<br>
<br>

## Screenshot

![](https://github.com/TheHeadlessOfficial/conky_crypto_single_coin/blob/main/.conky/crypto/docs/screenshot.png)<br>

<br>
<br>

<br>

---
[Markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)


