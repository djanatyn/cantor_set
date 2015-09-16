##prints out the cantor ternary set. asks user the number of times to iterate and a char to be used

def cantorSet(N, char_print, count):  ##function that prints the cantor set
    line = "";  ##line to be printed
    if (N == 0):  ##base case
        return();
    else:

        if(count == 0):  ##prints initial line where there is no whitespace and the second line
            print char_print*3**N;
            print char_print*((3**N)/3)," "*(((3**N)/3)-2),char_print*((3**N)/3);

        else:
            line = char_print*3**(N-1) + ' '*3**(N-1) + char_print*3**(N-1);
            for i in range(count):
                line+=' '*len(line) + line;

            print line;
    return cantorSet(N-1,char_print,count+1);  ##recursive call

N = int(raw_input("Enter the number of iterations: "));
too_long = True;
##while(too_long):  ##error checking
  ##  if(3**N > 210):  ##approx number of chars that fit in a line in my term. should fix!!
    ##    print "Number of iterations will result in a line outside of screen bounds!"
      ##  N = int(raw_input("Please enter a smaller number of iterations: "));
    ##else:
      ##  too_long = False;
char_print = raw_input("Enter the char you wish to print: ");

cantorSet(N,char_print, 0);
