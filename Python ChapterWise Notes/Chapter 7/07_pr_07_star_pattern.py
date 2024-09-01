n = int(input("Enter the number of lines\n"))
for i in range(n):
    print(" "*(n-1-i),end="") 
    print("*"*((2*i)+1),end="")
    print(" "*(n-1-i))
'''The end="" argument in the print function is used to avoid printing a newline 
character after each part. This allows the stars, spaces, and the newline character 
to be printed on the same line.'''

#Same program in c

#include <stdio.h>

# int main() {
#     int n, i, j;

#     printf("Enter the number of lines: ");
#     scanf("%d", &n);

#     for (i = 0; i < n; i++) {
#         for (j = 0; j < n - i - 1; j++) {
#             printf(" ");
#         }
#         for (j = 0; j < 2 * i + 1; j++) {
#             printf("*");
#         }
#         for (j = 0; j < n - i - 1; j++) {
#             printf(" ");
#         }
#         printf("\n");
#     }

#     return 0;
# }
