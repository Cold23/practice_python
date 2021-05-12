if __name__ == "__main__":
    my_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz",
                          "cdefghijklmnopqrstuvwxyzab")
    my_str = my_str.translate(table)
    print(my_str)
