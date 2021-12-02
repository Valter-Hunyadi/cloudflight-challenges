import copy

def bakery(sales_payment_data):
    
    def transaction_chain_finder(day, balance, time_frame, chain_len=1):
        current_payment_list = copy.deepcopy(payment_list)
        for payment in payment_list:
            if chain_len > 4:
                break
            if payment not in transaction_list:
                if int(payment[0]) >= int(day):
                    if int(payment[0]) <= int(day) + int(time_frame):
                        transaction_list.append(payment)
                        if balance - int(payment[1]) == 0:
                            #print(f"we found a good one, transaction {str(transaction_list)}")
                            #print(f"We got day {str(day)} right")
                            for transaction in transaction_list:
                                payment_list.remove(transaction)
                            return
                        if balance -int(payment[1]) > 0:
                            transaction_chain_finder(day, balance-int(payment[1]), chain_len+1)
                        transaction_list.remove(payment)
    payment_list = sales_payment_data.split("B ")[1:]
    payment_dict = {}
    sales_dict = {}
    for i, payment in enumerate(payment_list):
        payment_dict[int(payment.split()[0])] = payment_dict.get(int(payment.split()[0]), 0) + int(payment.split()[1])
        payment_list[i] = payment.split()
    sales_list = sales_payment_data.split("F ")[1:]
    sales_list[-1] = sales_list[-1].split(" B ")[0]
    for i, sale in enumerate(sales_list):
        sales_dict[int(sale.split()[0])] = int(sale.split()[1])
        sales_list[i] = sale.split()
    #print("Payment list: " + str(payment_list))
    #print("Sales list: " + str(sales_dict))
    cheating_days = ""  
    for day, driver, time_frame, sale in sales_list:
        print(day,driver,time_frame,sale)
        transaction_list = []
        #print(f"Day {str(day)}, sale {str(sale)}")
        balance = int(sale)
        #print(f"payment_list at start: {str(payment_list)}")
        transaction_chain_finder(day, balance, time_frame)
        if len(transaction_list) == 0:
            cheating_days += str(day) + ":" + str(driver) + " "

    print("cheating days: " + str(cheating_days))

    
bakery("F 1 1 4 407 F 1 2 4 632 F 2 1 4 649 F 2 2 4 530 B 1 203 B 1 316 B 2 324 B 2 265 B 3 204 B 3 316 B 4 240 B 4 265")

bakery("F 1 1 4 347 F 1 2 4 397 F 2 1 4 431 F 2 2 4 878 B 1 173 B 1 198 B 2 215 B 2 439 B 3 174 B 3 28 B 4 2 B 4 222")

bakery("F 1 1 2 305517 F 1 2 2 365415 F 1 3 2 360606 F 1 4 2 72756 F 2 1 2 384041 F 2 2 2 372450 F 2 3 2 383375 F 2 4 2 323634 F 3 1 2 77477 F 3 2 2 121856 F 3 3 2 265482 F 3 4 2 15471 F 4 1 2 84358 F 4 2 2 173377 F 4 3 2 25382 F 4 4 2 60144 F 5 1 2 346571 F 5 2 2 107302 F 5 3 2 47122 F 5 4 2 54274 F 6 1 2 106312 F 6 2 2 234202 F 6 3 2 153353 F 6 4 2 201285 F 7 1 2 101866 F 7 2 2 170833 F 7 3 2 253479 F 7 4 2 86552 F 8 1 2 211061 F 8 2 2 238532 F 8 3 2 37138 F 8 4 2 5664 F 9 1 2 378937 F 9 2 2 318373 F 9 3 2 233545 F 9 4 2 152662 F 10 1 2 196238 F 10 2 2 8783 F 10 3 2 287955 F 10 4 2 71041 F 11 1 2 384568 F 11 2 2 135199 F 11 3 2 237506 F 11 4 2 106658 F 12 1 2 59273 F 12 2 2 304880 F 12 3 2 37513 F 12 4 2 47501 F 13 1 2 334092 F 13 2 2 397160 F 13 3 2 124874 F 13 4 2 303213 F 14 1 2 261504 F 14 2 2 4353 F 14 3 2 219085 F 14 4 2 51220 F 15 1 2 163662 F 15 2 2 232629 F 15 3 2 152912 F 15 4 2 58918 F 17 1 2 69067 F 17 2 2 280835 F 17 3 2 24461 F 17 4 2 207547 F 16 1 2 21752 F 16 2 2 99364 F 16 3 2 140062 F 16 4 2 39670 F 19 1 2 5252 F 19 2 2 392098 F 19 3 2 394878 F 19 4 2 299715 F 18 1 2 290560 F 18 2 2 115509 F 18 3 2 47671 F 18 4 2 52638 F 21 1 2 330149 F 21 2 2 323368 F 21 3 2 259842 F 21 4 2 201185 F 20 1 2 186702 F 20 2 2 33499 F 20 3 2 144284 F 20 4 2 376419 F 23 1 2 37388 F 23 2 2 55491 F 23 3 2 199117 F 23 4 2 383462 F 22 1 2 26134 F 22 2 2 324966 F 22 3 2 318524 F 22 4 2 178976 F 25 1 2 16210 F 25 2 2 383535 F 25 3 2 343289 F 25 4 2 284223 F 24 1 2 220841 F 24 2 2 248312 F 24 3 2 258300 F 24 4 2 150250 F 27 1 2 169907 F 27 2 2 306961 F 27 3 2 295032 F 27 4 2 27665 F 26 1 2 359104 F 26 2 2 99176 F 26 3 2 18294 F 26 4 2 332528 F 29 1 2 20490 F 29 2 2 325237 F 29 3 2 383987 F 29 4 2 128086 F 28 1 2 322692 F 28 2 2 248533 F 28 3 2 389395 F 28 4 2 351524 F 31 1 2 96266 F 31 2 2 150489 F 31 3 2 138606 F 31 4 2 109321 F 30 1 2 13048 F 30 2 2 21786 F 30 3 2 362044 F 30 4 2 380617 F 34 1 2 336471 F 34 2 2 79320 F 34 3 2 316699 F 34 4 2 14722 F 35 1 2 29906 F 35 2 2 43783 F 35 3 2 343392 F 35 4 2 246633 F 32 1 2 138717 F 32 2 2 22705 F 32 3 2 135874 F 32 4 2 83342 F 33 1 2 388471 F 33 2 2 110383 F 33 3 2 256623 F 33 4 2 246846 F 38 1 2 243342 F 38 2 2 68291 F 38 3 2 123302 F 38 4 2 49966 F 39 1 2 100754 F 39 2 2 280191 F 39 3 2 234055 F 39 4 2 92168 F 36 1 2 280537 F 36 2 2 32682 F 36 3 2 321297 F 36 4 2 390264 F 37 1 2 119519 F 37 2 2 52592 F 37 3 2 46599 F 37 4 2 105822 B 1 152758 B 1 182707 B 1 180303 B 1 36378 B 2 192020 B 2 186225 B 2 191687 B 2 161817 B 3 152759 B 3 182708 B 3 180303 B 3 36378 B 3 38738 B 3 60928 B 3 132741 B 3 7735 B 4 192021 B 4 186225 B 4 191688 B 4 161817 B 4 42179 B 4 86688 B 4 12691 B 4 30072 B 5 38739 B 5 60928 B 5 132741 B 5 7736 B 5 173285 B 5 53651 B 5 23561 B 5 27137 B 6 42179 B 6 45420 B 6 12691 B 6 30072 B 6 53156 B 6 117101 B 6 76676 B 6 100642 B 7 173286 B 7 53651 B 7 23561 B 7 27137 B 7 50933 B 7 85416 B 7 126739 B 7 43276 B 8 39220 B 8 117101 B 8 76677 B 8 100643 B 8 105530 B 8 119266 B 8 18569 B 8 2832 B 9 50933 B 9 85417 B 9 126740 B 9 43276 B 9 189468 B 9 159186 B 9 116772 B 9 76331 B 10 105531 B 10 119266 B 10 18569 B 10 2832 B 10 98119 B 10 4391 B 10 143977 B 10 35520 B 11 189469 B 11 159187 B 11 116773 B 11 76331 B 11 192284 B 11 67599 B 11 118753 B 11 53329 B 12 98119 B 12 4041 B 12 143978 B 12 35521 B 12 29636 B 12 152440 B 12 18756 B 12 23750 B 13 192284 B 13 67600 B 13 118753 B 13 53329 B 13 167046 B 13 198580 B 13 62437 B 13 151606 B 14 29637 B 14 152440 B 14 18757 B 14 23751 B 14 130752 B 14 2176 B 14 109542 B 14 25610 B 15 167046 B 15 198580 B 15 62437 B 15 151607 B 15 81831 B 15 116314 B 15 76456 B 15 29459 B 17 81831 B 17 116315 B 17 76456 B 17 17153 B 17 34533 B 17 140417 B 17 12230 B 17 103773 B 16 130752 B 16 2177 B 16 109543 B 16 25610 B 16 10876 B 16 49682 B 16 70031 B 16 19835 B 19 34534 B 19 140418 B 19 12231 B 19 103774 B 19 2626 B 19 196049 B 19 197439 B 19 149857 B 18 10876 B 18 49682 B 18 70031 B 18 19835 B 18 145280 B 18 57754 B 18 23835 B 18 26319 B 21 2626 B 21 196049 B 21 197439 B 21 149858 B 21 165074 B 21 161684 B 21 129921 B 21 100592 B 20 145280 B 20 57755 B 20 23836 B 20 26319 B 20 93351 B 20 16749 B 20 72142 B 20 188209 B 23 165075 B 23 161684 B 23 129921 B 23 100593 B 23 18694 B 23 27745 B 23 99558 B 23 191731 B 22 93351 B 22 16750 B 22 72142 B 22 188210 B 22 13067 B 22 162483 B 22 159262 B 22 89488 B 25 18694 B 25 27746 B 25 99559 B 25 191731 B 25 8105 B 25 191767 B 25 171644 B 25 142111 B 24 13067 B 24 162483 B 24 159262 B 24 77811 B 24 110420 B 24 124156 B 24 129150 B 24 75125 B 27 8105 B 27 191768 B 27 171645 B 27 142112 B 27 84953 B 27 153480 B 27 147516 B 27 13832 B 26 110421 B 26 124156 B 26 129150 B 26 75125 B 26 179552 B 26 49588 B 26 9147 B 26 166264 B 29 84954 B 29 153481 B 29 147516 B 29 13833 B 29 10245 B 29 162618 B 29 191993 B 29 64043 B 28 179552 B 28 49588 B 28 9147 B 28 166264 B 28 161346 B 28 124266 B 28 194697 B 28 175762 B 31 10245 B 31 162619 B 31 191994 B 31 64043 B 31 48133 B 31 75244 B 31 69303 B 31 54660 B 30 161346 B 30 124267 B 30 194698 B 30 175762 B 30 6524 B 30 10893 B 30 181022 B 30 190308 B 34 69359 B 34 11353 B 34 67937 B 34 41671 B 34 168235 B 34 39660 B 34 158349 B 34 7361 B 35 194236 B 35 55192 B 35 128312 B 35 123423 B 35 14953 B 35 21891 B 35 171696 B 35 123316 B 32 6524 B 32 10893 B 32 181022 B 32 190309 B 32 69358 B 32 11352 B 32 67937 B 32 41671 B 33 48133 B 33 75245 B 33 69303 B 33 54661 B 33 194235 B 33 55191 B 33 128311 B 33 123423 B 38 140269 B 38 16341 B 38 160649 B 38 195132 B 38 121671 B 38 34145 B 38 61651 B 38 24983 B 39 59760 B 39 26296 B 39 23300 B 39 52911 B 39 50377 B 39 140095 B 39 117027 B 39 46084 B 36 168236 B 36 39660 B 36 158350 B 36 7361 B 36 140268 B 36 16341 B 36 160648 B 36 195132 B 37 14953 B 37 21892 B 37 171696 B 37 72889 B 37 59759 B 37 26296 B 37 23299 B 37 52911 B 40 121671 B 40 34146 B 40 61651 B 40 24983 B 41 50377 B 41 140096 B 41 117028 B 41 46084")
bakery("F 1 1 2 380313 F 1 2 2 2592 F 1 3 2 279776 F 1 4 2 35478 F 2 1 2 389342 F 2 2 2 308459 F 2 3 2 224882 F 2 4 2 172280 F 3 1 2 54380 F 3 2 2 328518 F 3 3 2 306418 F 3 4 2 250748 F 4 1 2 374579 F 4 2 2 64128 F 4 3 2 238615 F 4 4 2 377914 F 5 1 2 77741 F 5 2 2 123194 F 5 3 2 180394 F 5 4 2 354880 F 6 1 2 314245 F 6 2 2 147156 F 6 3 2 183697 F 6 4 2 247132 F 7 1 2 124316 F 7 2 2 55504 F 7 3 2 23961 F 7 4 2 294141 F 8 1 2 247348 F 8 2 2 1505 F 8 3 2 223851 F 8 4 2 159782 F 9 1 2 333018 F 9 2 2 369771 F 9 3 2 347671 F 9 4 2 262944 F 10 1 2 29665 F 10 2 2 72933 F 10 3 2 308441 F 10 4 2 255839 F 11 1 2 169415 F 11 2 2 17011 F 11 3 2 81927 F 11 4 2 171260 F 12 1 2 152122 F 12 2 2 202056 F 12 3 2 15720 F 12 4 2 103457 F 13 1 2 168122 F 13 2 2 213575 F 13 3 2 236522 F 13 4 2 106702 F 14 1 2 165925 F 14 2 2 88629 F 14 3 2 175234 F 14 4 2 313595 F 15 1 2 257440 F 15 2 2 215795 F 15 3 2 193695 F 15 4 2 249957 F 17 1 2 66627 F 17 2 2 115830 F 17 3 2 244794 F 17 4 2 253197 F 16 1 2 350722 F 16 2 2 339616 F 16 3 2 375219 F 16 4 2 27571 F 19 1 2 264666 F 19 2 2 149184 F 19 3 2 32510 F 19 4 2 6660 F 18 1 2 145399 F 18 2 2 62213 F 18 3 2 300273 F 18 4 2 164839 F 21 1 2 193049 F 21 2 2 377094 F 21 3 2 93653 F 21 4 2 297474 F 20 1 2 274446 F 20 2 2 140591 F 20 3 2 87989 F 20 4 2 288059 F 23 1 2 293730 F 23 2 2 61160 F 23 3 2 129826 F 23 4 2 46248 F 22 1 2 123015 F 22 2 2 222842 F 22 3 2 5555 F 22 4 2 127008 F 25 1 2 263975 F 25 2 2 117991 F 25 3 2 123092 F 25 4 2 267968 F 24 1 2 135974 F 24 2 2 285766 F 24 3 2 36578 F 24 4 2 236648 F 27 1 2 213518 F 27 2 2 199022 F 27 3 2 190529 F 27 4 2 305887 F 26 1 2 243253 F 26 2 2 231173 F 26 3 2 178571 F 26 4 2 235771 F 29 1 2 218497 F 29 2 2 206417 F 29 3 2 293412 F 29 4 2 338798 F 28 1 2 228591 F 28 2 2 172436 F 28 3 2 232435 F 28 4 2 97260 F 31 1 2 101858 F 31 2 2 357668 F 31 3 2 49108 F 31 4 2 247779 F 30 1 2 11318 F 30 2 2 172149 F 30 3 2 372219 F 30 4 2 375741 F 34 1 2 34275 F 34 2 2 361191 F 34 3 2 17452 F 34 4 2 286015 F 35 1 2 123040 F 35 2 2 168493 F 35 3 2 2816 F 35 4 2 98234 F 32 1 2 55729 F 32 2 2 149979 F 32 3 2 209979 F 32 4 2 252097 F 33 1 2 34338 F 33 2 2 288355 F 33 3 2 396214 F 33 4 2 343612 F 38 1 2 348501 F 38 2 2 219875 F 38 3 2 126669 F 38 4 2 135071 F 39 1 2 130478 F 39 2 2 134891 F 39 3 2 163612 F 39 4 2 141512 F 36 1 2 314413 F 36 2 2 267619 F 36 3 2 158905 F 36 4 2 266764 F 37 1 2 200507 F 37 2 2 59003 F 37 3 2 36904 F 37 4 2 276179 B 1 190156 B 1 1296 B 1 139888 B 1 17739 B 2 194671 B 2 154229 B 2 112441 B 2 86140 B 3 190157 B 3 1296 B 3 139888 B 3 17739 B 3 27190 B 3 164259 B 3 153209 B 3 125374 B 4 194671 B 4 154230 B 4 112441 B 4 86140 B 4 187289 B 4 32064 B 4 119307 B 4 188957 B 5 27190 B 5 164259 B 5 153209 B 5 125374 B 5 38870 B 5 61597 B 5 90197 B 5 177440 B 6 187290 B 6 32064 B 6 119308 B 6 188957 B 6 157122 B 6 73578 B 6 91848 B 6 123566 B 7 38871 B 7 61597 B 7 90197 B 7 177440 B 7 62158 B 7 27752 B 7 11980 B 7 147070 B 8 157123 B 8 73578 B 8 41177 B 8 123566 B 8 123674 B 8 752 B 8 111925 B 8 79891 B 9 62158 B 9 9602 B 9 11981 B 9 147071 B 9 166509 B 9 184885 B 9 173835 B 9 131472 B 10 123674 B 10 753 B 10 111926 B 10 79891 B 10 14832 B 10 36466 B 10 154220 B 10 127919 B 11 166509 B 11 184886 B 11 173836 B 11 131472 B 11 84707 B 11 8505 B 11 40963 B 11 85630 B 12 14833 B 12 36467 B 12 154221 B 12 127920 B 12 76061 B 12 101028 B 12 7860 B 12 51728 B 13 84708 B 13 8506 B 13 40964 B 13 85630 B 13 84061 B 13 106787 B 13 118261 B 13 53351 B 14 76061 B 14 101028 B 14 7860 B 14 51729 B 14 82962 B 14 44314 B 14 87617 B 14 156797 B 15 84061 B 15 106788 B 15 118261 B 15 53351 B 15 128720 B 15 107897 B 15 96847 B 15 124978 B 17 128720 B 17 107898 B 17 96848 B 17 124979 B 17 33313 B 17 57915 B 17 122397 B 17 126598 B 16 82963 B 16 44315 B 16 87617 B 16 156798 B 16 175361 B 16 169808 B 16 187609 B 16 13785 B 19 33314 B 19 57915 B 19 122397 B 19 126599 B 19 132333 B 19 74592 B 19 16255 B 19 3330 B 18 175361 B 18 169808 B 18 187610 B 18 13786 B 18 72699 B 18 31106 B 18 150136 B 18 82419 B 21 132333 B 21 74592 B 21 16255 B 21 3330 B 21 96524 B 21 188547 B 21 46826 B 21 148737 B 20 72700 B 20 31107 B 20 150137 B 20 82420 B 20 137223 B 20 70295 B 20 43994 B 20 144029 B 23 96525 B 23 188547 B 23 46827 B 23 148737 B 23 146865 B 23 30580 B 23 64913 B 23 23124 B 22 137223 B 22 70296 B 22 43995 B 22 144030 B 22 61507 B 22 111421 B 22 2777 B 22 63504 B 25 146865 B 25 30580 B 25 64913 B 25 23124 B 25 131987 B 25 58995 B 25 61546 B 25 133984 B 24 61508 B 24 111421 B 24 2778 B 24 63504 B 24 67987 B 24 142883 B 24 18289 B 24 118324 B 27 131988 B 27 58996 B 27 61546 B 27 133984 B 27 106759 B 27 99511 B 27 95264 B 27 152943 B 26 67987 B 26 142883 B 26 18289 B 26 118324 B 26 121626 B 26 115586 B 26 89285 B 26 117885 B 29 69937 B 29 99511 B 29 95265 B 29 152944 B 29 109248 B 29 103208 B 29 146706 B 29 169399 B 28 121627 B 28 115587 B 28 89286 B 28 117886 B 28 114295 B 28 86218 B 28 116217 B 28 48630 B 31 109249 B 31 103209 B 31 146706 B 31 169399 B 31 50929 B 31 178834 B 31 24554 B 31 123889 B 30 114296 B 30 86218 B 30 116218 B 30 48630 B 30 5659 B 30 86074 B 30 186109 B 30 187870 B 34 27865 B 34 74990 B 34 104990 B 34 126049 B 34 17137 B 34 180595 B 34 8726 B 34 143007 B 35 17169 B 35 144178 B 35 198107 B 35 171806 B 35 61520 B 35 84246 B 35 1408 B 35 49117 B 32 5659 B 32 86075 B 32 186110 B 32 187871 B 32 27864 B 32 74989 B 32 104989 B 32 126048 B 33 50929 B 33 178834 B 33 24554 B 33 123890 B 33 17169 B 33 144177 B 33 198107 B 33 171806 B 38 157207 B 38 133810 B 38 79453 B 38 133382 B 38 174250 B 38 109937 B 38 63334 B 38 67535 B 39 100254 B 39 29502 B 39 18452 B 39 138090 B 39 65239 B 39 67445 B 39 81806 B 39 70756 B 36 17138 B 36 180596 B 36 8726 B 36 143008 B 36 157206 B 36 133809 B 36 79452 B 36 133382 B 37 61520 B 37 84247 B 37 1408 B 37 49117 B 37 100253 B 37 29501 B 37 18452 B 37 138089 B 40 174251 B 40 109938 B 40 63335 B 40 67536 B 41 65239 B 41 41223 B 41 81806 B 41 70756")
bakery("F 1 1 2 186596 F 1 2 2 311272 F 1 3 2 322636 F 1 4 2 345583 F 2 1 2 341965 F 2 2 2 245160 F 2 3 2 250009 F 2 4 2 53829 F 3 1 2 364477 F 3 2 2 291393 F 3 3 2 92170 F 3 4 2 261738 F 4 1 2 221102 F 4 2 2 175282 F 4 3 2 183684 F 4 4 2 18007 F 5 1 2 12476 F 5 2 2 196521 F 5 3 2 65083 F 5 4 2 33541 F 6 1 2 270565 F 6 2 2 346521 F 6 3 2 246035 F 6 4 2 12559 F 7 1 2 71783 F 7 2 2 25222 F 7 3 2 93888 F 7 4 2 119648 F 8 1 2 54790 F 8 2 2 227011 F 8 3 2 99553 F 8 4 2 303373 F 9 1 2 64205 F 9 2 2 228741 F 9 3 2 202891 F 9 4 2 132907 F 10 1 2 232483 F 10 2 2 53847 F 10 3 2 220371 F 10 4 2 3533 F 11 1 2 131250 F 11 2 2 15237 F 11 3 2 60690 F 11 4 2 253426 F 12 1 2 230076 F 12 2 2 296198 F 12 3 2 8973 F 12 4 2 17376 F 13 1 2 225165 F 13 2 2 324992 F 13 3 2 276833 F 13 4 2 254733 F 14 1 2 365554 F 14 2 2 2990 F 14 3 2 380891 F 14 4 2 37153 F 15 1 2 148911 F 15 2 2 15101 F 15 3 2 287643 F 15 4 2 260624 F 17 1 2 396736 F 17 2 2 350916 F 17 3 2 393034 F 17 4 2 162602 F 16 1 2 150213 F 16 2 2 7772 F 16 3 2 154800 F 16 4 2 79922 F 19 1 2 309753 F 19 2 2 324704 F 19 3 2 189529 F 19 4 2 5708 F 18 1 2 161054 F 18 2 2 176005 F 18 3 2 293112 F 18 4 2 148921 F 21 1 2 172981 F 21 2 2 296170 F 21 3 2 164733 F 21 4 2 159990 F 20 1 2 30679 F 20 2 2 105387 F 20 3 2 373985 F 20 4 2 351885 F 23 1 2 337231 F 23 2 2 325789 F 23 3 2 87594 F 23 4 2 321916 F 22 1 2 183711 F 22 2 2 175382 F 22 3 2 166398 F 22 4 2 192158 F 25 1 2 365767 F 25 2 2 176369 F 25 3 2 154269 F 25 4 2 182793 F 24 1 2 121905 F 24 2 2 13716 F 24 3 2 5223 F 24 4 2 49253 F 27 1 2 364971 F 27 2 2 291886 F 27 3 2 348148 F 27 4 2 392177 F 26 1 2 64893 F 26 2 2 219050 F 26 3 2 244810 F 26 4 2 192208 F 29 1 2 31667 F 29 2 2 215942 F 29 3 2 344906 F 29 4 2 161086 F 28 1 2 153009 F 28 2 2 167960 F 28 3 2 91048 F 28 4 2 270835 F 31 1 2 378779 F 31 2 2 244923 F 31 3 2 326028 F 31 4 2 321285 F 30 1 2 172450 F 30 2 2 322242 F 30 3 2 67135 F 30 4 2 75538 F 34 1 2 280869 F 34 2 2 132291 F 34 3 2 270652 F 34 4 2 317311 F 35 1 2 348138 F 35 2 2 10949 F 35 3 2 135703 F 35 4 2 165165 F 32 1 2 274492 F 32 2 2 244860 F 32 3 2 335443 F 32 4 2 320553 F 33 1 2 301415 F 33 2 2 114827 F 33 3 2 384558 F 33 4 2 26677 F 38 1 2 317632 F 38 2 2 287027 F 38 3 2 213767 F 38 4 2 239527 F 39 1 2 312840 F 39 2 2 247208 F 39 3 2 34840 F 39 4 2 8990 F 36 1 2 193886 F 36 2 2 100680 F 36 3 2 123627 F 36 4 2 1668 F 37 1 2 106796 F 37 2 2 171712 F 37 3 2 131087 F 37 4 2 153096 B 1 93298 B 1 155636 B 1 161318 B 1 172791 B 2 170982 B 2 122580 B 2 125004 B 2 26914 B 3 93298 B 3 155636 B 3 161318 B 3 172792 B 3 182238 B 3 145696 B 3 46085 B 3 130869 B 4 170983 B 4 122580 B 4 125005 B 4 4823 B 4 110551 B 4 87641 B 4 91842 B 4 9003 B 5 182239 B 5 145697 B 5 46085 B 5 130869 B 5 6238 B 5 98260 B 5 32541 B 5 16770 B 6 110551 B 6 87641 B 6 91842 B 6 9004 B 6 135282 B 6 173260 B 6 123017 B 6 6279 B 7 6238 B 7 98261 B 7 3718 B 7 16771 B 7 35891 B 7 12611 B 7 46944 B 7 59824 B 8 135283 B 8 173261 B 8 123018 B 8 6280 B 8 27395 B 8 113505 B 8 49776 B 8 151686 B 9 35892 B 9 12611 B 9 46944 B 9 59824 B 9 32102 B 9 114370 B 9 101445 B 9 66453 B 10 27395 B 10 113506 B 10 49777 B 10 151687 B 10 116241 B 10 26923 B 10 110185 B 10 1766 B 11 32103 B 11 114371 B 11 101446 B 11 5764 B 11 65625 B 11 7618 B 11 30345 B 11 126713 B 12 76916 B 12 26924 B 12 110186 B 12 1767 B 12 115038 B 12 148099 B 12 4486 B 12 8688 B 13 65625 B 13 7619 B 13 30345 B 13 126713 B 13 112582 B 13 162496 B 13 138416 B 13 127366 B 14 115038 B 14 148099 B 14 4487 B 14 8688 B 14 182777 B 14 1495 B 14 190445 B 14 18576 B 15 112583 B 15 162496 B 15 138417 B 15 127367 B 15 74455 B 15 7550 B 15 143821 B 15 130312 B 17 74456 B 17 7551 B 17 143822 B 17 130312 B 17 198368 B 17 175458 B 17 196517 B 17 81301 B 16 182777 B 16 1495 B 16 190446 B 16 18577 B 16 75106 B 16 3886 B 16 77400 B 16 39961 B 19 198368 B 19 175458 B 19 196517 B 19 81301 B 19 154876 B 19 162352 B 19 94764 B 19 2854 B 18 75107 B 18 3886 B 18 77400 B 18 39961 B 18 80527 B 18 88002 B 18 146556 B 18 74460 B 21 154877 B 21 162352 B 21 45433 B 21 2854 B 21 86490 B 21 148085 B 21 82366 B 21 79995 B 20 80527 B 20 88003 B 20 52458 B 20 74461 B 20 15339 B 20 52693 B 20 186992 B 20 175942 B 23 70456 B 23 148085 B 23 82367 B 23 79995 B 23 168615 B 23 162894 B 23 43797 B 23 160958 B 22 15340 B 22 45339 B 22 186993 B 22 175943 B 22 91855 B 22 87691 B 22 83199 B 22 96079 B 25 168616 B 25 162895 B 25 43797 B 25 160958 B 25 182883 B 25 88184 B 25 77134 B 25 91396 B 24 91856 B 24 87691 B 24 83199 B 24 96079 B 24 60952 B 24 6858 B 24 2611 B 24 24626 B 27 182884 B 27 88185 B 27 77135 B 27 91397 B 27 182485 B 27 145943 B 27 174074 B 27 196088 B 26 60953 B 26 6858 B 26 2612 B 26 24627 B 26 32446 B 26 109525 B 26 122405 B 26 96104 B 29 182486 B 29 145943 B 29 174074 B 29 196089 B 29 15833 B 29 107971 B 29 172453 B 29 80543 B 28 32447 B 28 109525 B 28 122405 B 28 96104 B 28 76504 B 28 83980 B 28 45524 B 28 135417 B 31 9074 B 31 107971 B 31 96906 B 31 80543 B 31 189389 B 31 122461 B 31 163014 B 31 160642 B 30 76505 B 30 83980 B 30 3136 B 30 135418 B 30 86225 B 30 161121 B 30 33567 B 30 37769 B 34 137246 B 34 122430 B 34 167722 B 34 160277 B 34 140434 B 34 66145 B 34 135326 B 34 158655 B 35 150708 B 35 57414 B 35 192279 B 35 13339 B 35 174069 B 35 5474 B 35 67851 B 35 82582 B 32 86225 B 32 161121 B 32 33568 B 32 37769 B 32 137246 B 32 122430 B 32 167721 B 32 160276 B 33 189390 B 33 122462 B 33 163014 B 33 160643 B 33 150707 B 33 57413 B 33 192279 B 33 13338 B 38 96943 B 38 50340 B 38 61814 B 38 130 B 38 158816 B 38 143513 B 38 106883 B 38 119763 B 39 53398 B 39 85856 B 39 65544 B 39 76548 B 39 156420 B 39 123604 B 39 17420 B 39 4495 B 36 140435 B 36 66146 B 36 54621 B 36 158656 B 36 96943 B 36 50340 B 36 61813 B 36 834 B 37 174069 B 37 5475 B 37 67852 B 37 82583 B 37 53398 B 37 85856 B 37 65543 B 37 76548 B 40 158816 B 40 143514 B 40 106884 B 40 119764 B 41 145964 B 41 123604 B 41 17420 B 41 4495")
