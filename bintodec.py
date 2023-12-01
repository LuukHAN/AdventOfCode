def binaryToDeci(convertNumb):
    if(convertNumb == 0):
        return 0
    return(convertNumb % 10 + 2 * binaryToDeci(convertNumb // 10))

endEpsilonVal = int(endEpsilonVal)
endGammaVal = int(endGammaVal)
endEpsilonVal = binaryToDeci(endEpsilonVal)
endGammaVal = binaryToDeci(endGammaVal)