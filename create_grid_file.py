# Python script to generate HTML code for an image grid

# List of image URLs (replace this string with your actual list)
image_list = '''
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972j(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972j(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972g(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972g(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972e(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972e(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972d(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972d(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972c(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972c(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972b(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972b(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972a(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1972/1972a(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1973/1973g(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1973/1973g(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1973/1973e(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1973/1973e(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1973/1973d(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1973/1973d(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1973/1973c(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1973/1973c(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1973/1973b(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1973/1973b(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1973/1973a(c)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1973/1973a(c)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1974/1974g(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1974/1974g(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1974/1974e(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1974/1974e(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1974/1974d(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1974/1974d(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1974/1974c(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1974/1974c(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1974/1974b(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1974/1974b(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1974/1974a(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1974/1974a(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1975/1975g(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1975/1975g(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1975/1975e(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1975/1975e(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1975/1975d(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1975/1975d(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1975/1975c(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1975/1975c(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1975/1975b(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1975/1975b(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1975/1975a(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1975/1975a(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1976/1976g(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1976/1976g(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1976/1976e(c)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1976/1976e(c)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1976/1976d(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1976/1976d(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1976/1976c(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1976/1976c(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1976/1976b(c)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1976/1976b(c)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1976/1976a(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1976/1976a(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977j(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977j(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977g(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977g(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977e(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977e(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977d(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977d(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977c(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977c(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977b(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977b(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977a(c)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1977/1977a(c)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1978/1978g(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1978/1978g(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1978/1978e(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1978/1978e(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1978/1978d(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1978/1978d(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1978/1978c(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1978/1978c(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1978/1978b(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1978/1978b(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1978/1978a(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1978/1978a(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1979/1979g(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1979/1979g(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1979/1979e(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1979/1979e(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1979/1979d(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1979/1979d(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1979/1979c(b)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1979/1979c(b)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1979/1979b(c)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1979/1979b(c)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1979/1979a(c)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1979/1979a(c)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1985/1985g%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1985/1985g%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986i%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986i%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986h%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986h%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986g%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986g%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986f%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986f%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986e%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986e%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986d%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986d%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986c%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986c%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986b(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1986/1986b(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988h%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988h%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988g%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988g%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988f%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988f%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988e%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988e%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988d%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988d%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988c(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988c(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988b(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1988/1988b(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989i1%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989i1%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989i2%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989i2%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989h%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989h%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989g%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989g%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989f%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989f%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989e%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989e%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989d%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989d%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989c(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989c(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989b%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1989/1989b%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990h%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990h%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990g%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990g%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990f%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990f%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990e%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990e%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990d1%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990d1%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990d2%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990d2%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990c(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990c(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990b%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1990/1990b%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992h%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992h%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992g2%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992g2%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992g1%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992g1%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992f%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992f%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992e1%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992e1%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992e2%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992e2%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992d%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992d%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992c(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992c(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992b(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1992/1992b(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993j%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993j%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993h%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993h%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993g%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993g%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993f%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993f%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993e%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993e%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993d%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993d%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993c%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993c%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993b%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1993/1993b%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997j%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997j%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997i%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997i%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997h%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997h%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997g1%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997g1%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997g2%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997g2%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997f%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997f%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997e(a)%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997e(a)%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997d%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997d%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997c%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997c%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997b%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_1997/1997b%20(2).jpg
https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_2016/2016h%20(1).jpg|https://raw.githubusercontent.com/MaxifireGit/coin_photos_ebay_2024/refs/heads/main/proof_2016/2016h%20(2).jpg
'''

# Split the list into lines and remove empty lines
lines = [line.strip() for line in image_list.strip().split('\n') if line.strip()]

# Initialize a list to hold all image data
images = []

# Process each line to extract image URLs and alt text
for line in lines:
    # Split the line by '|' to get individual image URLs
    urls = line.split('|')
    for url in urls:
        # Extract the filename from the URL for alt text
        filename = url.split('/')[-1]
        alt_text = filename.replace('%20', ' ')
        images.append({'url': url, 'alt': alt_text})

# Determine the number of columns for the grid
columns = 6  # Adjust the number of columns as needed
rows = (len(images) + columns - 1) // columns  # Calculate the number of rows

# Start building the HTML content
html_content = '''
<style>
.grid-container {{
    display: grid;
    grid-template-columns: repeat({columns}, 1fr);
    grid-gap: 0;
    width: 100%;
}}

.grid-item {{
    position: relative;
    overflow: hidden;
}}

.grid-item::before {{
    content: "";
    display: block;
    padding-top: 100%; /* 1:1 aspect ratio */
}}

.grid-item img {{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
}}
</style>

<div class="grid-container">
'''.format(columns=columns)

# Add each image to the HTML content
for img in images:
    html_content += '''
    <div class="grid-item">
        <img src="{url}" alt="{alt}">
    </div>
    '''.format(url=img['url'], alt=img['alt'])

# Close the grid container div
html_content += '\n</div>'

# Output the generated HTML content
print(html_content)

# run 
# > python create_grid_file.py > grid.html