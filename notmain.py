# try:
#     print('Start code')
#     print(error)
#     print('no errors')
# except:
#     print('we have an error')
# print('code after capsule')



# try:
#     print('start code')
#     print(10 / 0)
#     print('mgm')
# except ZeroDivisionError:
#     print('nuh uh bro u cant divide by 0 how did u end up with dividing by 0 bro wth')
# print('hello world')


# try:
#     print('start code')
#     print(10 / 0)
#     print('mgm')
# except (NameError, ZeroDivisionError) as error:
#     print(error)
#
# print('yay')




# try:
#     x=int(input('ddtlsnm xbckj'))
#     r=10/x
#     print(r)
# except ZeroDivisionError:
#     print('Yt vj;yf yf 0 lskbnb')
# except ValueError:
#     print('<kz[f xbckj f yt ntrcn fkj qjvfqj!!!!!')


try:
    x=int(input('Введіть число'))
    r=10/x
    print(r)
except (ZeroDivisionError, ValueError) as error:
    print('Бляха братан тут не получається поділити ти щось не так ввів давай переписуй.')
























